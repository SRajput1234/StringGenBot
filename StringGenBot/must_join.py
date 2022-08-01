from env import MUST_JOIN
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden


@Client.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not MUST_JOIN:  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await bot.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(photo="https://telegra.ph/file/1657fd009d20d2b2e8a1a.jpg", caption=f"» 𝐀𝐂𝐂𝐎𝐑𝐃𝐈𝐍𝐆 𝐓𝐎 𝐌𝐘 𝐁𝐀𝐓𝐀𝐁𝐀𝐒𝐄 𝐘𝐎𝐔'𝐑𝐄 𝐍𝐎𝐓 𝐉𝐎𝐈𝐍𝐄𝐃 [🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 𝄟⃟💫]({link})𝐈𝐅 𝐘𝐎𝐔 𝐖𝐀𝐍𝐓 𝐔𝐒𝐄 𝐌𝐄 𝐓𝐇𝐄𝐍 𝐉𝐎𝐈𝐍 [🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 𝄟⃟💫]({link}) 𝐀𝐍𝐃 𝐒𝐓𝐀𝐑𝐓 𝐌𝐄 𝐀𝐆𝐀𝐈𝐍 !",
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("🥺 🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 𝄟⃟💫 🥺", url=f"{link}")]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"Promote me as an admin in the MUST_JOIN chat : {MUST_JOIN} !")
