import aiohttp
from aiogram import Router
from aiogram.filters import Command, CommandObject
from aiogram.types import Message, BufferedInputFile

router = Router()



@router.message(Command('start'))
async def start(message: Message):
    await message.answer('hey')
#docker-compose up --build в консоль при изменении любого скрипта


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
                await message.answer(f'ошибка: {response.status} ')


@router.message(Command('cat1'))
async def cat(message: Message):
    status_code = 200
    url = f"https://http.cat/{status_code}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                image_data = BufferedInputFile(await response.read(), filename='cat.png')
                await message.answer_photo(photo=image_data)
            else:
                await message.answer(f'ошибка: {response.status} ')
