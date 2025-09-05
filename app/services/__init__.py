from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import redis
from app.models import Base

# ----------------------------
# DATABASE SETUP
# ----------------------------
# Use PostgreSQL if DATABASE_URL is set, otherwise fallback to local SQLite for testing
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./test.db"  # Local file-based SQLite DB for testing
)

# Create SQLAlchemy engine
if DATABASE_URL.startswith("sqlite"):
    engine = create_engine(
        DATABASE_URL, connect_args={"check_same_thread": False}
    )
else:
    engine = create_engine(DATABASE_URL)

# Create sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables (if they don't exist)
Base.metadata.create_all(bind=engine)

# Dependency for FastAPI routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ----------------------------
# REDIS SETUP
# ----------------------------
REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379/0")
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)
