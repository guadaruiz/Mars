import numpy as np
from plateau import Plateau
from rover import Rover

rover_lines=[] #Creates an array with each line of the instructions file
with open('rover.txt') as f:
    for line in f:
        rover_lines.append(line.strip())
#print(rover_lines)
#print(rover_lines[0])

#### GET THE SIZE OF PLATEAU FROM INPUT FILE AND PUT IT IN A LIST ####

plateau = []
plateau[:0] = rover_lines[0].split(' ')
Plateau_mars = Plateau(plateau[0],plateau[1])
#### GET the INITIAL POSITION and DIRECTION OF ROVERS from input files and put THEM in vectors ####


rover1 = [] # Vector for Rover 1: (x, y, direction)
rover1[:0] = rover_lines[1].split(' ')

rover1_position = np.array([int(rover1[0]),int(rover1[1])]) # (x,y) position (int) of Rover 1
rover1_direction=[rover1[2]] # Direction (str) of Rover 1

instructions_rover1 = [] #Gives a vector of strings with each instruction for Rover 1 as an element
instructions_rover1[:0] = rover_lines[2]

rover2= [] # Vector for Rover 2: (x, y, direction)
rover2[:0] = rover_lines[3].split(' ')

rover2_position=np.array([int(rover2[0]),int(rover2[1])]) # (x,y) position (int) of Rover 1
rover2_direction=[rover2[2]] # Direction (str) of Rover 1

instructions_rover2 = []  #Gives a vector of strings with each instruction for Rover 2 as an element
instructions_rover2[:0] = rover_lines[4]

Rover_1=Rover(rover1_position, rover1_direction, instructions_rover1)
Rover_2=Rover(rover2_position, rover2_direction, instructions_rover2)


Rover_1.move()
Rover_2.move()
