from typing import Optional
from fastapi import Body, FastAPI, Response, status, HTTPException
from pydantic import BaseModel
from random import randrange

app = FastAPI()
my_blogs = [{"title": "title of post", "text": "body", "id": 1}]
class Post(BaseModel):
  title: str
  text: str
  published: bool = True
  rating: Optional[int] = None

my_blogs = [{"title": "title of blog", "text": "content if blog", "id":1},
{"title": "Favourite food", "text": "Burgers", "id":2}]

def find_post(id):
  for elem in enumerate(my_blogs):
    if elem["id"] == int(id):
      return elem
def delete_post(id):
  for i, elem in enumerate(my_blogs):
    if elem["id"] == int(id):
      return i

@app.get("/")
async def root():
  return {"message": "Hello Darkness!"}

@app.get("/blogs")
def get_blogs():
  return {"data": my_blogs}

@app.post("/blogs", status_code=status.HTTP_201_CREATED)
def create_blog(post: Post):
  post_dict = post.dict()
  post_dict["id"] = randrange(0, 1000000)
  my_blogs.append(post_dict)
  return {"data": post_dict}

@app.get("/blogs/{id}")
def get_blogs(id: int, response: Response):
  post, _ = find_post(id)
  if not post:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
  return {"data": post}

@app.delete("/blogs/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_blog(id: int, response: Response):
  idx = delete_post(id)
  if idx == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
  my_blogs.pop(idx)
  return Response(status_code=status.HTTP_204_NO_CONTENT)

@app.put("/blogs/{id}")
def update_blog(id: int, post: Post):
  idx = delete_post(id)
  if idx == None:
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} was not found")
  post_dict = post.dict()
  post_dict['id'] = id
  my_blogs[idx] = post_dict
  return {"data": post_dict}


