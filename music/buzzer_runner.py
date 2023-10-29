"""
REF:  https://github.com/james1236/buzzer_music/
"""

from time import sleep
from machine import Pin

from .buzzer_music import music
from config import side

if side == 'dark':
    from .songs import cantina as song_string
elif side == 'light':
    from .songs import darth_march as song_string

def play_song(mysong, count=500):
    """ Send an instance of music as mysong"""
    while count > 0:
        #print(mysong.tick())
        mysong.tick()
        sleep(0.04)
        count-=1
    mysong.stop()

#if __name__ == "__main__":
Buzz1 = Pin(16)
mySong = music(song_string, pins=[Buzz1])
play_song(mySong, count=370)        
