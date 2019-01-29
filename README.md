# Mars_Git

** Version 1.0.0 **
    Programming language version used: Python 3.7.0  
    Python unit testing framework used: pytest  

1. PROBLEM DESCRIPTION:

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

2. a. PROGRAM GENERAL IDEA:

Three type classes were created in order to tackle this problem: reader.py, plateau.py and rover.py.

    Reader() class: reads an input file and assigns to different variables information from the input text.

    Plateau() class: can be used to create a plateau with the input dimensions. It includes a function to show dimensions.

    Rover() class: can be used to create rover objects, taking as input a vector of initial position, a pointing direction represented by a cardinal letter string (N, S, W or E), and a set of movement instructions indicated with the letters L, R and M. This class includes a move() function which reads from the input file the initial position and initial direction of the rover and moves it according to its instructions.

The main scrip of this program is the mars_main.py file. It takes the input data, creates 2 rovers, and performs the input instructions in each one. When executed, the program returns the final position of Rover 1 and its direction in the first line, and the same values for Rover 2 in the second line.

Remark:
plateau.py is not currently used by the main program since for the provided input data, the rovers do not exceed the plateau dimensions when moving. Nevertheless, in order to make it more general, an error message should be included in a future version when final position gets out of range.

Finally, a test file is included (test_rover.py) which runs some tests to check the functions defined in the rover.py file (run with pytest). A rober created for testing purposes (Object Rover_test) is created and 3 test functions can be run with it in the rover.py file.

2. b. FILE STRUCTURE:

The folder consists of the following files:

    1. mars_main.py : Main file for executing the program
    2. reader.py : Class Reader file
    2. plateau.py : Class Plateau file
    3. rover.py : Class Rover file
    4. marsinput.txt : input file
    5. test_rover.py : Python unit testing file
    6. README.md : The current readme file.

3. a. INPUT:

Input file 'marsinput.txt' needs to be placed in the same folder as the rest of the files. The name of this file is specified in mars_main.py after comments (line 24).

Input file should be written in the following manner:

    Line 1: x and y dimensions of plateau separated by a space.
    Line 2: Position and direction on Rover 1. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation.
    Line 3: Set of instructions for Rover 1. This is indicated with a string of letters L, R and M (no spaces).
    Line 4: Position and direction on Rover 2. The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation.
    Line 5: Set of instructions for Rover 2. This is indicated with a string of letters L, R and M (no spaces).

3. b. OUTPUT:

The output for each rover should be its final co-ordinates and heading indicated by the cardinal point letter.

3. c. EXAMPLE OF INPUT AND OUTPUT:

    Input:

    5 5  
    1 2 N  
    LMLMLMLMM  
    3 3 E  
    MMRMMRMRRM  

    Output:  

    [1 3] N  
    [5 1] E  


4. a. RUNNING THE CODE:

Simply execute in the folder containing all files the command line:

python main_main.py

The output shown in the example (section 3.c of this README) should be displayed in the terminal.

4. b. RUNNING TESTS:

Three test functions can be executed from the test_rover.py file. In order to do so, go to the containing folder in the terminal and run the following command line:

pytest test_rover.py

All tests should be run and passed as is.
