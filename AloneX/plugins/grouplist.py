
# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AloneXMusic
# ALONE-CODER

from pyrogram import Client, filters
from datetime import datetime

from AloneX import app, db


@app.on_message(filters.command("grouplist") & filters.user(app.owner))
async def send_group_list(client: Client, message):
    # Get all chats from database
    chat_ids = await db.get_chats()
    if not chat_ids:
        return await message.reply_text("No groups found!")

    # Prepare group list
    group_info_list = []
    for chat_id in chat_ids:
        try:
            chat = await client.get_chat(chat_id)
            chat_name = chat.title
            # Get last played time from database
            chat_doc = await db.chatsdb.find_one({"_id": chat_id})
            last_played_ts = chat_doc.get("last_played") if chat_doc else None
            if last_played_ts:
                last_played = datetime.fromtimestamp(last_played_ts).strftime("%Y-%m-%d %H:%M:%S")
            else:
                last_played = "Never"
            group_info_list.append(f"{chat_name} (<code>{chat_id}</code>)\nLast Played: {last_played}")
        except Exception as e:
            # Chat not found or error
            group_info_list.append(f"[Chat ID: <code>{chat_id}</code>] - Could not retrieve info")

    # Split into chunks (Telegram message limit is 4096 chars)
    chunk_size = 30
    for i in range(0, len(group_info_list), chunk_size):
        chunk = group_info_list[i:i + chunk_size]
        text = f"📋 Group List ({len(chat_ids)} total):\n\n" + "\n\n".join(chunk)
        await message.reply_text(text)

