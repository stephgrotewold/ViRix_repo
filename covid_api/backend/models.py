from pydantic import BaseModel, Field
from bson import ObjectId
from typing import Optional, List

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

class CovidData(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    date_reported: Optional[str]
    country_code: Optional[str]
    country: Optional[str]
    who_region: Optional[str]
    new_cases: Optional[int]
    cumulative_cases: Optional[int]
    new_deaths: Optional[int]
    cumulative_deaths: Optional[int]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}

class HealthCenter(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    name: str
    address: Optional[str]
    phone_number: Optional[str]
    services: Optional[List[str]]
    latitude: Optional[float]
    longitude: Optional[float]

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}