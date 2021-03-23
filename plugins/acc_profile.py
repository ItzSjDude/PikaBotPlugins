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
@ItzSjDude(outgoing=True, pattern="pbio (.*)")
async def pbio(event):
    if event.fwd_from:
        return
    bio = event.pattern_match.group(1)
    try:
        await event.client(functions.account.UpdateProfileRequest(about=bio))
        await event.edit("Succesfully changed my profile bio")
    except Exception as e:
        await event.edit(str(e))

@ItzSjDude(outgoing=True, pattern="pname ((.|\n)*)")
async def pname(event):
    if event.fwd_from:
        return
    names = event.pattern_match.group(1)
    first_name = names
    last_name = ""
    if "\\n" in names:
        first_name, last_name = names.split("\\n", 1)
    try:
        await event.client(
            functions.account.UpdateProfileRequest(
                first_name=first_name, last_name=last_name
            )
        )
        await event.edit("My name was changed successfully")
    except Exception as e:
        await event.edit(str(e))

@ItzSjDude(outgoing=True, pattern="animepfp ?(.*)")
async def anpfp(event):
    await event.edit(f"{r}")
    while True:
        await animepp()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(60)

@ItzSjDude(outgoing=True, pattern="avengerspfp ?(.*)")
async def avpfp(event):
    await event.edit(f"{s}")
    while True:
        await avengerspic()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(600)

@ItzSjDude(outgoing=True, pattern="gamerpfp ?(.*)")
async def gmpfp(event):
    await event.edit(f"{t}")
    while True:
        await gamerpic()
        file = await event.client.upload_file("donottouch.jpg")
        await event.client(functions.photos.UploadProfilePhotoRequest(file))
        os.system("rm -rf donottouch.jpg")
        await asyncio.sleep(60)

@ItzSjDude(outgoing=True, pattern="autoname$")
async def atnm(event):
    if event.fwd_from:
        return
    while True:
        dname = await pikaa(event, "ALIVE_NAME")
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%H:%M")
        name = f"🕒{HM} ⚡{dname}⚡ 📅{DM}"
        pikalog.info(name)
        try:
            await event.client(functions.account.UpdateProfileRequest(first_name=name))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
    await event.edit(f"Auto Name has been started Master")

@ItzSjDude(outgoing=True, pattern="autobio$")
async def atb(event):
    if event.fwd_from:
        return
    while True:
        DMY = time.strftime("%d.%m.%Y")
        HM = time.strftime("%H:%M:%S")
        bio = f"📅 {DMY} | {DBIO} | ⌚️ {HM}"
        pikalog.info(bio)
        try:
            await event.client(functions.account.UpdateProfileRequest(about=bio))
        except FloodWaitError as ex:
            logger.warning(str(e))
            await asyncio.sleep(ex.seconds)
        await asyncio.sleep(DEL_TIME_OUT)
