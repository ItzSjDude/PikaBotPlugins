""" Powered by @Google
Available Commands:
.go <query> credits to owner of bot
"""

from . import _gsearch


@Infinix(outgoing=True, pattern="go (.*)")
@Infinix(sudo=True, pattern="go (.*)")
async def _(event):
    await _gsearch(event)
