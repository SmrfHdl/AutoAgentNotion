import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# Get the absolute path to the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Create the database in the project root directory
DB_FILE = BASE_DIR / "app.db"
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_FILE}"

print(f"Database location: {DB_FILE}")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 