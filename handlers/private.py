from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import other_filters2


@Client.on_message(other_filters2)
async def start(_, message: Message):
    await message.reply_text(
        f"""Selam Ben {bn}
Sesli sohbetlerde müzik dinlemenize olanak sağlarım.
          📜Kullanma Kılavuzu📜
💠 /play - Şarkıyı oynatır.
💠 /pause - Şarkıyı durdurur.
💠 /resume - Şarkıyı devam ettirir.
💠 /skip - Diğer şarkıya geçer.
💠 /end - Botu kapatır.
💠 /song - Şarkı aratır.
💠 /arama - Şarkıyı youtube üzerinden link olarak sıralar.
💠 /userbotjoin - Asistanı sohbete davet etmek için. 
💠 /userbotleave - Asistanı sohbetten çıkartmak için. 
****
        """,
       
    )
