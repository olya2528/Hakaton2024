from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.for_main_menu import main_menu_kb
from aiogram.filters import Text

router = Router()


@router.message(Text(text="📝 История вложений"))
async def action_chosen_incorrectly(message: Message):
    await message.answer(
        text="За последнее время вы отправляли следующие файлы:",
        reply_markup=main_menu_kb()
    )