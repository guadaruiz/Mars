#from reader import Reader

class Plateau():

    ''' This class can be used to create the plateau on which rovers can move. It takes two inputs as arguments:
    x and y size.'''

    def __init__ (self, x_size, y_size):
        self.x_size = x_size
        self.y_size = y_size

    def show_plateau(self):
        # This function is called in order to show (print) the plateau size.
        dimensions=[self.x_size, self.y_size]
        return print(dimensions)

############################################################################################################

# Test inputs:
#reader=Reader('marsinput.txt')
#plateau=Plateau(reader.get_plateau()[0], reader.get_plateau()[1])

#plateau.show_plateau()
