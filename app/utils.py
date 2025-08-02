from telebot.types import Message
from typing import Optional

from app import logger


def parse_id(message: Message) -> int:
    try:
        return message.chat.id
    except Exception as e:
        logger.error(f"Error: failed to parse chat_id: {e}")
        raise