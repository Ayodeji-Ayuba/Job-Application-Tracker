from fastapi import FastAPI
from dotenv import load_dotenv
from routers.auth import router as auth_router



load_dotenv()

app = FastAPI(
    title="Job Application Tracker",
    description="API for tracking job applications",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "ok"} 

app.include_router(auth_router)


