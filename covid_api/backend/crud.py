from sqlalchemy.orm import Session
from typing import Optional  # Agregar esta línea para importar Optional
from repositories import HealthCenterRepository, CovidDataRepository
import schemas
from models import HealthCenter


# Función para obtener datos de COVID por país
def get_covid_data_by_country(db: Session, country: str):
    repo = CovidDataRepository(db)
    data = repo.get_by_country(country)
    if data:
        return {
            'country': data.country,
            'new_cases': data.new_cases or 0,
            'cumulative_cases': data.cumulative_cases or 0,
            'new_deaths': data.new_deaths or 0,
            'cumulative_deaths': data.cumulative_deaths or 0,
        }
    return None


# Función para obtener datos para el mapa de calor
def get_heatmap_data(db: Session):
    repo = CovidDataRepository(db)
    data = repo.get_heatmap_data()
    return [
        {
            'country': item.country,
            'cumulative_cases': item.cumulative_cases or 0,
            'cumulative_deaths': item.cumulative_deaths or 0,
            'new_cases': item.new_cases or 0,
            'new_deaths': item.new_deaths or 0,
        }
        for item in data
    ]


# Funciones CRUD para HealthCenter
def create_health_center(db: Session, health_center: schemas.HealthCenterCreate):
    repo = HealthCenterRepository(db)
    db_center = HealthCenter(**health_center.dict())
    return repo.add(db_center)


def get_health_centers(db: Session, skip: int = 0, limit: int = 10, services: Optional[str] = None):
    repo = HealthCenterRepository(db)
    return repo.get_with_filter(services=services, skip=skip, limit=limit)


def update_health_center(db: Session, center_id: int, updated_data: schemas.HealthCenterUpdate):
    repo = HealthCenterRepository(db)
    center = repo.get(HealthCenter, center_id)
    if not center:
        return None

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(center, key, value)

    return repo.update(center)


def delete_health_center(db: Session, center_id: int):
    repo = HealthCenterRepository(db)
    center = repo.get(HealthCenter, center_id)
    if not center:
        return False

    repo.delete(center)
    return True