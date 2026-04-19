from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from database import get_db
from models import User, CommunityPost
from schemas import CommunityPost as CommunityPostSchema, CommunityPostCreate
from auth import get_current_active_user

router = APIRouter(prefix="/api/community", tags=["Community"])


@router.get("/", response_model=List[CommunityPostSchema])
def get_community_posts(
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Get all community posts."""
    posts = db.query(CommunityPost).order_by(
        CommunityPost.created_at.desc()
    ).offset(skip).limit(limit).all()
    return posts


@router.post("/", response_model=CommunityPostSchema, status_code=status.HTTP_201_CREATED)
def create_post(
    post: CommunityPostCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Create a new community post."""
    db_post = CommunityPost(
        user_id=current_user.id,
        content=post.content
    )
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
    post_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_active_user)
):
    """Delete a community post (only by owner)."""
    post = db.query(CommunityPost).filter(CommunityPost.id == post_id).first()
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    
    if post.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not authorized to delete this post")
    
    db.delete(post)
    db.commit()
    return None

# Made with Bob
