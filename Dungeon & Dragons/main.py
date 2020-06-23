#-------------------------#
#Dungeon and Dragons
#Author: Albert Bagdasarov
#-------------------------#
import random
import time


def displayIntro():

    print('''You located in the land, dragon of belayed.
in front of you  you could see two caves. In one of them - friendly dragon,
which ready to give you his treasures.IN the second cave - the greedy and hungry dragon who instantly eats you ''')

    print()


def chooseCave():
    cave = ''

    while cave != '1' and cave != '2':

        print("In which cave do you go? (enter 1 or 2)")
        cave = input()

        return cave


def checkCave(chosenCave):
    print("you are getting close to the cave....")

    time.sleep(2)

    print('''her darknes make you tremble with fear...n
                you feel cold.  ''')
    time.sleep(2)

    print(
        "The big dragon jumps, in front of you! He opens his mouth and.....")

    print()
    time.sleep(3)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print("....sharing with you his treasures")
    else:
        print("instantly eat you!")


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'yeah':

    displayIntro()
    caveNumber = chooseCave()

    checkCave(caveNumber)

    print("Try your luck again? (yes or no)")
    playAgain = input()
