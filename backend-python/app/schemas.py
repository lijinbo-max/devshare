from pydantic import BaseModel
from typing import List
from datetime import datetime


class PostBase(BaseModel):
    title: str
    content: str
    author: str
    tags: List[str]


class PostCreate(PostBase):
    pass


class Post(PostBase):
    id: int
    createdAt: str
    updatedAt: str

    class Config:
        from_attributes = True


class SnippetBase(BaseModel):
    title: str
    code: str
    language: str
    description: str


class SnippetCreate(SnippetBase):
    pass


class Snippet(SnippetBase):
    id: int
    createdAt: str

    class Config:
        from_attributes = True
