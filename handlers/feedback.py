from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.for_main_menu import main_menu_kb
from aiogram.filters import Text

router = Router()


@router.message(Command(commands=["feedback"]))
async def cmd_feedback(message: Message):
    await message.answer(
        text="Для обратной связи обратитесь к @kcygan",
        reply_markup=main_menu_kb()
    )

@router.message(Text(text="🗳️ Обратная связь"))
async def action_chosen_feed(message: Message):
    await message.answer(
        text="Для обратной связи обратитесь к @kcygan",
        reply_markup=main_menu_kb()
    )