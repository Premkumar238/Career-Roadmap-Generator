from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class CareerPathBase(BaseModel):
    name:str
    description: Optional[str]= None

class CareerPathCreate(CareerPathBase):
    pass

class CareerPathResponse(CareerPathBase):
    id:int
    created_at:datetime
    class Config:
        from_attributes = True

class SkillBase(BaseModel):
    name: str
    career_path_id: int
    level: Optional[str] = None

class SkillCreate(SkillBase):
    pass

class SkillResponse(SkillBase):
    id: int
    created_at:datetime
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password: str
    career_goal: Optional[str] = None
    experience_level: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    full_name: str
    email: EmailStr
    career_goal: Optional[str] = None
    experience_level: Optional[str] = None
    created_at: datetime
    class Config:
        from_attributes = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None


class CourseBase(BaseModel):
    title: str
    platform: Optional[str] = None
    url: Optional[str] = None
    duration: Optional[str] = None
    difficulty: Optional[str] = None
    career_path_id: Optional[int] = None

class CourseCreate(CourseBase):
    pass

class CourseResponse(CourseBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class CertificationBase(BaseModel):
    name: str
    provider: Optional[str] = None
    career_path_id: Optional[int] = None
    cost: Optional[str] = None
    duration: Optional[str] = None

class CertificationCreate(CertificationBase):
    pass

class CertificationResponse(CertificationBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class RoadmapBase(BaseModel):
    user_id: int
    career_path_id: int
    title: Optional[str] = None
    description: Optional[str] = None

class RoadmapCreate(RoadmapBase):
    pass

class RoadmapResponse(RoadmapBase):
    id: int
    created_at: datetime
    class Config:
        from_attributes = True

class ProgressBase(BaseModel):
    user_id: int
    course_id: int
    status: Optional[str] = None
    completion_percentage: Optional[int] = 0

class ProgressCreate(ProgressBase):
    pass

class ProgressResponse(ProgressBase):
    id: int
    started_at: Optional[datetime] = None
    completed_at: Optional[datetime] = None
    class Config:
        from_attributes = True