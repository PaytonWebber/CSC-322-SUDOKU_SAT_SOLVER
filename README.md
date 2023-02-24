# CSC-323-SUDOKU_SAT_SOLVER

Names:
Cole Alexander Piche, V00954002
Howie please put your full name student number here
Payton please put your full name and student number here

This submission is a tar file that contains sat2sud.py sat2sud2.py, sat2sud3.py, sud2sat.py, sud2sat2.py, and sud2sat3.py. The code does not produce linux executables. To run them, just have your input in a file (we will assume it is called puzzle.txt for this example) and choose one pair of files to test (we will assume you chose sud2sat.py and sat2sud.py for the example) and run the following commands:

./sud2sat.py <puzzle.txt >puzzle.cnf
minisat puzzle.cnf assign.txt >stat.txt
./sat2sud.py <assign.txt >solution.txt

and the solution will appear in solution.txt, and the runtime stats will appear in stat.txt