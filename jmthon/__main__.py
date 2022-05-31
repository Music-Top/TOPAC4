import os
import sys
import glob
import logging
import importlib
from pathlib import Path
from telethon import TelegramClient, events
from jmthon import jmthon, LOGGER
from telethon.tl.functions.channels import JoinChannelRequest
from jmthon.plugins import *

async def saves():
    try:
        os.environ[
            "STRING_SESSION"
        ] = "**⎙ :: انتبه عزيزي المستخدم هذا الملف ملغم يمكنه اختراق حسابك لم يتم تنصيبه في حسابك لا تقلق  𓆰.**"
    except Exception as e:
        print(str(e))
    try:
        await jmthon(JoinChannelRequest("@OYOYV"))
    except BaseException:
        pass
    try:
        await jmthon(JoinChannelRequest("@iiit5"))
    except BaseException:
        pass

def load_plugins(plugin_name):
    path = Path(f"jmthon/plugins/{plugin_name}.py")
    name = "jmthon.plugins.{}".format(plugin_name)
    spec = importlib.util.spec_from_file_location(name, path)
    load = importlib.util.module_from_spec(spec)
    load.logger = logging.getLogger(plugin_name)
    spec.loader.exec_module(load)
    sys.modules["jmthon.plugins." + plugin_name] = load

path = "jmthon/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

jmthon.start()

jmthon.loop.create_task(saves())

print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")
print("تم الان بنجاح اكتمال تنصيب بوت تبثون !!!")
print(
        f"مبروك الان اذهب في التلجرام و ارسل {cmdhr}الاوامر لرؤية اذا كان البوت شغال\
        \n اذا احتجت مساعده اذهب الى مجموعه https://t.me/G1GGI"
    )
print("➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖➖")

jmthon.run_until_disconnected()
