#!/bin/bash
# Testing harness for the solver
# Usage: test_solver.sh
rm performance_extended1.txt
# Tests 50 puzzles
for i in {1..50}
do
    echo "Testing puzzle $i"

    python3 ./sud2sat1.py < extended_task1_puzzles/ex_test_puzzle_$i.txt > puzzle.cnf
    
    minisat puzzle.cnf assign.txt > stat.txt

    python3 ./performance.py stat.txt $i >> performance_extended1.txt

done

rm puzzle.cnf
rm stat.txt