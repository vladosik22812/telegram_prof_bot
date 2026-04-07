from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

# Главное меню с обычными кнопками
def get_main_menu():
    buttons = [
        [KeyboardButton(text="📚 Специальности")],
        [KeyboardButton(text="🧪 Пройти тест")],
        [KeyboardButton(text="❓ Часто задаваемые вопросы")],
        [KeyboardButton(text="📞 Контакты")]
    ]
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard

# Inline клавиатура для специальностей
def get_specialties_inline():
    buttons = [
        [InlineKeyboardButton(text="🤖 Мехатроника", callback_data="spec_mechatron")],
        [InlineKeyboardButton(text="⚖️ Правоохранительная деятельность", callback_data="spec_law")],
        [InlineKeyboardButton(text="🔍 Дефектоскопист", callback_data="spec_defect")],
        [InlineKeyboardButton(text="💻 Компьютерные системы", callback_data="spec_compsys")],
        [InlineKeyboardButton(text="👨‍💻 Разработка и управление ПО", callback_data="spec_prog")],
        [InlineKeyboardButton(text="⚡ Эксплуатация электрического оборудования", callback_data="spec_electric")],
        [InlineKeyboardButton(text="⚙️ Технология машиностроения", callback_data="spec_tech")],
        [InlineKeyboardButton(text="📄 Документационное обеспечение", callback_data="spec_doc")],
        [InlineKeyboardButton(text="🌾 Землеустройство", callback_data="spec_zem")],
        [InlineKeyboardButton(text="🏠 Мастер отделочных работ", callback_data="spec_otdel")],
        [InlineKeyboardButton(text="🔥 Сварщик", callback_data="spec_weld")],
        [InlineKeyboardButton(text="⚖️ Юриспруденция", callback_data="spec_jur")],
        [InlineKeyboardButton(text="🏗️ Строительство зданий", callback_data="spec_build")],
        [InlineKeyboardButton(text="🔥 Сварочное производство", callback_data="spec_weldprod")],
        [InlineKeyboardButton(text="🤖 Интеграция решений с ИИ", callback_data="spec_ai")]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard