#!/usr/bin/python3
import sys

# This program takes in a file that contains one or more unsolved, 9x9 sudoku puzzles.
# It then converts the sudoku puzzles into a DIMACS file that can be solved by minisat.
# The output is to STDOUT.

# This class represents a variable in the DIMACS file.
# A variable is a 3-tuple of integers: (row, column, value)
class Variable:
    symbol = []
    isNegated = False
    def __init__(self, sym, isNo):
        self.symbol = sym
        self.isNegated = isNo

# This class represents a clause in the DIMACS file.
class Clause:
    vars = []
    def __init__(self):
        self.vars = []

    def append(self, var):
        self.vars.append(var)

    def pop(self, i):
        return self.vars.pop(i)
    
# This function takes in a list of clauses and prints them to STDOUT in DIMACS format.
def printClauses(clauses):
    # Print the number of clauses
    print("p cnf 999 " + str(len(clauses)))
    # Print each clause
    for clause in clauses:
        for var in clause.vars:
            # If the variable is negated, print a negative sign
            if var.isNegated:
                print("-", end = "")
            # Print the variable
            print(str(var.symbol[0]) + str(var.symbol[1]) + str(var.symbol[2]), end = " ")
        # Print a 0 to indicate the end of the clause
        print("0")

# Create an empty list of clauses
allClauses = []


'''
# Create a list of clauses that represent the rule that each cell must have a value
for i in range(1, 10):
    for j in range(1, 10):
        # Create a new clause
        tempClause = Clause()
        # For each value that can be placed in the cell
        for k in range(1, 10):
            # Create a variable representing the cell having that value
            var = Variable([i, j, k], False)
            # Add the variable to the clause
            tempClause.append(var)
        # Add the clause to the list of all clauses
        allClauses.append(tempClause)

# Create a list of clauses that represent the rule that each cell can only have one value
for i in range(1, 10):
    for j in range(1, 10):
        # For each value that can be placed in the cell
        for k in range(1, 10):
            # Create a new clause
            tempClause = Clause()
            # For each value that can be placed in the cell
            for l in range(1, 10):
                # If the two values are the same, skip this iteration
                if k == l:
                    continue
                # Create a variable representing the cell not having the value
                var = Variable([i, j, l], True)
                # Add the variable to the clause
                tempClause.append(var)
            # Add the clause to the list of all clauses
            allClauses.append(tempClause)

# Create a list of clauses that represent the rule that each row can only have one of each value
for i in range(1, 10):
    # For each value that can be placed in the cell
    for k in range(1, 10):
        # Create a new clause
        tempClause = Clause()
        # For each cell in the row
        for j in range(1, 10):
            # Create a variable representing the cell having the value
            var = Variable([i, j, k], False)
            # Add the variable to the clause
            tempClause.append(var)
        # Add the clause to the list of all clauses
        allClauses.append(tempClause)

# Create a list of clauses that represent the rule that each column can only have one of each value
for j in range(1, 10):
    # For each value that can be placed in the cell
    for k in range(1, 10):
        # Create a new clause
        tempClause = Clause()
        # For each cell in the column
        for i in range(1, 10):
            # Create a variable representing the cell having the value
            var = Variable([i, j, k], False)
            # Add the variable to the clause
            tempClause.append(var)
        # Add the clause to the list of all clauses
        allClauses.append(tempClause)

# Create a list of clauses that represent the rule that each 3x3 box can only have one of each value
for i in range(1, 10, 3):
    for j in range(1, 10, 3):
        # For each value that can be placed in the cell
        for k in range(1, 10):
            # Create a new clause
            tempClause = Clause()
            # For each cell in the box
            for m in range(0, 3):
                for n in range(0, 3):
                    # Create a variable representing the cell having the value
                    var = Variable([i + m, j + n, k], False)
                    # Add the variable to the clause
                    tempClause.append(var)
            # Add the clause to the list of all clauses
            allClauses.append(tempClause)
'''

##Now I will go generate the clauses
#1
for i in range(1, 10):
    for j in range(1, 10):
        tempClause = Clause()
        for k in range(1, 10):
            var = Variable()
            var.symbol = [i, j, k]
            var.isNegated = False
            tempClause.append(var)
            L = 0
            allClauses.append(tempClause)

        

#2
for i in range(1, 10):
    for k in range(1, 10):
            for j in range(1, 9):
                for L in range(j+1, 10):
                    tempClause = Clause()
                    var = Variable()
                    var.symbol = [i, j, k]
                    var.isNegated = True
                    tempClause.append(var)
                    
                    var2 = Variable()
                    var2.symbol = [i, L, k]
                    var2.isNegated = True
                    tempClause.append(var2)
                    allClauses.append(tempClause)


#3
for j in range(1, 10):
    for k in range(1, 10):
        for i in range(1, 8):
            for L in range(i+1, 10):
                tempClause = Clause()
                var = Variable()
                var.symbol = [i, j, k]
                var.isNegated = True
                tempClause.append(var)
                
                var2 = Variable()
                var2.symbol = [L, j, k]
                var2.isNegated = True
                tempClause.append(var2)
                allClauses.append(tempClause)
            
#4
for k in range(1, 10):
    for a in range(0, 3):
        for b in range(0, 3):
            for u in range(1,4):
                for v in range(1, 3):
                    for w in range(v+1, 4):
                        tempClause = Clause()
                        var = Variable()
                        var.symbol = [3*a + u, 3*b + v, k]
                        var.isNegated = True
                        tempClause.append(var)
                        
                        var2 = Variable()
                        var2.symbol = [3*a + u, 3*b + w, k]
                        var2.isNegated = True
                        tempClause.append(var2)
                        allClauses.append(tempClause)

#5
for k in range(1, 10):
    for a in range(0, 3):
        for b in range(0, 3):
            for u in range(1,3):
                for v in range(1, 4):
                    for w in range(v+1, 4):
                        for t in range(1, 4):
                            tempClause = Clause()
                            var = Variable()
                            var.symbol = [3*a + u, 3*b + v, k]
                            var.isNegated = True
                            tempClause.append(var)
                            
                            var2 = Variable()
                            var2.symbol = [3*a + w, 3*b + t, k]
                            var2.isNegated = True
                            tempClause.append(var2)
                            allClauses.append(tempClause)

# Read in the sudoku puzzle from the input file.
# The puzzle is in the format of a 9x9 grid of integers, or one line.
# A 0, ., *, or ? represents an empty cell.
# Any other character is ignored.
# The input file is read from STDIN.

# Read in the first line of the input file
line = sys.stdin.readline()
# While there are still lines to read
while line:
    # For each character in the line
    for i in range(0, len(line)):
        # If the character is a digit
        if line[i].isdigit() and int(line[i]) != 0:
            # Create a new clause
            tempClause = Clause()
            # Create a variable representing the cell having the value
            var = Variable([int(i / 9) + 1, i % 9 + 1, int(line[i])], False)
            # Add the variable to the clause
            tempClause.append(var)
            # Add the clause to the list of all clauses
            allClauses.append(tempClause)
    # Read in the next line of the input file
    line = sys.stdin.readline()

# Print the list of clauses to STDOUT in DIMACS format
printClauses(allClauses)
