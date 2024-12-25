import typing as t

from minio import Minio
from minio.error import S3Error

from core.storage.base import Storage


class MinioStorage(Storage):
    """
    MinIO Storage class.
    """

    def __init__(
        self, endpoint: str, access_key: str, secret_key: str, bucket_name: str, secure: bool = True, *args, **kwargs
    ):
        super().__init__(*args, **kwargs)
        self.client = Minio(endpoint, access_key=access_key, secret_key=secret_key, secure=secure, **kwargs)
        self.bucket_name = bucket_name
        self._ensure_bucket_exists()

    def _ensure_bucket_exists(self):
        if not self.client.bucket_exists(self.bucket_name):
            self.client.make_bucket(self.bucket_name)

    async def open(self, path: t.Union[str, bytes], mode: t.Literal["rb", "r"] = "rb") -> t.IO:
        return self.client.get_object(self.bucket_name, path)

    async def write(self, path: t.Union[str, bytes], data: bytes) -> None:
        try:
            self.client.put_object(
                self.bucket_name,
                path,
                data,
                length=len(data),
                part_size=1 * 1024 * 1024,  # 1MB part size
            )
        except S3Error as e:
            print(f"Error occurred: {e}")

    async def read(self, path: t.Union[str, bytes], mode: t.Literal["rb", "r"] = "rb") -> bytes:
        try:
            response = self.client.get_object(self.bucket_name, path)
            return response.read()
        except S3Error as e:
            print(f"Error occurred: {e}")
            return b""

    async def stream(
        self, path: t.Union[str, bytes], mode: t.Literal["rb", "r"] = "rb", chunk_size: int = 1024
    ) -> t.AsyncGenerator[bytes, None]:
        try:
            response = self.client.get_object(self.bucket_name, path)
            while chunk := response.read(chunk_size):
                yield chunk
        except S3Error as e:
            print(f"Error occurred: {e}")

    async def delete(self, path: t.Union[str, bytes]) -> None:
        try:
            self.client.remove_object(self.bucket_name, path)
        except S3Error as e:
            print(f"Error occurred: {e}")
