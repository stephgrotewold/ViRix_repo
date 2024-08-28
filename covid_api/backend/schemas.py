from pydantic import BaseModel
from typing import Optional

class CovidDataBase(BaseModel):
    country: str
    new_cases: Optional[int] = 0
    cumulative_cases: Optional[int] = 0
    new_deaths: Optional[int] = 0
    cumulative_deaths: Optional[int] = 0

    class Config:
        from_attributes = True

class CovidData(CovidDataBase):
    class Config:
        from_attributes = True