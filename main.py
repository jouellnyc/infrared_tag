import time

import machine
led = machine.Pin("LED", machine.Pin.OUT)
led.on()

from all_off import all_off
all_off()

from ir_rx.test import test
test()