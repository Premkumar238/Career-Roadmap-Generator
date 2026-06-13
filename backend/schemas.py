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

