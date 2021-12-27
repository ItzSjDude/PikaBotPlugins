from . import helper

# ____Main/Multiclients____


@Infinix(outgoing=True, pattern=r"help ?(.*)")
@Infinix(sudo=True, pattern=r"help ?(.*)")
async def _(event):
    await helper(event)
