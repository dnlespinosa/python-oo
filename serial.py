"""Python serial number generator."""

from random import randint

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        self.start = start
        current_num = start
        self.current = current_num
    
    def generate(self):
        new_num = self.current
        self.current = self.current + 1
        return new_num
    def reset(self):
        self.current = self.start

