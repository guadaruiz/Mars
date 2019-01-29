#from plateau import Plateau
from rover import Rover
from reader import Reader

''' This is the main file of the Mars Rover program. It takes the input data, creates 2 rovers, and performs
    the input instructions in each one. When executed, the program returns the final position of Rover 1 and
    its direction in the first line, and the same values for Rover 2 in the second line.

    The script in this file is presently divided in 4 main sections:

    1. Reading Input data
    2. Creating and moving object Rover 1
    3. Creating and moving object Rover 2
    4. Creating and showing plateau size (not executed since it is not necessary with current instructions.)

    This program was created using Python 3.7.0 and can be run in the terminal by typing:

    python mars_main
 '''

######################## INPUT FILE ########################
#Reader class gets called and reader1 object is initialized with input file.

reader=Reader('marsinput.txt')

######################## ROVER 1 ########################
# Rover class gets called to create a rover object. This is done with the data of rover1 from reader.

# Create Rover 1 object with input data:
Rover1=Rover(reader.get_rover1_pos(), reader.get_rover1_dir(), reader.get_instructions1())

# Move Rover 1 according to input instructions:
Rover1.move()

######################## ROVER 2 ########################
# Rover class gets called to create a rover object. This is done with the data of rover2 from reader.

# Create Rover 2 object with input data:
Rover2=Rover(reader.get_rover2_pos(), reader.get_rover2_dir(), reader.get_instructions2())

# Move Rover 2 according to input instructions:
Rover2.move()

######################## PLATEAU ########################

# Create plateau object with input data:
#plateau=Plateau(reader.get_plateau()[0], reader.get_plateau()[1])

# Show plateau dimensions with input data:
#plateau.show_plateau()
