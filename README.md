# ViRix

ViRix es una aplicación web diseñada para proporcionar información actualizada y precisa sobre COVID-19, incluyendo consejos de prevención, noticias y datos estadísticos de países de todo el mundo. La aplicación incluye visualizaciones interactivas de mapas y otra información útil como centros de salud por pais y los servicios que ofrecen para ayudar a los usuarios a mantenerse informados sobre la pandemia.

# Bitácora
Link a la historia de ViRix, incluyendo features, problemas y sus soluciones de una manera cronológica. 
```bash
https://gamma.app/docs/Bitacora-de-ViRix-u2n5mlebvoplcay
```
# Load Testing y Profiling
Un breve resumen de los hallazgos de las pruebas:
```bash
https://www.canva.com/design/DAGWf1hZNGU/G5Y2ksN2iji1i7f6YvyTRw/edit?utm_content=DAGWf1hZNGU&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton
```
Aqui esta el detalle de las pruebas realizadas de SQL vs MongoDB:
```bash
https://docs.google.com/document/d/1VRjic3-vr7f4FP5YZQRdxqbkiIcAC81TeFs9VfrgT7Y/edit?usp=sharing
```
# Documentación del Proyecto

## 1. Introducción

Este proyecto está dividido en dos partes: un frontend desarrollado en **React** y un backend en **FastAPI**, incialmente con **postgresql** y actualmente con **MongoDB**.

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

## 3. Instalación y Configuración

### Requisitos

- **Node.js** (para el frontend)
- **Python 3.x** y las librerías necesarias (para el backend)

### Instrucciones de Instalación

1. En la raiz del proyecto instala las dependencias con:
   ```bash
   pip install -r requirements.txt
   ```
#### Backend

1. Navega a la carpeta `backend`.
2. Inicia el backend con:
   ```bash
   uvicorn main:app --reload
   ```
#### Frontend

1. Navega a la carpeta `frontend`.
2. Ejecuta `npm install` para instalar las dependencias.
3. Ejecuta `npm install react-phone-input-2` y `npm install leaflet.heat`
4. Usa `npm start` para iniciar la aplicación.

### 4. Funcionalidades Clave

#### Frontend

- **Componentes de Interfaz**: Describe cada componente en la carpeta `components`.

#### Backend

- **API Endpoints (FastAPI)**: Lista y describe los endpoints principales de FastAPI.
- **Operaciones CRUD**: Describe las funciones en `crud.py` y `repositories.py`.
- **Conexión a la Base de Datos**: Explica cómo `database.py` gestiona la conexión.

### 5. Scripts Adicionales

- **profile_script.py**: Herramienta para analizar el rendimiento de la aplicación, incluye cómo usarlo y ejemplos.
- **migration**: En esta carpeta se encuentran los scripts utilizados para migrar a mongoDB.
- **locustfile.py**: Estan los tasks que se utilizaron para realizar en LoadTesting.

### API Integration

El proyecto se integra con las siguientes APIs para obtener datos en tiempo real y noticias:

1. **News API**: Obtiene los últimos artículos de noticias relacionados con COVID-19.
   - Endpoint: `https://newsapi.org/v2/everything?q=COVID-19`
  

#### Notas
En caso se quiere probar la versión solo aplicada con SQL se encuentra en el Commit fc0529e, el cual fue el último update antes de la migración. Seguir los mismos pasos del backend y frontend para poder levantarlo. 
```bash
https://github.com/stephgrotewold/ViRix_repo/tree/fc0529e5acc49fadbf8302ec2e9757c88d13a2c3
```



