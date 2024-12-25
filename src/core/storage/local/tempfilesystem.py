import os
import tempfile

import aiofiles

from core.storage.base import Storage


class TempFileSystemStorage(Storage):
    """
    Temporary File System Storage class.
    All files are automatically deleted when the class is destroyed.
    """

    def __init__(self, *args, **kwargs):
        self.temp_dir = tempfile.TemporaryDirectory()
        super().__init__(*args, **kwargs)

    def open(self, path, mode):
        full_path = os.path.join(self.temp_dir.name, path)
        return aiofiles.open(full_path, mode)

    async def write(self, path, data):
        async with self.open(path, "wb") as f:
            await f.write(data)

    async def read(self, path, mode="rb"):
        async with self.open(path, mode) as f:
            return await f.read()

    async def stream(self, path, mode, chunk_size=1024):
        async with self.open(path, mode) as f:
            while chunk := await f.read(chunk_size):
                yield chunk

    async def delete(self, path):
        try:
            full_path = os.path.join(self.temp_dir.name, path)
            os.remove(full_path)
        except FileNotFoundError:
            pass

    def __del__(self):
        self.temp_dir.cleanup()
