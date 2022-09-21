import board
import math
import time
from Encoder import Encoder
from EncoderButton import EncoderButton
from EncoderColor import EncoderColor
from Light import Light
from colors import Colors

encoder = Encoder()

button = EncoderButton()

rotor_pixels = EncoderColor(board.D2, 1, 1)

#light
light1 = Light(board.D4, 8, 1)
light2 = Light(board.D7, 8, 1)


current_color = 0

light1.set_color(Colors.BLACK)
light2.set_color(Colors.BLUE)

while True:
    position = encoder.get_position()
    if encoder.get_last_position() is None or position != encoder.get_last_position():
        degrees = position * 15
        revolutions = math.trunc(position/24) # math.trunc() rounds towards 0
        print("Position: {0} steps  \t Degrees: {1}° \t\t Revolutions: {2}".format(position, degrees, revolutions))
        light1.set_brightness(degrees/180*0.1)
    encoder.set_last_position(position)
    if button.get_value() is True and button.get_last_state() is False:
        print("The button was clicked")
        if(current_color % 3 == 0):
            light1.set_color(Colors.RED)
            print("Im in red")
        elif(current_color % 3 == 1):
            light1.set_color(Colors.GREEN)
            print("Im in green")
        elif(current_color % 3 == 2):
            light1.set_color(Colors.BLUE)
        current_color = current_color + 1
        #print(current_color)
    button.set_last_state(button.get_value())

