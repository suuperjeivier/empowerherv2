# Kintsugi Empodera

A comprehensive learning platform designed to empower women through education, community support, and personal growth tracking.

## 🌟 Project Overview

Kintsugi Empodera is inspired by the Japanese art of Kintsugi (金継ぎ), which repairs broken pottery with gold, making it more beautiful and valuable. Similarly, this platform helps women transform their challenges into opportunities for growth and empowerment.

### Key Features

- **12 Interactive Screens**: Complete learning experience from onboarding to achievement tracking
- **Course Management**: Browse, enroll, and track progress in various empowerment courses
- **Community Support**: Connect with other learners, share experiences, and support each other
- **Emotional Tracking**: Monitor and reflect on emotional well-being throughout the learning journey
- **Daily Inspiration**: Receive motivational phrases and affirmations
- **Progress Tracking**: Visualize learning achievements and milestones
- **Calendar & Planning**: Organize learning activities and set goals

## 🏗️ Architecture

### Backend (Python/FastAPI)
- **Framework**: FastAPI with async support
- **Database**: PostgreSQL with SQLAlchemy ORM
- **Authentication**: JWT-based authentication
- **API Documentation**: Auto-generated with Swagger/OpenAPI

### Frontend (Angular)
- **Framework**: Angular 17+ with standalone components
- **State Management**: RxJS with services
- **Styling**: SCSS with custom design system
- **Routing**: Lazy-loaded routes for performance

## 📋 Prerequisites

### Backend
- Python 3.9+
- PostgreSQL 12+
- pip (Python package manager)

### Frontend
- Node.js 18+
- npm or yarn
- Angular CLI 17+

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone <repository-url>
cd empowerherv2
```

### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env

# Update .env with your database credentials
# DATABASE_URL=postgresql://user:password@localhost:5432/kintsugi_db
# SECRET_KEY=your-secret-key-here

# Create database
# In PostgreSQL:
# CREATE DATABASE kintsugi_db;

# Run the application
python main.py
```

The backend API will be available at `http://localhost:8000`
- API Documentation: `http://localhost:8000/docs`
- Alternative docs: `http://localhost:8000/redoc`

### 3. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend/kintsugi-empodera

# Install dependencies
npm install

# Run development server
ng serve
```

The frontend application will be available at `http://localhost:4200`

## 📱 Application Screens

1. **Bienvenida/Onboarding** - Welcome and introduction
2. **Inicio (Home)** - Dashboard with overview and quick actions
3. **Cursos** - Browse available courses
4. **Detalle del curso** - Course modules and lessons
5. **Progreso & Logros** - Track achievements and progress
6. **Calendario & Planificador** - Schedule learning activities
7. **Comunidad** - Community posts and interactions
8. **Perfil** - User profile and information
9. **Estado emocional** - Emotional well-being tracking
10. **Frases diarias** - Daily inspirational quotes
11. **Notificaciones** - Platform notifications
12. **Ajustes** - Application settings

## 🔐 Authentication Flow

1. User registers with email and password
2. User logs in and receives JWT token
3. Token is stored in localStorage
4. All API requests include the token in Authorization header
5. Protected routes require valid authentication

## 📊 Database Schema

### Main Tables
- **users** - User accounts and profiles
- **courses** - Available courses
- **modules** - Course modules
- **lessons** - Module lessons
- **enrollments** - User course enrollments
- **progress** - Learning progress tracking
- **community_posts** - Community interactions
- **emotional_logs** - Emotional state tracking
- **notifications** - User notifications
- **daily_phrases** - Inspirational content
- **calendar_events** - Scheduled activities

## 🎨 Design System

### Color Palette
- **Primary**: Purple (#8B5CF6) - Growth and transformation
- **Secondary**: Pink (#EC4899) - Empowerment
- **Accent**: Amber (#F59E0B) - Achievement
- **Success**: Green (#10B981)
- **Error**: Red (#EF4444)

### Typography
- Font Family: Inter, system fonts
- Responsive sizing for mobile and desktop

## 🔧 Development

### Backend Development

```bash
# Run with auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000

# Run tests
pytest

# Create database migration
alembic revision --autogenerate -m "description"

# Apply migrations
alembic upgrade head
```

### Frontend Development

```bash
# Generate new component
ng generate component components/component-name --standalone

# Generate service
ng generate service services/service-name

# Build for production
ng build --configuration production

# Run tests
ng test
```

## 📦 Deployment

### Backend Deployment

1. Set up PostgreSQL database
2. Configure environment variables
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `alembic upgrade head`
5. Start server: `uvicorn main:app --host 0.0.0.0 --port 8000`

### Frontend Deployment

1. Update `environment.prod.ts` with production API URL
2. Build: `ng build --configuration production`
3. Deploy `dist/kintsugi-empodera` folder to hosting service
4. Configure web server (nginx, Apache, etc.)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Commit changes: `git commit -m 'Add amazing feature'`
4. Push to branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## 📝 API Endpoints

### Authentication
- `POST /api/auth/register` - Register new user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user

### Courses
- `GET /api/courses` - List all courses
- `GET /api/courses/{id}` - Get course details
- `GET /api/courses/{id}/modules` - Get course modules
- `POST /api/courses/enroll` - Enroll in course
- `GET /api/courses/my-courses` - Get user's courses

### Progress
- `POST /api/progress` - Update progress
- `GET /api/progress/dashboard` - Get dashboard stats

### Community
- `GET /api/community` - Get community posts
- `POST /api/community` - Create post
- `DELETE /api/community/{id}` - Delete post

### Emotional Tracking
- `GET /api/emotional` - Get emotional logs
- `POST /api/emotional` - Create emotional log

### Notifications
- `GET /api/notifications` - Get notifications
- `PUT /api/notifications/{id}/read` - Mark as read
- `PUT /api/notifications/read-all` - Mark all as read

### Daily Phrases
- `GET /api/daily-phrases/today` - Get today's phrase
- `GET /api/daily-phrases` - Get all phrases

## 📄 License

Private - All rights reserved

## 👥 Team

Developed with ❤️ for women empowerment

## 🙏 Acknowledgments

- Inspired by the Kintsugi philosophy
- Built to support women's education and growth
- Community-driven development

---

For more information, see the individual README files in `/backend` and `/frontend/kintsugi-empodera` directories.