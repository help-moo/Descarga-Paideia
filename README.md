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
USERNAME = '' 
PASSWORD = '' 
DOWNLOAD_DIR = ''
```

- **USERNAME:** tu usuario de la plataforma Paideia.
- **PASSWORD:** tu contraseña de Paideia.
- **DOWNLOAD_DIR:** *(opcional)* Si lo dejas vacío (`''`), la carpeta de descarga será el mismo directorio donde se encuentra `main.py`.
 
> ⚠️ **Importante:**
> Por seguridad, los datos de `USERNAME` y `PASSWORD` se eliminarán automáticamente del `config.py` al finalizar la ejecución del script.


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