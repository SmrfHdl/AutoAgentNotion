import os
from notion_client import Client
from typing import Optional

notion = Client(auth=os.getenv("NOTION_API_KEY"))
database_id = os.getenv("NOTION_DATABASE_ID")

def split_content(content: str, max_length: int = 2000) -> list[str]:
    """Split content into chunks that fit Notion's character limit."""
    # Split by paragraphs first
    paragraphs = content.split('\n\n')
    chunks = []
    current_chunk = ""
    
    for paragraph in paragraphs:
        # If a single paragraph is too long, split it by sentences
        if len(paragraph) > max_length:
            sentences = paragraph.replace('. ', '.\n').split('\n')
            for sentence in sentences:
                if len(current_chunk) + len(sentence) + 2 <= max_length:
                    current_chunk += sentence + '. '
                else:
                    if current_chunk:
                        chunks.append(current_chunk.strip())
                    current_chunk = sentence + '. '
        # If adding this paragraph would exceed limit, start a new chunk
        elif len(current_chunk) + len(paragraph) + 2 > max_length:
            chunks.append(current_chunk.strip())
            current_chunk = paragraph + '\n\n'
        else:
            current_chunk += paragraph + '\n\n'
    
    if current_chunk:
        chunks.append(current_chunk.strip())
    
    return chunks

async def create_page(title: str, content: str) -> str:
    """Create a new page in Notion database with content split into blocks."""
    try:
        # Split content into chunks
        content_chunks = split_content(content)
        
        # Create children blocks for each chunk
        children = []
        for chunk in content_chunks:
            children.append({
                "object": "block",
                "type": "paragraph",
                "paragraph": {
                    "rich_text": [
                        {
                            "type": "text",
                            "text": {
                                "content": chunk
                            }
                        }
                    ]
                }
            })
        
        # Create the page with all content blocks
        new_page = notion.pages.create(
            parent={"database_id": database_id},
            properties={
                "Name": {
                    "title": [
                        {
                            "text": {
                                "content": title
                            }
                        }
                    ]
                }
            },
            children=children
        )
        
        # Construct the URL using page ID
        page_id = new_page["id"].replace("-", "")
        workspace_id = database_id.split("-")[0]
        page_url = f"https://notion.so/{workspace_id}/{page_id}"
        
        return page_url
    except Exception as e:
        raise Exception(f"Error creating Notion page: {str(e)}") 