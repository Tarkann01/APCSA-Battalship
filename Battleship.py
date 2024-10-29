import random
x = 0
y = 0
terminate = 0
shotCount = 0
ocean = [[]]

def createOcean():
    global ocean
    rows = int(input("How many rows do you want?"))
    columns = int(input("How many columns do you want?"))
    ocean = [["O" for _ in range(columns)] for _ in range(rows)]


def startTurn():
    global shotCount
    global ocean
    for z in range (0, 5):
        print(ocean[z])

    #TESTING PURPOSES
    print(x)
    print(y)
    #TESTING PURPOSES

    xGuess = int(input("Please input the x position of where you believe the ship is."))
    yGuess = int(input("Please input the y position of where you believe the ship is."))

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



