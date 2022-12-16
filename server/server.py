from typing import List

from fastapi import FastAPI, UploadFile, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from starlette.responses import Response
from starlette.status import HTTP_204_NO_CONTENT
from sqlalchemy.orm import Session

from server.model import HobbyRequest, HobbyResponse
from domain.repo import get_db
from domain.entity.hobby import HobbyEntity
from domain.service.info import InfoService
from domain.service.hobby import HobbyService
from domain.service.debug import DebugService

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
service_info = InfoService()
service_hobby = HobbyService()
service_debug = DebugService()

## Info handlers
@server.get("/infos/name")
def get_info_name() -> dict[str, str]:
    return service_info.read_info_name()


@server.get("/infos/picture")
def get_info_piecture() -> FileResponse:
    return service_info.read_info_piecture()


@server.put("/infos/picture")
def post_info_piecture(file: UploadFile) -> dict[str, str]:
    return service_info.update_info_piecture(file)


## Hobby handlers
@server.get("/hobbies", response_model=List[HobbyResponse])
def list_hobby(db: Session = Depends(get_db)) -> List[HobbyEntity]:
    return service_hobby.list_hobbies(db)


@server.post("/hobbies", response_model=HobbyResponse)
def create_hobby(req: HobbyRequest, db: Session = Depends(get_db)):
    hobby = HobbyEntity(**req.dict())
    return service_hobby.create_hobby(db, hobby)


@server.get("/hobbies/{hobby_id}", response_model=HobbyResponse)
def read_hobby(hobby_id: int, db: Session = Depends(get_db)) -> HobbyEntity:
    return service_hobby.read_hobby(db, hobby_id)


@server.delete("/hobbies/{hobby_id}")
def delete_hobby(hobby_id: int, db: Session = Depends(get_db)) -> dict[str, str]:
    service_hobby.delete_hobby(db, hobby_id)
    return Response(status_code=HTTP_204_NO_CONTENT)


## Debug handlers
@server.get("/debugs/hostname")
def get_debug_hostname() -> dict[str, str]:
    return service_debug.read_hostname()


@server.get("/debugs/region")
def get_debug_region() -> dict[str, str]:
    return service_debug.read_region()


@server.get("/debugs/version")
def get_debug_version() -> dict[str, str]:
    return service_debug.read_version()


## Health handlers
@server.get("/healthz")
def get_heatlhz() -> dict[str, str]:
    return {"status": "UP"}
