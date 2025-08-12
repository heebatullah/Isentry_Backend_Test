from app.models import item
from sqlalchemy.orm import Session

def get_item(db: Session, item_id: int):
    return db.query(item).get(item_id)

def get_items(db: Session, skip: int=0, limit: int=10):
    return db.query(item).offset(skip).limit(limit).all()

def create_item(db: Session, item_create):
    db_item = item(name=item_create.name, description=item_create.description)
    db.session.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
