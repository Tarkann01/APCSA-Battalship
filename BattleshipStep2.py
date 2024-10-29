import random

ocean = [
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
    ["O", "O", "O", "O", "O"],
]

def startTurn():
    for x in range (0, 5):
        print(ocean[x])

def hideBoat():
    x = random.randint(0,4)
    y = random.randint(0,4)
    ocean[x][y] = "X"

hideBoat()
startTurn()
x = 1
while x != 0:
    
