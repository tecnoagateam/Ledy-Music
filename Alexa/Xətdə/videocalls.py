# A Powerful Music Bot Property Of Rocks Indian Largest Chatting Group
# Without Credit (Mother Fucker)
# Rocks © @Dr_Asad_Ali © Rocks
# Owner Asad Ali
# Harshit Sharma



from pyrogram.types import (CallbackQuery, InlineKeyboardButton,
                            InlineKeyboardMarkup, InputMediaPhoto, Message)


def choose_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎵 Musiqi oynat",
                callback_data=f"MusicStream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🎥 Video oynat",
                callback_data=f"Choose {videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="🗑 bağla",
                callback_data=f"forceclose {videoid}|{user_id}",
            )
        ],
    ]
    return buttons


def livestream_markup(quality, videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="🎥  canlı başlat",
                callback_data=f"LiveStream {quality}|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 bağla",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons


def stream_quality_markup(videoid, duration, user_id):
    buttons = [
        [
            InlineKeyboardButton(
                text="📽 360P",
                callback_data=f"VideoStream 360|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 720P",
                callback_data=f"VideoStream 720|{videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="📽 480P",
                callback_data=f"VideoStream 480|{videoid}|{duration}|{user_id}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="⬅️ geri qayıt",
                callback_data=f"gback_list_chose_stream {videoid}|{duration}|{user_id}",
            ),
            InlineKeyboardButton(
                text="🗑 bağla",
                callback_data=f"forceclose {videoid}|{user_id}",
            ),
        ],
    ]
    return buttons
