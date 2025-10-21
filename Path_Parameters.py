# Path Parameters
from fastapi import FastAPI
app=FastAPI()

@app.get("/")
def index():
    return{"message":"Hello World"}

@app.get("/blog/unpublished")
def show_unpublished():
    return{"Blog:All unpublished blog"}

@app.get("/blog/{id}")
def show(id):
    return {"id":id}

@app.get("/blog/comment/{id}")
def show_comment(id):
    return {"public comment":id}


