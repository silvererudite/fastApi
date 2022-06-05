from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
  return {"message": "Hello Darkness!"}

@app.get("/blogs")
def get_blogs():
  return {"data": "These are your posts"}

