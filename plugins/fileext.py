"""Get info about a File Extension
{i}filext <extension>"""

from . import _getfilext


@Infinix(outgoing=True, pattern="filext (.*)")
@Infinix(sudo=True, pattern="filext (.*)")
async def _(event):
    await _getfilext(event)
