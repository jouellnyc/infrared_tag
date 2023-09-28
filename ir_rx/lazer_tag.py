import machine
from all_off import all_off

grn  = machine.Pin(18, machine.Pin.OUT)
yll  = machine.Pin(19, machine.Pin.OUT)
red  = machine.Pin(20, machine.Pin.OUT)

hits=0

def lazer_check(data):
    #The 'OK' Button
     if data == 64:
            global hits
            print(f"hits: {hits}")
            hits+=1
            print(f"hits: {hits}")
            if hits == 1:
                grn.on()
                yll.off()
                red.off()
            if hits == 2:
                grn.off()
                yll.on()
                red.off()
            if hits == 3:    
                grn.off()
                yll.off()
                red.on()
            if hits == 4:
                hits=0
                all_off()
                
                