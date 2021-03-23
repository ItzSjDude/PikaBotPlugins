import heroku3
from var import Var
Heroku = heroku3.from_key(Var.HEROKU_API_KEY)
pika = Heroku.app(Var.HEROKU_APP_NAME)
try:
    from pikabot import bot, bot2, bot3, bot4
    i1 = bot.uid
    i2 = bot2.uid
    i3 = bot3.uid
    i4 = bot4.uid

except BaseException:
    pass

if bot is not None:
    pika_id1 = i1
else:
    pika_id1 = 1111
if bot2 is not None:
    pika_id2 = i2
else:
    pika_id2 = 1011
if bot3 is not None:
    pika_id3 = i3
else:
    pika_id3 = 1010
if bot4 is not None:
    pika_id4 = i4
else:
    pika_id4 = 1001


async def pikaa(event, shortname):
    pika_pi = await event.client.get_me()
    AS = get(f"{shortname}", None).split('|')
    er = "[Error?](https://t.me/PikaBotErrors/2)"
    try:
        c1d = AS[0]
    except BaseException:
        if shortname.startswith("ALIVE"):
            c1d = er
        else:
            c1d = 'Not Found'

    try:
        c2d = AS[1]
    except BaseException:
        if shortname.startswith("ALIVE"):
            c2d = er
        else:
            c2d = 'Not Found'
    try:
        c3d = AS[2]
    except BaseException:
        if shortname.startswith("ALIVE"):
            c3d = er
        else:
            c3d = 'Not Found'
    try:
        c4d = AS[3]
    except BaseException:
        if shortname.startswith("ALIVE"):
            c4d = er
        else:
            c4d = 'Not Found'

    if pika_id1 == pika_pi.id:
        return c1d
    if pika_id2 == pika_pi.id:
        return c2d
    if pika_id3 == pika_pi.id:
        return c3d
    if pika_id4 == pika_pi.id:
        return c4d


async def _pika(text, _sudo):
    pika = await _sudo.client.get_me()
    if _sudo.sender_id in Var.SUDO_USERS and pika_id1 == pika.id:
        reply_to = await _sudo.get_reply_message()
        if reply_to:
            return await reply_to.reply(text)
        return await _sudo.reply(text)
    return await _sudo.edit(text)


def pikarestart():
    pika.restart()
