#!/usr/bin/python3
# Reads from the stat.txt file and creates a file called performance.txt with the performance data.
# This program is called from test_solver.sh with the following command:
# ./performance.py stat.txt <test number> >> performance.txt

import sys
import os

# Read the stat.txt file
f = open("stat.txt", "r")
lines = f.readlines()
f.close()

# Get the test number
test = sys.argv[2]

print("*********************************** Test " + test + " ***********************************")
print(lines[3].strip())
print(lines[4].strip())
for i in range(14, len(lines)):
    print(lines[i].strip())
print("")
