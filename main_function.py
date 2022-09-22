#This file runs the main functionalities of the system

#Importing libraries
import board
import math
import time
from Encoder import Encoder
from EncoderButton import Encoder_Button
from EncoderColor import Encoder_Color
from Light import Light
from Colors import Colors
from VibrationMotor import Vibration_Motor

#Initializing components
encoder = Encoder()
vibration_motor = Vibration_Motor()
button = Encoder_Button()
rotor_pixels = Encoder_Color(board.D2, 1, 1)
light1 = Light(board.D4, 1, 1)
#light2 = Light(board.D7, 1, 1)

#Setting up the initial values of variables
current_color = 0 #This variable keeps track of the color changes
light1.set_color(Colors.BLACK)
#light2.set_color(Colors.BLUE)
no_colors = 3 #Indicates how many colors are used in the show

while True:

    #Keeps track of the position of the encoder and adjusts brightness depending on its position - each half revolution  results in brightness change of 10%
    position = encoder.get_position()
    if encoder.get_last_position() is None or position != encoder.get_last_position():
        degrees = encoder.get_degrees()
        print("Position: {0} steps  \t Degrees: {1}° \t\t Revolutions: {2}".format(position, degrees , encoder.get_revolutions()))
        light1.set_brightness(degrees/180*0.1)
    encoder.set_last_position(position)

    #Checks whether user clicked the button - if yes, the color is changed according to a color scheme
    if button.get_value() is True and button.get_last_state() is False:
        print("The button was clicked")
        if(current_color % no_colors == 0):
            light1.set_color(Colors.RED)
            print("Im in red")
        elif(current_color % no_colors == 1):
            light1.set_color(Colors.GREEN)
            print("Im in green")
        elif(current_color % no_colors == 2):
            light1.set_color(Colors.BLUE)
        current_color = (current_color + 1) % no_colors
        #print(current_color)
    button.set_last_state(button.get_value())

    #Checks whether the vibration motor should be on - if the light operates at full brightness and it is not turned off, the motor starts.
    if(light1.get_brightness() == 1 and light1.get_color() != Colors.BLACK):
        vibration_motor.update(True)
    elif(light1.get_brightness() < 1 and vibration_motor.get_value()):
        vibration_motor.update(False)

