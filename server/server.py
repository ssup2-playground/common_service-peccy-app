from typing import List
import socket

from fastapi import FastAPI, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session

from server.model import HobbyRequest, HobbyResponse
from domain.repo import get_db
from domain.entity.hobby import HobbyEntity
from domain.service.hobby import HobbyService

# Server
server = FastAPI()

## Middelware
server.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

## Services
service_hobby = HobbyService()

## Info
@server.get("/infos/name")
def get_info_name() -> dict[str, str]:
    return {"name": "peccy v0.1.0"}


@server.put("/infos/picture")
def post_info_piecture(file: UploadFile) -> dict[str, str]:
    picture = file.file.read()
    with open("assets/peccy.png", "wb") as f:
        f.write(picture)
    return {"result": "ok"}


@server.get("/infos/picture")
def get_info_piecture() -> FileResponse:
    return FileResponse("assets/peccy.png", media_type="image/png")


## Hobby
@server.get("/hobbies", response_model=List[HobbyResponse])
def list_hobby(db: Session = Depends(get_db)) -> List[HobbyEntity]:
    return service_hobby.list_hobbies(db)


@server.post("/hobbies", response_model=HobbyResponse)
def create_hobby(req: HobbyRequest, db: Session = Depends(get_db)):
    hobby = HobbyEntity(**req.dict())
    return service_hobby.create_hobby(db, hobby)


@server.get("/hobbies/{hobby_id}", response_model=HobbyResponse)
def get_hobby(hobby_id: int, db: Session = Depends(get_db)) -> HobbyEntity:
    return service_hobby.get_hobby(db, hobby_id)


@server.delete("/hobbies/{hobby_id}")
def delete_hobby(hobby_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    service_hobby.delete_hobby(db, hobby_id)
    return Response(status_code=HTTP_204_NO_CONTENT)


## Health
@server.get("/healthz")
def get_heatlhz() -> dict[str, str]:
    return {"status": "UP"}


## Debug
@server.get("/debugs/hostname")
def get_debug_hostname() -> dict[str, str]:
    return {"hostname": socket.gethostname()}
