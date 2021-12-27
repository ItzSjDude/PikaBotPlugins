"""Beautifies nd convert python code into image
{i}ncode <reply to file for normal image>
{i}ncode doc <reply to file for document format>
"""
# created by @Buddhhu, Rebased by @Infinix. All Rights Reserved


from . import _ncode


@Infinix(pattern=r"ncode (.*)")
async def _(event):
    await _ncode(event)
