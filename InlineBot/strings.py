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

HELP_MESSAGE = f"""<b><u>Hauptbefehle</u></b>

○ <b>/{FILTER_COMMAND.lower()}</b> <i>[Schlüsselwort] [Nachricht oder reply]</i>
    <i>Erstellt einen Filter. Du kannst Markdown nutzen.</i>
    
○ <b>/{DELETE_COMMAND.lower()}</b> <i>[Schlüsselwort]</i>
    <i>Löscht einen Filter</i>
    
○ <b>/filters</b>
    <i>Zeigt alle Filter</i>
    
○ <b>/export</b>
    <i>Exportiert alle Daten, um sie woanders nutzen zu können.</i>
    
○ <b>/stats</b>
    <i>Zeigt Bot-Statistiken</i>
    
○ <b>/broadcast</b> <i>[Nachricht oder reply]</i>
    <i>Broadcast-Nachricht an alle Nutzer</i>
    
<b><u>Inhaber-Befehle</u></b>

○ <b>/delall</b>
    <i>Löscht alle Filter</i>
    
○ <b>/import</b> <i>[Antowort auf Backup-Datei]</i>
    <i>Importiert Filter von einer Datei</i>
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
