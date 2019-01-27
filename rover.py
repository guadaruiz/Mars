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

############################################################################################################

################## CREATE A ROVER WITH INSTRUCTIONS FROM INPUT FILE ##################

rover_lines=[] #Creates an array with each line of the instructions file
with open('rover.txt') as f:
    for line in f:
        rover_lines.append(line.strip())
#print(rover_lines)

################## CREATE ROVER 1 WITH INSTRUCTIONS FROM INPUT FILE ##################

rover1 = [] # Vector for Rover 1: (x, y, direction)
rover1[:0] = rover_lines[1].split(' ')

rover1_position = np.array([int(rover1[0]),int(rover1[1])]) # (x,y) position (int) of Rover 1
rover1_direction=[rover1[2]] # Direction (str) of Rover 1

instructions_rover1 = [] #Gives a vector of strings with each instruction for Rover 1 as an element
instructions_rover1[:0] = rover_lines[2]

Rover_1=Rover(rover1_position, rover1_direction, instructions_rover1)

################## CREATE ROVER 2 WITH INSTRUCTIONS FROM INPUT FILE ##################

rover2= [] # Vector for Rover 2: (x, y, direction)
rover2[:0] = rover_lines[3].split(' ')

rover2_position=np.array([int(rover2[0]),int(rover2[1])]) # (x,y) position (int) of Rover 1
rover2_direction=[rover2[2]] # Direction (str) of Rover 1

instructions_rover2 = []  #Gives a vector of strings with each instruction for Rover 2 as an element
instructions_rover2[:0] = rover_lines[4]

Rover_2=Rover(rover2_position, rover2_direction, instructions_rover2)
