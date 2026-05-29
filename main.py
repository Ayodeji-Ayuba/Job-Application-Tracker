from fastapi import FastAPI
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Job Application Tracker",
    description="API for tracking job applications",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"}