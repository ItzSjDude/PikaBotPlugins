# Copyright (C) 2019 The Raphielscape Company LLC.
#
# Licensed under the Raphielscape Public License, Version 1.c (the "License");
# you may not use this file except in compliance with the License.
#
""" Userbot module for purging unneeded messages(usually spam or ot). """

from asyncio import sleep
from telethon.errors import rpcbaseerrors

@Infinix(outgoing=True, pattern=r"purge")
async def fastpurger(purg):
    """ For .purge command, purge all messages starting from the reply. """
    chat = await purg.get_input_chat()
    msgs = []
    count = 0

    async for msg in purg.client.iter_messages(chat, min_id=purg.reply_to_msg_id):
        msgs.append(msg)
        count = count + 1
        msgs.append(purg.reply_to_msg_id)
        if len(msgs) == 100:
            await purg.client.delete_messages(chat, msgs)
            msgs = []

    if msgs:
        await purg.client.delete_messages(chat, msgs)
    done = await purg.client.send_message(
        purg.chat_id,
        "`Fast purge complete!\n`Purged " + str(count) + " messages.",
    )

    if pdb.Botlog_chat:
        await purg.client.send_message(
            pdb.Botlog_chat, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    await done.delete()


@Infinix(outgoing=True, pattern=r"purgeme")
async def purgeme(delme):
    """ For .purgeme, delete x count of your latest message."""
    message = delme.text
    count = int(message[9:])
    i = 1

    async for message in delme.client.iter_messages(delme.chat_id, from_user="me"):
        if i > count + 1:
            break
        i = i + 1
        await message.delete()

    smsg = await delme.client.send_message(
        delme.chat_id,
        "`Purge complete!` Purged " + str(count) + " messages.",
    )
    if pdb.Botlog_chat:
        await delme.client.send_message(
            pdb.Botlog_chat, "Purge of " + str(count) + " messages done successfully."
        )
    await sleep(2)
    i = 1
    await smsg.delete()


@Infinix(outgoing=True, pattern=r"del")
async def delete_it(delme):
    """ For .del command, delete the replied message. """
    msg_src = await delme.get_reply_message()
    if delme.reply_to_msg_id:
        try:
            await msg_src.delete()
            await delme.delete()
            if pdb.Botlog_chat:
                await delme.client.send_message(
                    pdb.Botlog_chat, "Deletion of message was successful"
                )
        except rpcbaseerrors.BadRequestError:
            if pdb.Botlog_chat:
                await delme.client.send_message(
                    pdb.Botlog_chat, "Well, I can't delete a message"
                )


@Infinix(outgoing=True, pattern=r"edit")
async def editer(edit):
    """ For .editme command, edit your last message. """
    message = edit.text
    chat = await edit.get_input_chat()
    self_id = await edit.client.get_peer_id("me")
    string = str(message[6:])
    i = 1
    async for message in edit.client.iter_messages(chat, self_id):
        if i == 2:
            await message.edit(string)
            await edit.delete()
            break
        i = i + 1
    if pdb.Botlog_chat:
        await edit.client.send_message(
            pdb.Botlog_chat, "Edit query was executed successfully"
        )


@Infinix(outgoing=True, pattern=r"sd")
async def selfdestruct(destroy):
    """ For .sd command, make seflf-destructable messages. """
    message = destroy.text
    counter = int(message[4:6])
    text = str(destroy.text[6:])
    await destroy.delete()
    smsg = await destroy.client.send_message(destroy.chat_id, text)
    await sleep(counter)
    await smsg.delete()
    if pdb.Botlog_chat:
        await destroy.client.send_message(pdb.Botlog_chat, "sd query done successfully")


