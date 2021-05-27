from callsmusic.callsmusic import client as USER
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from pyrogram.errors import UserAlreadyParticipant
from helpers.decorators import errors, authorized_users_only

@Client.on_message(filters.group & filters.command(["userbotkatil"]))
@authorized_users_only
@errors
async def addchannel(client, message):
    chid = message.chat.id
    try:
        invitelink = await client.export_chat_invite_link(chid)
    except:
        await message.reply_text(
            "<b>Önce Anonim Gönder seçeneği dışında tüm izinler beni Grubunun yöneticisi olarak ekle ve kontrol etmelisin /help</b>",
        )
        return

    try:
        user = await USER.get_me()
    except:
        user.first_name =  "EfsaneStarMusic"

    try:
        await USER.join_chat(invitelink)
        await USER.send_message(message.chat.id,"I joined here as you requested")
    except UserAlreadyParticipant:
        await message.reply_text(
            "<b>Asistanınız zaten sohbetinizde</b>",
        )
        pass
    except Exception as e:
        print(e)
        await message.reply_text(
            f"<b>🛑 Taşan Bekleme Hatası 🛑 \n kullanıcı {user.first_name} userbot için yoğun katılım istekleri nedeniyle grubunuza katılamadı! Kullanıcının grupta yasaklı olmadığından emin olun."
            "\n\nVeya grubunuza el ile EfsaneStarMusic ekleyin ve yeniden deneyin</b>",
        )
        return
    await message.reply_text(
            "<b>Adayanıklı userbot sohbetinize katıldı</b>",
        )
    
@USER.on_message(filters.group & filters.command(["userbotayril"]))
async def rem(USER, message):
    try:
        await USER.leave_chat(message.chat.id)
    except:  
        await message.reply_text(
            f"<b>Kullanıcı grubunuzdan ayrılamadı! Floodwaits olabilir."
            "\n\nYa da beni manuel olarak grubunuza Al veya kovmalısın.</b>",
        )
        return
 
