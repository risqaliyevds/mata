from fastapi import FastAPI, Response, status, HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
import random
import psycopg2
from psycopg2.extras import RealDictCursor

try:
    conn = psycopg2.connect(host = 'localhost', 
                            database = 'fastapi',
                            username = 'postgres',
                            password = "0073",
                            cursor_factory= RealDictCursor)
    cur = conn.cursor()
    print('Databese connection was succesfull!')
except Exception as error:
    print('Databese connection was faild!')
    print('Error: ', error)

app = FastAPI()

my_db = {}
last_post_id = None

def find_post(id):
    return my_db[id]

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get('/')
async def root():
    return {'message' : 'Welcome to my first API! Yehuu!!!'}

@app.get('/posts')
async def get_posts():
    return {"data" : 'This is your posts'}

@app.post('/posts', status_code=status.HTTP_201_CREATED)
async def create_post(post: Post):
    post_dict = post.dict()
    id = random.randrange(1, 1000)
    my_db[id] = post_dict
    
    global last_post_id
    last_post_id = id

    return {"data": my_db}

@app.get('/posts/latest')
async def get_last_post():
    return {'last_post' : my_db[last_post_id]}

@app.get('/posts/{id}')
async def get_post(id: int, response: Response):
    post = find_post(id)
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Post with {id} not found. Try again")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"message" : f"post wit {id} not found"}

    return {"post_detail" : post}

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(id: int):
    try:
        del my_db[id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Post with {id} not found. Try again")


@app.put('/posts/{id}')
async def update_post(id: int, post: Post):
    try:
        my_db[id] = post
        return {"message" : 'Post updated!'}
    except:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail= f"Post with {id} not found. Try again")
    
    

