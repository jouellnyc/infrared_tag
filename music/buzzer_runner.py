"""
REF:  https://github.com/james1236/buzzer_music/
"""

from time import sleep
from machine import Pin

from .buzzer_music import music
from config import side

if side == 'dark':
    from .songs import light_song as song_string
    count=575
elif side == 'light':
    from .songs import darth_march as song_string
    count=750

def play_song(mysong, count=500):
    """ Send an instance of music as mysong"""
    while count > 0:
        mysong.tick()
        sleep(0.04)
        count-=1
    mysong.stop()

mySong = music(song_string, pins=[Pin(0),Pin(4),Pin(9),Pin(12)],duty=50000)
play_song(mySong, count=count)  