import time

import machine
machine.Pin("LED", machine.Pin.OUT).on()

from ir_rx.leds import all_off
all_off()

from ir_rx.test import test
test()