# Database Seeding Guide

## ⚠️ SECURITY WARNING - DEVELOPMENT ONLY ⚠️

**This seeding script contains HARDCODED PASSWORDS that are INSECURE and intended ONLY for development and testing environments.**

**NEVER use these credentials in production:**
- `password123` - INSECURE development password
- `admin123` - INSECURE development password

**In production environments, you MUST:**
- Use strong, unique passwords
- Store credentials securely (environment variables, secrets management systems)
- Implement proper password policies and complexity requirements
- Use secure authentication mechanisms (OAuth, SSO, MFA)
- Never commit passwords to version control

---

## Overview
The `seed_data.py` script populates the database with sample data for development and testing purposes.

## What Gets Seeded

### Users (3)
- **Valeria García** (Student)
  - Email: `valeria@example.com`
  - Password: `password123` ⚠️ **INSECURE - DEV ONLY**
  - Has enrollments in 3 courses with varying progress

- **María López** (Student)
  - Email: `maria@example.com`
  - Password: `password123` ⚠️ **INSECURE - DEV ONLY**
  - Has 1 course enrollment

- **Admin User** (Admin)
  - Email: `admin@example.com`
  - Password: `admin123` ⚠️ **INSECURE - DEV ONLY**

### Courses (4)
1. **Marketing digital para emprendedoras** (💼)
   - 4 modules with multiple lessons
   - Color: Purple (#E8B4F9)
   - Progress: 65%

2. **Finanzas personales para mujeres** (💰)
   - 2 modules with lessons
   - Color: Pink (#FFB4C8)
   - Progress: 40%

3. **Liderazgo y confianza en ti misma** (⭐)
   - 1 module with lessons
   - Color: Orange (#FFD4A3)
   - Progress: 15%

4. **Diseño de marca personal** (🎨)
   - Color: Blue (#B4E8F9)
   - Not enrolled yet

### Additional Data
- **Daily Phrases**: 7 inspirational quotes
- **Community Posts**: 2 sample posts
- **Emotional Logs**: 2 mood entries
- **Notifications**: 3 sample notifications

## How to Run

### First Time Setup
```bash
cd backend
python seed_data.py
```

### Reset Database and Re-seed
If you need to clear existing data and start fresh:

**Option 1: Delete the database file (SQLite)**
```bash
# Delete the database file
rm kintsugi.db  # or whatever your database file is named

# Run seed script
python seed_data.py
```

**Option 2: Drop all tables (PostgreSQL)**
```bash
# Connect to PostgreSQL and drop the database
psql -U postgres
DROP DATABASE kintsugi_db;
CREATE DATABASE kintsugi_db;
\q

# Run seed script
python seed_data.py
```

## Testing the Application

After seeding, you can:

1. **Login** with Valeria's credentials ⚠️ **DEVELOPMENT ONLY**:
   - Email: `valeria@example.com`
   - Password: `password123` (INSECURE - for testing only)

2. **View the Home Page** to see:
   - Daily inspirational phrase
   - Course progress (65%, 40%, 15%)
   - Dashboard stats
   - Recommended courses

3. **Explore Features**:
   - Browse all 4 courses
   - View community posts
   - Check notifications
   - See emotional logs

## Script Features

- ✅ **Idempotent**: Won't duplicate data if run multiple times
- ✅ **Safe**: Checks for existing data before seeding
- ✅ **Comprehensive**: Seeds all necessary tables
- ✅ **Realistic**: Uses meaningful sample data

## Troubleshooting

### "Database already contains data"
This means the database has been seeded. To re-seed, delete the database first.

### Unicode Errors on Windows
The script uses ASCII-safe characters for Windows compatibility.

### Connection Errors
Ensure your `.env` file has the correct `DATABASE_URL`:
```
DATABASE_URL=postgresql://postgres:password@localhost:5432/kintsugi_db
```

## Made with Bob