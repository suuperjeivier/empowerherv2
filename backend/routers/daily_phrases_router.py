from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func
from database import get_db
from models import User, DailyPhrase, UserDailyPhrase
from schemas import DailyPhrase as DailyPhraseSchema
from auth import get_current_active_user
from datetime import datetime, timedelta

router = APIRouter(prefix="/api/daily-phrases", tags=["Daily Phrases"])


@router.get("/today", response_model=DailyPhraseSchema)
def get_daily_phrase(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get the daily phrase for the current user."""
    today = datetime.utcnow().date()
    
    # Check if user already has a phrase for today
    user_phrase = db.query(UserDailyPhrase).join(DailyPhrase).filter(
        UserDailyPhrase.user_id == current_user.id,
        func.date(UserDailyPhrase.shown_date) == today
    ).first()
    
    if user_phrase:
        return user_phrase.phrase
    
    # Get a random phrase that hasn't been shown to the user recently (last 30 days)
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)
    
    shown_phrase_ids = db.query(UserDailyPhrase.phrase_id).filter(
        UserDailyPhrase.user_id == current_user.id,
        UserDailyPhrase.shown_date >= thirty_days_ago
    ).all()
    shown_ids = [pid[0] for pid in shown_phrase_ids]
    
    # Get a random phrase not in the shown list
    query = db.query(DailyPhrase)
    if shown_ids:
        query = query.filter(~DailyPhrase.id.in_(shown_ids))
    
    phrase = query.order_by(func.random()).first()
    
    if not phrase:
        # If all phrases have been shown, get any random phrase
        phrase = db.query(DailyPhrase).order_by(func.random()).first()
    
    if not phrase:
        raise HTTPException(status_code=404, detail="No daily phrases available")
    
    # Record that this phrase was shown to the user
    user_phrase_record = UserDailyPhrase(
        user_id=current_user.id,
        phrase_id=phrase.id
    )
    db.add(user_phrase_record)
    db.commit()
    
    return phrase


@router.get("/", response_model=List[DailyPhraseSchema])
def get_all_phrases(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all daily phrases (for browsing)."""
    phrases = db.query(DailyPhrase).offset(skip).limit(limit).all()
    return phrases

# Made with Bob
