from aiogram import types
from keyboards.main_menu import get_main_menu, get_specialties_inline

async def show_specialties(message: types.Message):
    await message.answer(
        "Выберите интересующую специальность:",
        reply_markup=get_specialties_inline()
    )

async def show_faq(message: types.Message):
    faq_text = "❓ Часто задаваемые вопросы:\n\n"
    faq_text += "• Какие документы нужны для поступления?\n"
    faq_text += "• Какие экзамены нужно сдавать?\n"
    faq_text += "• Есть ли общежитие?\n"
    faq_text += "• Какие сроки подачи документов?\n\n"
    faq_text += "Скоро здесь будут подробные ответы!"

    await message.answer(faq_text)

async def show_contacts(message: types.Message):
    contacts_text = "📞 Контакты приемной комиссии ЮТМиИТ:\n\n"
    contacts_text += "📍 Адрес: г. Юрга, ул. Ленина, д. ...\n"
    contacts_text += "📞 Телефон: 8 (38451) ...\n"
    contacts_text += "📧 Email: priem@yutmiit.ru\n"
    contacts_text += "🌐 Сайт: www.yutmiit.ru\n\n"
    contacts_text += "Режим работы: Пн-Пт с 9:00 до 17:00"

    await message.answer(contacts_text)

async def show_specialties_callback(callback: types.CallbackQuery):
    await callback.message.edit_text(
        "Выберите интересующую специальность:",
        reply_markup=get_specialties_inline()
    )
    await callback.answer()

async def handle_menu(message: types.Message):
    if message.text == "📚 Специальности":
        await show_specialties(message)
    elif message.text == "❓ Часто задаваемые вопросы":
        await show_faq(message)
    elif message.text == "📞 Контакты":
        await show_contacts(message)

def register_handlers(dp):
    dp.message.register(handle_menu, lambda msg: msg.text in [
        "📚 Специальности",
        "❓ Часто задаваемые вопросы",
        "📞 Контакты"
    ])
    dp.callback_query.register(show_specialties_callback, lambda c: c.data == "back_to_specs")
