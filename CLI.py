import time
import random
from math import sin, cos, radians

def typePause():
    time.sleep(random.randrange(7)/100)

def printSim(string):
    for ele in string:
        print(ele, end="")
        typePause()
    print()

def inputSim(string):
    printSim(string)
    answer = input()
    time.sleep(1)
    if answer == "":
        return inputSim("What was that?")
    return answer.lower()