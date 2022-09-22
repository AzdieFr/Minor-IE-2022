# The Light class
import board
import neopixel
from rainbowio import colorwheel
from Colors import Colors


class Light():

    # Class constructor
    def __init__(self, pin, pixnum, br):
        self.pin = pin
        self.pixnum = pixnum
        self.brightness = br
        self.pixels = neopixel.NeoPixel(self.pin, self.pixnum, brightness = self.brightness, auto_write=False, pixel_order=neopixel.RGB)
        self.color = Colors.BLACK

    #Allows to set the color of the light to an RGB color
    def set_color(self, color):
        self.pixels.fill(color)
        self.pixels.show()
        self.color = color

    #Allows to set the brightness of the light to 0 - 100%
    def set_brightness(self, br):
        self.pixels.brightness = br
        self.pixels.show()

    #Gets the current brightness of the light
    def get_brightness(self):
        return self.pixels.brightness

    #Gets the current color of the light
    def get_color(self):
        return self.color
