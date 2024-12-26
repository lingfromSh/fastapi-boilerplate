from tortoise import Tortoise

from core.logger import logger


async def success_handler(**kwargs) -> dict:
    return {"status": "ok", "checks": kwargs}


async def failure_handler(**kwargs) -> dict:
    return {"status": "error", "checks": kwargs}


async def is_database_ready() -> bool:
    """
    Check if the database is ready
    """
    try:
        await Tortoise.get_connection("default").execute_query("SELECT 1")
        return True
    except Exception as e:
        logger.error(f"database is not ready: {e}")
        return False
