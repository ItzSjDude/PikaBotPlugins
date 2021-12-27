"""Design plugin
{i}join
{i}pay"""
from . import jon, pay


@Infinix(outgoing=True, pattern="join$")
@Infinix(sudo=True, pattern="join$")
async def _(event):
    await jon(event)


@Infinix(outgoing=True, pattern="pay$")
@Infinix(sudo=True, pattern="pay$")
async def _(event):
    await pay(event)
