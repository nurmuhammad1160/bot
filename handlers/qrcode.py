from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command
import segno 
from io import BytesIO
from telegraph import Telegraph
telegraph = Telegraph()

qrcode_router: Router = Router()

def save_qr(word):
    qrcode = segno.make_qr(word)
    img = BytesIO()
    qrcode.save(img, kind='png', scale=10)
    img.seek(0)
    response = telegraph.upload_file(img)
    link = 'https://telegra.ph' + response[0]['src'] 
    return link


@qrcode_router.message(Command('start'))
async def start(message: Message):
    await message.answer("Iltimos matn yuboring")


@qrcode_router.message()
async def qr(message: Message):

    link = save_qr(message.text)
    await message.reply(link)