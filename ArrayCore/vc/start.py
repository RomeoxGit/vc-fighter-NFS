from pyrogram import Client, filters
from pyrogram.types import Message

from search import vcbot, SUDO_USERS, HNDLR, hl


@vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["start"], prefixes=HNDLR))
async def start(_, e: Message):
    await vcbot.send_message(f"Vc Raid Bot Is Working Fine. \nSend `{hl}help` To Know Your Commands. \n\n< Powered By @ArrayCore >")
