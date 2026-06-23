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
        )
        self.owner = config.OWNER_ID
        self.logger = config.LOGGER_ID
        self.bl_users = pyrogram.filters.user()
        self.sudoers = pyrogram.filters.user(self.owner)

    async def send_message(
        self,
        chat_id: int | str,
        text: str,
        parse_mode: pyrogram.enums.ParseMode | str | None = None,
        entities: list | None = None,
        disable_web_page_preview: bool | None = None,
        disable_notification: bool | None = None,
        reply_to_message_id: int | None = None,
        reply_to_chat_id: int | str | None = None,
        reply_to_story_id: int | None = None,
        quote: str | None = None,
        quote_entities: list | None = None,
        quote_offset: int | None = None,
        schedule_date: int | None = None,
        protect_content: bool | None = None,
        reply_markup: InlineKeyboardMarkup | ReplyKeyboardMarkup | list | None = None
    ):
        if disable_web_page_preview is None:
            disable_web_page_preview = True
        return await super().send_message(
            chat_id,
            text,
            parse_mode,
            entities,
            disable_web_page_preview,
            disable_notification,
            reply_to_message_id,
            reply_to_chat_id,
            reply_to_story_id,
            quote,
            quote_entities,
            quote_offset,
            schedule_date,
            protect_content,
            reply_markup
        )

    async def edit_message_text(
        self,
        chat_id: int | str,
        message_id: int,
        text: str,
        parse_mode: pyrogram.enums.ParseMode | str | None = None,
        entities: list | None = None,
        disable_web_page_preview: bool | None = None,
        reply_markup: InlineKeyboardMarkup | None = None
    ):
        if disable_web_page_preview is None:
            disable_web_page_preview = True
        return await super().edit_message_text(
            chat_id,
            message_id,
            text,
            parse_mode,
            entities,
            disable_web_page_preview,
            reply_markup
        )

    async def boot(self):
        """
        Starts the bot and performs initial setup.

        Raises:
            SystemExit: If the bot fails to access the log group or is not an administrator in the logger group.
        """
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(self.logger, "Bot Started", disable_web_page_preview=True)
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
