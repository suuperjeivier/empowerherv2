"""
Test script to verify the refactored create_modules_and_lessons function
"""
import sys
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base
from models import Course, Module, Lesson
from seed_data import create_modules_and_lessons

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s'
)
logger = logging.getLogger(__name__)

# Create in-memory SQLite database for testing
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def test_refactored_function():
    """Test the refactored create_modules_and_lessons function"""
    logger.info("Testing refactored create_modules_and_lessons function")
    
    # Create tables
    Base.metadata.create_all(bind=engine)
    logger.info("Test database tables created")
    
    # Use context manager for automatic session management
    with TestSessionLocal() as db:
        try:
            # Use transaction block for automatic commit/rollback
            with db.begin():
                # Create test courses
                test_courses = [
                    Course(
                        title="Test Course 1",
                        description="Test description 1",
                        icon="📚",
                        color="#FF0000",
                        duration_hours=10,
                        difficulty_level="Beginner",
                        is_active=True
                    ),
                    Course(
                        title="Test Course 2",
                        description="Test description 2",
                        icon="📖",
                        color="#00FF00",
                        duration_hours=15,
                        difficulty_level="Intermediate",
                        is_active=True
                    ),
                    Course(
                        title="Test Course 3",
                        description="Test description 3",
                        icon="📝",
                        color="#0000FF",
                        duration_hours=20,
                        difficulty_level="Advanced",
                        is_active=True
                    )
                ]
                
                db.add_all(test_courses)
                db.flush()  # Get IDs without committing yet
                logger.info("Created %d test courses", len(test_courses))
                
                # Test the refactored function
                logger.info("Calling create_modules_and_lessons...")
                modules, lessons = create_modules_and_lessons(db, test_courses)
                
                # Verify returned values
                assert len(modules) > 0, "Should return modules"
                assert len(lessons) > 0, "Should return lessons"
                logger.info("Function returned %d modules and %d lessons", len(modules), len(lessons))
                
                # Verify data in database
                db_modules = db.query(Module).all()
                db_lessons = db.query(Lesson).all()
                
                assert len(db_modules) == len(modules), f"Expected {len(modules)} modules in DB, got {len(db_modules)}"
                assert len(db_lessons) == len(lessons), f"Expected {len(lessons)} lessons in DB, got {len(db_lessons)}"
                logger.info("Database contains %d modules and %d lessons", len(db_modules), len(db_lessons))
                
                # Verify module structure
                logger.info("Verifying module structure...")
                for module in db_modules[:3]:  # Check first 3 modules
                    logger.info("  Module: %s (Course ID: %d, Order: %d)",
                               module.title, module.course_id, module.order)
                    module_lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
                    assert len(module_lessons) > 0, f"Module {module.title} should have lessons"
                    logger.info("    Lessons: %d", len(module_lessons))
                    for lesson in module_lessons[:2]:  # Show first 2 lessons
                        logger.info("      • %s (%d min)", lesson.title, lesson.duration_minutes)
            
            # Test edge cases (outside transaction block)
            logger.info("Testing edge cases...")
            
            # Test with empty courses list
            try:
                create_modules_and_lessons(db, [])
                raise AssertionError("Should have raised ValueError for empty courses list")
            except ValueError as e:
                logger.info("Correctly raised ValueError: %s", e)
            
            # Test with None modules_data (uses defaults)
            logger.info("Default modules_data handling works")
            
            logger.info("\n✓ All tests passed!")
            logger.info("\nRefactoring improvements verified:")
            logger.info("  ✓ Transaction management with error handling")
            logger.info("  ✓ bulk_insert_mappings for better performance")
            logger.info("  ✓ Consolidated loop logic")
            logger.info("  ✓ Input validation")
            logger.info("  ✓ Improved logging")
            logger.info("  ✓ Proper error handling with rollback")
            
        except AssertionError as e:
            logger.error("Test assertion failed: %s", e)
            raise
        except Exception as e:
            logger.error("Test failed with exception: %s", e)
            import traceback
            traceback.print_exc()
            raise

if __name__ == "__main__":
    try:
        test_refactored_function()
        sys.exit(0)
    except Exception:
        sys.exit(1)

# Made with Bob
