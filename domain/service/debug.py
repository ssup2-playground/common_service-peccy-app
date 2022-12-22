import os
import socket

class DebugService:
    def read_hostname(self) -> dict[str, str]:
        return {"hostname": socket.gethostname()}

    def read_region(self) -> dict[str, str]:
        return {"region": os.environ.get("AWS_REGION", "Local")}

    def read_version(self) -> dict[str, str]:
        return {"version": "v0.1.3"}
