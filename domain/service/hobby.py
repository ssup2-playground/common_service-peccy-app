from typing import List
from domain.entity.hobby import Hobby
from domain.repo.hobby import HobbyRepository


class HobbyService:
    def list_hobbies(self) -> List[Hobby]:
        return HobbyRepository().list()

    def get_hobby(self, hobby_id: int) -> Hobby:
        return HobbyRepository().read(hobby_id)

    def create_hobby(self, hobby: Hobby) -> Hobby:
        return HobbyRepository().create(hobby)

    def delete_hobby(self, hobby_id: int) -> bool:
        return HobbyRepository().delete(hobby_id)
