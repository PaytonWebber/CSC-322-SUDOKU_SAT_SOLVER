#!/usr/bin/python3
import sys
import os

restarts = []
conflicts = []
decisions = []
propagations = []
conflictLiterals = []
memoryUsed = []
cpuTime = []


def readSet(f):
    tempList = f.readline().split()
    if(tempList[0]=="restarts"):
        restarts.append(int(tempList[2]))
        conflicts.append(int(f.readline().split()[2]))
    else:
        restarts.append(0)
        print(tempList)
        conflicts.append(int(tempList[2]))
    
    decisions.append(int(f.readline().split()[2]))

    propagations.append(int(f.readline().split()[2]))

    conflictLiterals.append(int(f.readline().split()[3]))
    memoryUsed.append(float(f.readline().split()[3]))
    cpuTime.append(float(f.readline().split()[3]))

def skipJunk(f):
    for i in range(1,7):
        line = f.readline()

# Read the file
f = open("performance_extended.txt", "r")
for i in range(1, 4):
    line = f.readline()

for count in range(1, 50):
    readSet(f)
    skipJunk(f)

readSet(f)

print("length: " + str(len(restarts)))
print("the maximum number of decisions needed was: " + str(max(decisions)))
print("the maximum number of propagations needed was: " + str(max(propagations)))
print("the maximum number of megabytes of memory used was: " + str(max(memoryUsed)))
print("the maximum amount of cpu time used (in seconds) was: " + str(max(cpuTime)))
print("the maximum number of conflicts was: " + str(max(conflicts)))
print("the maximum number of conflictLiterals was: " + str(max(conflictLiterals)))
print()
print("the ave number of decisions needed was: " + str(sum(decisions)/len(decisions)))
print("the ave number of propagations needed was: " + str(sum(propagations)/len(propagations)))
print("the ave number of megabytes of memory used was: " + str(sum(memoryUsed)/len(memoryUsed)))
print("the ave amount of cpu time used (in seconds) was: " + str(sum(cpuTime)/len(cpuTime)))
print("the ave amount of conflicts was: " + str(sum(conflicts)/len(conflicts)))
print("the ave amount of conflictLiterals was: " + str(sum(conflictLiterals)/len(conflictLiterals)))