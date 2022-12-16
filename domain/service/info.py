from fastapi import UploadFile
from fastapi.responses import FileResponse


class InfoService:
    def read_info_name(self) -> dict[str, str]:
        return {"name": "peccy"}

    def read_info_piecture(self) -> FileResponse:
        return FileResponse("assets/peccy.png", media_type="image/png")

    def update_info_piecture(self, file: UploadFile) -> dict[str, str]:
        picture = file.file.read()
        with open("assets/peccy.png", "wb") as f:
            f.write(picture)
        return {"result": "ok"}
