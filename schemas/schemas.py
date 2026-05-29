from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class UserCreate(BaseModel):
    email: str
    password: str


class UserResponse(BaseModel):
    id: int
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class ApplicationCreate(BaseModel):
    company: str
    role: str
    country: str
    status: str
    date_applied: datetime
    notes: Optional[str] = None

class ApplicationResponse(BaseModel):
    id: int
    user_id: int
    company: str
    role: str
    country: str
    status: str
    date_applied: datetime
    notes: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True