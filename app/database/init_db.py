import os
import sys
from pathlib import Path
from sqlalchemy import inspect

# Add the parent directory to Python path to fix imports
current_dir = Path(__file__).resolve().parent
parent_dir = current_dir.parent.parent
sys.path.append(str(parent_dir))

from app.database.database import Base, engine, DB_FILE
from app.database.models import Content

def init_database():
    print(f"\nInitializing database at: {DB_FILE}")
    
    # Create database directory if it doesn't exist
    DB_FILE.parent.mkdir(parents=True, exist_ok=True)
    
    # Create all tables
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    
    # Verify table creation
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    print("\nCreated tables:")
    for table in tables:
        print(f"- {table}")
    
    if "contents" in tables:
        print("\nDatabase initialized successfully! ✓")
    else:
        print("\nError: 'contents' table was not created properly!")
        sys.exit(1)

if __name__ == "__main__":
    init_database() 