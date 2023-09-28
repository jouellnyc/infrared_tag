import machine
grn  = machine.Pin(18, machine.Pin.OUT)
yll  = machine.Pin(19, machine.Pin.OUT)
red  = machine.Pin(20, machine.Pin.OUT)

def all_off():
    for x in [yll, red, grn]:
        x.off()