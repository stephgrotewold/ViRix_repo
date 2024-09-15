from pydantic import BaseModel
from typing import Optional

class CovidData(BaseModel):
    country: str
    new_cases: Optional[int] = 0
    cumulative_cases: Optional[int] = 0
    new_deaths: Optional[int] = 0
    cumulative_deaths: Optional[int] = 0

    class Config:
        orm_mode = True