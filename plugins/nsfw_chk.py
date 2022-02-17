"""To check nudity of a pic
{i}boobs <reply to image>
{i}butts <reply to image>"""


import asyncio
import os
import urllib

import requests


@Infinix(pattern=r"boobs")
async def boobs(event):
    if not os.path.isdir(Var.pdb.Dldir):
        os.makedirs(Var.pdb.Dldir)
    pic_loc = os.path.join(Var.pdb.Dldir, "bobs.jpg")
    a = await event.reply("`Finding some big bobs 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some big bobs 🌚...`")
    nsfw = requests.get("http://api.oboobs.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.oboobs.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()


@Infinix(pattern=r"butts")
async def butts(event):
    if not os.path.isdir(Var.pdb.Dldir):
        os.makedirs(Var.pdb.Dldir)
    pic_loc = os.path.join(Var.pdb.Dldir, "butts.jpg")
    a = await event.reply("`Finding some beautiful butts 🧐...`")
    await asyncio.sleep(0.5)
    await a.edit("`Sending some beautiful butts 🌚...`")
    nsfw = requests.get("http://api.obutts.ru/noise/1").json()[0]["preview"]
    urllib.request.urlretrieve("http://media.obutts.ru/{}".format(nsfw), pic_loc)
    await event.client.send_file(event.chat_id, pic_loc, force_document=False)
    os.remove(pic_loc)
    await event.delete()
    await a.delete()
