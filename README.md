# Game-Playing-Problem
CSE  5360 : Artificial Intelligence

Developed a Python program named red_blue_nim, allowing users to play two versions (standard and misére) of a Nim variant against a computer opponent. Implemented command line invocation with options for the number of red and blue marbles, game version (standard or misére), starting player (computer or human), and optional depth for MinMax search.Developed a Python program named red_blue_nim, allowing users to play two versions (standard and misére) of a Nim variant against a computer opponent. Implemented command line invocation with options for the number of red and blue marbles, game version (standard or misére), starting player (computer or human), and optional depth for MinMax search.
Skills: Algorithms · Artificial Intelligence (AI) · Problem Solving · Algorithm · Python (Programming Language)

What programming language is used for this task:python

How the code is structured:
Python program for playing a game known as "Red-Blue Nim" in both misère and standard versions using the minimax algorithm for making computer-based moves. The program allows the user to play against the computer and human

Here's a breakdown of the key components of the code:

1.Import Statements:
-->sys is used to access command-line arguments, and 

2.EvaFun Function:
-->This function evaluates the current state of the game. It takes a state s as input, where s is a list with two elements representing the number of red and blue stones in the game.
-->It calculates a score based on the number of red and blue stones and returns it. The score is determined by subtracting twice the number of red stones from three times the number of blue stones.

3.MinMaxmisere Function:
-->This function implements the minimax algorithm for the misère version of Red-Blue Nim.
-->It takes several arguments, including the current state s, the current depth d, and alpha-beta pruning parameters a and b.
-->It uses recursion to explore possible moves in the game tree, prioritizing red moves over blue. It returns the best value found in the search.

4.RedBlueNim_misere Function:
-->This function allows playing a game of Red-Blue Nim in the misère version.
-->It takes the initial numbers of red and blue stones, the first player's choice (human or computer), and a depth parameter.
-->It iteratively prompts the players for their moves and uses the minimax algorithm to make the computer's moves.
-->The game continues until there are no more valid moves, and it prints the final score and the winner.

5.MinMaxstandard Function:
-->This function implements the minimax algorithm for the standard version of Red-Blue Nim, where blue moves are prioritized over red.
-->Similar to MinMaxmisere, it takes arguments like the current state, depth, and alpha-beta pruning parameters.

6.RedBlueNim_standard Function:
-->This function allows playing a game of Red-Blue Nim in the standard version.
-->It follows a similar structure to RedBlueNim_misere but uses the MinMaxstandard function for computer moves.

7.main Function:
-->This is the main entry point of the program.
-->It reads command-line arguments to determine the initial state, version (misère or standard), first player, and depth.
-->Depending on the version specified, it calls the appropriate function to start the game.

8.Execution of the Game:
-->The program starts by calling the main function, which reads the command-line arguments and launches the game accordingly.

How to run the code:
1. open visual studio.
2. unzip the folder
3. open the command prompt with correct path where file exists
4. run the command 
	"python red_blue_nim.py 2 3 standard human 3" for standard version and human as first player
	"python red_blue_nim.py 2 3 misere human 2" for misere version and human as first player
	"python red_blue_nim.py 2 3 standard computer 3" for standard version and computer as first player
	"python red_blue_nim.py 2 3 misere computer 3" for misere version and computer as first player
