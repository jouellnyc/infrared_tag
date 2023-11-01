import time

from .oled_setup import oled, first_text
from .leds import grn, grn2, yll, yll2, red, all_off
from config import side, quotes

"""red2 is plugged into the same GPIO as red 1, so it will turn on when red is turn on
   and not referenced here """


#Most common on Amazon
pri_scan_codes=[28,64]

hits=0


def led_state(leds, state):
    for led in leds:
        if state == 'on':
            led.on()
        else:
            led.off()
    
def green(ledsstate):
    if state == "on":
        grn.on()
        grn2.on()
    else:
        grn.off()
        grn2.off()



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

def reset():
    import sys
    del sys.modules['music.buzzer_runner']
                
def lazer_check(data):
    #The 'OK' Button
     if data in pri_scan_codes:
            global hits
            hits+=1
            if hits == 1:
                display_hits(quotes[side][hits-1])
                led_state([grn,grn2],'on')
                led_state([yll,yll2],'off')
                red.off()
            if hits == 2:
                display_hits(quotes[side][hits-1])
                led_state([grn,grn2],'off')
                led_state([yll,yll2],'on')
                red.off()
            if hits == 3:
                display_hits(quotes[side][hits-1])
                led_state([grn,grn2],'off')
                led_state([yll,yll2],'off')
                red.on()
                time.sleep(5)
                display_surrender()
                import music.buzzer_runner
            if hits > 3:
                hits=0
                display_restart()
                reset()
                all_off()
                               
                