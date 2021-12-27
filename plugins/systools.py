"""**HEROKU MANAGER**\n\n
{i}set|get|del var <VarName>
**Usage**: set|get|del Heroku Vars\n
{i}usage
**Usage**: Shows Dynos usage\n
{i}logs
**Usage**: Sends your botlogs in current chat\n
{i}restart
**Usage**: Restarts Pikabot"""

from . import _dyno, _logs, _restart, _vars


@Infinix(outgoing=True, pattern=r"(set|get|del) var(?: |$)(.*)(?: |$)([\s\S]*)")
async def _(var):
    await _vars(var)


@Infinix(outgoing=True, pattern=r"usage(?: |$)")
async def _(dyno):
    await _dyno(dyno)


@Infinix(outgoing=True, pattern="restart")
async def _(rstrt):
    await _restart(rstrt)


@Infinix(outgoing=True, pattern=r"logs")
async def _(dyno):
    await _logs(dyno)
