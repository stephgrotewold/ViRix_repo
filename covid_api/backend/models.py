# from sqlalchemy import Column, Integer, String, Date, Numeric
# from database import Base

from pydantic import BaseModel, Field
from bson import ObjectId
from pydantic.errors import PydanticUserError
from typing import Optional, List, Union

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


# class CovidData(Base):
#     __tablename__ = "covid_data"

#     id = Column(Integer, primary_key=True, index=True)
#     date_reported = Column(Date)
#     country_code = Column(String(10))
#     country = Column(String(100))
#     who_region = Column(String(50))
#     new_cases = Column(Integer)
#     cumulative_cases = Column(Integer)
#     new_deaths = Column(Integer)
#     cumulative_deaths = Column(Integer)

# class HealthCenter(Base):
#     __tablename__ = "health_centers"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String, index=True)
#     address = Column(String)
#     phone_number = Column(String)
#     services = Column(String)
#     latitude = Column(Numeric(10, 8))
#     longitude = Column(Numeric(11, 8))