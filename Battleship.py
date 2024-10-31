import random
x1 = 0
y1 = 0
x2 = 0
y2 = 0
terminate = 0
shotCount = 0

ocean = [[]]

oceanRC = 0
totalShips = 2
shipsHit = 0

def createOcean():
    global ocean
    global oceanRC
    oceanRC = int(input("How many rows and columns do you want?"))
    #oceanColumns = int(input("How many columns do you want?"))
     #Sadly I had to comment out this an give the user only 1 input due to step 12b, as after asking the teacher the user
    #Is only supposed to have one input for rows and columns.

    ocean = [["O" for _ in range(oceanRC)] for _ in range(oceanRC)]

def startTurn():
    xGuess = -1
    yGuess = -1
    global shotCount
    for z in range (0, oceanRC):
        print(ocean[z])

    #TESTING PURPOSES
    print(x1)
    print(y1)
    print(x2)
    print(y2)
    #TESTING PURPOSES

    while xGuess < 0 or xGuess > oceanRC:
        xGuess = int(input("Please input the x position of where you believe the ship is."))
        if xGuess > oceanRC or xGuess < 1:
            print("Guess is out of bounds, try again")
    while yGuess < 0 or yGuess > oceanRC:
        yGuess = int(input("Please input the y position of where you believe the ship is."))
        if yGuess > oceanRC or yGuess < 1:
            print("Guess is out of bounds, try again")

    if x1 == xGuess and y1 == yGuess or x2 == xGuess and y2 == yGuess:
        global terminate
        global shipsHit
        global totalShips
        shipsHit += 1
        print("You guessed Correctly!")
        print("Shot Count:",shotCount)
        print("Ships Hit:",shipsHit)
        if totalShips == shipsHit:
            print("You Win!!")
            terminate = 1

    else:
        print("WRONG! Try again!")
        ocean[yGuess-1][xGuess-1] = "X"
        shotCount +=1
        print("Shot Count:",shotCount)
        print("Ships Hit:",shipsHit)
        if shotCount == oceanRC + totalShips:
            print("You guessed too many times. You lose!")
            terminate = 1


def hideBoat():
    global x1
    global y1
    global x2
    global y2
    x1 = random.randint(1,oceanRC)
    y1 = random.randint(1,oceanRC)
    x2 = random.randint(1,oceanRC)
    y2 = random.randint(1,oceanRC)
    #ocean.insert("X", ocean[y,x])

createOcean()
hideBoat()

while terminate == 0:
    startTurn()



