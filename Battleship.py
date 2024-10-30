import random
x = 0
y = 0
terminate = 0
shotCount = 0

ocean = [[]]

oceanRows = 0
oceanColumns = 0

def createOcean():
    global ocean
    global oceanRows
    global oceanColumns
    oceanRows = int(input("How many rows do you want?"))
    oceanColumns = int(input("How many columns do you want?"))
    ocean = [["O" for _ in range(oceanColumns)] for _ in range(oceanRows)]

def startTurn():
    xGuess = -1
    yGuess = -1
    global shotCount
    for z in range (0, 5):
        print(ocean[z])

    #TESTING PURPOSES
    print(x)
    print(y)
    #TESTING PURPOSES

    while xGuess < 0 or xGuess > oceanRows:
        xGuess = int(input("Please input the x position of where you believe the ship is."))
        if xGuess > oceanRows or xGuess < 0:
            print("Guess is out of bounds, try again")
    while yGuess < 0 or yGuess > oceanColumns:
        yGuess = int(input("Please input the y position of where you believe the ship is."))
        if yGuess > oceanColumns or yGuess < 0:
            print("Guess is out of bounds, try again")

    if x == xGuess and y == yGuess:
        global terminate
        print("You guessed Correctly!")
        terminate = 1
    else:
        print("WRONG! Try again!")
        ocean[xGuess-1][yGuess-1] = "X"
        shotCount +=1
        print("Shot Count:",shotCount)


def hideBoat():
    global x
    global y
    x = random.randint(0,4)
    y = random.randint(0,4)
    #ocean.insert("X", ocean[y,x])

createOcean()
hideBoat()

while terminate == 0:
    startTurn()



