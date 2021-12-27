"""Dictionary Plugin
{i}mean <word>"""

# Credits @UniBorg


@Infinix(outgoing=True, pattern="mean (.*)")
@Infinix(sudo=True, pattern="mean (.*)")
async def _(event):
    await dict(event)
