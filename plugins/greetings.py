"""Greetings plugin
{i}gm
Usage: Good Morning art

{i}gn
Usage: Good Night art

{i}lul
Usage: Lol Art

{i}like
Usage: Like art
"""


@Infinix(pattern="gn$")
async def gn(event):
    await event.edit(GN)


@Infinix(pattern="gm$")
async def gm(event):
    await event.edit(GM)


@Infinix(pattern="lul$")
async def _(event):
    await event.edit(LOL)


@Infinix(pattern="like$")
async def _(event):
    await event.edit(LIKE)
