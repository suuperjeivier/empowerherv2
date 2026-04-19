# Kintsugi Empodera - Backend API

FastAPI backend for the Kintsugi Empodera learning platform.

## Setup

### Prerequisites
- Python 3.9+
- PostgreSQL database

### Installation

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create a `.env` file based on `.env.example`:
```bash
cp .env.example .env
```

5. Update the `.env` file with your database credentials and secret key:
```
DATABASE_URL=postgresql://user:password@localhost:5432/kintsugi_db
SECRET_KEY=your-secret-key-here
```

### Database Setup

1. Create the PostgreSQL database:
```sql
CREATE DATABASE kintsugi_db;
```

2. Run the application (it will create tables automatically):
```bash
python main.py
```

Or use uvicorn:
```bash
uvicorn main:app --reload
```

## API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Project Structure

```
backend/
├── routers/              # API route handlers
│   ├── auth_router.py
│   ├── courses_router.py
│   ├── progress_router.py
│   ├── community_router.py
│   ├── emotional_router.py
│   ├── notifications_router.py
│   └── daily_phrases_router.py
├── models.py            # Database models
├── schemas.py           # Pydantic schemas
├── database.py          # Database configuration
├── auth.py              # Authentication utilities
├── config.py            # Application configuration
├── main.py              # Application entry point
└── requirements.txt     # Python dependencies
```

## API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login and get token
- `GET /api/auth/me` - Get current user info

### Courses
- `GET /api/courses/` - Get all courses
- `GET /api/courses/{id}` - Get course details
- `GET /api/courses/{id}/modules` - Get course modules
- `POST /api/courses/enroll` - Enroll in a course
- `GET /api/courses/my-courses` - Get user's enrolled courses

### Progress
- `POST /api/progress/` - Update module progress
- `GET /api/progress/dashboard` - Get dashboard statistics

### Community
- `GET /api/community/` - Get community posts
- `POST /api/community/` - Create a post
- `DELETE /api/community/{id}` - Delete a post

### Emotional Tracking
- `GET /api/emotional/` - Get emotional logs
- `POST /api/emotional/` - Create emotional log

### Notifications
- `GET /api/notifications/` - Get notifications
- `PUT /api/notifications/{id}/read` - Mark as read
- `PUT /api/notifications/read-all` - Mark all as read

### Daily Phrases
- `GET /api/daily-phrases/today` - Get today's phrase
- `GET /api/daily-phrases/` - Get all phrases

## Development

Run with auto-reload:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Testing

```bash
pytest