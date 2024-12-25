import os

import aiofiles

from core.storage.base import File
from core.storage.base import Storage


class FileSystemStorage(Storage):
    """
    File System Storage class.
    File operations are based on the open function.
    """

    def open(self, path) -> File:
        return File(self, path)

    async def write(self, path, data):
        async with aiofiles.open(path, "wb") as f:
            await f.write(data)

    async def read(self, path, mode="rb"):
        async with aiofiles.open(path, mode) as f:
            return await f.read()

    async def stream(self, path, mode, chunk_size=1024):
        async with aiofiles.open(path, mode) as f:
            while chunk := await f.read(chunk_size):
                yield chunk

    async def delete(self, path):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
