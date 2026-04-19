from pydantic import BaseModel, EmailStr, Field
from typing import Optional, List
from datetime import datetime
from models import UserRole, EmotionalState


# User Schemas
class UserBase(BaseModel):
    email: EmailStr
    username: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class User(UserBase):
    id: int
    role: UserRole
    is_active: bool
    profile_image: Optional[str] = None
    created_at: datetime

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# Course Schemas
class CourseBase(BaseModel):
    title: str
    description: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    duration_hours: Optional[int] = None
    difficulty_level: Optional[str] = None


class CourseCreate(CourseBase):
    pass


class Course(CourseBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True


# Module Schemas
class ModuleBase(BaseModel):
    title: str
    description: Optional[str] = None
    order: int
    is_locked: bool = False


class ModuleCreate(ModuleBase):
    course_id: int


class Module(ModuleBase):
    id: int
    course_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Lesson Schemas
class LessonBase(BaseModel):
    title: str
    content: Optional[str] = None
    video_url: Optional[str] = None
    order: int
    duration_minutes: Optional[int] = None


class LessonCreate(LessonBase):
    module_id: int


class Lesson(LessonBase):
    id: int
    module_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Enrollment Schemas
class EnrollmentBase(BaseModel):
    course_id: int


class EnrollmentCreate(EnrollmentBase):
    pass


class Enrollment(EnrollmentBase):
    id: int
    user_id: int
    enrolled_at: datetime
    completed_at: Optional[datetime] = None
    progress_percentage: float

    class Config:
        from_attributes = True


# Progress Schemas
class ProgressBase(BaseModel):
    module_id: int
    is_completed: bool = False


class ProgressCreate(ProgressBase):
    pass


class Progress(ProgressBase):
    id: int
    user_id: int
    completed_at: Optional[datetime] = None
    created_at: datetime

    class Config:
        from_attributes = True


# Achievement Schemas
class AchievementBase(BaseModel):
    title: str
    description: Optional[str] = None
    icon: Optional[str] = None


class Achievement(AchievementBase):
    id: int
    user_id: int
    earned_at: datetime

    class Config:
        from_attributes = True


# Emotional Log Schemas
class EmotionalLogBase(BaseModel):
    emotional_state: EmotionalState
    note: Optional[str] = None


class EmotionalLogCreate(EmotionalLogBase):
    pass


class EmotionalLog(EmotionalLogBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Community Post Schemas
class CommunityPostBase(BaseModel):
    content: str


class CommunityPostCreate(CommunityPostBase):
    pass


class CommunityPost(CommunityPostBase):
    id: int
    user_id: int
    likes_count: int
    comments_count: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True


# Notification Schemas
class NotificationBase(BaseModel):
    title: str
    message: str
    notification_type: Optional[str] = None


class NotificationCreate(NotificationBase):
    user_id: int


class Notification(NotificationBase):
    id: int
    user_id: int
    is_read: bool
    created_at: datetime

    class Config:
        from_attributes = True


# Daily Phrase Schemas
class DailyPhraseBase(BaseModel):
    phrase: str
    author: Optional[str] = None
    category: Optional[str] = None


class DailyPhraseCreate(DailyPhraseBase):
    pass


class DailyPhrase(DailyPhraseBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Calendar Event Schemas
class CalendarEventBase(BaseModel):
    title: str
    description: Optional[str] = None
    event_date: datetime
    event_type: Optional[str] = None


class CalendarEventCreate(CalendarEventBase):
    pass


class CalendarEvent(CalendarEventBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        from_attributes = True


# Dashboard Schemas
class DashboardStats(BaseModel):
    total_courses: int
    completed_courses: int
    in_progress_courses: int
    total_achievements: int
    overall_progress: float


class CourseProgress(BaseModel):
    course: Course
    progress_percentage: float
    completed_modules: int
    total_modules: int

# Made with Bob
