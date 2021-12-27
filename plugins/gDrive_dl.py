"""
G-Drive File Downloader Plugin For Userbot.
usage: {i}gdl File-Link
"""
# By: @Zero_cool7870


@Infinix(pattern=r"gdl", outgoing=True)
@Infinix(pattern=r"gdl", sudo=True)
async def _(event):
    await _gdl(event)
