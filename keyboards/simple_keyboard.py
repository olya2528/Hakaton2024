from aiogram.utils.keyboard import ReplyKeyboardMarkup, KeyboardButton


def make_row_keyboard(items: [str]) -> ReplyKeyboardMarkup:
    row = [[KeyboardButton(text=item)] for item in items]
    return ReplyKeyboardMarkup(keyboard=row, resize_keyboard=True)


def make_row_cancel(items: [str]) -> ReplyKeyboardMarkup:
    row = [[KeyboardButton(text=item)] for item in items]
    row = row + [[KeyboardButton(text="❌ Отмена")]]
    return ReplyKeyboardMarkup(keyboard=row, resize_keyboard=True)
