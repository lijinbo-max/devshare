from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import Post, PostCreate
from app.database import (
    get_all_posts,
    get_post_by_id,
    create_post as db_create_post,
    update_post as db_update_post,
    delete_post as db_delete_post
)
from datetime import datetime

router = APIRouter(prefix="/api/posts", tags=["posts"])


@router.get("", response_model=List[Post])
def get_posts():
    return get_all_posts()


@router.get("/{post_id}", response_model=Post)
def get_post(post_id: int):
    post = get_post_by_id(post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.post("", response_model=Post)
def create_post(post: PostCreate):
    new_post = Post(
        id=len(get_all_posts()) + 1,
        title=post.title,
        content=post.content,
        author=post.author,
        tags=post.tags,
        createdAt=datetime.now().isoformat(),
        updatedAt=datetime.now().isoformat()
    )
    return db_create_post(new_post)


@router.put("/{post_id}", response_model=Post)
def update_post(post_id: int, post: PostCreate):
    existing_post = get_post_by_id(post_id)
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    
    updated_post = Post(
        id=post_id,
        title=post.title,
        content=post.content,
        author=post.author,
        tags=post.tags,
        createdAt=existing_post.createdAt,
        updatedAt=datetime.now().isoformat()
    )
    return db_update_post(post_id, updated_post)


@router.delete("/{post_id}")
def delete_post(post_id: int):
    success = db_delete_post(post_id)
    if not success:
        raise HTTPException(status_code=404, detail="Post not found")
    return {"message": "Post deleted successfully"}
