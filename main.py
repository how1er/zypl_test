from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
import messages_crud, users_auth

app = FastAPI()

app.include_router(users_auth.router, tags=['auth'])
app.include_router(messages_crud.router, tags=['Message'], prefix='/api/v1/messages')

register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['models']},
    generate_schemas=True,
    add_exception_handlers=True
)
