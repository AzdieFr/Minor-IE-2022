import neopixel
from rainbowio import colorwheel

class EncoderColor:

    def __init__(self, pin, pixnum, br):
        self.pixels = neopixel.NeoPixel(pin, pixnum, brightness = br, auto_write=False, pixel_order=neopixel.RGB)
