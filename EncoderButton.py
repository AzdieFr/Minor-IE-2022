# Encoder_Button Class
import digitalio
import board

class Encoder_Button:

    # Constructor for the class object
    def __init__(self):
        self.last_state = False
        self.button = digitalio.DigitalInOut(board.D3)

    # The function returns the last state of the button
    def get_last_state(self):
        return self.last_state

    #The function allows to change the last state of the button
    def set_last_state(self, st):
        self.last_state = st

    #The function checks the current value of the button
    def get_value(self):
        return self.button.value
