from aiogram import types
from aiogram.filters import Command
from database import add_user, get_user
from keyboards.main_menu import get_main_menu

async def start_command(message: types.Message):
    user_id = message.from_user.id
    first_name = message.from_user.first_name
    username = message.from_user.username
    
    user = get_user(user_id)
    if not user:
        add_user(user_id, first_name, username)
    
    welcome_text = f"👋 Привет, {first_name}!\n\n"
    welcome_text += "Я бот-помощник для абитуриентов Юргинского техникума машиностроения и информационных технологий (ЮТМиИТ).\n\n"
    welcome_text += "Я помогу тебе:\n"
    welcome_text += "• Узнать о специальностях техникума\n"
    welcome_text += "• Пройти профориентационный тест\n"
    welcome_text += "• Получить ответы на частые вопросы\n"
    welcome_text += "• Связаться с приемной комиссией\n\n"
    welcome_text += "Выбери, что тебя интересует 👇"
    
    await message.answer(welcome_text, reply_markup=get_main_menu())

def register_handlers(dp):
    dp.message.register(start_command, Command("start"))