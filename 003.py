# encoding:utf-8

from mutagen.mp3 import MP3
audio = MP3("sound/red_song/2.mp3")
print(audio.info.length)
