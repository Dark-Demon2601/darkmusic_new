from pyrogram import Client
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn
from helpers.filters import filters


@Client.on_message(filters.command('start'))
async def start(_, message: Message):
    await message.reply_text(
        f"""I am **{bn}** !!
https://telegra.ph/file/1bac7eac76a16f64d8afb.jpg
๐ด ๐๐๐ ๐๐๐ ๐๐๐๐ ๐๐๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐'๐ ๐๐๐๐๐ ๐๐๐๐ ๐
โข๐ฎ๐๐๐๐๐๐๐๐ ๐ด ๐๐ ๐๐๐๐๐ ๐ ๐๐๐๐๐๐๐ ๐๐ ๐๐๐๐๐ ๐๐๐๐๐๐ โฉ
โข๐ฟ๐ ๐๐๐ ๐๐ ๐๐๐๐ ๐๐๐๐๐๐๐๐๐๐ ๐๐๐๐ [๐บ๐๐๐๐](https://t.me/akshi_s_ashu)
โข๐ฟิาฝ ฦฯษฑษฑฮฑษณิส ๐ด ฦฯษพษพาฝษณฦสแง สฯฯฯฯษพฦ ฮฑษพาฝ:
โ๏ธ /play-Tฯ สาฝฮฑษพฦิ สฯษณษ  ฯษพฯษฑ แงฯฯฦฯแฆาฝ ฮฑษณิ ฯสฮฑแง ิฮนษพาฝฦฦสแง
โ๏ธ/pause - Pฮฑฯสาฝ Vฯฮนฦาฝ Cิฮฑฦ Mฯสฮนฦ.
โ๏ธ /resume - Rาฝสฯษฑาฝ Vฯฮนฦาฝ Cิฮฑฦ Mฯสฮนฦ.
โ๏ธ /skip - Sฦฮนฯส ฦิาฝ ฦฯษพษพาฝษณฦ Mฯสฮนฦ Pสฮฑแงฮนษณษ  Iษณ Vฯฮนฦาฝ Cิฮฑฦ.
โ๏ธ /stop - Cสาฝฮฑษพส Tิาฝ Qฯาฝฯาฝ ฮฑส ษฏาฝสส ฮฑส าฝษณิส Vฯฮนฦาฝ Cิฮฑฦ Mฯสฮนฦ.
โ๏ธ /song (สฯษณษ  ษณฮฑษฑาฝ) - Tฯ สาฝฮฑษพฦิ สฯษณษ  ฮฑษณิ สาฝษณิ สฯษณษ  ิฮนษพาฝฦฦสแง.
โ๏ธ /fplay (ษพาฝฯสแง ฦฯ ฮฑฯิฮนฯ ฯษพ สฮนษณฦ) - Pสฮฑแงส ฦิาฝ ษพาฝฯสฮนาฝิ ฮฑฯิฮนฯ ฯฮนสาฝ ฯษพ YฯฯTฯแฆาฝ สฮนิาฝฯ ฦิษพฯฯษ ิ สฮนษณฦ. 
        """,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group ๐ฌ", url="https://t.me/phoenix_music_suport"
                    ),
                    InlineKeyboardButton(
                        "Channel ๐ฃ", url="https://t.me/phoenix_music_new"
                    ),
                    InlineKeyboardButton(
                        "Owner ๐", url="https://t.me/akshi_s_ashu"
                    ),
                ], 
                [
                    InlineKeyboardButton(
                        "About ๐ฅ", url="https://telegra.ph/Doreamon-Bot-09-10"   
                    )
                ]
            ]
        )
    )

from pyrogram import Client, filters

import youtube_dl
from youtube_search import YoutubeSearch
import requests

import os

# Convert hh:mm:ss to seconds
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60 ** i for i, x in enumerate(reversed(stringt.split(':'))))


@Client.on_message(filters.command(['song']))
def a(client, message):
    query = ''
    for i in message.command[1:]:
        query += ' ' + str(i)
    print(query)
    m = message.reply(f"**๐ Searching For** `{query}`")
    ydl_opts = {"format": "bestaudio[ext=m4a]"}
    try:
        results = []
        count = 0
        while len(results) == 0 and count < 6:
            if count>0:
                time.sleep(1)
            results = YoutubeSearch(query, max_results=1).to_dict()
            count += 1
        # results = YoutubeSearch(query, max_results=1).to_dict()
        try:
            link = f"https://youtube.com{results[0]['url_suffix']}"
            # print(results)
            title = results[0]["title"]
            thumbnail = results[0]["thumbnails"][0]
            duration = results[0]["duration"]
            views = results[0]["views"]

            ## UNCOMMENT THIS IF YOU WANT A LIMIT ON DURATION. CHANGE 1800 TO YOUR OWN PREFFERED DURATION AND EDIT THE MESSAGE (30 minutes cap) LIMIT IN SECONDS
            # if time_to_seconds(duration) >= 1800:  # duration limit
            #     m.edit("Exceeded 30mins cap")
            #     return

            performer = f"[MรSรC แบรธโ ]" 
            thumb_name = f'thumb{message.message_id}.jpg'
            thumb = requests.get(thumbnail, allow_redirects=True)
            open(thumb_name, 'wb').write(thumb.content)

        except Exception as e:
            print(e)
            m.edit('**Found Literary Noting. Please Try Another Song or Use Correct Spelling!**')
            return
    except Exception as e:
        m.edit(
            "**Enter Song Name with Command!**"
        )
        print(str(e))
        return
    m.edit(f"๐ฅ **Uploading Song**  `{query}` !")
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(link, download=False)
            audio_file = ydl.prepare_filename(info_dict)
            ydl.process_info(info_dict)
        rep = f'๐ท <b>Title:</b> <a href="{link}">{title}</a>\nโณ <b>Duration:</b> <code>{duration}</code>\n๐ <b>Views:</b> <code>{views}</code>\n'
        secmul, dur, dur_arr = 1, 0, duration.split(':')
        for i in range(len(dur_arr)-1, -1, -1):
            dur += (int(dur_arr[i]) * secmul)
            secmul *= 60
        message.reply_audio(audio_file, caption=rep, parse_mode='HTML',quote=False, title=title, duration=dur, performer=performer, thumb=thumb_name)
        m.delete()
        message.delete()
    except Exception as e:
        m.edit('**An Error Occured. Please Report This To [SUPORT GROUP](https://t.me/phoenix_music_suport) !!**')
        print(e)
    try:
        os.remove(audio_file)
        os.remove(thumb_name)
    except Exception as e:
        print(e)
