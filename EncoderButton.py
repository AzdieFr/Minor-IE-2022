# EncoderButtonClass
import digitalio
import board

class EncoderButton:

    def __init__(self):
        self.last_state = False
        self.button = digitalio.DigitalInOut(board.D3)

    def get_last_state(self):
        return self.last_state

    def set_last_state(self, st):
        self.last_state = st

    def get_value(self):
        return self.button.value
