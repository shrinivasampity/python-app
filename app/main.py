from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Incident(BaseModel):
    title: str
    description: str

incidents = []

@app.get("/")
def health():
    return {"status": "ok"}

@app.post("/incident")
def create_incident(incident: Incident):
    data = incident.dict()
    data["id"] = len(incidents) + 1
    data["status"] = "open"
    incidents.append(data)
    return data

@app.get("/incidents")
def get_incidents():
    return incidents
