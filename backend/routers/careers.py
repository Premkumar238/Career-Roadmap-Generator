from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
import models
import schemas
from typing import List

router = APIRouter(
    prefix="/careers",
    tags=["Career Paths"]
)

@router.get("/", response_model=List[schemas.CareerPathResponse])
def get_all_careers(db: Session = Depends(get_db)):
    careers = db.query(models.CareerPath).all()
    return careers

@router.get("/{id}", response_model=schemas.CareerPathResponse)
def get_career(id: int, db: Session = Depends(get_db)):
    career = db.query(models.CareerPath).filter(
        models.CareerPath.id == id
    ).first()
    if not career:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Career path not found"
        )
    return career

@router.post("/", response_model=schemas.CareerPathResponse)
def create_career(career: schemas.CareerPathCreate, db: Session = Depends(get_db)):
    new_career = models.CareerPath(
        name=career.name,
        description=career.description
    )
    db.add(new_career)
    db.commit()
    db.refresh(new_career)
    return new_career

@router.put("/{id}", response_model=schemas.CareerPathResponse)
def update_career(id: int, updated_career: schemas.CareerPathCreate, db: Session = Depends(get_db)):
    career = db.query(models.CareerPath).filter(
        models.CareerPath.id == id
    ).first()
    if not career:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Career path not found"
        )
    career.name = updated_career.name
    career.description = updated_career.description
    db.commit()
    db.refresh(career)
    return career

@router.delete("/{id}")
def delete_career(id: int, db: Session = Depends(get_db)):
    career = db.query(models.CareerPath).filter(
        models.CareerPath.id == id
    ).first()
    if not career:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Career path not found"
        )
    db.delete(career)
    db.commit()
    return {"message": "Career path deleted successfully"}