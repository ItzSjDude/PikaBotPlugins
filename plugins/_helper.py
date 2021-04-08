from . import bot, bot2, bot3, bot4, helper
# ____Main/Multiclients____
@ItzSjDude(outgoing=True, pattern=r"help ?(.*)")
async def _(event):
    await helper(event)
