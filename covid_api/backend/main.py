from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
import models, schemas, crud
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/covid-data", response_model=schemas.CovidData)
def read_covid_data(location: str, db: Session = Depends(get_db)):
    data = crud.get_covid_data_by_country(db, country=location)
    if data is None:
        raise HTTPException(status_code=404, detail="Data not found")
    return data