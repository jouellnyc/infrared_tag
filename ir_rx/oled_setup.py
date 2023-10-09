from machine import Pin, SoftI2C
import ssd1306

oled_width = 128
oled_height = 64

i2c = SoftI2C(scl=Pin(9), sda=Pin(8), freq=400000)
oled = ssd1306.SSD1306_I2C(oled_width, oled_height, i2c)

oled.text('Defending...', 0, 20)
oled.show()