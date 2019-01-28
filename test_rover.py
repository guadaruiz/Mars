from rover import Rover
import numpy as np

Rover_test=Rover(np.array([int(0),int(1)]), 'N', 'MMLMRRM')
direction_dictionary=Rover_test.create_direction_dictionary()
mathdir_rover=direction_dictionary[Rover_test.direction[0]]

print(Rover_test.get_key(mathdir_rover, direction_dictionary))

#Rover_test.move()

def test_move_dir():
    assert Rover_test.move()[1] == "E"

def test_move_position():
   assert np.array_equal(Rover_test.move()[0], np.array([0,3]))

def test_get_key():
    assert Rover_test.get_key(mathdir_rover, direction_dictionary) == "N"

#print(Rover_test.get_key()[0])

#print(get_key(direction_dictionary[Rover_test[0]], direction_dictionary))
