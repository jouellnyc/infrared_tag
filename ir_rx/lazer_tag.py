import time
import machine

from all_off import all_off
from .oled_setup import oled, first_text
from config import side, quotes

grn  = machine.Pin(18, machine.Pin.OUT)
yll  = machine.Pin(19, machine.Pin.OUT)
red  = machine.Pin(20, machine.Pin.OUT)

#Most common on Amazon
pri_scan_codes=[28,64]

hits=0

def display_hits(text):
    print(f"hits: {hits}")
    oled.fill(0)
    oled.text(f"{text}", 0, 0)
    oled.text(f"Total Hits: {hits}", 0, 20)
    oled.show()
    
def display_restart():
    oled.fill(0)
    first_text()    
    
def display_surrender():
    oled.fill(0)
    oled.text(f"Wars not make", 0, 20)
    oled.text(f"one great...",  0, 40)
    oled.show()
                
def lazer_check(data):
    #The 'OK' Button
     if data in pri_scan_codes:
            global hits
            hits+=1
            if hits == 1:
                display_hits(quotes[side][hits-1])
                grn.on()
                yll.off()
                red.off()
            if hits == 2:
                display_hits(quotes[side][hits-1])
                grn.off()
                yll.on()
                red.off()
            if hits == 3:
                display_hits(quotes[side][hits-1])
                grn.off()
                yll.off()
                red.on()
                time.sleep(5)
                display_surrender()
                import music.buzzer_runner
            if hits > 3:
                hits=0
                display_restart()
                all_off()
                               
                