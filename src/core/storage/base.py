import typing as t
from os import PathLike


class Storage:
    """
    Base Storage class.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the storage.

        subclasses can override this method to initialize the storage.
        """

    def open(self, path: t.Union[PathLike, str], mode: t.Literal["rb", "r"] = "rb") -> t.IO:
        """
        Open a file with the given mode.

        :param path: The path to the file.
        :param mode: The mode to open the file in. defaults to "rb".
        :return: The io object.
        """
        raise NotImplementedError

    async def write(self, path: t.Union[PathLike, str], data: t.Any) -> None:
        """
        Write data to a file.

        :param path: The path to the file.
        :param data: The data to write to the file.
        :return: None
        """
        raise NotImplementedError

    async def read(self, path: t.Union[PathLike, str], mode: t.Literal["rb", "r"]) -> t.Any:
        """
        Read data from a file.

        :param path: The path to the file.
        :param mode: The mode to open the file in.
        :return: The data read from the file.
        """
        opened = await self.open(path, mode)
        return await opened.read()

    async def stream(
        self, path: t.Union[PathLike, str], mode: t.Literal["rb", "r"], chunk_size: int = 1024
    ) -> t.AsyncGenerator[bytes, None]:
        """
        Stream data from a file.

        :param path: The path to the file.
        :param mode: The mode to open the file in.
        :param chunk_size: The size of each chunk to read.
        """
        raise NotImplementedError

    async def delete(self, path: t.Union[PathLike, str]) -> None:
        """
        Delete a file.

        :param path: The path to the file.
        :return: None
        """
        raise NotImplementedError
