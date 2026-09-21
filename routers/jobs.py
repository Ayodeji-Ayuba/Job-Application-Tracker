from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from models.models import JobApplication, User
from schemas.schemas import ApplicationCreate, ApplicationResponse
from utils.auth import get_db, get_current_user

router = APIRouter(prefix="/jobs", tags=["jobs"])

@router.post("/", response_model=ApplicationResponse)
def create_job(job: ApplicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_job = JobApplication(
        user_id=current_user.id,
        company=job.company,
        role=job.role,
        country=job.country,
        status=job.status,
        date_applied=job.date_applied,
        notes=job.notes
    )

    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    return new_job

@router.get("/", response_model=list[ApplicationResponse])
def return_jobs(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    user_jobs = db.query(JobApplication).filter(JobApplication.user_id == current_user.id).all()
    return user_jobs

@router.get("/{job_id}", response_model=ApplicationResponse)
def return_job(job_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = db.query(JobApplication).filter(JobApplication.id == job_id, JobApplication.user_id == current_user.id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job application not found")
    return job

@router.put("/{job_id}", response_model=ApplicationResponse)
def update_job(job_id: int, job_update: ApplicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = db.query(JobApplication).filter(JobApplication.id == job_id, JobApplication.user_id == current_user.id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job application not found")

    job.company = job_update.company
    job.role = job_update.role
    job.country = job_update.country
    job.status = job_update.status
    job.date_applied = job_update.date_applied
    job.notes = job_update.notes

    db.commit()
    db.refresh(job)

    return job

@router.delete("/{job_id}")
def delete_job(job_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job = db.query(JobApplication).filter(JobApplication.id == job_id, JobApplication.user_id == current_user.id).first()
    if not job:
        raise HTTPException(status_code=404, detail="Job application not found")

    db.delete(job)
    db.commit()

    return {"detail": "Job application deleted successfully"}