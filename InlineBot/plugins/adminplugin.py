# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

import asyncio
from InlineBot import (
    CodeXBotz,
    filters,
    Message,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from InlineBot.database import (
    get_status,
    get_users,
    del_from_userbase
)
from pyrogram.errors import (
    FloodWait,
    PeerIdInvalid,
    UserIsBlocked,
    InputUserDeactivated
)

@CodeXBotz.on_message(filters.private & filters.command('stats') & filters.admins)
async def getstatus(client: CodeXBotz, message: Message):
    sts_msg = await message.reply('<code>Suche Infos..</code>')
    stats = await get_status()
    await sts_msg.edit(stats)
    
@CodeXBotz.on_message(filters.private & filters.command('broadcast') & filters.admins & filters.reply)
async def broadcast(client: CodeXBotz, message: Message):
    broadcast_msg = message.reply_to_message
    broadcast_msg = await broadcast_msg.copy(
        chat_id = message.chat.id,
        reply_to_message_id = broadcast_msg.message_id
    )
    await broadcast_msg.reply(
        text = 'Möchtest du das wirklich Broadcasten?',
        quote = True,
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text = 'Ja', callback_data = 'bdcast_cnfrm'),
                    InlineKeyboardButton(text = 'Nein', callback_data = 'close')
                ]
            ]
        )
    )
    return

@CodeXBotz.on_callback_query(filters.admins & filters.regex('^bdcast_cnfrm$'))
async def broadcast_confrm(client: CodeXBotz, query):
    if not query.message.reply_to_message:
        await query.answer(
            text = 'Nachricht nicht gefunden',
            show_alert = True
        )
        await query.message.delete()
        return

    message = query.message.reply_to_message
    user_ids = await get_users()
    
    success = 0
    deleted = 0
    blocked = 0
    peerid = 0
    
    await query.message.edit(text = 'Broadcaste.. Bitte warten!', reply_markup = None)
    
    for user_id in user_ids:
        try:
            await message.copy(user_id)
            success += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            await message.copy(user_id)
            success += 1
        except UserIsBlocked:
            blocked += 1
        except PeerIdInvalid:
            peerid += 1
        except InputUserDeactivated:
            deleted += 1
            await del_from_userbase(user_id)
            
    text = f"""<b>Broadcast gesendet</b>
    
Nutzer gesamt: {str(len(user_ids))}
Nutzer blockiert: {str(blocked)}
Gelöschte Accounts: {str(deleted)} (<i>Aus der Datenbank gelöscht</i>)
Fehlgeschlagen: {str(peerid)}"""

    await query.message.reply(text)
    await query.message.delete()
    await message.delete()
