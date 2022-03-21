#@TheVenomXD

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

from .. import vcbot, SUDO_USERS, HNDLR, hl, START_VID

# @vcbot.on_message(filters.user(SUDO_USERS) & filters.private & filters.command(["start"], prefixes=HNDLR))
# async def start(_, e: Message):
   # video=START_VID,
  # await vcbot.send_video(e.chat.id, video, f"Vc Raid Bot Is Working Fine. \nSend `{hl}help` To Know Your Commands. \n\n< Powered By @ArrayCore >")

START_MSG = "**𝗛𝖾𝗅𝗅𝗈 [{}](tg://user?id={}) !** \n\n __ • 𝖨'𝗆 𝖠𝗇 𝖠𝖽𝗏𝖺𝗇𝖼𝖾 𝖡𝗈𝗍 𝖳𝗈 𝖥𝗎𝖼𝗄 𝖳𝗁𝖾 𝘃𝗰 𝗙𝗂𝗀𝗁𝗍𝖾𝗋𝗌\𝗇 𝗗𝖾𝗌𝗂𝗀𝗇𝖾𝖽 𝗕𝗒 𝐌𝐫. 𝗥𝗈𝗆𝖾𝗈 <\🇮🇳**",         
Hn = "/"
@vcbot.on_message(filters.private & filters.incoming & filters.command(['start'], prefixes=Hn))
async def _start(_, ok: Message):
        await vcbot.send_message(Message.chat.id,
        text=START_MSG.format(Message.from_user.first_name, Message.from_user.id),
            reply_markup=InlineKeyboardMarkup(
                [[
                    InlineKeyboardButton(
                        "𝗨𝗉𝖽𝖺𝗍𝖾𝗌", url="https://t.me/NFSxBOTZ"),
                    InlineKeyboardButton(
                        "𝗦𝗎𝗉𝗉𝗈𝗋𝗍", url="https://t.me/NFSxSUPPORT")
                ], [
                    InlineKeyboardButton(
                        "𝗥𝖾𝗉𝗈", url="https://t.me/Its_romeoo")
                ]]
            ))
