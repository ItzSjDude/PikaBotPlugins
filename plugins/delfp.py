"""Plugin For Removing  n no. Of profile pics
{i}delpfp <no. of pics> """

from . import remppic


@Infinix(outgoing=True, pattern="delpfp ?(.*)")
@Infinix(sudo=True, pattern="delpfp ?(.*)")
async def _(delpfp):
    await remppic(delpfp)
