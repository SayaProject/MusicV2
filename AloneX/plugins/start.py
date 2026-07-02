# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AloneXMusic
#ALONE-CODER

import asyncio
import random
from pyrogram import enums, filters, types

from AloneX import app, config, db, lang
from AloneX.helpers import buttons, utils, extra_inline


@app.on_message(filters.command(["help"]) & filters.private & ~app.bl_users)
@lang.language()
async def _help(_, m: types.Message):
    await m.reply_text(
        text=m.lang["help_menu"],
        reply_markup=buttons.help_markup(m.lang),
        quote=True,
    )


@app.on_message(filters.command(["start"]))
@lang.language()
async def start(_, message: types.Message):
    if message.from_user.id in app.bl_users and message.from_user.id not in db.notified:
        return await message.reply_text(message.lang["bl_user_notify"])

    if len(message.command) > 1 and message.command[1] == "help":
        return await _help(_, message)

    private = message.chat.type == enums.ChatType.PRIVATE

    # Start animation
    msg = await message.reply_text(
        "⚡  <b>𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</b>\n▰▱▱▱▱  20%",
        disable_web_page_preview=True,
    )
    await asyncio.sleep(0.8)

    await msg.edit_text(
        "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
        "🎧  <b>𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</b>\n▰▰▱▱▱  40%",
        disable_web_page_preview=True,
    )
    await asyncio.sleep(0.8)

    await msg.edit_text(
        "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
        "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
        "🔌  <b>𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</b>\n▰▰▰▱▱  60%",
        disable_web_page_preview=True,
    )
    await asyncio.sleep(0.8)

    await msg.edit_text(
        "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
        "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
        "<s>🔌  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</s> ✅\n"
        "⚙️  <b>𝑰𝒏𝒊𝒕𝒊𝒂𝒍𝒊𝒔𝒊𝒏𝒈...</b>\n▰▰▰▰▱  80%",
        disable_web_page_preview=True,
    )
    await asyncio.sleep(0.8)

    await msg.edit_text(
        "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
        "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
        "<s>🔌  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</s> ✅\n"
        "<s>⚙️  𝑰𝒏𝒊𝒕𝒊𝒂𝒍𝒊𝒔𝒊𝒏𝒈...</s> ✅\n"
        "🚀  <b>𝑨𝒍𝒎𝒐𝒔𝒕 𝑹𝒆𝒂𝒅𝒚...</b>\n▰▰▰▰▰  100%",
        disable_web_page_preview=True,
    )
    await asyncio.sleep(0.8)

    await msg.edit_text(
        "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
        "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
        "<s>🔌  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</s> ✅\n"
        "<s>⚙️  𝑰𝒏𝒊𝒕𝒊𝒂𝒍𝒊𝒔𝒊𝒏𝒈...</s> ✅\n"
        "<s>🚀  𝑨𝒍𝒎𝒐𝒔𝒕 𝑹𝒆𝒂𝒅𝒚...</s> ✅\n\n"
        "🚀  <b>𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕 𝒊𝒔 𝑶𝒏𝒍𝒊𝒏𝒆!</b>",
        disable_web_page_preview=True,
    )
    await asyncio.sleep(0.5)

    # Delete animation message
    await msg.delete()

    _text = (
        message.lang["start_pm"].format(message.from_user.first_name, app.name)
        if private
        else message.lang["start_gp"].format(app.name)
    )

    key = buttons.start_key(message.lang, private)
    # Replace source button URL
    for row in key.inline_keyboard:
        for button in row:
            if button.text == message.lang["source"]:
                button.url = config.GIT_REPO

    try:
        await message.reply_photo(
            photo=random.choice(config.START_IMG),
            caption=_text,
            reply_markup=key,
            quote=not private,
        )
    except Exception as e:
        # Handle privacy restrictions and other button-related errors
        if "BUTTON_USER_PRIVACY_RESTRICTED" in str(e):
            # Send text-only response without inline buttons
            await message.reply_text(
                text=_text,
                quote=not private,
            )
        else:
            # Re-raise other exceptions
            raise

    if private:
        if await db.is_user(message.from_user.id):
            return
        await utils.send_log(message)
        await db.add_user(message.from_user.id)
    else:
        if await db.is_chat(message.chat.id):
            return
        await utils.send_log(message, True)
        await db.add_chat(message.chat.id)


@app.on_message(filters.command(["playmode", "settings"]) & filters.group & ~app.bl_users)
@lang.language()
async def settings(_, message: types.Message):
    admin_only = await db.get_play_mode(message.chat.id)
    cmd_delete = await db.get_cmd_delete(message.chat.id)
    pmsg_delete = await db.get_playmsg_delete(message.chat.id)
    skip_mode = await db.get_skip_mode(message.chat.id)
    _language = await db.get_lang(message.chat.id)
    await message.reply_text(
        text=message.lang["start_settings"].format(message.chat.title),
        reply_markup=extra_inline.settings_markup(
            message.lang, admin_only, cmd_delete, pmsg_delete, skip_mode, message.chat.id
        ),
        quote=True,
    )


@app.on_message(filters.new_chat_members, group=7)
@lang.language()
async def _new_member(_, message: types.Message):
    if message.chat.type != enums.ChatType.SUPERGROUP:
        return await message.chat.leave()

    await asyncio.sleep(3)
    for member in message.new_chat_members:
        if member.id == app.id:
            if await db.is_chat(message.chat.id):
                return
            await utils.send_log(message, True)
            await db.add_chat(message.chat.id)
