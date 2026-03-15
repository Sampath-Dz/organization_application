from sqlalchemy.orm import Session

def create_item(db: Session, model_class, obj_data: dict):
    db_obj = model_class(**obj_data)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def get_all_items(db: Session, model_class):
    return db.query(model_class).all()
