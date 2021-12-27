"""18+ friendly animations
{i}fuck
{i}kess
{i}sux
"""
from . import _fuck


@Infinix(outgoing=True, pattern=r"(.*)")
@Infinix(sudo=True, pattern=r"(.*)")
async def _(event):
    await _fuck(event)
