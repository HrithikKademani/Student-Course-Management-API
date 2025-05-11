from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime

class StudentBase(BaseModel):
    name: str
    email: EmailStr

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int
    courses: List[str] = []

    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    title: str
    description: str

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    id: int
    students: List[str] = []

    class Config:
        orm_mode = True

class EnrollRequest(BaseModel):
    student_id: int
    course_id: int