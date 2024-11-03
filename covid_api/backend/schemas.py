from pydantic import BaseModel, Field
from typing import Optional, List, Union
from bson import ObjectId

class PyObjectId(ObjectId):
    @classmethod
    def __get_pydantic_core_schema__(cls, source_type, handler):
        return handler(str)

    @classmethod
    def __get_pydantic_json_schema__(cls, schema):
        return {
            "type": "string",
            "format": "objectid"
        }

class HealthCenterBase(BaseModel):
    name: str
    address: str
    phone_number: str
    services: str
    latitude: float
    longitude: float

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class HealthCenter(HealthCenterBase):
    id: Optional[PyObjectId] = Field(default_factory=PyObjectId, alias="_id")

class HealthCenterCreate(HealthCenterBase):
    pass

class HealthCenterUpdate(BaseModel):
    name: Optional[str] = None
    address: Optional[str] = None
    phone_number: Optional[str] = None
    services: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class HealthCenterListResponse(BaseModel):
    centers: List[HealthCenter]
    total: int

# Esquema para los datos de COVID
class CovidData(BaseModel):
    country: str
    new_cases: Optional[int] = 0
    cumulative_cases: Optional[int] = 0
    new_deaths: Optional[int] = 0
    cumulative_deaths: Optional[int] = 0
    risk_level: Optional[str] = "Low"

    class Config:
        populate_by_name = True
        arbitrary_types_allowed = True

class CovidDataList(BaseModel):
    data: List[CovidData]