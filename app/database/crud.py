# CRUD: Create, Read, Update, Delete
from sqlalchemy.orm import Session
from . import models

def create_content(db: Session, prompt: str, content: str, notion_url: str):
    db_content = models.Content(
        prompt=prompt,
        content=content,
        notion_url=notion_url
    )
    db.add(db_content)
    db.commit()
    db.refresh(db_content)
    return db_content

def get_all_contents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Content).offset(skip).limit(limit).all()

def get_content(db: Session, content_id: int):
    return db.query(models.Content).filter(models.Content.id == content_id).first() 