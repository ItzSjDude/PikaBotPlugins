"""conversation starter questions...
{i}convoqt
"""

# inspired by @Deonnn's being_logical.py, edited by : @mahshook_bot
from . import _convoqt


@Infinix(outgoing=True, pattern=r"convoqt$")
@Infinix(sudo=True, pattern=r"convoqt$")
async def _(event):
    await _convoqt(event)
