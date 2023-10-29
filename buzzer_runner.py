"""
REF:  https://github.com/james1236/buzzer_music/
"""
from time import sleep
from machine import Pin

from buzzer_music import music
from songs import cantina as song_string
Buzz1 = Pin(16)

def play_song(mysong,count = 500):
    """ Send an instance of music as mysong"""
    while count > 0:
        print(count)
        print(mysong.tick())
        sleep(0.04)
        count-=1
    mysong.stop()
    
if __name__ == "__main__":
    mySong = music(song_string, pins=[Buzz1])
    play_song(mySong, count=370)        
