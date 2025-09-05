import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.services import Base, get_db
from fastapi.testclient import TestClient
from app.main import app

# SQLite in-memory DB for tests
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)
TestingSessionLocal = sessionmaker(bind=engine)

# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency override for FastAPI
def override_get_db():
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

