from fastapi import FastAPI
from app.routes import users
from app import crud

app = FastAPI()

crud.create_tables()

# Routers
app.include_router(users.router)
