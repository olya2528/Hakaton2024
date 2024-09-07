from pathlib import Path
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Text
from aiogram import Router, F
from aiogram.types import ContentType, Voice, Audio, Message
from keyboards.for_main_menu import main_menu_kb
from keyboards.simple_keyboard import make_row_cancel

router = Router()

settings_menu = ["Официальный протокол", "Неофициальный протокол", "Расшифровка вcтречи"]
start_menu = [".docx", ".pdf"]
yon = ["Да","Нет"]

class Transcrib(StatesGroup):
    send_audio = State()
    choosing_format = State()
    choosing_format_file = State()
    password = State()
    password_confrim = State()



@router.message(Text(text="🎙️ Расшифровать аудио"))
async def action_chosen_incorrectly(message: Message, state: FSMContext):
    await message.answer(
        text="Отправьте, пожалуйста, аудиофайл совещания📚"
    )
    await state.set_state(Transcrib.send_audio)


@router.message(Transcrib.send_audio, F.audio)
async def action_chosen_(message: Message, state: FSMContext):
    await message.answer(
        text="Расшифровано, выберите формат протокола расшифровки",
        reply_markup=make_row_cancel(settings_menu)
    )
    await state.set_state(Transcrib.choosing_format)


@router.message(Transcrib.send_audio, F.voice)
async def action_chosen(message: Message, state: FSMContext):
    await message.answer(
        text="Расшифровано, выберите формат протокола расшифровки",
        reply_markup=make_row_cancel(settings_menu)
    )
    await state.set_state(Transcrib.choosing_format)


@router.message(Transcrib.choosing_format, Text(text="Официальный протокол"))
async def action_chosen1(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите формат документа📌",
        reply_markup=make_row_cancel(start_menu)
    )
    await state.set_state(Transcrib.choosing_format_file)


@router.message(Transcrib.choosing_format, Text(text="Неофициальный протокол"))
async def action_chosen2(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите формат документа📌",
        reply_markup=make_row_cancel(start_menu)
    )
    await state.set_state(Transcrib.choosing_format_file)


@router.message(Transcrib.choosing_format, Text(text="Расшифровка встречи"))
async def action_chosen3(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите формат документа📌",
        reply_markup=make_row_cancel(start_menu)
    )
    await state.set_state(Transcrib.choosing_format_file)


@router.message(Transcrib.choosing_format_file, Text(text=".docx"))
async def action_chosen4(message: Message, state: FSMContext):
    await message.answer(
        text="Подождите, обрабатываю файл💬",
        reply_markup=main_menu_kb()
    )
    await state.clear()

@router.message(Transcrib.choosing_format_file, Text(text=".pdf"))
async def action_chosen5(message: Message, state: FSMContext):
    await message.answer(
        text="Потребуется ли пароль?",
        reply_markup=make_row_cancel(yon)
    )
    await state.set_state(Transcrib.password)

@router.message(Transcrib.password, Text(text="Да"))
async def action_chosen6(message: Message, state: FSMContext):
    await message.answer(
        text="Введите пароль",
    )
    await state.set_state(Transcrib.password_confrim)

@router.message(Transcrib.password, Text(text="Нет"))
async def action_chosen7(message: Message, state: FSMContext):
    await message.answer(
        text="Подождите, обрабатываю файл💬",
        reply_markup=main_menu_kb()
    )
    await state.clear()

@router.message(Transcrib.password_confrim)
async def action_chosen7(message: Message, state: FSMContext):
    await message.answer(
        text="Подождите, обрабатываю файл💬",
        reply_markup=main_menu_kb()
    )
    await state.clear()


@router.message(Transcrib.send_audio)
async def action_chosen8(message: Message, state: FSMContext):
    await message.answer(
        text="‼️ Вы отправили сообщение не в том формате",
    )