from pyrogram import Client
from pyrogram import filters
from pyrogram.types import Message
from config import bot, call_py, HNDLR, contact_filter
from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue
from var import Var

SUDO_USERS = []
for x in Var.SUDO_USERS: 
    SUDO_USERS.append(x)

@Client.on_message(filters.command(["pause"], prefixes=f"{HNDLR}"))
async def ping(_, e: Message):
    if e.from_user.id in SUDO_USERS:
    await e.delete()
    chat_id = e.chat.id
    if chat_id in QUEUE:
        try:
            await call_py.pause_stream(chat_id)
            await e.reply(
                f"**Paued In {chat_id}**"
            )
        except Exception as e:
            await e.reply(f"**ERROR** \n`{e}`")
    else:
        await e.reply("**Nothing is playing!**")
      
