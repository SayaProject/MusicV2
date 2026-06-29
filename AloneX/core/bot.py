# Copyright (c) 2025 TheHamkerAlone 
# Licensed under the MIT License.
# This file is part of AloneXMusic


import pyrogram
from pyrogram.types import InlineKeyboardMarkup, ReplyKeyboardMarkup

from AloneX import config, logger


class Bot(pyrogram.Client):
    def __init__(self):
        super().__init__(
            name="AloneX",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
            parse_mode=pyrogram.enums.ParseMode.HTML,
            max_concurrent_transmissions=7,
            workers=64,
        )
        self.owner = config.OWNER_ID
        self.logger = config.LOGGER_ID
        self.bl_users = pyrogram.filters.user()
        self.sudoers = pyrogram.filters.user(self.owner)

    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        **kwargs
    ):
        if "disable_web_page_preview" not in kwargs:
            kwargs["disable_web_page_preview"] = True
        return await super().send_message(chat_id, text, **kwargs)

    async def edit_message_text(
        self,
        chat_id: int | str,
        message_id: int,
        text: str,
        **kwargs
    ):
        if "disable_web_page_preview" not in kwargs:
            kwargs["disable_web_page_preview"] = True
        return await super().edit_message_text(chat_id, message_id, text, **kwargs)

    async def boot(self):
        """
        Starts the bot and performs initial setup.

        Raises:
            SystemExit: If the bot fails to access the log group or is not an administrator in the logger group.
        """
        import asyncio

        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            # ── Step 1 : Loading Modules ─────────────────────────────────────
            msg = await self.send_message(
                self.logger,
                "⚡  <b>𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</b>\n▰▱▱▱▱  20%",
                disable_web_page_preview=True,
            )
            await asyncio.sleep(1.2)

            # ── Step 2 : Connecting Voice Chat ───────────────────────────────
            await self.edit_message_text(
                self.logger,
                msg.id,
                "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
                "🎧  <b>𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</b>\n▰▰▱▱▱  40%",
                disable_web_page_preview=True,
            )
            await asyncio.sleep(1.2)

            # ── Step 3 : Loading Plugins ─────────────────────────────────────
            await self.edit_message_text(
                self.logger,
                msg.id,
                "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
                "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
                "🔌  <b>𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</b>\n▰▰▰▱▱  60%",
                disable_web_page_preview=True,
            )
            await asyncio.sleep(1.2)

            # ── Step 4 : Initialising ────────────────────────────────────────
            await self.edit_message_text(
                self.logger,
                msg.id,
                "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
                "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
                "<s>🔌  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</s> ✅\n"
                "⚙️  <b>𝑰𝒏𝒊𝒕𝒊𝒂𝒍𝒊𝒔𝒊𝒏𝒈...</b>\n▰▰▰▰▱  80%",
                disable_web_page_preview=True,
            )
            await asyncio.sleep(1.2)

            # ── Step 5 : Almost Ready ────────────────────────────────────────
            await self.edit_message_text(
                self.logger,
                msg.id,
                "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
                "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
                "<s>🔌  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</s> ✅\n"
                "<s>⚙️  𝑰𝒏𝒊𝒕𝒊𝒂𝒍𝒊𝒔𝒊𝒏𝒈...</s> ✅\n"
                "🚀  <b>𝑨𝒍𝒎𝒐𝒔𝒕 𝑹𝒆𝒂𝒅𝒚...</b>\n▰▰▰▰▰  100%",
                disable_web_page_preview=True,
            )
            await asyncio.sleep(1.2)

            # ── Final : Bot is Online ────────────────────────────────────────
            await self.edit_message_text(
                self.logger,
                msg.id,
                "<s>⚡  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑴𝒐𝒅𝒖𝒍𝒆𝒔...</s> ✅\n"
                "<s>🎧  𝑪𝒐𝒏𝒏𝒆𝒄𝒕𝒊𝒏𝒈 𝑽𝒐𝒊𝒄𝒆 𝑪𝒉𝒂𝒕...</s> ✅\n"
                "<s>🔌  𝑳𝒐𝒂𝒅𝒊𝒏𝒈 𝑷𝒍𝒖𝒈𝒊𝒏𝒔...</s> ✅\n"
                "<s>⚙️  𝑰𝒏𝒊𝒕𝒊𝒂𝒍𝒊𝒔𝒊𝒏𝒈...</s> ✅\n"
                "<s>🚀  𝑨𝒍𝒎𝒐𝒔𝒕 𝑹𝒆𝒂𝒅𝒚...</s> ✅\n\n"
                "🚀  <b>𝑴𝒖𝒔𝒊𝒄 𝑩𝒐𝒕 𝒊𝒔 𝑶𝒏𝒍𝒊𝒏𝒆!</b>",
                disable_web_page_preview=True,
            )

            get = await self.get_chat_member(self.logger, self.id)
        except Exception as ex:
            raise SystemExit(f"Bot has failed to access the log group: {self.logger}\nReason: {ex}")

        if get.status != pyrogram.enums.ChatMemberStatus.ADMINISTRATOR:
            raise SystemExit("Please promote the bot as an admin in logger group.")
        logger.info(f"Bot started as @{self.username}")

    async def exit(self):
        """
        Asynchronously stops the bot.
        """
        await super().stop()
        logger.info("Bot stopped.")
