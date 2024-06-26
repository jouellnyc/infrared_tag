## Table of Contents
- [Introduction](#introduction)
- [Components](#Components)
- [Schmatic](#schematic)
- [Images](#images)
- [StarWars](#starwars)
- [Credits](#credits)
- [License](#license)

## Introduction

Remember Laser tag?  

Put one of these on your desk and one on your co-worker's and using the remote, it's a shoot out until 3 shots hit...


## Embellishing
- Customize the text as you wish. I've added Star Wars themes for the light and dark sides with Peizo buzzer(s).
- They fit on the side of the pico reaching into the GND bank on the breadboard.
- Each respective side's them will play if the other sides loses ("Emperial March" vs "Cantina")
- See pic below

## Components
- [IR Receiver](https://www.amazon.com/gp/product/B06XYNDRGF)
- [Remote](https://www.amazon.com/gp/product/B0C7BPJYH1/)
- Pi Pico
- Leds - Red, Yellow, Green
- 470 Ohm (or similar) resistors


## Schematic 
![Fritzing](images/ir_tag_sketch.png)

**OLED Connections**

| GPIO Pin | Connection|
| -------- | --------- |
| GPIO 8   | SDA       |
| GPIO 9   | SCL       |
| GND      | GND       |
| 5V/PIN40 | VCC       |  

**IR Receiver Connections**

| GPIO Pin | Connection|
| -------- | --------- |
| GPIO 15  | IN  (left leg) |
| GND 5    | GND (middle leg) |
| 5V/Pin 40| VCC (right leg|

**LEDs**

| GPIO Pin | Color     |
| -------- | --------- |
| GPIO 18  | Green     |
| GPIO 19  | Yellow    |
| GPIO 20  | Red       |

Each LED also connects to it's own resistor.  

Each resistor connects to the blue jumper which is connected to GND. 



## Images 
![Action 1](images/LT1.jpg)
![Action 2](images/LT4.jpg)
![Action 3](images/LT2.jpg)

## StarWars
## 4 Piezos, and 2 Sets of synchronized leds as Star Wars Themes play!
![4 Piezos and 2 Sets of LEDs!](images/4piezos.jpg)


## Installation
- git clone https://github.com/jouellnyc/infrared_tag  
- Upload via Thonny to / on your pico pi.


## Credits
- This code relies extensively on https://github.com/peterhinch/micropython_ir/tree/master
- PWM music from https://github.com/james1236/buzzer_music/ 

## License 
MIT  
