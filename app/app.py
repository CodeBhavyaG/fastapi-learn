from fastapi import FastAPI, HTTPException
from app.schema import CreatePost
from app.db import create_db_and_tables, get_async_session, Post
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
    


app = FastAPI(lifespan=lifespan)

text_post = [{"1": {"title": "bhavya", "content": "lbraba"}}, 
             {"2": {"title": "sample post", "content": "this is a test content"}}, 
             {"3": {"title": "hello world", "content": "welcome to fastapi"}}, 
             {"4": {"title": "random title", "content": "some random content here"}}, 
             {"5": {"title": "tech news", "content": "latest updates in technology"}}, 
             {"6": {"title": "fun fact", "content": "did you know this interesting fact"}}, 
             {"7": {"title": "recipe", "content": "how to make a simple dish"}}, 
             {"8": {"title": "travel", "content": "best places to visit this year"}}, 
             {"9": {"title": "book review", "content": "my thoughts on this book"}}, 
             {"10": {"title": "music", "content": "favorite songs playlist"}}]

@app.get("/post")
def post():
    return text_post

@app.get("/post/{id}")
def post_id(id: str):

    if id not in text_post:
        raise HTTPException(status_code=404,detail="id not found")
    return text_post[id]

@app.post("/postImage")
def postImage(CP: CreatePost):
    new_id = str(len(text_post) + 1)
    new_post = {new_id: {"title": CP.title, "content": CP.content}}
    text_post.append(new_post)
    return new_post