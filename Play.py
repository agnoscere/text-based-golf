import time
import random
from math import sin, cos, radians


#******************************
# Functions
#******************************

def calculateDistance(velocityInitial, angle):
    velocityX = velocityInitial * cos(radians(angle))
    time = 2 * velocityInitial * sin(radians(angle)) / 9.8
    return velocityX * time


def typePause():
    time.sleep(random.randrange(7)/100)

def print2(string):
    for ele in string:
        print(ele, end="")
        typePause()
    print()

def input2(string):
    print2(string)
    answer = input()
    time.sleep(1)
    if answer == "":
        return input2("What was that?")
    return answer.lower()


#******************************
# Lists of potential common inputs
#******************************

yesList = ["yes", "definitely", "ya", "yea", "yeah", "sure", "ok", "yep", "yup", "of course", "i do", "i would", "more"]
noList = ["no", "neg", "n't", "nah", "nt"]


#******************************
# THE GAME
#******************************

answer = input2("Are you left-handed or right-handed?")
if "right" in answer:
    rightHanded = True
elif "left" in answer:
    rightHanded = False
else:
    rightHanded = True
    print2("Well, most people are right-handed. Let's assume you're right handed hmm?")
    #this could interrupt people if they take longer than like a second

print2("You square up to the ball.")

answer = input2("Do you want to take a practice swing?")
while (not any(ele in answer for ele in noList)) and (any(ele in answer for ele in yesList)):
    #if count = 5, 10, etc.
    #if everyone else is ready 
    print2("You take a practice swing.")
    answer = input2("Do you want to take another practice swing?")

angleZ = 0
angleZModifier = 0
answer = input2("Do you want to angle your hips to the left, to the right, or not at all?")
if ("left" in answer and rightHanded) or ("right" in answer and not rightHanded):
    angleZModifier = -1
    angleZ = input2("How much?")
    while not angleZ.isdecimal():
        angleZ = input2("How about we represent that in, like, a plain-old number for now?")
elif ("right" in answer and rightHanded) or ("left" in answer and not rightHanded):
    angleZModifier = 1
    angleZ = input2("How much?")
    while not angleZ.isdecimal():
        angleZ = input2("How about we represent that in, like, a plain-old number for now?")
angleZ = int(angleZ) * angleZModifier

angleY = input2("What angle are we trying to get on the ball?")
while not angleY.isdecimal():
        angleY = input2("How about we represent that in, like, a plain-old number for now?")

power = input2("Finally, how hard do you want to hit it?")
while not power.isdecimal():
    power = input2("How about we represent that in, like, a plain-old number for now?")
#Alternatively, ask the user if the ball is still going up at various points. Could even time it! 


print2("Alright. Here goes.")
time.sleep(2)
print2("SWINGING!!!!!!!!!!!!!!!!!!!!!!!")
time.sleep(1)
print2(".........")
time.sleep(1)
print2("...")
time.sleep(3)

distance = calculateDistance(int(power), int(angleY))

print2("You hit it " + str(distance) + " meters, yards, or whatever down the fairway!")
time.sleep(1)
print2("I think it's called the fairway at least!")