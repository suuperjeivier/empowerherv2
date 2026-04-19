from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, Course, Module, Enrollment, Progress
from schemas import (
    Course as CourseSchema,
    CourseCreate,
    Module as ModuleSchema,
    Enrollment as EnrollmentSchema,
    EnrollmentCreate,
    CourseProgress
)
from auth import get_current_active_user

router = APIRouter(prefix="/api/courses", tags=["Courses"])


@router.get("/", response_model=List[CourseSchema])
def get_courses(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all available courses."""
    courses = db.query(Course).filter(Course.is_active == True).offset(skip).limit(limit).all()
    return courses


@router.get("/{course_id}", response_model=CourseSchema)
def get_course(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get a specific course by ID."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return course


@router.get("/{course_id}/modules", response_model=List[ModuleSchema])
def get_course_modules(
    course_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all modules for a specific course."""
    course = db.query(Course).filter(Course.id == course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    modules = db.query(Module).filter(Module.course_id == course_id).order_by(Module.order).all()
    return modules


@router.post("/enroll", response_model=EnrollmentSchema, status_code=status.HTTP_201_CREATED)
def enroll_in_course(
    enrollment: EnrollmentCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Enroll current user in a course."""
    # Check if course exists
    course = db.query(Course).filter(Course.id == enrollment.course_id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    
    # Check if already enrolled
    existing_enrollment = db.query(Enrollment).filter(
        Enrollment.user_id == current_user.id,
        Enrollment.course_id == enrollment.course_id
    ).first()
    
    if existing_enrollment:
        raise HTTPException(status_code=400, detail="Already enrolled in this course")
    
    # Create enrollment
    db_enrollment = Enrollment(
        user_id=current_user.id,
        course_id=enrollment.course_id
    )
    db.add(db_enrollment)
    db.commit()
    db.refresh(db_enrollment)
    return db_enrollment


@router.get("/my-courses", response_model=List[CourseProgress])
def get_my_courses(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all courses the current user is enrolled in with progress."""
    enrollments = db.query(Enrollment).filter(
        Enrollment.user_id == current_user.id
    ).all()
    
    result = []
    for enrollment in enrollments:
        course = db.query(Course).filter(Course.id == enrollment.course_id).first()
        total_modules = db.query(Module).filter(Module.course_id == course.id).count()
        completed_modules = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.module_id.in_(
                db.query(Module.id).filter(Module.course_id == course.id)
            ),
            Progress.is_completed == True
        ).count()
        
        result.append({
            "course": course,
            "progress_percentage": enrollment.progress_percentage,
            "completed_modules": completed_modules,
            "total_modules": total_modules
        })
    
    return result


@router.post("/", response_model=CourseSchema, status_code=status.HTTP_201_CREATED)
def create_course(
    course: CourseCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new course (admin only)."""
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Not authorized")
    
    db_course = Course(**course.dict())
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

# Made with Bob
