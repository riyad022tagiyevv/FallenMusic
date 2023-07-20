


from pyrogram import filters
from pyrogram.types import Message
 
from FallenMusic import SUDOERS, app
from FallenMusic.Helpers.active import get_active_chats
from FallenMusic.Helpers.inline import close_key
 
 
@app.on_message(filters.command("activevc", [".", "/", "!"]) & SUDOERS)
async def activevc(_, message: Message):
    mystic = await message.reply_text("♻️ Aktiv səsli qrupların siyahısı əldə edilir...")
    chats = await get_active_chats()
    text = ""
    j = 0
    for chat in chats:
        try:
            title = (await app.get_chat(chat)).title
        except Exception:
            title = "Şəxsi söhbət"
        if (await app.get_chat(chat)).username:
            user = (await app.get_chat(chat)).username
            text += f"<b>{j + 1}.</b>  [{title}](https://t.me/{user})\n"
        else:
            text += f"<b>{j + 1}. {title}</b> [`{chat}`]\n"
        j += 1
    if not text:
        await mystic.edit_text("❌ Musiqi botunda aktiv səsli qrup yoxdur")
    else:
        await mystic.edit_text(
            f"**📊 Musiqi botunda hazırda aktiv səsli qrupların siyahısı:**\n\n{text}",
            reply_markup=close_key,
            disable_web_page_preview=True,
        )
