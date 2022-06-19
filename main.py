from typing import Optional
from fastapi import Body, FastAPI
from pydantic import BaseModel

app = FastAPI()
my_blogs = [{"title": "title of post", "text": "body", "id": 1}]
class Post(BaseModel):
  title: str
  text: str
  published: bool = True
  rating: Optional[int] = None

@app.get("/")
async def root():
  return {"message": "Hello Darkness!"}

@app.get("/blogs")
def get_blogs():
  return {"data": "These are your posts"}

@app.post("/blogs")
def create_blog(post: Post):
  print(post.rating)
  print(post.dict())
  return {"data":"new post"}