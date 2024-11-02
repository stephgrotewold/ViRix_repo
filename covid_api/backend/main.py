from fastapi import Depends, FastAPI, HTTPException, Query
from sqlalchemy.orm import Session
from sqlalchemy import func
import models, schemas, crud
from database import SessionLocal, engine, get_db
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from line_profiler import profile
from models import HealthCenter


# Crear las tablas en la base de datos
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permitir todas las URLs, puedes restringir a dominios específicos en producción
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

# Dependencia para la base de datos
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@profile
# Ruta para obtener los datos de COVID por país
@app.get("/covid-data", response_model=schemas.CovidData)
def read_covid_data(location: str, db: Session = Depends(get_db)):
    data = crud.get_covid_data_by_country(db, country=location)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@profile
# Ruta para obtener los datos del mapa de calor
@app.get("/heatmap-data", response_model=List[schemas.CovidData])
def get_heatmap_data(db: Session = Depends(get_db)):
    try:
        # Obtener datos agregados por país
        data = crud.get_heatmap_data(db)
        if not data:
            raise HTTPException(status_code=404, detail="Data not found")
        return data
    except Exception as e:
        # Captura y muestra el error en la consola
        print(f"Error al obtener los datos: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")
@profile
# Ruta para crear un nuevo centro de salud
@app.post("/health_centers/", response_model=schemas.HealthCenterCreate)
def create_health_center(health_center: schemas.HealthCenterCreate, db: Session = Depends(get_db)):
    return crud.create_health_center(db, health_center)

@profile
# Ruta para obtener una lista de centros de salud
@app.get("/health_centers/")
def get_health_centers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    total_centers = db.query(HealthCenter).count()  # Total de registros sin paginación
    centers = db.query(HealthCenter).offset(skip).limit(limit).all()  # Registros paginados
    return {"centers": centers, "total": total_centers}  # Incluye el total en la respuesta

@profile
@app.put("/health_centers/{center_id}", response_model=schemas.HealthCenterBase)
def update_health_center(center_id: int, updated_data: schemas.HealthCenterUpdate, db: Session = Depends(get_db)):
    print(f"ID recibido para actualización: {center_id}")  # Registro de depuración
    print(f"Datos recibidos para actualizar: {updated_data}")  # Registro de depuración
    
    center = crud.update_health_center(db, center_id, updated_data)
    if not center:
        raise HTTPException(status_code=404, detail="Health center not found")
    return center

@profile
@app.delete("/health_centers/{center_id}")
def delete_health_center(center_id: int, db: Session = Depends(get_db)):
    print(f"ID recibido para eliminar: {center_id}")  # Registro de depuración
    
    success = crud.delete_health_center(db, center_id)
    if not success:
        raise HTTPException(status_code=404, detail="Health center not found")
    return {"message": "Health center deleted successfully"}