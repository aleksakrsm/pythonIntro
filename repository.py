from sqlmodel import Session, SQLModel, select
from typing import Type, Optional


def create_entity(session: Session, entity):
    session.add(entity)
    session.commit()
    session.refresh(entity)
    return entity

# how to update?

def delete_entity(session: Session, model: Type[SQLModel], entity_id: int) -> bool:
    obj = session.get(model, entity_id)
    if obj:
        session.delete(obj)
        session.commit()
        return True
    return False

# def get_entity(session: Session, model: Type[SQLModel], object_id: int):
def get_entity(session: Session, model: Type[SQLModel], entity_id: int) -> Optional[SQLModel]:
    return session.get(model, entity_id)

def get_entities(session: Session, model: Type[SQLModel]):
    return session.exec(select(model)).all()


