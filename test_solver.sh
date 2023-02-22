#!/bin/bash
for i in {01..50}; do
    echo "Running test $i"

    ./sud2sat.py < test_puzzles/test_puzzle_$i.txt > temp.cnf
    echo "******************************* Test $i ********************************" >> result.txt
    minisat temp.cnf >> result.txt

done
