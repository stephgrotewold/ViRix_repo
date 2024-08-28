from sqlalchemy import Column, Integer, String, Date, Numeric
from database import Base

class CovidData(Base):
    __tablename__ = "covid_data"

    id = Column(Integer, primary_key=True, index=True)
    date_reported = Column(Date)
    country_code = Column(String(10))
    country = Column(String(100))
    who_region = Column(String(50))
    new_cases = Column(Integer)
    cumulative_cases = Column(Integer)
    new_deaths = Column(Integer)
    cumulative_deaths = Column(Integer)