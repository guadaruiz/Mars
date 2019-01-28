import numpy as np

class Rover():

    ''' This class can be used to create rover objects that take as input: a vector of initial position,
     a pointing direction represented by a cardinal letter (N, S, W or E), and a set of movement instructions. '''

    def __init__(self, position, direction, instructions):
        self.position = position
        self.direction = direction
        self.instructions = instructions

    def create_direction_dictionary(self):
        # The current dictionary translates the direction letter into a mathematical vector. For example, N (north) is
        # mathematically represented by np.array([0,1]) .

        direction = ['N', 'S', 'W', 'E']
        direction_math = [np.array([0,1]), np.array([0,-1]), np.array([-1,0]), np.array([1,0])]
        direction_dictionary = dict(zip(direction, direction_math))
        return direction_dictionary

    def get_key(self, direction_math, direction_dictionary):
        # The get_key function converts the mathematical direction vector back into a letter (N,S,W or E) by matching the
        # value with the key in the direction_dictionary .

        for key, value in direction_dictionary.items():
            if np.array_equal(direction_math, value):
                return key

        return "key doesn't exist"

    def move(self):
        # The move function calls the create_direction_dictionary function in order to create the direction_dictionary. Then,
        # it assigns an initial direction and position for the rover object. By reading its set of instructions the rover is
        # moved forward by rewriting its final position (positionFinal), or turned left (L) or right (R) by multiplying its
        # mathematical direction vector (mathdir_rover) by the corresponding rotational matrix. Finally, the get_key()
        # function is called to translate the final mathematical direction vector back into the direction letter (N, S, W or E).
        # Final position and the letter corresponding to the direction of the rover after moving are printed as output.

        direction_dictionary=self.create_direction_dictionary()
        mathdir_rover=direction_dictionary[self.direction[0]]
        positionFinal=self.position

        for instruction in self.instructions:
            if instruction == 'M':
                positionFinal = positionFinal + mathdir_rover

            elif instruction == 'R':
                mathdir_rover= np.dot(np.array([[0 ,1],[-1,0]]), mathdir_rover)

            elif instruction == 'L':
                mathdir_rover= np.dot(np.array([[0,-1],[1, 0]]), mathdir_rover)

        print(positionFinal,self.get_key(mathdir_rover, direction_dictionary))

        return positionFinal, self.get_key(mathdir_rover, direction_dictionary)

############################################################################################################

################## READ INPUT FILE ##################

rover_lines=[] #Creates an array with each line of the instructions file
with open('marsinput.txt') as f:
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

Rover_1=Rover(rover1_position, rover1_direction, instructions_rover1) # Object Rover_1 is created


################## CREATE ROVER 2 WITH INSTRUCTIONS FROM INPUT FILE ##################

rover2= [] # Vector for Rover 2: (x, y, direction)
rover2[:0] = rover_lines[3].split(' ')

rover2_position=np.array([int(rover2[0]),int(rover2[1])]) # (x,y) position (int) of Rover 1
rover2_direction=[rover2[2]] # Direction (str) of Rover 1

instructions_rover2 = []  #Gives a vector of strings with each instruction for Rover 2 as an element
instructions_rover2[:0] = rover_lines[4]

Rover_2=Rover(rover2_position, rover2_direction, instructions_rover2) # Object Rover_2 is created
