from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, Progress, Module, Enrollment
from schemas import Progress as ProgressSchema, ProgressCreate, DashboardStats
from auth import get_current_active_user

router = APIRouter(prefix="/api/progress", tags=["Progress"])


@router.post("/", response_model=ProgressSchema, status_code=status.HTTP_201_CREATED)
def update_progress(
    progress: ProgressCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Update or create progress for a module."""
    # Check if module exists
    module = db.query(Module).filter(Module.id == progress.module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    # Check if progress already exists
    existing_progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.module_id == progress.module_id
    ).first()
    
    if existing_progress:
        # Update existing progress
        existing_progress.is_completed = progress.is_completed
        if progress.is_completed:
            from datetime import datetime
            existing_progress.completed_at = datetime.utcnow()
        db.commit()
        db.refresh(existing_progress)
        
        # Update course enrollment progress
        update_course_progress(db, current_user.id, module.course_id)
        
        return existing_progress
    else:
        # Create new progress
        db_progress = Progress(
            user_id=current_user.id,
            module_id=progress.module_id,
            is_completed=progress.is_completed
        )
        if progress.is_completed:
            from datetime import datetime
            db_progress.completed_at = datetime.utcnow()
        
        db.add(db_progress)
        db.commit()
        db.refresh(db_progress)
        
        # Update course enrollment progress
        update_course_progress(db, current_user.id, module.course_id)
        
        return db_progress


@router.get("/dashboard", response_model=DashboardStats)
def get_dashboard_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get dashboard statistics for the current user."""
    # Get all enrollments
    enrollments = db.query(Enrollment).filter(Enrollment.user_id == current_user.id).all()
    
    total_courses = len(enrollments)
    completed_courses = len([e for e in enrollments if e.progress_percentage == 100])
    in_progress_courses = len([e for e in enrollments if 0 < e.progress_percentage < 100])
    
    # Get achievements count (placeholder - implement achievements logic)
    total_achievements = 0
    
    # Calculate overall progress
    if total_courses > 0:
        overall_progress = sum(e.progress_percentage for e in enrollments) / total_courses
    else:
        overall_progress = 0.0
    
    return {
        "total_courses": total_courses,
        "completed_courses": completed_courses,
        "in_progress_courses": in_progress_courses,
        "total_achievements": total_achievements,
        "overall_progress": overall_progress
    }


def update_course_progress(db: Session, user_id: int, course_id: int):
    """Helper function to update course enrollment progress percentage."""
    # Get total modules for the course
    total_modules = db.query(Module).filter(Module.course_id == course_id).count()
    
    if total_modules == 0:
        return
    
    # Get completed modules
    completed_modules = db.query(Progress).join(Module).filter(
        Progress.user_id == user_id,
        Module.course_id == course_id,
        Progress.is_completed == True
    ).count()
    
    # Calculate progress percentage
    progress_percentage = (completed_modules / total_modules) * 100
    
    # Update enrollment
    enrollment = db.query(Enrollment).filter(
        Enrollment.user_id == user_id,
        Enrollment.course_id == course_id
    ).first()
    
    if enrollment:
        enrollment.progress_percentage = progress_percentage
        if progress_percentage == 100:
            from datetime import datetime
            enrollment.completed_at = datetime.utcnow()
        db.commit()

# Made with Bob
