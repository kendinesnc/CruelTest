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
🤖 @Mehmett_12 tarafından @RgSohbet grubuna özel kodlanmıştır.
**Grubunuza özel müzik botu yaptırmak için sahibim ile iletişime geçebilirsiniz.**
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Sohbet Grubumuz", url="https://t.me/cruelmuzikanal"
                    ),
                    InlineKeyboardButton(
                        "Grubunuza Özel Bot Yaptırmak İçin", url="https://t.me/sancaklar_federasyonu"
                    )
                ]
            ]
        )
    )