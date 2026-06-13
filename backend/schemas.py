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
