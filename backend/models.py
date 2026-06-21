from sqlalchemy import Column, Integer, String, Text, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from database import Base

class CareerPath(Base):
    __tablename__ = "career_paths"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

class Skill(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    career_path_id = Column(Integer, ForeignKey("career_paths.id"))
    level = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    career_goal = Column(String(100))
    experience_level = Column(String(20))
    created_at = Column(TIMESTAMP, server_default=func.now())

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    platform = Column(String(100))
    url = Column(Text)
    duration = Column(String(50))
    difficulty = Column(String(20))
    career_path_id = Column(Integer, ForeignKey("career_paths.id"))
    created_at = Column(TIMESTAMP, server_default=func.now())

class Certification(Base):
    __tablename__ = "certifications"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200), nullable=False)
    provider = Column(String(100))
    career_path_id = Column(Integer, ForeignKey("career_paths.id"))
    cost = Column(String(50))
    duration = Column(String(50))
    created_at = Column(TIMESTAMP, server_default=func.now())

class Roadmap(Base):
    __tablename__ = "roadmaps"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    career_path_id = Column(Integer, ForeignKey("career_paths.id"))
    title = Column(String(200))
    description = Column(Text)
    created_at = Column(TIMESTAMP, server_default=func.now())

class ProgressTracking(Base):
    __tablename__ = "progress_tracking"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    course_id = Column(Integer, ForeignKey("courses.id"))
    status = Column(String(20))
    completion_percentage = Column(Integer, default=0)
    started_at = Column(TIMESTAMP)
    completed_at = Column(TIMESTAMP)