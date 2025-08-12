from fastapi import FastAPI
from app.routers import item

app = FastAPI(title="CRUD Intern Test")

app.include_router(item.router)
