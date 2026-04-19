"""
Seed data script for Kintsugi Empodera
Populates the database with sample data for testing and development

⚠️  SECURITY WARNING - DEVELOPMENT ONLY ⚠️
This script contains HARDCODED PASSWORDS that are INSECURE and intended
ONLY for development and testing environments.

NEVER use these credentials in production:
- password123
- admin123

In production environments:
- Use strong, unique passwords
- Store credentials securely (environment variables, secrets management)
- Implement proper password policies
- Use secure authentication mechanisms
"""
import logging
from datetime import datetime, timedelta
from typing import List, Dict, Any, Optional, Tuple
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, OperationalError, IntegrityError
from sqlalchemy import inspect as sqlalchemy_inspect
from database import SessionLocal, engine, Base
from models import (
    User, Course, Module, Lesson, Enrollment, Progress,
    Achievement, EmotionalLog, CommunityPost, Notification,
    DailyPhrase, UserDailyPhrase, CalendarEvent,
    UserRole, EmotionalState
)
from auth import get_password_hash

# Configure logging
logger = logging.getLogger(__name__)
# Development credentials constants (INSECURE - FOR DEVELOPMENT ONLY)
DEV_EMAIL = "valeria@example.com"
DEV_PASSWORD = "password123"
DEV_PASSWORD_WARNING = """
[WARNING] DEVELOPMENT CREDENTIALS (INSECURE - DO NOT USE IN PRODUCTION):
   Email: {email}
   Password: {password}
[WARNING] These passwords are for TESTING ONLY and are NOT SECURE!
""".strip()



def create_users(db: Session):
    """Create sample users with INSECURE development-only passwords"""
    # ⚠️  WARNING: These are INSECURE passwords for DEVELOPMENT ONLY
    # NEVER use these in production environments
    student_password_hash = get_password_hash("password123")  # INSECURE - DEV ONLY
    admin_password_hash = get_password_hash("admin123")  # INSECURE - DEV ONLY
    
    users = [
        User(
            email="valeria@example.com",
            username="valeria",
            hashed_password=student_password_hash,
            full_name="Valeria García",
            role=UserRole.STUDENT,
            is_active=True,
            profile_image="https://i.pravatar.cc/150?img=1"
        ),
        User(
            email="maria@example.com",
            username="maria",
            hashed_password=student_password_hash,
            full_name="María López",
            role=UserRole.STUDENT,
            is_active=True,
            profile_image="https://i.pravatar.cc/150?img=5"
        ),
        User(
            email="admin@example.com",
            username="admin",
            hashed_password=admin_password_hash,
            full_name="Admin User",
            role=UserRole.ADMIN,
            is_active=True
        )
    ]
    
    for user in users:
        db.add(user)
    db.commit()
    print(f"[OK] Created {len(users)} users")
    return users


def create_courses(db: Session):
    """Create sample courses"""
    courses = [
        Course(
            title="Marketing digital para emprendedoras",
            description="Aprende las estrategias fundamentales del marketing digital para impulsar tu negocio",
            icon="💼",
            color="#E8B4F9",
            duration_hours=20,
            difficulty_level="Intermedio",
            is_active=True
        ),
        Course(
            title="Finanzas personales para mujeres",
            description="Domina tus finanzas personales y aprende a invertir inteligentemente",
            icon="💰",
            color="#FFB4C8",
            duration_hours=15,
            difficulty_level="Principiante",
            is_active=True
        ),
        Course(
            title="Liderazgo y confianza en ti misma",
            description="Desarrolla habilidades de liderazgo y fortalece tu autoconfianza",
            icon="⭐",
            color="#FFD4A3",
            duration_hours=18,
            difficulty_level="Intermedio",
            is_active=True
        ),
        Course(
            title="Diseño de marca personal",
            description="Crea y desarrolla tu marca personal profesional",
            icon="🎨",
            color="#B4E8F9",
            duration_hours=12,
            difficulty_level="Principiante",
            is_active=True
        )
    ]
    
    for course in courses:
        db.add(course)
    db.commit()
    print(f"[OK] Created {len(courses)} courses")
    return courses


# Default modules template data for seeding
# Each entry maps to a course by index and defines its modules structure
_DEFAULT_MODULES_TEMPLATE = [
    {
        "course_index": 0,  # Marketing digital
        "modules": [
            {
                "title": "Introducción al marketing digital",
                "description": "Conceptos básicos y fundamentos",
                "order": 1,
                "lessons": [
                    {"title": "¿Qué es el marketing digital?", "duration": 15},
                    {"title": "Principales canales digitales", "duration": 20},
                    {"title": "Definiendo tu audiencia", "duration": 25}
                ]
            },
            {
                "title": "Estrategia de marca",
                "description": "Construye tu identidad de marca",
                "order": 2,
                "lessons": [
                    {"title": "Identidad de marca", "duration": 30},
                    {"title": "Propuesta de valor", "duration": 25}
                ]
            },
            {
                "title": "Redes sociales",
                "description": "Domina las redes sociales para tu negocio",
                "order": 3,
                "lessons": [
                    {"title": "Instagram para negocios", "duration": 35},
                    {"title": "Facebook Ads básico", "duration": 40}
                ]
            },
            {
                "title": "Publicidad digital",
                "description": "Aprende a crear campañas efectivas",
                "order": 4,
                "is_locked": True,
                "lessons": [
                    {"title": "Google Ads introducción", "duration": 45},
                    {"title": "Métricas y análisis", "duration": 30}
                ]
            }
        ]
    },
    {
        "course_index": 1,  # Finanzas personales
        "modules": [
            {
                "title": "Fundamentos financieros",
                "description": "Bases de las finanzas personales",
                "order": 1,
                "lessons": [
                    {"title": "Presupuesto personal", "duration": 20},
                    {"title": "Ahorro inteligente", "duration": 25}
                ]
            },
            {
                "title": "Inversiones básicas",
                "description": "Primeros pasos en inversión",
                "order": 2,
                "lessons": [
                    {"title": "Tipos de inversión", "duration": 30},
                    {"title": "Gestión de riesgos", "duration": 25}
                ]
            }
        ]
    },
    {
        "course_index": 2,  # Liderazgo
        "modules": [
            {
                "title": "Autoconocimiento",
                "description": "Conoce tus fortalezas",
                "order": 1,
                "lessons": [
                    {"title": "Identificando fortalezas", "duration": 20},
                    {"title": "Áreas de mejora", "duration": 20}
                ]
            }
        ]
    }
]


def _get_default_modules_data(courses: List[Course]) -> List[Dict[str, Any]]:
    """
    Get default modules data structure for courses.
    
    Creates a predefined set of modules and lessons for the first three courses
    in the provided list. This is used during database seeding to populate
    initial course content.
    
    Args:
        courses: List of Course objects. Must contain at least 3 courses.
                 Uses courses[0] for Marketing, courses[1] for Finance,
                 courses[2] for Leadership.
        
    Returns:
        List of dictionaries, each containing:
            - course: Course object reference
            - modules: List of module dictionaries with title, description,
                      order, is_locked (optional), and lessons
    
    Raises:
        ValueError: If courses list has fewer than 3 items
        
    Example:
        >>> courses = create_courses(db)
        >>> modules_data = _get_default_modules_data(courses)
        >>> len(modules_data)
        3
    """
    required_courses = len(_DEFAULT_MODULES_TEMPLATE)
    
    if len(courses) < required_courses:
        raise ValueError(
            f"Expected at least {required_courses} courses for default modules, "
            f"got {len(courses)}. Please ensure courses are created first."
        )
    
    return [
        {
            "course": courses[template["course_index"]],
            "modules": template["modules"]
        }
        for template in _DEFAULT_MODULES_TEMPLATE
    ]


def _create_module_from_data(course_id: int, module_data: Dict[str, Any]) -> Module:
    """
    Create a Module instance from dictionary data.
    
    Args:
        course_id: ID of the course this module belongs to
        module_data: Dictionary containing module information
        
    Returns:
        Module instance
    """
    return Module(
        course_id=course_id,
        title=module_data["title"],
        description=module_data["description"],
        order=module_data["order"],
        is_locked=module_data.get("is_locked", False)
    )


def _create_lessons_from_data(module: Module, lessons_data: List[Dict[str, Any]]) -> List[Lesson]:
    """
    Create Lesson instances for a module.
    
    Args:
        module: Module instance these lessons belong to
        lessons_data: List of dictionaries containing lesson information
        
    Returns:
        List of Lesson instances
    """
    lessons = []
    for idx, lesson_data in enumerate(lessons_data, 1):
        lesson = Lesson(
            module_id=module.id,
            title=lesson_data["title"],
            content=f"Contenido de la lección: {lesson_data['title']}",
            order=idx,
            duration_minutes=lesson_data["duration"]
        )
        lessons.append(lesson)
    return lessons




def create_modules_and_lessons(
    db: Session,
    courses: List[Course],
    modules_data: Optional[List[Dict[str, Any]]] = None
) -> Tuple[List[Module], List[Lesson]]:
    """
    Create modules and lessons for courses with optimized batch operations.
    
    Uses bulk_insert_mappings for maximum performance and wraps operations
    in a transaction for atomicity. This approach minimizes database round-trips
    and ensures data consistency.
    
    Args:
        db: SQLAlchemy database session
        courses: List of Course objects to create modules for
        modules_data: Optional custom modules data structure. If None, uses default data.
        
    Returns:
        Tuple of (modules, lessons) that were created
        
    Raises:
        ValueError: If courses is empty or modules_data is invalid
        SQLAlchemyError: If database operations fail
    """
    # Input validation
    if not courses:
        raise ValueError("Cannot create modules for empty courses list")
    
    if modules_data is None:
        modules_data = _get_default_modules_data(courses)
    
    logger.info("Creating modules for %d courses", len(modules_data))
    
    try:
        # Build module dictionaries and track lesson data in one pass
        modules_and_lessons = [
            (
                {
                    "course_id": course_data["course"].id,
                    "title": mod_data["title"],
                    "description": mod_data["description"],
                    "order": mod_data["order"],
                    "is_locked": mod_data.get("is_locked", False)
                },
                mod_data["lessons"]
            )
            for course_data in modules_data
            for mod_data in course_data["modules"]
        ]
        
        if not modules_and_lessons:
            logger.warning("No modules to create")
            return [], []
        
        module_dicts, lessons_data_list = zip(*modules_and_lessons)
        
        # Bulk insert modules
        db.bulk_insert_mappings(Module, module_dicts)  # type: ignore[arg-type]
        db.flush()  # Ensure IDs are generated
        
        # Fetch created modules to get their IDs
        course_ids = [cd["course"].id for cd in modules_data]
        modules = db.query(Module).filter(
            Module.course_id.in_(course_ids)
        ).order_by(Module.course_id, Module.order).all()
        
        # Build lesson dictionaries
        lesson_dicts = [
            {
                "module_id": module.id,
                "title": lesson_data["title"],
                "content": f"Contenido de la lección: {lesson_data['title']}",
                "order": idx,
                "duration_minutes": lesson_data["duration"]
            }
            for module, lessons_data in zip(modules, lessons_data_list)
            for idx, lesson_data in enumerate(lessons_data, 1)
        ]
        
        # Bulk insert lessons
        db.bulk_insert_mappings(Lesson, lesson_dicts)  # type: ignore[arg-type]
        db.flush()
        
        # Fetch created lessons
        module_ids = [m.id for m in modules]
        lessons = db.query(Lesson).filter(
            Lesson.module_id.in_(module_ids)
        ).order_by(Lesson.module_id, Lesson.order).all()
        
        logger.info("Successfully created %d modules and %d lessons",
                   len(modules), len(lessons))
        
        return modules, lessons
        
    except SQLAlchemyError as e:
        logger.error("Failed to create modules and lessons: %s", str(e))
        db.rollback()
        raise


def create_enrollments(db: Session, users, courses):
    """Create enrollments for users"""
    enrollments = [
        Enrollment(
            user_id=users[0].id,  # Valeria
            course_id=courses[0].id,  # Marketing digital
            progress_percentage=65.0,
            enrolled_at=datetime.now() - timedelta(days=15)
        ),
        Enrollment(
            user_id=users[0].id,
            course_id=courses[1].id,  # Finanzas
            progress_percentage=40.0,
            enrolled_at=datetime.now() - timedelta(days=10)
        ),
        Enrollment(
            user_id=users[0].id,
            course_id=courses[2].id,  # Liderazgo
            progress_percentage=15.0,
            enrolled_at=datetime.now() - timedelta(days=5)
        ),
        Enrollment(
            user_id=users[1].id,  # María
            course_id=courses[0].id,
            progress_percentage=30.0,
            enrolled_at=datetime.now() - timedelta(days=8)
        )
    ]
    
    for enrollment in enrollments:
        db.add(enrollment)
    db.commit()
    print(f"[OK] Created {len(enrollments)} enrollments")


def create_daily_phrases(db: Session):
    """Create daily inspirational phrases"""
    phrases = [
        DailyPhrase(
            phrase="No tienes que ser perfecta para ser increíble.",
            author="Anónimo",
            category="Autoestima"
        ),
        DailyPhrase(
            phrase="Cada día es una nueva oportunidad para construir la vida que sueñas.",
            author="Kintsugi Empodera",
            category="Motivación"
        ),
        DailyPhrase(
            phrase="Tu valor no disminuye por la incapacidad de alguien para ver tu valía.",
            author="Anónimo",
            category="Autoestima"
        ),
        DailyPhrase(
            phrase="Las grietas son donde entra la luz.",
            author="Leonard Cohen",
            category="Resiliencia"
        ),
        DailyPhrase(
            phrase="Eres más fuerte de lo que crees y más capaz de lo que imaginas.",
            author="Kintsugi Empodera",
            category="Fortaleza"
        ),
        DailyPhrase(
            phrase="El éxito no es la clave de la felicidad. La felicidad es la clave del éxito.",
            author="Albert Schweitzer",
            category="Éxito"
        ),
        DailyPhrase(
            phrase="Cree en ti misma y todo será posible.",
            author="Anónimo",
            category="Confianza"
        )
    ]
    
    for phrase in phrases:
        db.add(phrase)
    db.commit()
    print(f"[OK] Created {len(phrases)} daily phrases")
    return phrases


def create_community_posts(db: Session, users):
    """Create sample community posts"""
    posts = [
        CommunityPost(
            user_id=users[1].id,  # María
            content="¡Hoy di un paso hacia mi sueño! También puedes hacerlo. 💪",
            likes_count=5,
            comments_count=3,
            created_at=datetime.now() - timedelta(hours=2)
        ),
        CommunityPost(
            user_id=users[0].id,  # Valeria
            content="Gracias a este curso entendí mejor cómo manejar mis finanzas. ¡Recomendado!",
            likes_count=8,
            comments_count=2,
            created_at=datetime.now() - timedelta(days=1)
        )
    ]
    
    for post in posts:
        db.add(post)
    db.commit()
    print(f"[OK] Created {len(posts)} community posts")


def create_emotional_logs(db: Session, users):
    """Create emotional state logs"""
    logs = [
        EmotionalLog(
            user_id=users[0].id,
            emotional_state=EmotionalState.HAPPY,
            note="¡Completé un módulo importante hoy!",
            created_at=datetime.now()
        ),
        EmotionalLog(
            user_id=users[0].id,
            emotional_state=EmotionalState.CONTENT,
            note="Progresando bien en mis cursos",
            created_at=datetime.now() - timedelta(days=1)
        )
    ]
    
    for log in logs:
        db.add(log)
    db.commit()
    print(f"[OK] Created {len(logs)} emotional logs")


def create_notifications(db: Session, users):
    """Create sample notifications"""
    notifications = [
        Notification(
            user_id=users[0].id,
            title="¡Felicidades!",
            message="Completaste el módulo 2 del curso de Marketing Digital",
            notification_type="achievement",
            is_read=False,
            created_at=datetime.now() - timedelta(hours=1)
        ),
        Notification(
            user_id=users[0].id,
            title="Recordatorio",
            message="No te pierdas la frase del día",
            notification_type="reminder",
            is_read=True,
            created_at=datetime.now() - timedelta(days=1)
        ),
        Notification(
            user_id=users[0].id,
            title="Nueva actividad",
            message="María comentó en tu publicación",
            notification_type="social",
            is_read=False,
            created_at=datetime.now() - timedelta(hours=3)
        )
    ]
    
    for notification in notifications:
        db.add(notification)
    db.commit()
    print(f"[OK] Created {len(notifications)} notifications")


def _drop_tables_if_forced(force: bool) -> None:
    """Drop all database tables if force mode is enabled.
    
    Args:
        force: If True, drops all tables
    """
    if force:
        logger.warning("Force mode enabled - dropping all tables...")
        Base.metadata.drop_all(bind=engine)
        logger.info("All tables dropped")


def _create_tables() -> None:
    """Create all database tables based on models."""
    Base.metadata.create_all(bind=engine)
    logger.info("Database tables created")


def _check_existing_data(db: Session) -> bool:
    """Check if database already contains data.
    
    Args:
        db: Database session
        
    Returns:
        bool: True if data exists, False otherwise
    """
    existing_users = db.query(User).count()
    return existing_users > 0


def _seed_all_data(db: Session) -> None:
    """Coordinate all data seeding operations.
    
    Args:
        db: Database session
    """
    users = create_users(db)
    courses = create_courses(db)
    create_modules_and_lessons(db, courses)
    create_enrollments(db, users, courses)
    phrases = create_daily_phrases(db)
    create_community_posts(db, users)
    create_emotional_logs(db, users)
    create_notifications(db, users)


def _log_success_message() -> None:
    """Log successful database seeding completion with development credentials."""
    logger.info("Database seeding completed successfully!")
    logger.warning(DEV_PASSWORD_WARNING.format(email=DEV_EMAIL, password=DEV_PASSWORD))


def _handle_operational_error(error: OperationalError) -> None:
    """Handle database operational errors with helpful guidance.
    
    Args:
        error: The operational error that occurred
    """
    logger.error(f"Database connection error: {error}")
    logger.info("Please check the following:")
    logger.info("  1. Verify your DATABASE_URL is correctly set in the .env file")
    logger.info("  2. Ensure the database server is running and accessible")
    logger.info("  3. Check network connectivity and firewall settings")
    logger.info("  4. Verify database credentials (username/password)")


def _handle_integrity_error(error: IntegrityError) -> None:
    """Handle database integrity constraint violations with helpful guidance.
    
    Args:
        error: The integrity error that occurred
    """
    logger.error(f"Database constraint violation: {error}")
    logger.info("Please check the following:")
    logger.info("  1. Ensure the database schema is up to date")
    logger.info("  2. Check for duplicate data or constraint violations")
    logger.info("  3. Verify foreign key relationships are valid")
    logger.info("  4. Consider using --force flag to recreate the database")


def _handle_general_error(error: Exception) -> None:
    """Handle general database errors.
    
    Args:
        error: The error that occurred
    """
    logger.error(f"Error seeding database: {error}")


def _handle_database_error(error: Exception) -> None:
    """Unified error handler with type-specific guidance.
    
    Dispatches to appropriate error handler based on exception type,
    providing context-specific troubleshooting information.
    
    Args:
        error: The database error that occurred
    """
    error_handlers = {
        OperationalError: _handle_operational_error,
        IntegrityError: _handle_integrity_error,
    }
    
    handler = error_handlers.get(type(error), _handle_general_error)
    handler(error)


def seed_database(force: bool = False) -> bool:
    """Main function to seed the database with sample data.
    
    This function orchestrates the complete database seeding process, including
    table creation, data population, and error handling. It uses a context manager
    for automatic session cleanup and transaction management for atomic operations.
    
    Args:
        force: If True, drops all tables and recreates them before seeding.
               Use with caution as this will delete all existing data.
        
    Returns:
        bool: True if seeding completed successfully, False if skipped due to
              existing data (when force=False).
        
    Raises:
        OperationalError: Database connection or operational issues
        IntegrityError: Data constraint violations (duplicates, foreign keys, etc.)
        SQLAlchemyError: Other database-related errors
        
    Example:
        >>> seed_database(force=True)  # Drop and recreate all data
        True
        >>> seed_database()  # Skip if data exists
        False
    """
    logger.info("Starting database seeding...")
    
    with SessionLocal() as db:
        try:
            # Handle force mode and table creation
            _drop_tables_if_forced(force)
            _create_tables()
            
            # Check if seeding is needed
            if not force and _check_existing_data(db):
                logger.warning("Database already contains data. Skipping seed.")
                logger.info("Use --force flag to drop and recreate all data.")
                return False
            
            # Perform all seeding operations in a single transaction
            with db.begin():
                _seed_all_data(db)
            
            # Log success
            _log_success_message()
            return True
            
        except (OperationalError, IntegrityError, SQLAlchemyError) as e:
            _handle_database_error(e)
            raise


if __name__ == "__main__":
    import sys
    force_mode = "--force" in sys.argv or "-f" in sys.argv
    seed_database(force=force_mode)

# Made with Bob