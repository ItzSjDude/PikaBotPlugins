"""Android Related Commands
{i}magisk
**Usage**:Get latest Magisk releases\n
{i}device <codename>
**Usage**: Get info about android device codename or model.\n
{i}codename <brand> <device>
**Usage**: Search for android device codename.\n
{i}specs <brand> <device>
**Usage**: Get device specifications info.\n
{i}twrp <codename>
**Usage**: Get latest twrp download for android device.\n
"""
from . import codename_info, device_info, dspecs, magisk, twrp


@Infinix(outgoing=True, pattern="magisk$")
@Infinix(sudo=True, pattern="magisk$")
async def _(request):
    await magisk(request)


@Infinix(outgoing=True, pattern=r"device(?: |$)(\S*)")
@Infinix(sudo=True, pattern=r"device(?: |$)(\S*)")
async def _(request):
    await device_info(request)


@Infinix(outgoing=True, pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)")
@Infinix(sudo=True, pattern=r"codename(?: |)([\S]*)(?: |)([\s\S]*)")
async def _(request):
    await codename_info(request)


@Infinix(outgoing=True, pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)")
@Infinix(sudo=True, pattern=r"specs(?: |)([\S]*)(?: |)([\s\S]*)")
async def _(request):
    await dspecs(request)


@Infinix(outgoing=True, pattern=r"twrp(?: |$)(\S*)")
@Infinix(sudo=True, pattern=r"twrp(?: |$)(\S*)")
async def _(request):
    await twrp(request)
