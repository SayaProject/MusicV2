# Copyright (c) 2025 TheHamkerAlone
# Licensed under the MIT License.
# This file is part of AloneXMusic
# ALONE-CODER

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Inline:
    """Handles inline keyboard creation for the bot."""

    def start_key(self, lang, private=True):
        """Create start command keyboard markup."""
        try:
            buttons = []
            
            # First row - commands
            buttons.append([
                InlineKeyboardButton(
                    text=lang.get("commands", "🎛️ Commands"),
                    callback_data="commands"
                ),
                InlineKeyboardButton(
                    text=lang.get("info", "ℹ️ Info"),
                    callback_data="info"
                )
            ])
            
            # Second row - support and source
            buttons.append([
                InlineKeyboardButton(
                    text=lang.get("support", "👥 Support"),
                    url="https://t.me/SayaProjectSupport"
                ),
                InlineKeyboardButton(
                    text=lang.get("source", "📝 Source"),
                    url="https://github.com/SayaProject/MusicV2"
                )
            ])
            
            return InlineKeyboardMarkup(inline_keyboard=buttons)
        except Exception as e:
            # Fallback to empty markup if any error occurs
            return InlineKeyboardMarkup(inline_keyboard=[[]])

    def help_markup(self, lang):
        """Create help command keyboard markup."""
        try:
            buttons = []
            
            buttons.append([
                InlineKeyboardButton(
                    text=lang.get("back", "◀️ Back"),
                    callback_data="start"
                )
            ])
            
            return InlineKeyboardMarkup(inline_keyboard=buttons)
        except Exception as e:
            return InlineKeyboardMarkup(inline_keyboard=[[]])
