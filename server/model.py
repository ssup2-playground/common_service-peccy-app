from pydantic import BaseModel


# Hobby
class HobbyRequest(BaseModel):
    name: str


class HobbyResponse(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True
