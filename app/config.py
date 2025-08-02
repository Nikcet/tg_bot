import os
from dotenv import load_dotenv
from functools import lru_cache
from typing import Optional

from pydantic_settings import BaseSettings

from app import logger

load_dotenv()


class Config(BaseSettings):
    bot_token: str = os.getenv("BOT_TOKEN", "")
    open_api_url: str = os.getenv("OPEN_API_URL", "")
    open_api_key: str = os.getenv("OPEN_API_KEY", "")
    webhook_url: Optional[str] = os.getenv("WEBHOOK_URL")
    webhook_port: int = int(os.getenv("WEBHOOK_PORT", "8443"))
    debug: bool = os.getenv("DEBUG", "False").lower() == "true"
    log_file: str = os.getenv("LOG_FILE", "logs.log")


@lru_cache
def get_config() -> Config:
    logger.info("Loading config from env...")
    return Config()


config = get_config()
