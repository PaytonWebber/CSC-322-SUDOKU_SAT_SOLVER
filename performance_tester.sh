#!/usr/bin/bash
# Testing harness for the solver
# Usage: test_solver.sh

# Tests 50 puzzles
for i in {01..50}
do
    echo "Testing puzzle $i"

    ./sud2sat.py < test_puzzles/test_puzzle_$i.txt > puzzle.cnf
    
    minisat puzzle.cnf > stat.txt

    ./performance.py stat.txt $i >> performance_minimal.txt

done

rm puzzle.cnf
rm stat.txt