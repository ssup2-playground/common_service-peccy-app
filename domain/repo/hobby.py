from typing import List
from domain.entity.hobby import Hobby


class HobbyRepository:
    def list(self) -> List[Hobby]:
        return [Hobby(0, "zero"), Hobby(1, "one")]

    def create(self, hobby: Hobby) -> Hobby:
        return Hobby(0, hobby.name)

    def read(self, hobby_id: int) -> Hobby:
        return Hobby(hobby_id, "get")

    def delete(self, hobby_id: int) -> bool:
        return True
