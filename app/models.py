from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

enrollment_table = Table(
    'enrollments', Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('course_id', Integer, ForeignKey('courses.id')),
    Column('enrolled_on', DateTime, default=datetime.utcnow)
)

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    courses = relationship('Course', secondary=enrollment_table, back_populates='students')

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(Text)
    students = relationship('Student', secondary=enrollment_table, back_populates='courses')