"""Check your internet speed powered by speedtest.net
{i}speedtest <image/file/text>
"""

from . import _speedtest


@Infinix(outgoing=True, pattern="speedtest ?(.*)")
async def _(event):
    await _speedtest(event)
