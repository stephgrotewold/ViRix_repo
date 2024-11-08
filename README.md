# ViRix - COVID-19 Information and Tracking WebApp

ViRix is a web application designed to provide up-to-date and accurate information about COVID-19, including prevention tips, news, and statistical data for countries around the world. The app includes interactive map visualizations and other useful information to help users stay informed about the pandemic.

# Documentación del Proyecto

## 1. Introducción

Este proyecto está dividido en dos partes: un frontend desarrollado en **React** y un backend en **FastAPI**, incialmente con SQL y actualmente con MongoDB.

## 2. Estructura del Proyecto

### Frontend

- **App.js / App.css**: Configuración y estilos principales de la aplicación React.
- **index.js / index.css**: Punto de entrada y configuración inicial.
- **components**: Contiene componentes reutilizables que conforman la interfaz de usuario.

### Backend

- **main.py**: Archivo de entrada del backend, inicia la aplicación FastAPI.
- **config.py**: Configuración general, posiblemente cargue variables de entorno o ajustes globales.
- **models.py**: Define las clases de datos que representan las tablas o entidades.
- **database.py**: Maneja la conexión a la base de datos.
- **constants.py**: Almacena constantes utilizadas en la aplicación.
- **schemas.py**: Define los esquemas de datos para validación de entrada y salida.
- **repositories.py** y **crud.py**: Contienen funciones para realizar operaciones CRUD (Create, Read, Update, Delete) sobre las entidades del sistema.
- **profile_script.py**: Un script de profiling para medir y analizar el rendimiento.
- **migration**: Scripts o configuraciones para manejar migraciones de base de datos.

## 3. Instalación y Configuración

### Requisitos

- **Node.js** (para el frontend)
- **Python 3.x** y las librerías necesarias (para el backend)

### Instrucciones de Instalación

#### Frontend

1. Navega a la carpeta `frontend`.
2. Ejecuta `npm install` para instalar las dependencias.
3. Usa `npm start` para iniciar la aplicación.

#### Backend

1. Navega a la carpeta `backend`.
2. Instala las dependencias con:

   ```bash
   pip install -r requirements.txt

   Configura las variables de entorno en `config.py` o en un archivo `.env`.

   Inicia el backend con:

   ```bash
   uvicorn main:app --reload

### 4. Funcionalidades Clave

#### Frontend

- **Componentes de Interfaz**: Describe cada componente en la carpeta `components`.

#### Backend

- **API Endpoints (FastAPI)**: Lista y describe los endpoints principales de FastAPI.
- **Operaciones CRUD**: Describe las funciones en `crud.py` y `repositories.py`.
- **Conexión a la Base de Datos**: Explica cómo `database.py` gestiona la conexión.

### 5. Scripts Adicionales

- **profile_script.py**: Herramienta para analizar el rendimiento de la aplicación, incluye cómo usarlo y ejemplos.

### 6. Migraciones de Base de Datos

Instrucciones para aplicar migraciones, incluyendo comandos y scripts en la carpeta `migration`.

### API Integration

The project integrates with the following APIs to fetch real-time data and news:

1. **News API**: Fetches the latest news articles related to COVID-19.
   - Endpoint: `https://newsapi.org/v2/everything?q=COVID-19`

Ensure you have valid API keys for these services and update them in the project files.

