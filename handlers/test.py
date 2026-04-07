from database import save_test_result
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from handlers.specialties import specialties_info

# Класс состояний для теста
class TestStates(StatesGroup):
    q1 = State()
    q2 = State()
    q3 = State()
    q4 = State()
    q5 = State()
    q6 = State()
    q7 = State()
    q8 = State()
    result = State()

# Словарь с вопросами и вариантами ответов
questions = {
    "q1": {
        "text": "1/8: Какой школьный предмет тебе нравился больше всего?",
        "options": {
            "а) Информатика / Математика": "it",
            "б) Физика": "tech",
            "в) Обществознание / История": "law",
            "г) Труд / Технология": "work",
            "д) Ничего не нравилось, я гуманитарий": "doc"
        }
    },
    "q2": {
        "text": "2/8: Что тебе больше нравится делать в свободное время?",
        "options": {
            "а) Сидеть за компом, кодить или играть": "it",
            "б) Ковыряться в технике, чинить, паять": "electric",
            "в) Смотреть фильмы про полицию, суды": "law",
            "г) Мастерить, строить, создавать руками": "build",
            "д) Гулять, общаться с друзьями": "zem"
        }
    },
    "q3": {
        "text": "3/8: Какая фраза тебе ближе?",
        "options": {
            "а) 'Лучше один раз увидеть, чем сто раз услышать'": "defect",
            "б) 'Семь раз отмерь, один раз отрежь'": "tech",
            "в) 'Закон суров, но это закон'": "law",
            "г) 'Делу время, потехе час'": "doc",
            "д) 'Сделай красиво'": "otdel"
        }
    },
    "q4": {
        "text": "4/8: Где бы ты хотел работать?",
        "options": {
            "а) В уютном офисе за компьютером": "it",
            "б) На современном производстве с роботами": "mechatron",
            "в) На свежем воздухе, на объектах": "zem",
            "г) В цеху, где пахнет металлом": "weld",
            "д) В кабинете с людьми, документами": "jur"
        }
    },
    "q5": {
        "text": "5/8: Что тебя больше всего мотивирует?",
        "options": {
            "а) Создать что-то новое": "it",
            "б) Понять, как работает механизм": "tech",
            "в) Восстановить справедливость": "law",
            "г) Сделать мир красивее": "build",
            "д) Стабильность и уверенность": "defect"
        }
    },
    "q6": {
        "text": "6/8: Какая у тебя суперсила?",
        "options": {
            "а) Вижу ошибки в коде за милю": "it",
            "б) Могу починить всё, что сломано": "electric",
            "в) Чувствую, когда люди врут": "law",
            "г) Могу ровно положить плитку": "otdel",
            "д) Вижу микротрещины в металле": "defect"
        }
    },
    "q7": {
        "text": "7/8: Что важнее в работе?",
        "options": {
            "а) Творчество и самовыражение": "it",
            "б) Чёткое следование инструкциям": "tech",
            "в) Общение с людьми и помощь": "law",
            "г) Конкретный результат своими руками": "weld",
            "д) Порядок и структура": "doc"
        }
    },
    "q8": {
        "text": "8/8: Что тебе кажется самым интересным?",
        "options": {
            "а) Создавать игры и приложения": "it",
            "б) Разбираться в технике и механизмах": "mechatron",
            "в) Следить за порядком и законом": "law",
            "г) Строить и ремонтировать": "build",
            "д) Искать дефекты и проверять качество": "defect"
        }
    }
}

# Словарь для подсчёта баллов
scores = {
    "it": 0,
    "tech": 0,
    "law": 0,
    "work": 0,
    "doc": 0,
    "electric": 0,
    "build": 0,
    "zem": 0,
    "defect": 0,
    "mechatron": 0,
    "weld": 0,
    "otdel": 0,
    "jur": 0
}

# Соответствие групп специальностям
specialty_groups = {
    "it": ["spec_compsys", "spec_prog", "spec_ai"],
    "tech": ["spec_tech", "spec_mechatron"],
    "law"
    : ["spec_law", "spec_jur"],
    "work": ["spec_weld", "spec_weldprod"],
    "doc": ["spec_doc"],
    "electric": ["spec_electric"],
    "build": ["spec_build"],
    "zem": ["spec_zem"],
    "defect": ["spec_defect"],
    "mechatron": ["spec_mechatron"],
    "weld": ["spec_weld", "spec_weldprod"],
    "otdel": ["spec_otdel"],
    "jur": ["spec_jur"]
}

# Функция для создания клавиатуры с вариантами ответов
def get_options_keyboard(options: dict):
    buttons = []
    for option_text in options.keys():
        buttons.append([KeyboardButton(text=option_text)])
    keyboard = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return keyboard

# Старт теста
async def start_test(message: types.Message, state: FSMContext):
    await state.clear()
    await state.set_state(TestStates.q1)
    await state.update_data(scores={key: 0 for key in scores.keys()})
    await message.answer(
        questions["q1"]["text"],
        reply_markup=get_options_keyboard(questions["q1"]["options"])
    )

# Обработчик ответов на вопросы
async def process_answer(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if not current_state:
        return

    data = await state.get_data()
    user_scores = data.get("scores", {key: 0 for key in scores.keys()})

    state_map = {
        TestStates.q1: "q1",
        TestStates.q2: "q2",
        TestStates.q3: "q3",
        TestStates.q4: "q4",
        TestStates.q5: "q5",
        TestStates.q6: "q6",
        TestStates.q7: "q7",
        TestStates.q8: "q8"
    }

    current_q = state_map.get(current_state)
    if not current_q:
        return

    selected_group = None
    for option_text, group in questions[current_q]["options"].items():
        if message.text == option_text:
            selected_group = group
            break

    if not selected_group:
        await message.answer("Пожалуйста, выбери вариант из кнопок")
        return

    user_scores[selected_group] = user_scores.get(selected_group, 0) + 1
    await state.update_data(scores=user_scores)

    next_states = {
        TestStates.q1: TestStates.q2,
        TestStates.q2: TestStates.q3,
        TestStates.q3: TestStates.q4,
        TestStates.q4: TestStates.q5,
        TestStates.q5: TestStates.q6,
        TestStates.q6: TestStates.q7,
        TestStates.q7: TestStates.q8,
        TestStates.q8: TestStates.result
    }

    next_state = next_states.get(current_state)

    if next_state == TestStates.result:
        await show_result(message, state)
    else:
        next_q = state_map[next_state]
        await state.set_state(next_state)
        await message.answer(
            questions[next_q]["text"],
            reply_markup=get_options_keyboard(questions[next_q]["options"])
        )

# Показ результата
async def show_result(message: types.Message, state: FSMContext):
    data = await state.get_data()
    user_scores = data.get("scores", {})

    specialty_scores = {}
    for group, score in user_scores.items():
        if group in specialty_groups:
            for spec_id in specialty_groups[group]:
                specialty_scores[spec_id] = specialty_scores.get(spec_id, 0) + score

    sorted_specs = sorted(specialty_scores.items(), key=lambda x: x[1], reverse=True)
    top_specs = sorted_specs[:3]

    result_text = "🎉 **Твои результаты:**\n\n"
    result_text += "Тебе больше всего подходят:\n\n"

    for i, (spec_id, score) in enumerate(top_specs, 1):
        spec_info = specialties_info.get(spec_id, {"name": "Специальность"})
        result_text += f"{i}. {spec_info['name']} — {score} баллов\n"

    result_text += "\nХочешь узнать подробнее о специальностях? Нажми 📚 Специальности"

    # Сохраняем результат в базу данных
    try:
        save_test_result(message.from_user.id, user_scores)
        print(f"✅ Результат теста сохранён для пользователя {message.from_user.id}")
    except Exception as e:
        print(f"❌ Ошибка сохранения результата: {e}")

    from keyboards.main_menu import get_main_menu
    await message.answer(
        result_text,
        reply_markup=get_main_menu(),
        parse_mode="Markdown"
    )

    await state.clear()

# Регистрация обработчиков
def register_handlers(dp):
    dp.message.register(start_test, lambda msg: msg.text == "🧪 Пройти тест")
    dp.message.register(process_answer, lambda msg: msg.text in [
        "а) Информатика / Математика",
        "б) Физика",
        "в) Обществознание / История",
        "г) Труд / Технология",
        "д) Ничего не нравилось, я гуманитарий",
        "а) Сидеть за компом, кодить или играть",
        "б) Ковыряться в технике, чинить, паять",
        "в) Смотреть фильмы про полицию, суды",
        "г) Мастерить, строить, создавать руками",
        "д) Гулять, общаться с друзьями",
        "а) 'Лучше один раз увидеть, чем сто раз услышать'",
        "б) 'Семь раз отмерь, один раз отрежь'",
        "в) 'Закон суров, но это закон'",
        "г) 'Делу время, потехе час'",
        "д) 'Сделай красиво'",
        "а) В уютном офисе за компьютером",
        "б) На современном производстве с роботами",
        "в) На свежем воздухе, на объектах",
        "г) В цеху, где пахнет металлом",
        "д) В кабинете с людьми, документами",
        "а) Создать что-то новое",
        "б) Понять, как работает механизм",
        "в) Восстановить справедливость",
        "г) Сделать мир красивее",
        "д) Стабильность и уверенность",
        "а) Вижу ошибки в коде за милю",
        "б) Могу починить всё, что сломано",
        "в) Чувствую, когда люди врут",
        "г) Могу ровно положить плитку",
        "д) Вижу микротрещины в металле",
        "а) Творчество и самовыражение",
        "б) Чёткое следование инструкциям",
        "в) Общение с людьми и помощь",
        "г) Конкретный результат своими руками",
        "д) Порядок и структура",
        "а) Создавать игры и приложения",
        "б) Разбираться в технике и механизмах",
        "в) Следить за порядком и законом",
        "г) Строить и ремонтировать",
        "д) Искать дефекты и проверять качество"
    ])