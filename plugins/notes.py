
from . import _allnotes, _remove_notes, _add_notes, note_incm, admin_cmd
from pikabot import bot, bot2, bot3, bot4

@ItzSjDude(outgoing=True, pattern="notes$")
async def _(event):
    await _allnotes(event)

@ItzSjDude(outgoing=True, pattern=r"save (\w*)")
async def _(event):
    await _add_notes(event)

@ItzSjDude(outgoing=True, pattern=r"clear (\w*)")
async def _(event):
    await _remove_notes(event)

@bot.on(admin_cmd(pattern=r"#\w*", incoming=True))
async def _(getnt):
    await note_incm(getnt)

if bot2:
    @bot2.on(admin_cmd(pattern=r"#\w*", incoming=True))
    async def _(getnt):
        await note_incm(getnt)

if bot3:
    @bot3.on(admin_cmd(pattern=r"#\w*", incoming=True))
    async def _(getnt):
        await note_incm(getnt)

if bot4:
    @bot4.on(admin_cmd(pattern=r"#\w*", incoming=True))
    async def _(getnt):
        await note_incm(getnt)
