from typing import List
from sqlalchemy.orm import Session

from domain.repo.hobby import HobbyRepository
from domain.entity.hobby import HobbyEntity


class HobbyService:
    def __init__(self) -> None:
        self.repo = HobbyRepository()
        return

    def list_hobbies(self, db: Session) -> List[HobbyEntity]:
        return self.repo.list(db)

    def get_hobby(self, db: Session, hobby_id: int) -> HobbyEntity:
        db.begin()
        hobby = self.repo.read(db, hobby_id)
        db.commit()
        return hobby

    def create_hobby(self, db: Session, hobby: HobbyEntity) -> HobbyEntity:
        db.begin()
        self.repo.create(db, hobby)
        db.commit()
        return hobby

    def delete_hobby(self, db: Session, hobby_id: int) -> None:
        db.begin()
        self.repo.delete(db, hobby_id)
        db.commit()
        return
