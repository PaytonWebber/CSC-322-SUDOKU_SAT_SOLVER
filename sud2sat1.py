#!/usr//bin/python3
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
    def __init__(self):
        self.symbol = []
        self.isNegated = False
        junk = 0

# This class represents a clause in the DIMACS file.
class Clause:
    vars = []
    def __init__(self):
        self.vars = []

    def append(self, var):
        self.vars.append(var)

    def pop(self, i):
        return self.vars.pop(i)
    
# convert from our current encoding to the encoding to have the min possible num variables
def returnMinEncoding(i, j, k):
    decVal =(81 * (i-1)) + (9*(j-1)) + (k-1) + 1
    newK = decVal % 10
    devVal = decVal - newK
    newJ = (decVal % 100)//10
    decVal = devVal - (newJ*10)
    newI = decVal//100
    minEnc = [newI, newJ, newK]
    return minEnc

# This function takes in a list of clauses and prints them to STDOUT in DIMACS format.
def printClauses(clauses):
    # Print the number of clauses
    print("p cnf 729 " + str(len(clauses)))
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

# Now I will go generate the clauses
#1 ensure every cell contains at least one number
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

#2 ensure every number appears at most once in every row
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
                    
#3 ensure every number appears at most once in every column
for j in range(1, 10):
    for k in range(1, 10):
        for i in range(1, 9):
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

#4 perform the first part of ensuring that each number appears at most once in every subgrid
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

#5 perform the second part of ensuring that each number appears at most once in every subgrid
for k in range(1, 10):
    for a in range(0, 3):
        for b in range(0, 3):
            for u in range(1,3):
                for v in range(1, 4):
                    for w in range(u+1, 4):
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
charCount = 0
for line in sys.stdin:
    line.rstrip()
    for char in line:
        charCount += 1
        # Exits loop if all 81 positons on the puzzle have been determined
        if charCount >= 81: break
        # Checks if current character is an empty cell
        if not char.isdigit() or int(char) == 0: continue

        tempClause = Clause()
        tempVar = Variable()
        tempVar.symbol = [1+((charCount-1)//9), ((charCount - 1)%9)+1, int(char)]
        tempVar.isNegated = False
        tempClause.append(tempVar)
        allClauses.append(tempClause)

        # Exits loop if all 81 positons on the puzzle have been determined
# now change all the encodings to be how the solver probably wants them
# Print each clause
for clause in allClauses:
    for var in clause.vars:
        minEnc = returnMinEncoding(var.symbol[0], var.symbol[1], var.symbol[2])
        var.symbol = minEnc

# Print the list of clauses to STDOUT in DIMACS format
printClauses(allClauses)
