from rover import Rover
import numpy as np


Rover_test=Rover(np.array([0,0]), 'N', 'L')
print(Rover_test)



def test_answer():
    assert Rover_test.move()[1] == "E"

def test_answer2():
    assert np.array_equal(Rover_test.move()[0], np.array([0, 0]))
