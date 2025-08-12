from sqlalchemy import Colum, Integer, String
from app.db.database import Base

class Item(Base):
    __tablename__ = "item"
    id = Colum(Integer, primary_key=True, index=True)
    name = Colum(String, nullable=False, unique=True)
    description = Colum(String, nullable=True)
