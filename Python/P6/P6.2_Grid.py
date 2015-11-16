import random
size = int(input("What size board would you like? "))
tries = 1
grid = []
def printGrid(mygrid):
        print("    ", end="")
        for i in range(10):
                print(str(i+1) + "  ", end="")
        print("")
        line = ("   " + ("+--")*size +"+")
        for i in range(size):
                print(line)
                if i >= 9:
                        print(str(i+1) + " ", end="")
                else:
                        print(str(i+1) + "  ", end="")
 
                for j in range(len(mygrid[i])):
                        print("|" + mygrid[i][j], end="")
                print("|")
        print(line)

def savestate(row, column):
        save = open('P6.2_SaveState.txt', 'w')
        save.write("")


for i in range(grid):
        line = []
        for j in range(grid):
                line.append("  ")
        grid.append(line)
 
row = random.randint(0,9)
column = random.randint(0,9)
 
print(str(row+1))
print(str(column+1))
 
while True:
        guessrow = int(input("Which row?: "))
        guesscolumn = int(input("Which column?: "))
        if ((guessrow-1) == row) and ((guesscolumn-1) == column):
                print("You win!!! Woooo!")
                print("It took you " + str(tries) + " goes.")
                break
        else:
                print("Sorry, try again.")
                tries += 1
                grid[guessrow-1][guesscolumn-1] = "# "
                printGrid(grid)
