#open it with Mu editor OR https://python.microbit.org/
# microbit compass
# made by Qusay laila 
from microbit import *
compass.calibrate()
while True:
    c = compass.heading()
    if c < 45 or c > 315:
        display.show("N")
    elif c < 135:
        display.show("E")
    elif c < 225:
        display.show("S")
    else:
        display.show("W")