from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import engine, Base
from routers import (
    auth_router,
    courses_router,
    progress_router,
    community_router,
    emotional_router,
    notifications_router,
    daily_phrases_router
)

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Kintsugi Empodera API",
    description="API for the Kintsugi Empodera learning platform",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router.router)
app.include_router(courses_router.router)
app.include_router(progress_router.router)
app.include_router(community_router.router)
app.include_router(emotional_router.router)
app.include_router(notifications_router.router)
app.include_router(daily_phrases_router.router)


@app.get("/")
def root():
    """Root endpoint."""
    return {
        "message": "Welcome to Kintsugi Empodera API",
        "docs": "/docs",
        "version": "1.0.0"
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

# Made with Bob
