import time
import random
from math import sin, cos, radians
from CLI import *


#******************************
# Functions
#******************************

def calculateDistance(velocityInitial, angle):
    velocityX = velocityInitial * cos(radians(angle))
    time = 2 * velocityInitial * sin(radians(angle)) / 9.8
    return velocityX * time


#******************************
# Lists of potential common inputs
#******************************

yesList = ["yes", "definitely", "ya", "yea", "yeah", "sure", "ok", "yep", "yup", "of course", "i do", "i would", "more"]
noList = ["no", "neg", "n't", "nah", "nt"]


#******************************
# THE GAME
#******************************

answer = inputSim("Are you left-handed or right-handed?")
if "right" in answer:
    rightHanded = True
elif "left" in answer:
    rightHanded = False
else:
    rightHanded = True
    printSim("Well, most people are right-handed. Let's assume you're right handed hmm?")
    #this could interrupt people if they take longer than like a second

printSim("You square up to the ball.")

answer = inputSim("Do you want to take a practice swing?")
while (not any(ele in answer for ele in noList)) and (any(ele in answer for ele in yesList)):
    #if count = 5, 10, etc.
    #if everyone else is ready 
    printSim("You take a practice swing.")
    answer = inputSim("Do you want to take another practice swing?")

angleZ = 0
angleZModifier = 0
answer = inputSim("Do you want to angle your hips to the left, to the right, or not at all?")
if ("left" in answer and rightHanded) or ("right" in answer and not rightHanded):
    angleZModifier = -1
    angleZ = inputSim("How much?")
    while not angleZ.isdecimal():
        angleZ = inputSim("How about we represent that in, like, a plain-old number for now?")
elif ("right" in answer and rightHanded) or ("left" in answer and not rightHanded):
    angleZModifier = 1
    angleZ = inputSim("How much?")
    while not angleZ.isdecimal():
        angleZ = inputSim("How about we represent that in, like, a plain-old number for now?")
angleZ = int(angleZ) * angleZModifier

angleY = inputSim("What angle are we trying to get on the ball?")
while not angleY.isdecimal():
        angleY = inputSim("How about we represent that in, like, a plain-old number for now?")

power = inputSim("Finally, how hard do you want to hit it?")
while not power.isdecimal():
    power = inputSim("How about we represent that in, like, a plain-old number for now?")
#Alternatively, ask the user if the ball is still going up at various points. Could even time it! 


printSim("Alright. Here goes.")
time.sleep(2)
printSim("SWINGING!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(1)
printSim(".........")
time.sleep(1)
printSim("...")
time.sleep(3)

distance = calculateDistance(int(power), int(angleY))

printSim("You hit it " + str(distance) + " meters, yards, or whatever down the fairway!")
time.sleep(1)
printSim("I think it's called the fairway at least!")