from fastapi import FastAPI
from app.routers import item 
from app.db.database import Base, engine

import app.models.item  

app = FastAPI(title="CRUD Intern Test")

Base.metadata.create_all(bind=engine)

app.include_router(item.router)
