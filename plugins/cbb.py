
from pyrogram import __version__
from levi import Bot
from config import OWNER_ID
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>○ Dᴇᴠ : <a href='https://t.me/LeviAckerman1709'>Lᴇᴠɪ</a>\n○ ᴍʏ ᴜᴘᴅᴀᴛᴇs : <a href='https://t.me/Ahjin_Sprt'>AʜJɪɴGᴜɪʟᴅ</a>\n○ Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ : <a href='https://t.me/Dub_Crunchyroll_Hindi'>Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ</a>\n○ Hᴇɴᴛᴀɪ : <a href='https://t.me/HanimeCafe'>Hᴇɴᴛᴀɪ</a>\n○ ᴀɴɪᴍᴇ ᴄʜᴀᴛ : <a href='https://t.me/Surveycorpschat'>ᴀɴɪᴍᴇ ᴄʜᴀᴛ</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("ᴄʟᴏsᴇ", callback_data = "close"),
                    InlineKeyboardButton('Aɴɪᴍᴇ Cʜᴀɴɴᴇʟ', url='https://t.me/Dub_Crunchyroll_Hindi')
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
