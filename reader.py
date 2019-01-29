import numpy as np

class Reader():

    ''' This class can be used to read different input files (.txt format) and assign each part of the text to
    different parameters of the current problem.'''

    def __init__(self, input):
        self.input = str(input)

    def get_plateau(self):
        # Plateau initializing parameters are called from input file
        plateau= []
        fo = open(str(self.input), "r")
        lines=fo.readlines()
        plateau = lines[0].split(' ')
        plateau[-1]=plateau[-1].rstrip('\n')
        fo.close()
        return plateau

    def get_rover1_pos(self):
        # Rover 1 position initializing parameters are called from input file
        rover1_pos_dir= []
        fo = open(str(self.input), "r")
        lines = fo.readlines()
        rover1_pos_dir = lines[1].split(' ')
        rover1_pos_dir[-1]=rover1_pos_dir[-1].rstrip('\n')
        rover1_position = np.array([int(rover1_pos_dir[0]),int(rover1_pos_dir[1])])
        fo.close()
        return rover1_position

    def get_rover1_dir(self):
        # Rover 1 direction initializing parameters are called from input file
        rover1_pos_dir= []
        fo = open(str(self.input), "r")
        lines = fo.readlines()
        rover1_pos_dir = lines[1].split(' ')
        rover1_pos_dir[-1]=rover1_pos_dir[-1].rstrip('\n')
        rover1_position = rover1_pos_dir[2]
        fo.close()
        return rover1_position

    def get_instructions1(self):
        # Rover 1 instructions are called from input file
        rover1_instructions= []
        fo = open(str(self.input), "r")
        lines = fo.readlines()
        rover1_instructions = lines[2]
        rover1_instructions = list(rover1_instructions.rstrip('\n'))
        fo.close()
        return rover1_instructions

    def get_rover2_pos(self):
        # Rover 2 position initializing parameters are called from input file
        rover2_pos_dir= []
        fo = open(str(self.input), "r")
        lines = fo.readlines()
        rover2_pos_dir = lines[3].split(' ')
        rover2_pos_dir[-1]=rover2_pos_dir[-1].rstrip('\n')
        rover2_position = np.array([int(rover2_pos_dir[0]),int(rover2_pos_dir[1])])
        fo.close()
        return rover2_position

    def get_rover2_dir(self):
        # Rover 2 direction initializing parameters are called from input file
        rover2_pos_dir= []
        fo = open(str(self.input), "r")
        lines = fo.readlines()
        rover2_pos_dir = lines[3].split(' ')
        rover2_pos_dir[-1]=rover2_pos_dir[-1].rstrip('\n')
        rover2_position = rover2_pos_dir[2]
        fo.close()
        return rover2_position

    def get_instructions2(self):
        # Rover 2 instructions are called from input file
        rover2_instructions= []
        fo = open(str(self.input), "r")
        lines = fo.readlines()
        rover2_instructions = lines[4]
        rover2_instructions = list(rover2_instructions.rstrip('\n'))
        fo.close()
        return rover2_instructions

############################################################################################################

# Test inputs:

#reader=Reader('marsinput.txt')

#print(reader.get_plateau())

#print(reader.get_rover1_pos())
#print(reader.get_rover1_dir())
#print(reader.get_instructions1())


#print(reader.get_rover2_pos())
#print(reader.get_rover2_dir())
#print(reader.get_instructions2())
