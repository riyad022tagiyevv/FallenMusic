








from pyrogram import filters
from pyrogram.types import Message
 
from FallenMusic import ASS_MENTION, LOGGER, SUDOERS, app, app2
 
 
@app.on_message(filters.command(["asspfp", "setpfp"], [".", "/", "!"]) & SUDOERS)
async def set_pfp(_, message: Message):
    if message.reply_to_message.photo:
        fuk = await message.reply_text("📡 Köməkçinin profil şəklinin dəyişdirilməsi...")
        img = await message.reply_to_message.download()
        try:
            await app2.set_profile_photo(photo=img)
            return await fuk.edit_text(
                f"✅ {ASS_MENTION} Profil şəkli uğurla dəyişdirildi."
            )
        except:
            return await fuk.edit_text("❌ Assistant profil şəklini dəyişmək alınmadı.")
    else:
        await message.reply_text(
            "ℹ️ Köməkçinin profil şəklini dəyişmək üçün fotoya cavab verin."
        )
 
 
@app.on_message(filters.command(["delpfp", "delasspfp"], [".", "/", "!"]) & SUDOERS)
async def set_pfp(_, message: Message):
    try:
        pfp = [p async for p in app2.get_chat_photos("me")]
        await app2.delete_profile_photos(pfp[0].file_id)
        return await message.reply_text(
            "✅ Köməkçinin profil şəkli uğurla silindi."
        )
    except Exception as ex:
        LOGGER.error(ex)
        await message.reply_text("❌ Assistantın profil şəklini silmək alınmadı.")
 
 
@app.on_message(filters.command(["assbio", "setbio"], [".", "/", "!"]) & SUDOERS)
async def set_bio(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            newbio = msg.text
            await app2.update_profile(bio=newbio)
            return await message.reply_text(
                f"✅ {ASS_MENTION} Bio uğurla dəyişdi."
            )
    elif len(message.command) != 1:
        newbio = message.text.split(None, 1)[1]
        await app2.update_profile(bio=newbio)
        return await message.reply_text(f"» ✅ {ASS_MENTION} Bio uğurla dəyişdi.")
    else:
        return await message.reply_text(
            "♻️ Mesaja cavab verin və ya onu köməkçinin tərcümeyi-halı kimi təyin etmək üçün mətn verin."
        )
 
 
@app.on_message(filters.command(["assname", "setname"], [".", "/", "!"]) & SUDOERS)
async def set_name(_, message: Message):
    msg = message.reply_to_message
    if msg:
        if msg.text:
            name = msg.text
            await app2.update_profile(first_name=name)
            return await message.reply_text(
                f"✅ {ASS_MENTION} Adı uğurla dəyişdi."
            )
    elif len(message.command) != 1:
        name = message.text.split(None, 1)[1]
        await app2.update_profile(first_name=name, last_name="")
        return await message.reply_text(f"✅ {ASS_MENTION} Adı uğurla dəyişdi.")
    else:
        return await message.reply_text(
            "♻️ Mesaja cavab verin və ya onu köməkçinin yeni adı kimi təyin etmək üçün mətn verin."
        )
