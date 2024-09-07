from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_menu_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="🎙️ Расшифровать аудио")
    kb.button(text="🆘 Помощь")
    kb.button(text="📝 История вложений")
    kb.button(text="🗳️ Обратная связь")
    kb.adjust(3)
    return kb.as_markup(resize_keyboard=True)
