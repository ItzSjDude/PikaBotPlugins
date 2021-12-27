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
from . import anpfp, atb, atnm, avpfp, gmpfp, pbio, pname


@Infinix(outgoing=True, pattern="pbio (.*)")
@Infinix(sudo=True, pattern="pbio (.*)")
async def _(event):
    await pbio(event)


@Infinix(outgoing=True, pattern="pname ((.|\n)*)")
@Infinix(sudo=True, pattern="pname ((.|\n)*)")
async def _(event):
    await pname(event)


@Infinix(outgoing=True, pattern="animepfp ?(.*)")
@Infinix(sudo=True, pattern="animepfp ?(.*)")
async def _(event):
    await anpfp(event)


@Infinix(outgoing=True, pattern="avengerspfp ?(.*)")
@Infinix(sudo=True, pattern="avengerspfp ?(.*)")
async def _(event):
    await avpfp(event)


@Infinix(outgoing=True, pattern="gamerpfp ?(.*)")
@Infinix(sudo=True, pattern="gamerpfp ?(.*)")
async def _(event):
    await gmpfp(event)


@Infinix(outgoing=True, pattern="autoname$")
@Infinix(sudo=True, pattern="autoname$")
async def _(event):
    await atnm(event)


@Infinix(outgoing=True, pattern="autobio$")
@Infinix(sudo=True, pattern="autobio$")
async def _(event):
    await atb(event)
