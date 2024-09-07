from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command
from keyboards.for_main_menu import main_menu_kb
from aiogram.filters import Text

router = Router()


@router.message(Command(commands=["help"]))
async def cmd_help(message: Message):
    await message.answer(
        text="Бот представляет собой разработку виртуального секретаря, который помогает в организации, учете и документировании проведенных совещаний. Он умеет: \n"
             " -Расшифровывать аудиофайлы в формате .mp3 🔉\n"
             " -Предоставление транскрипции записи в виде протоколов в форматах *.docx и *.pdf 📄\n"
             " -Отправляет историю вложений, отправленных ему🗂 ",
        reply_markup=main_menu_kb()
    )

@router.message(Text(text="🆘 Помощь"))
async def action_chosen_incorrectly(message: Message):
    await message.answer(
        text="Бот представляет собой разработку виртуального секретаря, который помогает в организации, учете и документировании проведенных совещаний. Он умеет: \n"
             " -Расшифровывать аудиофайлы в формате .mp3 🔉\n"
             " -Предоставление транскрипции записи в виде протоколов в форматах *.docx и *.pdf 📄\n"
             " -Отправляет историю вложений, отправленных ему🗂 ",
        reply_markup=main_menu_kb()
    )
