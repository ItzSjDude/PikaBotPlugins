"""Use cmd `{i}lcry` to cry"""

from . import _cry


@Infinix(outgoing=True, pattern="lcry")
@Infinix(sudo=True, pattern="lcry")
async def _(event):
    await _cry(event)
