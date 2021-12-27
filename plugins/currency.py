"""Currency Converter Plugin
{i}currency <from to>"""
# Credits @UniBorg
from . import _currency


@Infinix(outgoing=True, pattern="currency (.*)")
@Infinix(sudo=True, pattern="currency (.*)")
async def _(event):
    await _currency(event)
