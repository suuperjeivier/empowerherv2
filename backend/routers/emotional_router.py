from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, EmotionalLog
from schemas import EmotionalLog as EmotionalLogSchema, EmotionalLogCreate
from auth import get_current_active_user

router = APIRouter(prefix="/api/emotional", tags=["Emotional Tracking"])


@router.get("/", response_model=List[EmotionalLogSchema])
def get_emotional_logs(
    skip: int = 0,
    limit: int = 30,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get emotional logs for the current user."""
    logs = db.query(EmotionalLog).filter(
        EmotionalLog.user_id == current_user.id
    ).order_by(EmotionalLog.created_at.desc()).offset(skip).limit(limit).all()
    return logs


@router.post("/", response_model=EmotionalLogSchema, status_code=status.HTTP_201_CREATED)
def create_emotional_log(
    log: EmotionalLogCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new emotional log entry."""
    db_log = EmotionalLog(
        user_id=current_user.id,
        emotional_state=log.emotional_state,
        note=log.note
    )
    db.add(db_log)
    db.commit()
    db.refresh(db_log)
    return db_log

# Made with Bob
