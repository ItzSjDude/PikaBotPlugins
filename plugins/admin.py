# Officially made for Pikabot by ItzSjDude from Paperplane extended snippets
"""**Administration Commands**\n\n
{i}setgpic <reply to image>
**Usage**: Set replied Image as Group Profile pic\n
{i}promote reply to UserMsg or @username <CustomAdmintag>
**Usage**: Promote user with custom admin tag if given\n
{i}demote <reply to UserMsg> or @username
**Usage**: Demotes user from admin\n
{i}ban <reply to UserMsg> or @username
**Usage**: Ban user\n
{i}unban <reply to UserMsg> or @username
**Usage**: Unban user\n
{i}mute <reply to UserMsg> or @username
**Usage**: Mutes user from chat\n
{i}mute <reply to UserMsg> or @username
**Usage**: Unmutes User from Chat\n
{i}gmute <reply to UserMsg> <reason> or @username <reason>
**Usage**: Globally Mutes user nd Add to gban watcher\n
{i}ungmute <reply to UserMsg> or @username
**Usage**: Globally Unmutes Mutes user nd Remove from gmute watcher\n
{i}delusers
**Usage**: Removes Deleted/inactive Users from groups/channels\n
{i}adminlist
**Usage**: get admins in group\n
{i}users
**Usage**: Get all users From group\n
{i}kick reply to UserMsg or @username
**Usage**: kick User from group\n
{i}pin <reply to msg>
**Usage**: Pins replied msg\n
{i}invite <Username>
**Usage**: Invites User to Current Chat
"""

from . import (
    _ban,
    _demote,
    _gadmin,
    _gmte,
    _gusers,
    _invite,
    _kick,
    _mute,
    _muter,
    _pin,
    _promote,
    _rmdacc,
    _setgpic,
    _unban,
    _ungmute,
    _unmute,
    admin_cmd,
)


# @bot.on(pika_sudo(from_client=1, pattern=r"setgpic$"))
@ItzSjDude(groups_only=True, pattern=r"setgpic$")
async def _(gpic):
    await _setgpic(gpic)


# @bot.on(pika_sudo(from_client=1, pattern=r"promote(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"promote(?: |$)(.*)")
async def _(promt):
    await _promote(promt)


# @bot.on(pika_sudo(from_client=1, pattern=r"demote(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"demote(?: |$)(.*)")
async def _(dmod):
    await _demote(dmod)


# @bot.on(pika_sudo(from_client=1, pattern=r"ban(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"ban(?: |$)(.*)")
async def _(bon):
    await _ban(bon)


# @bot.on(pika_sudo(from_client=1, pattern=r"unban(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"unban(?: |$)(.*)")
async def _(unbon):
    await _unban(unbon)


# @bot.on(pika_sudo(from_client=1, pattern=r"mute(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"mute(?: |$)(.*)")
async def _(spdr):
    await _mute(spdr)


# @bot.on(pika_sudo(from_client=1, pattern=r"unmute(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"unmute(?: |$)(.*)")
async def _(unmot):
    await _unmute(unmot)


# @bot.on(pika_sudo(from_client=1, pattern=r"ungmute(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"ungmute(?: |$)(.*)")
async def _(un_gmute):
    await _ungmute(un_gmute)


# @bot.on(pika_sudo(from_client=1, pattern=r"gmute(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"gmute(?: |$)(.*)")
async def _(gspdr):
    await _gmte(gspdr)


# @bot.on(pika_sudo(from_client=1, pattern=r"delusers(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"delusers(?: |$)(.*)")
async def _(show):
    await _rmdacc(show)


# @bot.on(pika_sudo(from_client=1, pattern=r"listadmins$"))
@ItzSjDude(groups_only=True, pattern=r"listadmins$")
async def _(show):
    await _gadmin(show)


# @bot.on(pika_sudo(from_client=1, pattern=r"pin(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"pin(?: |$)(.*)")
async def _(msg):
    await _pin(msg)


# @bot.on(pika_sudo(from_client=1, pattern=r"kick(?: |$)(.*)"))
@ItzSjDude(groups_only=True, pattern=r"kick(?: |$)(.*)")
async def _(usr):
    await _kick(usr)


# @bot.on(pika_sudo(from_client=1, pattern="invite ?(.*)"))
@ItzSjDude(groups_only=True, pattern="invite ?(.*)")
async def _(event):
    await _invite(event)


# @bot.on(pika_sudo(from_client=1, pattern=r"users ?(.*)"))
@ItzSjDude(groups_only=True, pattern=r"users ?(.*)")
async def _(show):
    await _gusers(show)


@bot.on(admin_cmd(incoming=True))
async def _(moot):
    await _muter(moot)
