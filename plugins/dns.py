"""DA.GD helpers
Available Commands:
{i}isup URL
{i}dns google.com
{i}url <long url>
{i}unshort <short url>"""
# Credits @UniBorg


@Infinix(outgoing=True, pattern="dns (.*)")
@Infinix(sudo=True, pattern="dns (.*)")
async def _(event):
    await dns(event)


@Infinix(outgoing=True, pattern="url (.*)")
@Infinix(sudo=True, pattern="url (.*)")
async def _(event):
    await urlx(event)


@Infinix(outgoing=True, pattern="unsort (.*)")
@Infinix(sudo=True, pattern="unsort (.*)")
async def _(event):
    await unshort(event)
