from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import requests
import os
import time
import urllib.parse
import pandas as pd
import openpyxl
from openpyxl.styles import PatternFill, Border, Side, Alignment, Font
import re
from config import USERNAME, PASSWORD, DOWNLOAD_DIR  # Importar credenciales y configuración desde config.py

# Función para configurar el directorio de descargas para Chrome
def set_download_directory(driver, download_dir):
    driver.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
    params = {'cmd': 'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
    driver.execute("send_command", params)

# Función para obtener cookies de Selenium y agregarlas a la sesión de requests
def add_cookies_to_session(driver, session):
    for cookie in driver.get_cookies():
        session.cookies.set(cookie['name'], cookie['value'])

# Función para iniciar sesión
def login(driver, username, password):
    driver.get('https://pandora.pucp.edu.pe/pucp/login?service=https%3A%2F%2Fpandora.pucp.edu.pe%2Fpucp%2Fidp%2Fprofile%2FSAML2%2FCallback%3Fsrid%3D_737301cfd029b0244abd21131386b320%26entityId%3Dhttps%253A%252F%252Fcursoshistoricospaideia.pucp.edu.pe%252Fcursos%252Fshibboleth')
    driver.find_element(By.NAME, 'username').send_keys(username)
    driver.find_element(By.NAME, 'password').send_keys(password)
    driver.find_element(By.XPATH, '//input[@value="Acceder"]').click()
    time.sleep(3)  # Esperar a que cargue la sesión

# Función para obtener los cursos
def obtener_cursos(driver):
    driver.get('https://cursoshistoricospaideia.pucp.edu.pe/cursos/local/paideia_customs/miscursos/')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'coursebox')))
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    resultados = []
    for coursebox in soup.find_all('div', class_='coursebox'):
        course_id = coursebox.get('data-courseid')
        course_name_tag = coursebox.find('h3', class_='coursename').find('a')
        if course_id and course_name_tag:
            resultados.append({
                'courseid': course_id,
                'coursename': course_name_tag.text.strip(),
                'url': course_name_tag['href']
            })
    return resultados

# Función para descargar archivos y actualizar URLs
def descargar_archivos_y_actualizar_urls(driver, resultados):
    registro = []
    for r in resultados:
        courseid = r['courseid']
        coursename = r['coursename'].replace('/', '_')
        course_dir = os.path.join(DOWNLOAD_DIR or os.getcwd(), 'Descarga_cursos_historicos', coursename)
        os.makedirs(course_dir, exist_ok=True)  # Crear carpeta del curso
        print(f"Creando directorio: {course_dir}")

        # Configurar el directorio de descargas para el curso actual
        set_download_directory(driver, course_dir)

        retry_count = 3
        while retry_count > 0:
            try:
                driver.get(f'https://cursoshistoricospaideia.pucp.edu.pe/cursos/course/resources.php?id={courseid}')
                WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'a')))
                break
            except Exception as e:
                print(f"Error al acceder a los recursos del curso {coursename}: {e}")
                retry_count -= 1
                if retry_count == 0:
                    print(f"No se pudo acceder a los recursos del curso {coursename} después de varios intentos.")
                    continue
                time.sleep(5)  # Esperar antes de reintentar

        soup_resources = BeautifulSoup(driver.page_source, 'html.parser')
        main_content = soup_resources.find('div', {'role': 'main'})

        for link in main_content.find_all('a', href=True):
            href = link['href']
            name = link.text.strip() or 'archivo_sin_nombre'

            if 'resource/view.php?id=' in href:
                try:
                    driver.get(href)
                    redirected_url = driver.current_url
                    print(f"Redireccionado a: {redirected_url}")

                    if 'pluginfile.php' in redirected_url:
                        file_url = redirected_url
                        filename = urllib.parse.unquote(file_url.split('/')[-1])

                        # Usar sesión de requests con cookies de Selenium
                        session = requests.Session()
                        add_cookies_to_session(driver, session)
                        response = session.get(file_url, stream=True)

                        if response.status_code == 200:
                            filepath = os.path.join(course_dir, filename)
                            with open(filepath, 'wb') as f:
                                for chunk in response.iter_content(chunk_size=8192):
                                    f.write(chunk)
                            print(f"Descargado: {filename}")
                        else:
                            print(f"No se pudo descargar: {name} (Status code: {response.status_code})")
                    else:
                        print(f"Redirección sin descarga: {name}")
                except Exception as e:
                    print(f"Error descargando {name}: {e}")

            # Actualizar la URL final
            final_url = driver.current_url
            registro.append({
                'Curso': coursename,
                'Nombre enlace': name,
                'URL': final_url
            })
    return registro

# Función para guardar el registro en un archivo Excel
def guardar_registro_en_excel(df_registro, excel_file):
    df_registro.to_excel(excel_file, index=False)
    wb = openpyxl.load_workbook(excel_file)
    ws = wb.active
    yellow_fill = PatternFill(start_color='FFFF99', end_color='FFFF99', fill_type='solid')  # Cambiar a amarillo claro
    thin_border = Border(left=Side(style='thin'), right=Side(style='thin'), top=Side(style='thin'), bottom=Side(style='thin'))
    alignment = Alignment(vertical='center', wrap_text=True)
    font = Font(size=15)  # Aumentar el tamaño de la fuente a 15pt

    # Definir los patrones para buscar
    patterns = [
        r"cursos/mod/folder/",
        r"pucp\.zoom\.us/rec/",
        r"facebook",
        r"youtube",
        r"zoom\.us",
        r"drive\.google",
        r"accounts\.google"
    ]

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row, min_col=1, max_col=ws.max_column):
        url_cell = row[2]  # Asumiendo que la URL está en la tercera columna
        if any(re.search(pattern, url_cell.value) for pattern in patterns) or 'pluginfile.php' not in url_cell.value:
            for cell in row:
                cell.fill = yellow_fill
        for cell in row:
            cell.border = thin_border
            cell.alignment = alignment
            cell.font = font  # Aplicar el tamaño de fuente

    # Ajustar el ancho de las columnas y el alto de las filas
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter  # Obtener el nombre de la columna
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(cell.value)
            except:
                pass
        adjusted_width = (max_length + 2)
        ws.column_dimensions[column].width = adjusted_width

    for row in ws.iter_rows(min_row=2, max_row=ws.max_row):
        ws.row_dimensions[row[0].row].height = 20

    wb.save(excel_file)
    print("Archivo Excel creado y guardado en:", excel_file)

# Función principal
def main():
    # 1. Iniciar el navegador con Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)

    try:
        # 2. Iniciar sesión
        login(driver, USERNAME, PASSWORD)

        # 3. Obtener cursos
        resultados = obtener_cursos(driver)

        # 4. Descargar archivos y actualizar URLs
        registro = descargar_archivos_y_actualizar_urls(driver, resultados)

        # 5. Guardar el registro en un archivo Excel
        df_registro = pd.DataFrame(registro)
        excel_file = os.path.join(DOWNLOAD_DIR or os.getcwd(), 'registro_descargas.xlsx')
        guardar_registro_en_excel(df_registro, excel_file)

    finally:
        # 6. Borrar el archivo CSV
        csv_file = 'registro_descargas.csv'
        if os.path.exists(csv_file):
            os.remove(csv_file)
            print("Archivo CSV eliminado.")

        # 7. Borrar los datos en config.py por razones de seguridad
        with open('config.py', 'w') as config_file:
            config_file.write("### Estos datos se eliminaran una vez terminado la descarga de archivos ###\n\n")
            config_file.write("USERNAME = ''  # Reemplazar con tu usuario\n")
            config_file.write("PASSWORD = ''    # Reemplazar con tu contraseña\n")
            config_file.write("DOWNLOAD_DIR = ''  # Dejar vacío para usar el directorio actual, o especificar una ruta\n")
        print("Datos de configuración eliminados.")

        driver.quit()

if __name__ == "__main__":
    main()