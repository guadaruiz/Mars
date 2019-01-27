import numpy as np

class Rover():

    def __init__(self, position, direction, instructions):
        self.position = position
        self.direction = direction
        self.instructions = instructions
        #self.move= move_rover
        #self.get_key= get_key

    def get_key(self, direction_math, direction_dictionary):
        for key, value in direction_dictionary.items():
            if np.array_equal(direction_math, value):
                return key

        return "key doesn't exist"

    def move(self):

        direction = ['N', 'S', 'W', 'E']
        direction_math = [np.array([0,1]), np.array([0,-1]), np.array([-1,0]), np.array([1,0])]
        direction_dictionary = dict(zip(direction, direction_math))

        mathdir_rover=direction_dictionary[self.direction[0]]

        for instruction in self.instructions:
            if instruction == 'M':
                self.position = self.position + mathdir_rover

            elif instruction == 'R':
                #mathdir_rover1= mathdir_rover1*np.array('[[0 -1]; [1 0]]')
                mathdir_rover= np.dot( np.array([[0,1],
                                             [-1,0]]), mathdir_rover)

            elif instruction == 'L':
    #            mathdir_rover1= mathdir_rover1 * np.array('[[0 1]; [-1 0]]')
                mathdir_rover= np.dot( np.array([[0,-1],
                                                [1,0]]), mathdir_rover)

        print(self.position,self.get_key(mathdir_rover, direction_dictionary))

        return self.position, self.get_key(mathdir_rover, direction_dictionary)
