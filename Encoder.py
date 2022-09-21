# Encoder class
import rotaryio
import board

class Encoder:

    def __init__(self):

        self.last_position = None
        self.encoder = rotaryio.IncrementalEncoder(board.D13, board.D10)

    def get_position(self):
        return self.encoder.position

    def set_last_position(self, pos):
        self.last_position = pos

    def get_last_position(self):
        return self.last_position
