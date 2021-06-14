from pyrogram import filters
from pyrogram.types import Message

from HEMusicBot.services.callsmusic.callsmusic import client as USER


@USER.on_message(filters.text & filters.private & ~filters.me & ~filters.bot)
async def pmPermit(client: USER, message: Message):
    await USER.send_message(
        message.chat.id,
        "**Hi there, This is a music assistant service  @@Tg_Group_Music_Vc_V2_Bot.**\n\n ❗️ **Rules:**\n   - No chatting allowed\n   - No spam allowed \n\n 👉 **SEND GROUP INVITE LINK OR USERNAME IF USERBOT CAN'T JOIN YOUR GROUP.**\n\n **⚠️ Disclamer:** If you are sending a message here it means admin from @hackelite01 will see your message and join chat\n    - Don't add this user to secret groups.\n   - Don't Share private info here.\n\n**Feel Free to Contact Us @mayank_ka_b_for_bot.**",
    )
    return
