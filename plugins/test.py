
@Infinix(outgoing=True, pattern=r"test")
async def test(event):
    if event.fwd_from:
        return
    await event.edit("Test Successfull. Boss !")
