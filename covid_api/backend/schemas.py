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