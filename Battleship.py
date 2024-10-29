import random
x = 0
y = 0
terminate = 0

ocean = [
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
]



def startTurn():
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


def hideBoat():
    global x
    global y
    x = random.randint(0,4)
    y = random.randint(0,4)
    #ocean.insert("X", ocean[y,x])


hideBoat()

while terminate == 0:
    startTurn()



