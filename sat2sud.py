#!/usr/bin/python3
import sys

class Table:
     def __init__(self):  
          self.table = []
          for index in range(9):
               self.table.append([0,0,0,0,0,0,0,0,0])

     def insert(self, variable):
          row = 0
          column = 1
          value = 2
          if self.table[variable[row]-1][variable[column]-1] == 0:
               self.table[variable[row]-1][variable[column]-1] = variable[value]

     
def main():
     sys.stdin.readline()
     variable_list = data_parse(sys.stdin.readline())
     solution = Table()
     """
     first digit is row
     second digit is column
     third digit is value
     """
     for variable in variable_list:
          variable = convertbase9(int(variable))
          if int(variable) > 0:
               solution.insert(simplfy_var(str(variable)))
              
     for i in range(9):
          for j in range(9):
               print(solution.table[i][j], end="")
               if (j+1)%3 == 0:
                    print(" ", end="")
          print()
          
def data_parse(line):

     line = line.split()
     line = line[:-1]
     return line

def simplfy_var(data):
     variable = list(data)
     for index, value in enumerate(data):
          variable[index] = int(value)
         
     return variable

def convertbase9(number):
     negative = 1
     number -= 1
     #used for encoding, subtract 1 from decimal and then readd it for position
     if number == 0:
          return 111
     elif number < 0:
          negative = -1
     digits = ""
     number = abs(number)
     while number:
          digits = str(number % 9) + digits
          number //= 9
          
     return (int(digits)+ 111)*negative

#if __name__ == "__main__":
#     main()
main()