"""Evaluate Python Code inside Telegram
{i}eval PythonCode"""

from . import _eval


@Infinix(outgoing=True, pattern="eval")
@Infinix(sudo=True, pattern="eval")
async def _(event):
    await _eval(event)
