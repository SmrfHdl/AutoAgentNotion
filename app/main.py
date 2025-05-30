from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import Optional
import os
from dotenv import load_dotenv

from .services import llm_service, notion_service
from .database import models, crud, database
from .schemas import ContentRequest, ContentResponse

load_dotenv()

app = FastAPI(title="AutoAgent Notion")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_model=ContentResponse)
async def generate_content(
    request: ContentRequest,
    db: Session = Depends(database.get_db)
):
    try:
        # Generate content using LLM
        content = await llm_service.generate_content(request.prompt)
        
        # Save to Notion
        notion_url = await notion_service.create_page(
            title=request.title or "Generated Content",
            content=content
        )
        
        # Save to database
        db_record = crud.create_content(
            db=db,
            prompt=request.prompt,
            content=content,
            notion_url=notion_url
        )
        
        return ContentResponse(
            content=content,
            notion_url=notion_url,
            id=db_record.id
        )
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/history")
async def get_history(db: Session = Depends(database.get_db)):
    return crud.get_all_contents(db) 