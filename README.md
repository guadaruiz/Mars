# Mars_Git

** Version 1.0.0 **
Programming language version used: Python 3.7.0 \\
Python unit testing framework used: pytest \\

1. PROBLEM DESCRIPTION:

A squad of robotic rovers are to be landed by NASA on a plateau on Mars. This plateau, which is curiously rectangular, must be navigated by the rovers so that their on-board cameras can get a complete view of the surrounding terrain to send back to Earth.

A rover’s position and location is represented by a combination of x and y co-ordinates and a letter representing one of the four cardinal compass points. The plateau is divided up into a grid to simplify navigation. An example position might be 0, 0, N, which means the rover is in the bottom left corner and facing North.

In order to control a rover, NASA sends a simple string of letters. The possible letters are ‘L’, ‘R’ and ‘M’. ‘L’ and ‘R’ makes the rover spin 90 degrees left or right respectively, without moving from its current spot. ‘M’ means move forward one grid point, and maintain the same heading.

Assume that the square directly North from (x, y) is (x, y+1).

2. a. PROGRAM GENERAL IDEA:

Two type of classes were created in order to tackle this problem: plateau.py and rover.py. The former is used to create a plateau with the input dimensions, and the latter to create 2 rovers with the input data.

The rover.py file includes a move() function inside the Rover class, which reads from the input file the initial position and initial direction of the rover and moves it according to its instructions.

In mars_main the two rovers created in rover.py are called and the sequential instructions are followed by using the move() function in each case.

plateau.py is not currently used by the main program since for the provided input data, the rovers do not exceed the plateau dimensions when moving. Nevertheless, in order to make it more general, an error message should be included in a future version when final position gets out of range.

Finally, a test file is included (test_rover.py) which runs some test to check the functions defined in the rover.py file.

2. b. FILE STRUCTURE:

The folder consists of the following files:

    1. mars_main.py : Main file for executing the program. Calls plateau.py in order to create 2 rovers and move them according to instructions from input file.
    2. plateau.py : Class Plateau file. Plateau can be initialized with input file data by calling plateau.py.
    3. rover.py : Class Plateau file. Plateau can be initialized with input file data by calling rover.py.
    4. marsinput.txt : input file.
    5. test_rover.py : Python unit testing file (run with pytest). A rober used for testing purposes (Object Rover_test) is created and 3 test functions can be run with it in the rover.py file.
    6. README.md : The current readme file.

3. a. INPUT:

Input file 'marsinput.txt' needs to be placed in the same folder as the rest of the files. Name (or path, if needed) of this file is specified in rover.py after defining class rover (line 50) and in plateau.py after defining class plateau (line 11).

Input should be written in the following manner:
The first line is upper-right coordinates of the plateau, the lowerleft coordinates are assumed to be 0,0.
The rest of the input is information pertaining to the rovers that have been deployed. Each rover has two lines of input. The first line gives the rover’s position, and the second line is a series of instructions telling the rover how to explore the plateau.
The position is made up of two integers and a letter separated by spaces, corresponding to the x and y co-ordinates and the rover’s orientation.
Each rover will be finished sequentially, which means that the second rover won’t start to move until the first one has finished moving.

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

4. HOW TO RUN THE CODE:

4. a. RUNNING THE CODE:

Simply execute in the folder containing all files the command line:

python main_main.py

The output shown in the example (section 3.c of this README) should be displayed in the terminal.

4. b. RUNNING TESTS:

Three test functions can be executed from the test_rover.py file. In order to do so, go to the containing folder in the terminal and run the following command line:

pytest test_rover.py

All tests should be run and passed as is.
