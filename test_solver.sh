# Testing harness for the solver
# Usage: test_solver.sh <testfile>
# <testfile> is a file containing one or more 9x9 sudoku puzzles

# Calls sud2sat.py to convert the puzzle to a DIMACS file
# Calls minisat to solve the puzzle
# Determines performance of the solver from the output of minisat
# Calls sat2sud.py to convert the solution to a sudoku puzzle

# The output of this script is a file called performance.txt that
# contains the performance of the solver for each puzzle in the
# test file.


# Check for the correct number of arguments
if [ $# -ne 1 ]; then
    echo "Usage: test_solver.sh <testfile>"
    exit 1
fi

# Check that the test file exists
if [ ! -f $1 ]; then
    echo "Error: $1 does not exist"
    exit 1
fi

# Call sud2sat.py to convert the puzzle to a DIMACS file
./sud2sat.py $1 > puzzle.cnf

# Check that stat.txt does not exist
if [ -f stat.txt ]; then
    rm stat.txt
fi

# Call minisat to solve the puzzle
minisat puzzle.cnf assign.txt > stat.txt

# Determine performance of the solver from the output of minisat
# The number of conflicts is the second line of stat.txt
# The number of decisions is the third line of stat.txt
# The number of propagations is the fourth line of stat.txt
# The number of learned clauses is the fifth line of stat.txt
# The number of deleted clauses is the sixth line of stat.txt
# The number of restarts is the seventh line of stat.txt
# The number of CPU time is the eighth line of stat.txt

./performance.py stat.txt $1 >> performance.txt

# Call sat2sud.py to convert the solution to a sudoku puzzle
./sat2sud.py assign.txt > solution.txt