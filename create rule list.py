import sys

class Clause:
    vars = []
    def __init__(self):
        self.vars = []

    def append(self, var):
        self.vars.append(var)

    def pop(self, i):
        return self.vars.pop(i)

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



#first I generate an empty matrix
matrix = []
for i in range(1, 10):
    matRow = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    matrix.append(matRow)


allClauses = []


##Now I will go generate the clauses
#1
for i in range(1, 10):
    for j in range(1, 10):
        tempClause = Clause()
        for k in range(1, 10):
            #print("i: " + str(i) + " j: " + str(j) + " k: " + str(k))
            var = Variable()
            var.symbol = [i, j, k]
            var.isNegated = False
            tempClause.append(var)
            L = 0

            '''
            while(L < len(tempClause.vars)):
                tempVar = tempClause.vars[L]
                print("symbol: " + str(tempVar.symbol), end = "")
                L = L + 1
            print("")
            '''

            allClauses.append(tempClause)

            '''
            if(j==2 and k ==2):
                exit()
            '''
        

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

#now read the input from stdin
charCount = 0
doneReading = False
for line in sys.stdin:
    tempDigList = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    tempBlankList = ["0", ".", "*", "?"]
    tempLine = line.rstrip()
    #print("stripped: " + tempLine)
    for j in range (0, len(tempLine)):
        tempChar = tempLine[j:j+1:1]
        count = tempDigList.count(tempChar)

        #if the character is not a digit
        if(count == 0):
            count = tempBlankList.count(tempChar)
            #if the character is a blank
            if(count != 0):
                charCount = charCount + 1
                if(charCount==81):
                    doneReading = True
                    #print("doneReading is now true")
            count = 0

        #if the character is a digit
        if(count != 0):
            #print("its a digit")
            #print("the digit is: " + tempChar)
            charCount = charCount + 1

            digVal = tempDigList.index(tempChar)
            digVal = digVal + 1

            #the below code may result in a speedup if it works
            #but it might not, and it doesn't work yet and isn't critical
            '''
            i = 0
            while(i < len(allClauses)):
                tempClause = allClauses[i]
                L = 0
                while(L < len(tempClause.vars)):
                    tempVar = tempClause.vars[L]
                    print("symbol: " + str(tempVar.symbol), end = "")
                    if(tempVar.symbol[2]==digVal):
                        #print("found the digit")
                        if(not var.isNegated):
                            #print("gonna pop i")
                            allClauses.pop(i)
                            i = i - 1
                        else:
                            #print("gonna pop L")
                            allClauses[i].pop(L)
                            L = L - 1

                    L = L + 1
                i = i + 1
                print("")
            '''

            #create a clause with variable to say that the clause containing only the one value must be true
            trueClause = Clause()
            trueVar = Variable()

            trueVar.symbol = [1+((charCount-1)//9), ((charCount - 1)%9)+1, digVal]
            trueVar.isNegated = False

            trueClause.append(trueVar)

            allClauses.append(trueClause)

            #print("tempclause: " + str(tempClause.vars))

        if(charCount==81):
            doneReading = True
            #print("doneReading is now true")

    if(doneReading):
        break            

print("p cnf " + str((9*9*9)) + " " + str(len(allClauses)))
for i in range(0, len(allClauses)):
    tempClause = allClauses[i]
    
    for j in range(0, len(tempClause.vars)):
        tempStart = ""
        tempVar = tempClause.vars[j]
        if(tempVar.isNegated):
            tempStart = "-"
        #print(tempStart + str(tempVar.symbol[0]) + " " + str(tempVar.symbol[1]) + " " + str(tempVar.symbol[2]) + " ", end = " ")
        print(tempStart + str(tempVar.symbol[0]) + str(tempVar.symbol[1]) + str(tempVar.symbol[2]) + " ", end = "")

    print("")