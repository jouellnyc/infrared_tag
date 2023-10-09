import machine
from all_off import all_off
from .oled_setup import oled


grn  = machine.Pin(18, machine.Pin.OUT)
yll  = machine.Pin(19, machine.Pin.OUT)
red  = machine.Pin(20, machine.Pin.OUT)

hits=0

#Most common on Amazon
pri_scan_codes=[28,64]

def display_hits():
    print(f"hits: {hits}")
    oled.fill(0)
    oled.text(f"We've been hit!", 0, 0)
    oled.text(f"Total Hits: {hits}", 0, 20)
    oled.show()
    
def display_restart():
    oled.fill(0)
    oled.text('Defending...', 0, 20)
    oled.show()
    
def display_surrender():
    oled.fill(0)
    oled.text(f"Surrender!", 0, 20)
    oled.show()
                
def lazer_check(data):
    #The 'OK' Button
     if data in pri_scan_codes:
            global hits
            hits+=1
            if hits == 1:
                display_hits()
                grn.on()
                yll.off()
                red.off()
            if hits == 2:
                display_hits()
                grn.off()
                yll.on()
                red.off()
            if hits == 3:
                display_hits()
                grn.off()
                yll.off()
                red.on()
                display_surrender()
            if hits > 3:
                hits=0
                display_restart()
                all_off()
                               
                