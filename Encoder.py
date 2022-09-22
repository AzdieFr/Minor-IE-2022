# Encoder class
import rotaryio
import board
import math

class Encoder:

    #Constructor for the class
    def __init__(self):
        self.last_position = None
        self.encoder = rotaryio.IncrementalEncoder(board.D13, board.D10)

    #Gets the current position of the encoder
    def get_position(self):
        return self.encoder.position

    #Sets the last position of the encoder to pos
    def set_last_position(self, pos):
        self.last_position = pos

    #Gets the last (previous) position of the encoder
    def get_last_position(self):
        return self.last_position

    #Gets the current position of the encoder in degrees
    def get_degrees(self):
        return self.encoder.position * 15

    #Gets the current position of the encoder in knob revolutions
    def get_revolutions(self):
        rev = self.encoder.position/24
        rev = math.trunc(rev)
        return rev


