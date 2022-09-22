# The RGB Light of the Encoder Class
import neopixel
from rainbowio import colorwheel
import board

class Encoder_Color:

    #Constructor for the class
    def __init__(self, pin, pixnum, br):
        self.pixels = neopixel.NeoPixel(pin, pixnum, brightness = br, auto_write=False, pixel_order=neopixel.RGB)
