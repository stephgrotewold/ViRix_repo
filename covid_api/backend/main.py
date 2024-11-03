
# from sqlalchemy.orm import Session
# from sqlalchemy import func
# from database import SessionLocal, engine, get_db
# from models import HealthCenter


from fastapi import Depends, FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pymongo.database import Database
from bson import ObjectId
from config import get_database, get_collection
import crud, models
from schemas import (
    HealthCenter,
    HealthCenterCreate,
    HealthCenterUpdate,
    HealthCenterListResponse
)

app = FastAPI()
db = get_database()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Dependencia para obtener la base de datos
def get_db():
    return db

@app.get("/health_centers/")
def get_health_centers(
    skip: int = 0,
    limit: int = 100,
    db: Database = Depends(get_database)
):
    try:
        result = crud.get_health_centers(skip=skip, limit=limit)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/health_centers/")
async def create_health_center(
    health_center: HealthCenterCreate,
    db: Database = Depends(get_database)
):
    try:
        created_center = crud.create_health_center(db, health_center)
        if not created_center:
            raise HTTPException(
                status_code=500,
                detail="Error creating health center"
            )
        return created_center
    except ValueError as e:
        raise HTTPException(
            status_code=422,
            detail=str(e)
        )
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred: {str(e)}"
        )

@app.put("/health_centers/{center_id}")
async def update_health_center(
    center_id: str,
    center: HealthCenterUpdate,
    db: Database = Depends(get_database)
):
    try:
        # Convertir el modelo Pydantic a diccionario
        update_data = center.model_dump(exclude_unset=True)
        
        # Actualizar el centro de salud
        updated_center = crud.update_health_center(db, center_id, update_data)
        
        if not updated_center:
            raise HTTPException(
                status_code=404,
                detail="Health center not found or no changes applied"
            )
        return updated_center
    except Exception as e:
        raise HTTPException(
            status_code=422,
            detail=f"Could not update health center: {str(e)}"
        )

@app.delete("/health_centers/{center_id}")
async def delete_health_center(
    center_id: str,
    db: Database = Depends(get_database)
):
    try:
        if not ObjectId.is_valid(center_id):
            raise HTTPException(
                status_code=422,
                detail="Invalid center ID format"
            )
        
        success = crud.remove_health_center(db, center_id)
        if success:
            return {"message": "Health center deleted successfully"}
        else:
            raise HTTPException(
                status_code=404,
                detail="Health center not found"
            )
    except Exception as e:
        raise HTTPException(status_code=422, detail=str(e))

@app.get("/covid-data")
def read_covid_data(
    location: str,
    db: Database = Depends(get_db)
):
    data = crud.get_covid_data_by_country(db["covid_data"], country=location)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data

@app.get("/heatmap-data")
def get_heatmap_data(db: Database = Depends(get_db)):
    try:
        collection = db["covid_data"]
        data = crud.get_heatmap_data(collection)
        
        if not data:
            print("No heatmap data found")
            return []
            
        print(f"Returning {len(data)} records for heatmap")
        return data
    except Exception as e:
        print(f"Error in heatmap endpoint: {e}")
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
# # Crear las tablas en la base de datos
# models.Base.metadata.create_all(bind=engine)

# app = FastAPI()

# # Configurar CORS
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Permitir todas las URLs, puedes restringir a dominios específicos en producción
#     allow_credentials=True,
#     allow_methods=["*"],  # Permitir todos los métodos (GET, POST, PUT, DELETE, etc.)
#     allow_headers=["*"],  # Permitir todos los encabezados
# )


# # Dependencia para la base de datos
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# # Ruta para obtener los datos de COVID por país
# @app.get("/covid-data", response_model=schemas.CovidData)
# def read_covid_data(location: str, db: Session = Depends(get_db)):
#     data = crud.get_covid_data_by_country(db, country=location)
#     if data is None:
#         raise HTTPException(status_code=404, detail="Data not found")
#     return data


# # Ruta para obtener los datos del mapa de calor
# @app.get("/heatmap-data", response_model=List[schemas.CovidData])
# def get_heatmap_data(db: Session = Depends(get_db)):
#     try:
#         # Obtener datos agregados por país
#         data = crud.get_heatmap_data(db)
#         if not data:
#             raise HTTPException(status_code=404, detail="Data not found")
#         return data
#     except Exception as e:
#         # Captura y muestra el error en la consola
#         print(f"Error al obtener los datos: {e}")
#         raise HTTPException(status_code=500, detail="Internal Server Error")

# # Ruta para crear un nuevo centro de salud
# @app.post("/health_centers/", response_model=schemas.HealthCenterCreate)
# def create_health_center(health_center: schemas.HealthCenterCreate, db: Session = Depends(get_db)):
#     return crud.create_health_center(db, health_center)


# # Ruta para obtener una lista de centros de salud
# @app.get("/health_centers/")
# def get_health_centers(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     total_centers = db.query(HealthCenter).count()  # Total de registros sin paginación
#     centers = db.query(HealthCenter).offset(skip).limit(limit).all()  # Registros paginados
#     return {"centers": centers, "total": total_centers}  # Incluye el total en la respuesta


# @app.put("/health_centers/{center_id}", response_model=schemas.HealthCenterBase)
# def update_health_center(center_id: int, updated_data: schemas.HealthCenterUpdate, db: Session = Depends(get_db)):
#     print(f"ID recibido para actualización: {center_id}")  # Registro de depuración
#     print(f"Datos recibidos para actualizar: {updated_data}")  # Registro de depuración
    
#     center = crud.update_health_center(db, center_id, updated_data)
#     if not center:
#         raise HTTPException(status_code=404, detail="Health center not found")
#     return center


# @app.delete("/health_centers/{center_id}")
# def delete_health_center(center_id: int, db: Session = Depends(get_db)):
#     print(f"ID recibido para eliminar: {center_id}")  # Registro de depuración
    
#     success = crud.delete_health_center(db, center_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Health center not found")
#     return {"message": "Health center deleted successfully"}