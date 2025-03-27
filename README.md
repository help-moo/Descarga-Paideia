# Sobre la ejecución del script `main.py`

Si estas aquí. sabes para qué sirve. 


## ✅ Requisitos previos

Antes de comenzar, asegúrate de tener instalados en tu equipo:

1. **Python 3.10 o superior**
	- Descarga desde: [https://www.python.org/downloads/](https://www.python.org/downloads/) 
	- Durante la instalación, **marca la casilla "Add Python to PATH"**.

2. **Google Chrome**
	- Descarga desde: [https://www.google.com/chrome/](https://www.google.com/chrome/)

3. Descargar e instalar el proyecto

### Instalación mediante `git clone`

1. Abre tu terminal (CMD, PowerShell o terminal de Linux/macOS).
2. Navega hasta el directorio donde deseas clonar el proyecto.
3. Ejecuta el siguiente comando:

```bash
git clone https://github.com/help-moo/Descarga-Paideia.git
```

4. Ingresa al directorio del proyecto:

```bash
cd Descarga-Paideia
```

5. Sigue las instrucciones de instalación o configuración indicadas en el repositorio.

##  I. Configuración del entorno virtual

Se recomienda utilizar un entorno virtual para evitar conflictos de dependencias.
### Crear el entorno virtual e instalar las dependencias:

| **Windows**                                                 | **Linux / macOS**                                            |
| ----------------------------------------------------------- | ------------------------------------------------------------ |
| 1. Abrir la terminal (cmd o PowerShell).                    | 1. Abrir la terminal.                                        |
| 2. Navegar a la carpeta del proyecto.                       | 2. Navegar a la carpeta del proyecto.                        |
| 3. Crear el entorno virtual: `python -m venv venv`          | 3. Crear el entorno virtual: `python3 -m venv venv`          |
| 4. Activar el entorno virtual: `venv\Scripts\activate`      | 4. Activar el entorno virtual: `source venv/bin/activate`    |
| 5. Instalar dependencias: `pip install -r requirements.txt` | 5. Instalar dependencias: `pip3 install -r requirements.txt` |


## II. Configuración del archivo `config.py`

Antes de ejecutar `main.py`, abre el archivo `config.py` y completa lo siguiente:

```python
USUARIX = '' 
CONTRASEÑA = '' 
DIRECTORIO_DESCARGAS = ''
CURSOS_A_DESCARGAR = "soc, lenguaje, 2021"  # Ejemplo: Selecciona cursos con "soc", "lenguaje", o "2021" en el nombre
CURSOS_A_EXCLUIR = "teoría"  # Ejemplo: Excluye cursos con "teoría" en el nombre
```

- **USUARIX:** tu usuario de la plataforma Paideia.
- **CONTRASEÑA:** tu contraseña de Paideia.
- **DIRECTORIO_DESCARGAS:** *(opcional)* Si lo dejas vacío (`''`), la carpeta de descarga será el mismo directorio donde se encuentra `main.py`.
 
> ⚠️ **Importante:**
> Por seguridad, los datos de `USUARIX` y `CONTRASEÑA` se eliminarán automáticamente del `config.py` al finalizar la ejecución del script.

### Configuración de `CURSOS_A_DESCARGAR` y `CURSOS_A_EXCLUIR`

1. **`CURSOS_A_DESCARGAR`**:
   - Lista de palabras clave separadas por comas para seleccionar los cursos que deseas descargar.
   - El script buscará cursos cuyos nombres contengan alguna de estas palabras clave.
   - **Ejemplo**:
     ```python
     CURSOS_A_DESCARGAR = "soc, lenguaje, 2021"
     ```
     - Seleccionará cursos como:
       - `"2021-1 PROCESOS SOCIALES CONTEMPORÁNEOS"`
       - `"2021-1 LENGUAJE Y SOCIEDAD"`
       - Cualquier curso del año 2021.

2. **`CURSOS_A_EXCLUIR`**:
   - Lista de palabras clave separadas por comas para excluir cursos que no deseas descargar.
   - Si un curso coincide con alguna palabra clave, será excluido.
   - **Ejemplo**:
     ```python
     CURSOS_A_EXCLUIR = "teoría"
     ```
     - Excluirá cursos como `"2021-1 TEORÍA SOCIOLÓGICA"`.

3. **Cómo funcionan juntas**:
   - Primero, el script selecciona los cursos que coincidan con `CURSOS_A_DESCARGAR`.
   - Luego, excluye los cursos que coincidan con `CURSOS_A_EXCLUIR`.

### Notas importantes:
- Las palabras clave no distinguen entre mayúsculas y minúsculas.
- Si `CURSOS_A_DESCARGAR` está vacío, se descargarán **todos los cursos disponibles**.
- Si `CURSOS_A_EXCLUIR` está vacío, no se excluirá ningún curso.

```python
# Ejemplo completo:
CURSOS_A_DESCARGAR = "soc, lenguaje, 2021"
CURSOS_A_EXCLUIR = "teoría, matemáticas"
```
- Este ejemplo seleccionará cursos que contengan `"soc"`, `"lenguaje"`, o `"2021"`, pero excluirá aquellos que contengan `"teoría"` o `"matemáticas"`.

> 💡 **Consejo**: Usa palabras clave específicas para evitar descargar cursos innecesarios.

### Ejemplos de patrones regex

1. **`r"2021-1 .*SOCIAL.*"`**: Selecciona cursos del periodo `2021-1` que contienen "SOCIAL" en el nombre.
   - Ejemplo: `"2021-1 PROCESOS SOCIALES CONTEMPORÁNEOS (SOC726-0001)"`

2. **`r"2021-1 .*SOC689.*"`**: Selecciona cursos del periodo `2021-1` con el código `SOC689`.
   - Ejemplo: `"2021-1 TEORÍA SOCIOLÓGICA (SOC689-0001)"`

3. **`r".*TEORÍA.*"`**: Selecciona cualquier curso que contenga "TEORÍA" en el nombre, sin importar el periodo.
   - Ejemplo: `"2021-1 TEORÍA SOCIOLÓGICA (SOC689-0001)"`

4. **`r"2020-2 .*"`**: Selecciona todos los cursos del periodo `2020-2`.
   - Ejemplo: `"2020-2 HISTORIA DEL ARTE (ART123-0001)"`

5. **`r".*SOC.*"`**: Selecciona todos los cursos cuyo código contiene "SOC".
   - Ejemplo: `"2021-1 PROCESOS SOCIALES CONTEMPORÁNEOS (SOC726-0001)"`

6. **`r".*0001.*"`**: Selecciona cursos con el código de sección `0001`.
   - Ejemplo: `"2021-1 TEORÍA SOCIOLÓGICA (SOC689-0001)"`

> 💡 **Nota**: Los patrones regex son sensibles a mayúsculas y minúsculas. Si necesitas que no lo sean, puedes usar el modificador `(?i)` al inicio del patrón. Por ejemplo: `r"(?i).*teoría.*"`.


## III. Ejecutar el script
 
Con el entorno virtual activo y `config.py` configurado, ejecuta el script con:
 
```bash
python main.py
```

En Linux/macOS, si es necesario, usa `python3 main.py`.

> ℹ️ **Dato realista:**
> Descargar los cursos (**2013 y 2020**) tomó aproximadamente **una hora y 15 minutos** 
> -*según un cronómetro*



## IV. Estructura del *output* (carpeta de descarga)

Todos los recursos se descargarán y organizarán con la siguiente estructura:

```

Descarga_cursos_historicos
│
├─ 2020-1 Nombre del curso (código-horario)
│ ├─ archivo_1.pdf
│ ├─ archivo_2.docx
│ └─ ...
│
├─ 2020-2 Nombre del curso (código-horario)
│ ├─ archivo_19.pdf
│ ├─ archivo_3.eaf
│ └─ ...
│
│─ ...
│
├─ 2013-1 Nombre del curso (código-horario)
│ └─ (vacío - algunos cursos no tienen archivos descargables)
│
└─ registro_descargas.xlsx

```
 
> 💡 **Recuerda:**
> El script descargará **todos los recursos disponibles** (PDFs, DOCX, PPTX,, etc.) de cada curso.


##  V. Sobre `registro_descargas.xlsx`
 
Dentro de la carpeta de descarga encontrarás un archivo llamado **`registro_descargas.xlsx`**, que:

- Contiene una lista de todos los enlaces de información disponibles por curso.
- Resalta aquellos elementos **que NO pudieron descargarse automáticamente**, como:

	- Grabaciones de Zoom.
	- Carpetas de Google Drive.
	- Carpetas internas de Paideia.
	- Enlaces a páginas web.
	
- Funciona como un **registro de control** y una guía para que puedas completar esas descargas manualmente si lo deseas.


## VI. Personalización y soporte  

El código está **comentado línea por línea** para que puedas **modificarlo y adaptarlo.

👉 **Si encuentras bugs, errores o cualquier problema durante la ejecución, o tienes sugerencias de mejora, no dudes en reportarlo.**

## Referencias 

> Este proyecto fue desarrollado utilizando asistencia de **GitHub Copilot** y **ChatGPT** para la redacción, depuración y documentación. 🤖

---

## ⚠️ Problemas comunes y soluciones

### 1. **Permisos insuficientes para crear archivos o carpetas**
   - **Problema**: El script intenta crear carpetas o archivos en un directorio donde no tienes permisos de escritura.
   - **Solución**: Asegúrate de que `DIRECTORIO_DESCARGAS` en `config.py` apunte a un directorio donde tengas permisos de escritura, como tu carpeta de usuario.

### 2. **Problemas con ChromeDriver**
   - **Problema**: El script no puede iniciar el navegador debido a permisos insuficientes para ejecutar ChromeDriver.
   - **Solución**: Asegúrate de que el archivo `chromedriver` tenga permisos de ejecución:
     - En Linux/macOS:
       ```bash
       chmod +x /ruta/a/chromedriver
       ```
     - En Windows:
       - Asegúrate de que `chromedriver.exe` esté ubicado en un directorio accesible y no protegido por el sistema.

### 3. **El sistema entra en suspensión**
   - **Problema**: El sistema se suspende durante la ejecución del script, interrumpiendo el proceso.
   - **Solución**: Configura tu sistema para evitar la suspensión mientras el script está en ejecución:
     - En Windows: Cambia la configuración de energía en el Panel de Control.
     - En macOS/Linux: Usa el comando `caffeinate`:
       ```bash
       caffeinate -i python main.py
       ```