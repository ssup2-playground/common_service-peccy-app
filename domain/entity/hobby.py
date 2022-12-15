from sqlalchemy import Column, Integer, String
from domain.entity import ModelBase


class HobbyEntity(ModelBase):
    __tablename__ = "hobbies"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(255))

    def __init__(self, name=None):
        self.name = name
    
    def __repr__(self):
        return f"<Hobby(name={self.name})>"
