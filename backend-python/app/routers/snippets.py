from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Snippet, SnippetCreate
from app.database import (
    get_all_snippets,
    get_snippet_by_id,
    create_snippet as db_create_snippet
)
from datetime import datetime

router = APIRouter(prefix="/api/snippets", tags=["snippets"])


@router.get("", response_model=List[Snippet])
def get_snippets():
    return get_all_snippets()


@router.get("/{snippet_id}", response_model=Snippet)
def get_snippet(snippet_id: int):
    snippet = get_snippet_by_id(snippet_id)
    if snippet is None:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet


@router.post("", response_model=Snippet)
def create_snippet(snippet: SnippetCreate):
    new_snippet = Snippet(
        id=len(get_all_snippets()) + 1,
        title=snippet.title,
        code=snippet.code,
        language=snippet.language,
        description=snippet.description,
        createdAt=datetime.now().isoformat()
    )
    return db_create_snippet(new_snippet)
