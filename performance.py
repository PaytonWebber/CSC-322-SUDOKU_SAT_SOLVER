# Reads from the stat.txt file and creates a file called performance.txt with the performance data.
# This program is called from test_solver.sh with the following command:
# ./performance.py stat.txt <test_filename.txt> >> performance.txt

import sys
import os

# Read the stat.txt file
f = open("stat.txt", "r")
lines = f.readlines()
f.close()

# Get the test filename
test_filename = sys.argv[1]

# Create the performance.txt file if it does not exist
# If it exists, read the file and append the performance data to the end of the file
if os.path.isfile("performance.txt"):
    f = open("performance.txt", "a")
    f.write("\n")
else:
    f = open("performance.txt", "w")

# Write the header for the performance data
f.write("Performance for test: " + test_filename + "\n")
# Write the data
# The number of conflicts is the second line of stat.txt
# The number of decisions is the third line of stat.txt
# The number of propagations is the fourth line of stat.txt
# The number of learned clauses is the fifth line of stat.txt
# The number of deleted clauses is the sixth line of stat.txt
# The number of restarts is the seventh line of stat.txt
# The number of CPU time is the eighth line of stat.txt
f.write("Number of conflicts: " + lines[1])
f.write("Number of decisions: " + lines[2])
f.write("Number of propagations: " + lines[3])
f.write("Number of learned clauses: " + lines[4])
f.write("Number of deleted clauses: " + lines[5])
f.write("Number of restarts: " + lines[6])
f.write("Number of CPU time: " + lines[7])
