from pydantic import BaseModel
from typing import Optional, List

class CovidData(BaseModel):
    country: str
    new_cases: Optional[int] = 0
    cumulative_cases: Optional[int] = 0
    new_deaths: Optional[int] = 0
    cumulative_deaths: Optional[int] = 0
    risk_level: Optional[str] = "Low"  # Add risk_level if not already present

    class Config:
        orm_mode = True

# Wrapper for returning a list of CovidData
class CovidDataList(BaseModel):
    data: List[CovidData]

class HealthCenterBase(BaseModel):
    name: str
    address: str
    phone_number: str
    services: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True

# Esquema base para HealthCenter (común para creación y actualización)
class HealthCenterBase(BaseModel):
    name: str
    address: str
    phone_number: str
    services: str
    latitude: float
    longitude: float

    class Config:
        orm_mode = True


# Esquema para la creación de un nuevo centro de salud
class HealthCenterCreate(HealthCenterBase):
    pass


# Esquema para la actualización de un centro de salud existente
class HealthCenterUpdate(HealthCenterBase):
    pass


# Esquema que incluye el ID, usado para las respuestas (GET)
class HealthCenter(HealthCenterBase):
    id: int  # Incluir el ID del centro de salud