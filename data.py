from pyrogram.types import InlineKeyboardButton


class Data:
    generate_single_button = [InlineKeyboardButton("🙄 𝐆𝐄𝐍𝐄𝐑𝐀𝐓𝐄 𝐒𝐓𝐑𝐈𝐍𝐆 🙄", callback_data="generate")]

    generate_button = [generate_single_button]

    buttons = [
        generate_single_button,
        [InlineKeyboardButton("❣️ 𝐒𝐔𝐏𝐏𝐎𝐑𝐓 ❣️", url="https://t.me/rajput_ki_haveli"),
         InlineKeyboardButton("🥀 𝐃𝐄𝐏𝐋𝐎𝐏𝐄𝐑 🥀", url="https://t.me/s_rajputt"),
        ],
    ]

    START = """
𝐇𝐲𝐲 {},

𝐓𝐡𝐢𝐬 𝐢𝐬  {},
𝐀𝐧 𝐨𝐩𝐞𝐧 𝐬𝐨𝐮𝐫𝐜𝐞 𝐬𝐭𝐫𝐢𝐧𝐠 𝐬𝐞𝐬𝐬𝐢𝐨𝐧 𝐠𝐞𝐧𝐞𝐫𝐚𝐭𝐨𝐫 𝐛𝐨𝐭, 𝐰𝐫𝐢𝐭𝐭𝐞𝐧 𝐢𝐧 𝐩𝐲𝐭𝐡𝐨𝐧 𝐰𝐢𝐭𝐡 𝐭𝐡𝐞 𝐡𝐞𝐥𝐩 𝐨𝐟 🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 𝄟⃟💫 ..

𝐒𝐎𝐔𝐑𝐂𝐄 : [𝐑𝐚𝐣𝐩𝐮𝐭 GITHUB ](https://github.com/SRajput1234/StringGenBot)
𝐌𝐀𝐃𝐄 𝐁𝐘 : [🕊️⃝‌🦋𝐒 𝐑𝐚𝐣𝐩𝐮𝐭 𝄟⃟💫](https://t.me/s_rajputt) !
    """
