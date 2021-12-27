"""
{i}setwelcome <welcome message> or reply to msg
**Usage**: Sets the message as a welcome note in the chat
{i}getwelcome
**Usage**: Shows current welcome note in the chat\n
{i}delwelcome
**Usage**: Deletes the welcome note from current chat\n\n
**Available formats for formatting welcome Note**:
`{mention}, {title}, {count}, {first}, {last}, {fullname}, {userid}, {username}, {my_first}, {my_fullname}, {my_last}, {my_mention}, {my_username}`
"""

from . import ChatAction, _welcome, del_welcm, get_welcm, set_wlcm


@bot.on(ChatAction)
async def _(_infx):
    await _welcome(_infx)


@Infinix(outgoing=True, pattern=r"setwelcome(?: |$)(.*)")
async def _(_infx):
    await set_wlcm(_infx)


@Infinix(outgoing=True, pattern="getwelcome$")
async def _(_infx):
    await get_welcm(_infx)


@Infinix(outgoing=True, pattern="delwelcome$")
async def _(_infx):
    await del_welcm(_infx)
