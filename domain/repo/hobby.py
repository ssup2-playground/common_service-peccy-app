from typing import List

from domain.repo import engine
from domain.entity import ModelBase
from domain.entity.hobby import HobbyEntity
from sqlalchemy.orm import Session


class HobbyRepository:
    def __init__(self) -> None:
        ModelBase.metadata.create_all(bind=engine)
        return

    def list(self, db: Session) -> List[HobbyEntity]:
        return db.query(HobbyEntity).all()

    def create(self, db: Session, hobby: HobbyEntity) -> None:
        db.add(hobby)
        return

    def read(self, db: Session, hobby_id: int) -> HobbyEntity:
        return db.query(HobbyEntity).get(hobby_id)

    def delete(self, db: Session, hobby_id: int) -> None:
        hobby = db.query(HobbyEntity).get(hobby_id)
        db.delete(hobby)
        return
