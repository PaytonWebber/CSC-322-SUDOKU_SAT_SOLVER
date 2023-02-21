#!/user/bin/env python
import sys
import os #might need these 2, just incase

class Table:
     def __init__(self):  
          self.table = []
          for index in range(9):
               self.table.append([0,0,0,0,0,0,0,0,0])

     def insert(self, variable: list[int]):
          row = 0
          column = 1
          value = 2
          self.table[variable[row]-1][variable[column]-1] = variable[value]
          
     
     
def main(file: str):
     output = open("solution.txt", "w") #replace with a print statment to stdout, just have this incase I Want to test somthing
     variable_list = data_parse("testdoc.txt")
     solution = Table()
     
     """
     first digit is row
     second digit is column
     third digit is value
     """
     for variable in variable_list:
          if int(variable) > 0:
               solution.insert(simplfy_var(str(variable)))
               
     for i in range(9):
          for j in range(9):
               print(solution.table[i][j], end="")
               if (j+1)%3 == 0:
                    print(" ", end="")
          print()
     
     output.close() #remember to remove later
        
    
    
def data_parse(file: str) -> list[str]:
     try:
          solution = open(file, "r")
     except:
          print("somthing went terribly wrong")
          exit(1)
          
     solution.readline()
     assignments = solution.readline()
     
     #spliting up the line, as it should be given as 1 line
     assignments = assignments.split()
     assignments = assignments[:-1]
     solution.close() #closing file
     return assignments

def simplfy_var(data: str) -> list[int]:
     variable = list(data)
     for index, value in enumerate(data):
          variable[index] = int(value)
         
     return variable
        
    
if __name__ == "__main__":
     main(sys.argv[1:] )