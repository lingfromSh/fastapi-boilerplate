import asyncio
import os

from storage.local.filesystem import FileSystemStorage
from storage.local.tempfilesystem import TempFileSystemStorage
from storage.remote.minio_storage import MinioStorage

storage = FileSystemStorage()
asyncio.run(storage.write("test.txt", b"Hello, World!"))
assert os.path.exists("test.txt")
assert asyncio.run(storage.read("test.txt", "rb")) == b"Hello, World!"
asyncio.run(storage.delete("test.txt"))
assert not os.path.exists("test.txt")

storage = TempFileSystemStorage()
asyncio.run(storage.write("test.txt", b"Hello, World!"))
path = os.path.join(storage.temp_dir.name, "test.txt")
assert os.path.exists(path)
assert asyncio.run(storage.read(path, "rb")) == b"Hello, World!"
asyncio.run(storage.delete(path))
assert not os.path.exists(path)
asyncio.run(storage.write("test.txt", b"Hello, World!"))
path = os.path.join(storage.temp_dir.name, "test.txt")
del storage
assert not os.path.exists(path)

storage = MinioStorage(endpoint="localhost:9000", access_key="minioadmin", secret_key="minioadmin", bucket_name="test")
asyncio.run(storage.write("test.txt", b"Hello, World!"))
assert asyncio.run(storage.read("test.txt", "rb")) == b"Hello, World!"
asyncio.run(storage.delete("test.txt"))
