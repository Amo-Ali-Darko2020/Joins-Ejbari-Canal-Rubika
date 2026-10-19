
import os
import io
import json
import contextlib
import asyncio
import time

os.system("clear")

GREEN = "\033[38;5;46m"
RED = "\033[91m"
RESET = "\033[0m"

with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
    from maxrubika import Bot

print(GREEN + r"""
              /\
             /**\
            /****\
           /******\
          /********\
         /**********\
        /************\
       /**************\
             ||||
             ||||
""" + RESET)

print(GREEN + "           Bot Rubika" + RESET)
print()

GROUP_ID = input(RED + "[ Lotfan GUID goruh ra vared konid 🌟 ]: " + RESET).strip()
TOKEN = input(RED + "[ Lotfan token bot khod ra vared konid 🌟 ]: " + RESET).strip()
CHANNEL = input(RED + "[ Lotfan ID channel khod ra vared konid 🌟 ]: " + RESET).strip()

SLEEP = 100
warned_users = {}

print()
print(RED + "Dar hale amade sazi ..." + RESET)

bot = Bot(token=TOKEN)

@bot.on_new_message()
async def check_message(bot, event):
    if not getattr(event, "is_group", False):
        return

    if event.chat_id != GROUP_ID:
        return

    try:
        joined = await bot.member_is_joined(CHANNEL, event.author_id)

        if joined:
            return

        await event.delete()

        now = time.time()
        key = (event.chat_id, event.author_id)

        if now - warned_users.get(key, 0) < SLEEP:
            return

        warned_users[key] = now

        warning = (
            "درود !\n"
            f"< [ کاربر ]({event.author_id}) > برای ارسال پیامک\n"
            "در کانال زیر جوین شوید 🌟\n"
            f"««««««« < {CHANNEL} > »»»»»»»"
        )

        warn = await bot.send_message(event.chat_id, warning)

        asyncio.create_task(
            bot.auto_delete_message(
                event.chat_id,
                warn.message_id,
                60
            )
        )

    except Exception as e:
        print(RED + "Khata: " + repr(e) + RESET)

print(RED + "< Bot Join Ejbari Roshan Shod ☘️ >" + RESET)

bot.run()

