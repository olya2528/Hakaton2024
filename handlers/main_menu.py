import asyncio

from aiogram import Router, Dispatcher
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, ReplyKeyboardRemove
from keyboards.for_main_menu import main_menu_kb
from keyboards.simple_keyboard import make_row_cancel
from aiogram.filters import Command
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text
from aiogram import F



router = Router()


@router.message(Command(commands=["start"]))
async def cmd_start(message: Message, state: FSMContext):
    await message.answer(
        text="Здравствуйте, перед вами ИИ секретарь для совещаний🪄\n"
             "Выберите необходимый пункт из меню ниже⬇️",
        reply_markup=main_menu_kb()
    )


@router.message(Text(text="❌ Отмена"))
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text="❌ Действие отменено",
        reply_markup=main_menu_kb()
    )