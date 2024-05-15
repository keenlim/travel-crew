from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from crew import My_Crew
import json

class Inputs(BaseModel):
    country : str
    interests : str
    number_of_days : str

app = FastAPI()

@app.post("/travelplan/")
async def create_plan(inputs : Inputs):
    data = inputs.model_dump()
    country = data["country"]
    interests = data["interests"]
    numberofdays = data["number_of_days"]
    
    trip_crew = My_Crew(country, interests, numberofdays)
    result = trip_crew.run()
    return {"result":result}