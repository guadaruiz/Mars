class Plateau():
    def __init__ (self, x_size, y_size):
        self.x_size= x_size
        self.y_size= y_size

############################################################################################################

################## READ INPUT FILE ##################

rover_lines=[] #Creates an array with each line of the instructions file
with open('rover.txt') as f:
    for line in f:
        rover_lines.append(line.strip())

################## CREATE A PLATEAU FROM INPUT FILE ##################

plateau = []
plateau[:0] = rover_lines[0].split(' ')
Plateau_mars = Plateau(plateau[0],plateau[1])
#print(Plateau_mars.x_size, Plateau_mars.y_size)
