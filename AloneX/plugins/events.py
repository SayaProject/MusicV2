
# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AloneXMusic
# ALONE-CODER

from pyrogram import Client, filters
from pyrogram.types import ChatMemberUpdated
from pyrogram.enums import ChatMemberStatus

from AloneX import app, config, db, logger


@app.on_chat_member_updated()
async def handle_chat_member_update(_: Client, update: ChatMemberUpdated):
    chat = update.chat
    new_member = update.new_chat_member
    old_member = update.old_chat_member
    from_user = update.from_user

    # Check if the update is about the bot itself
    if new_member and new_member.user.id == app.id:
        # Case 1: Bot was added to chat
        if (old_member is None or 
            old_member.status in [
                ChatMemberStatus.KICKED, 
                ChatMemberStatus.LEFT, 
                ChatMemberStatus.RESTRICTED
            ]) and new_member.status not in [
                ChatMemberStatus.KICKED, 
                ChatMemberStatus.LEFT
            ]:
            # Get chat details
            chat_title = chat.title
            chat_id = chat.id
            try:
                chat_members_count = await app.get_chat_members_count(chat_id)
            except Exception as e:
                logger.error(f"Failed to get chat members count: {e}")
                chat_members_count = "Unknown"
            # Get who added
            adder_mention = from_user.mention if from_user else "Unknown"
            adder_id = from_user.id if from_user else "Unknown"
            
            log_message = (
                f"🎉 Bot Added To Chat:\n"
                f"Chat Name: {chat_title}\n"
                f"Chat ID: <code>{chat_id}</code>\n"
                f"Total Members: {chat_members_count}\n"
                f"Added By: {adder_mention} (ID: <code>{adder_id}</code>)"
            )
            
            try:
                await app.send_message(app.logger, log_message)
            except Exception as e:
                logger.error(f"Failed to send bot added log: {e}")

            # Add chat to database if not already present
            await db.add_chat(chat_id)

        # Case 2: Bot was removed/kicked
        elif (old_member and 
              old_member.status not in [
                  ChatMemberStatus.KICKED, 
                  ChatMemberStatus.LEFT
              ] and new_member.status in [
                  ChatMemberStatus.KICKED, 
                  ChatMemberStatus.LEFT
              ]):
            chat_title = chat.title
            chat_id = chat.id
            # Get who removed
            remover_mention = from_user.mention if from_user else "Unknown"
            remover_id = from_user.id if from_user else "Unknown"
            
            log_message = (
                f"⚠️ Bot Removed/Kicked From Chat:\n"
                f"Chat Name: {chat_title}\n"
                f"Chat ID: <code>{chat_id}</code>\n"
                f"Removed/Kicked By: {remover_mention} (ID: <code>{remover_id}</code>)"
            )
            
            try:
                await app.send_message(app.logger, log_message)
            except Exception as e:
                logger.error(f"Failed to send bot removed log: {e}")

            # Remove chat from database
            await db.rm_chat(chat_id)

