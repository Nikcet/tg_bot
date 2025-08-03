import asyncio

from app import config, logger
from app.utils import parse_id
from app.database.connection import DatabaseConnection
from app.database.models import Language

from telebot.async_telebot import AsyncTeleBot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from telebot.asyncio_handler_backends import ContinueHandling


bot = AsyncTeleBot(token=config.bot_token, colorful_logs=True)


@bot.message_handler(commands=["start"])
async def send_welcome(message: Message):

    if message.from_user is None:
        logger.error(f"Ошибка при получении пользователя: {message}")
        return

    user = db.create_user(
        user_id=message.from_user.id,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
        username=message.from_user.username,
        is_premium=(
            message.from_user.is_premium if message.from_user.is_premium else False
        ),
    )
    if user is None:
        logger.error(f"Ошибка при создании пользователя: {message.from_user.id}")
        return
    sent_message = await bot.reply_to(message, f"Привет, {user.first_name}!")
    # await bot.send_message(message.chat.id, f"Привет, {user.first_name}!")
    # await asyncio.sleep(5)
    # await bot.edit_message_text("Привет! Как дела?", message.chat.id, sent_message.message_id)


@bot.message_handler(commands=["settings"])
async def set_settings(message):
    markup = InlineKeyboardMarkup()
    markup.add(
        InlineKeyboardButton("Язык", callback_data="set_language"),
        InlineKeyboardButton("Страна", callback_data="set_country"),
    )
    text = "Выберите, что хотите настроить:"
    await bot.send_message(message.chat.id, text, reply_markup=markup)


@bot.callback_query_handler(
    func=lambda call: call.data in ["set_language", "set_country"]
)
async def handle_settings_callback(call):
    text: str = ""
    if call.data == "set_language":
        text = "Вы выбрали настройку языка. (Здесь будет выбор языка)"
    elif call.data == "set_country":
        text = "Вы выбрали настройку страны. (Здесь будет выбор страны)"
    await bot.answer_callback_query(call.id)
    await bot.send_message(call.message.chat.id, text)


@bot.message_handler(func=lambda message: True)
async def handle_massages(message):
    text = "Тут будет вся магия"
    await bot.send_message(message.chat.id, text)


if __name__ == "__main__":
    db = DatabaseConnection()
    asyncio.run(bot.polling())
