#!/bin/bash

# loop through extended_task1.txt and make a ex_test_puzzle_XX.txt file for each puzzle
# where XX is the puzzle number
# The puzzles are in the format of a single line of 81 characters

# Keep a line counter
line_num=0

# open the .txt file with the sudoku puzzles
file=$(cat extended_task1.txt)

# loop through the each line of file
for line in $file
do
    # increment the line counter
    line_num=$((line_num+1))
    # create a file with the puzzle in the format of a single line of 81 characters
    echo $line > ex_test_puzzle_$line_num.txt
done
