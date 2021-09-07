# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

from pyrogram import __version__
from InlineBot import (
    OWNER_ID,
    FILTER_COMMAND,
    DELETE_COMMAND,
    CUSTOM_START_MESSAGE
)

if CUSTOM_START_MESSAGE:
    START_MESSAGE = CUSTOM_START_MESSAGE
else:
    START_MESSAGE = """<b>Hi {mention},

Ich bin ein Inline Saver Bot, Du kannst Inline-Filter speichern und es kann leicht in jedem Deiner Chats verwendet werden. Klicke auf /help für weitere Details</b> 
"""

HELP_MESSAGE = f"""<b><u>Main Available Commands</u></b>

○ <b>/{FILTER_COMMAND.lower()}</b> <i>[keyword] [message or reply to message]</i>
    <i>Add an Inline filter, you can use MarkDown for formatting</i>
    
○ <b>/{DELETE_COMMAND.lower()}</b> <i>[keyword]</i>
    <i>Delete existing Filter</i>
    
○ <b>/filters</b>
    <i>To see the filters</i>
    
○ <b>/export</b>
    <i>Export a Backup file of filters, this can be import by others</i>
    
○ <b>/stats</b>
    <i>See the Bot's Statistics</i>
    
○ <b>/broadcast</b> <i>[reply to any message]</i>
    <i>Broadcast any Messages to Bot users</i>
    
<b><u>Owner only Commands</u></b>

○ <b>/delall</b>
    <i>Delete all of the filters</i>
    
○ <b>/import</b> <i>[reply to an exported file]</i>
    <i>Import filters from Backup file</i>
"""

ABOUT_MESSAGE = f"""<b><u>ÜBER MICH</u></b>

<b>○ Verwaltet von : @TLGRM_Support
○ Support : <a href='https://t.me/iSupportiBot'>iSupportiBot</a>
○ Source Code: <a href='https://github.com/CodeXBotz/Inline-Filter-Bot'>Hier</a>
○ Sprache: <a href='https://www.python.org/'>Python 3</a>
○ Bibiliothek: <a href='https://github.com/pyrogram/pyrogram'>Pyrogram Asyncio {__version__}</a></b>
"""

MARKDOWN_HELP = """<b><u>Markdown Formatierung</u></b>

○ <b>Fett</b> :
    Format: <code>*Fetter Text*</code>
    Aussehen: <b>Fetter Text</b>
    
○ <b>Kursiv</b>
    Format: <code>_Kursiver Text_</code>
    Aussehen: <i>Kursiver Text</i>
    
○ <b>Mono</b>
    Format: <code>`Code Text`</code>
    Aussehen: <code>Code Text</code>
    
○ <b>Unterstrichen</b>
    Format: <code>__Unterstrichener Text__</code>
    Aussehen: <u>__Unterstrichener Text</u>
    
○ <b>Durchgestrichen</b>
    Format: <code>~Duchgestrichener Text~</code>
    Aussehen: <s>Duchgestrichener Text</s>
    
○ <b>Link</b>
    Format: <code>[Text](https://t.me/iSupFilterBot)</code>
    Aussehen: <a href='https://t.me/iSupFilterBot'>Text</a>
    
○ <b>Buttons</b>
    <u>URL Button</u>:
    <code>[Button Text](buttonurl:https://t.me/iSupFilterBot)</code>
    
    <u>Popup</u>:
    <code>[Button Text](buttonalert:Popup Text)</code>
    
    <u>Gleiche Zeile</u>:
    <code>[Button Text](buttonurl:https://t.me/iSupFilterBot:same)</code></i>

○ <b>Merke:</b>
    <i>Behalte alle Schaltflächen bei der Formatierung in einer separaten Zeile.</i>
    <i>Dein Text muss weniger als 200 Zeichen lang sein, sonst ignoriert der Bot diese Schaltfläche</i>"""
