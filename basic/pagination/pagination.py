from fastapi import FastAPI, Depends
from pydantic import BaseModel

from fastapi_pagination import Page, pagination_params
from fastapi_pagination.paginator import paginate

app = FastAPI()


class User(BaseModel):
    name: str
    surname: str


users = [
    User(name='Yurii', surname='Karabas'),
    User(name='Yurii2', surname='Karabas2'),
    User(name='Yurii3', surname='Karabas3'),
    User(name='Yurii4', surname='Karabas4'),
    User(name='Yurii5', surname='Karabas5'),
]

'''
parameter를 page number, page size를 받는다.
'''
@app.get('/users', response_model=Page[User], dependencies=[Depends(pagination_params)])
async def get_users():
    return paginate(users)
