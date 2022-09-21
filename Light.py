import board
import neopixel
from rainbowio import colorwheel


class Light():

    def __init__(self, pin, pixnum, br):
        self.pin = pin
        self.pixnum = pixnum
        self.brightness = br
        self.pixels = neopixel.NeoPixel(self.pin, self.pixnum, brightness = self.brightness, auto_write=False, pixel_order=neopixel.RGB)

    def set_color(self, color):
        self.pixels.fill(color)
        self.pixels.show()

    def set_brightness(self, br):
        self.pixels.brightness = br
        self.pixels.show()
