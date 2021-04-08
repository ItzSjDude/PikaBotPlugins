"""Profile Related Commands
{i}autobio
**Usage**: Activates Autobio\n
{i}autoname
**Usage**: Activates Autoname\n
{i}autopfp
**Usage**: Activates Autopic\n
{i}avengerspfp
**Usage**: Activates auto Avengers pics\n
{i}animepfp
**Usage**: Activates Anime pics\n
{i}gamerpfp
**Usage**: Activates Gamer pics\n
{i}pbio <Bio>
**Usage**: sets Bio\n
{i}pname <Name>
**Usage**: sets Name\n
{i}ppic <Reply to pic>
**Usage**: sets Profile pic\n
"""
from . import (
    anpfp,
    atb,
    atnm,
    avpfp,
    bot,
    bot2,
    bot3,
    bot4,
    gmpfp,
    pbio,
    pname,
)


@ItzSjDude(outgoing=True, pattern="pbio (.*)")
async def _(event):
    await pbio(event)

@ItzSjDude(outgoing=True, pattern="pname ((.|\n)*)")
async def _(event):
    await pname(event)


@ItzSjDude(outgoing=True, pattern="animepfp ?(.*)")
async def _(event):
    await anpfp(event)


@ItzSjDude(outgoing=True, pattern="avengerspfp ?(.*)")
async def _(event):
    await avpfp(event)


@ItzSjDude(outgoing=True, pattern="gamerpfp ?(.*)")
async def _(event):
    await gmpfp(event)

@ItzSjDude(outgoing=True, pattern="autoname$")
async def _(event):
    await atnm(event)

@ItzSjDude(outgoing=True, pattern="autobio$")
async def _(event):
    await atb(event)
