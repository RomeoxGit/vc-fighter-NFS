from pyrogram import Client, filters
from pyrogram.types import Message

from ArrayCore.vc.handlers import skip_current_song, skip_item
from ArrayCore.vc.queues import QUEUE, clear_queue

from search import (Venom1, Venom2, Venom3, Venom4,
                    Venom5, Venom6, Venom7, Venom8,
                    Venom9, Venom10, Venom11, Venom12,
                    Venom13, Venom14, Venom15, vcbot,
                    HNDLR, call_py, contact_filter, SUDO_USERS)


@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["resume"], prefixes=HNDLR))
async def ping(_, e: Message):
    inp = e.text[5:]
    chat_ = await vcbot.get_chat(inp)
    chat_id = chat_.id
    if chat_id in QUEUE:
        try:
            await call_py.resume_stream(chat_id)
            await e.reply_text(f"**Resumed In {chat_.title}**")
        except Exception as e:
            await e.reply_text(f"**ERROR** \n`{e}`")
    else:
        await e.reply_text("**Nothing is currently paused!**")
