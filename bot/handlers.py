import aiohttp
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, BufferedInputFile

router = Router()



@router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"Привет, @{message.from_user.id} {message.from_user.full_name} {message.from_user.username}, используй команду /help")
#docker-compose up --build в консоль при изменении любого скрипта


@router.message(Command('help'))
async def help(message: Message):
    await message.answer(f"/cat http_status_number - показывает картинку с выбранным http статусом")


@router.message(Command('cat'))
async def cat(message: Message, command: CommandObject):
    status_code = command.args
    print(command)
    print(command.args)
    url = f"https://http.cat/{status_code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = BufferedInputFile(await response.read(), filename='cat.png')
                await message.answer_photo(photo=image_data)
            else:
                await message.answer(f'ошибка: {response.status}')
