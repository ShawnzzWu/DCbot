# import youtube_dl

import yt_dlp as youtube_dl
import variables as vr


youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'outtmpl': vr.voice_path + '\\%(title)s.%(ext)s',
    # 'format': 'bestaudio/best',
    # 'restrictfilenames': True,
    # 'noplaylist': True,
    # 'nocheckcertificate': True,
    # 'ignoreerrors': False,
    # 'logtostderr': False,
    # 'quiet': True,
    # 'no_warnings': True,
    # 'default_search': 'auto',
    # 'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}
#


with youtube_dl.YoutubeDL(ytdl_format_options) as ydl:
    ydl.download(['https://www.youtube.com/watch?v=OpKENhgud10'])