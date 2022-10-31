import pytest
#convention is to use test_ in functions so pytest can run it
class NotInRange(Exception):
    def __init__(self, message="Not in range"):
        self.input= input_
        self.message = message
        super.__init(self.message)

def test_generic():
    a = 5
    with pytes.raises(NotInRange):
        if a not in range(10, 20):
            raise NotInRange