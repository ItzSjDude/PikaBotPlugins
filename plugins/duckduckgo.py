"""use command {i}ducduckgo"""


@Infinix(outgoing=True, pattern="ducduckgo (.*)")
@Infinix(sudo=True, pattern="ducduckgo (.*)")
async def _(event):
    await ducgo(event)
