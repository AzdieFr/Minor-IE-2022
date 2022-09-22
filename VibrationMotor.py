# Vibration Motor Class
import board
import digitalio

class Vibration_Motor():

    #The constructor for the class
    def __init__(self):
        self.motor = digitalio.DigitalInOut(board.A0)
        self.motor.direction = digitalio.Direction.OUTPUT

    #Allows to turn the motor on and off with True and False values
    def update(self, value):
        self.motor.value = value

    #Allows to get the current state of the motor on (True) or off (False)
    def get_value(self):
        return self.motor.value
