"""Python serial number generator."""

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
        """Make a new generator, starting at start."""
        self.start = start
        self.next = start

    def __repr__(self):
        """ Show representation of the INSTANCE. """
        return f"<SerialGenerator start={self.start} next={self.next}>"


    def generate(self):
        """ return next sequential number """
        self.next += 1
        return self.next - 1
    
    def reset(self):
        """ resetting the number back to original start number """
        self.next = self.start
    