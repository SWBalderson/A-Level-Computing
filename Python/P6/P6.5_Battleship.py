import random
 
def generateBlankGrid(mygrid):
        for i in range(10):
                line = []
                for j in range(10):
                        line.append("  ")
                mygrid.append(line)
 
def printGridsave(mygrid):
        print("    ", end="")
        for i in range(10):
                print(str(i+1) + "  ", end="")
        print("")
 
 
        line = "   +--+--+--+--+--+--+--+--+--+--+"
        for i in range(len(mygrid)):
                print(line)
                if i >= 9:
                        print(str(i+1) + " ", end="")
                else:
                        print(str(i+1) + "  ", end="")
 
                for j in range(len(mygrid[i])):
                        print("|" + mygrid[i][j], end="")
                #print("|")
        print(line)

def printGridnew(mygrid):
        print("    ", end="")
        for i in range(10):
                print(str(i+1) + "  ", end="")
        print("")
 
 
        line = "   +--+--+--+--+--+--+--+--+--+--+"
        for i in range(len(mygrid)):
                print(line)
                if i >= 9:
                        print(str(i+1) + " ", end="")
                else:
                        print(str(i+1) + "  ", end="")
 
                for j in range(len(mygrid[i])):
                        print("|" + mygrid[i][j], end="")
                print("|")
        print(line)
 
def saveGrid(mygrid, brow, bcolumn):
        f = open("battleships.txt", "w")
 
        f.write(str(brow) + '\n')
        f.write(str(bcolumn) + '\n')
 
        for i in range(len(mygrid)):
                for j in range(len(mygrid[i])):
                        if j != '  ':
                                f.write(mygrid[i][j] + ",")
                f.write('\n')
        f.close()
 
def importGrid(mygrid):
        f = open("battleships.txt", "r")
        brow = int(f.readline())
        bcolumn = int(f.readline())
        while True:
                line = f.readline()
               
                if line:
                        linearray = line.split(',')
                        mygrid.append(linearray)
                else:
                        break
        f.close()
        return brow, bcolumn
       
found = False
tries = 1
 
grid = []
row = 0
column = 0
 
print("Welcome to Simple Battleships!")
loadSavedGame = input("Would you like to load the saved game?")
 
if loadSavedGame == "y" or loadSavedGame == "Y":
        row, column = importGrid(grid)
else:
        generateBlankGrid(grid)
        row = random.randint(0,9)
        column = random.randint(0,9)
 
print(str(row+1))
print(str(column+1))
 
while found == False:
        guessrow = int(input("Which row?: "))
        guesscolumn = int(input("Which column?: "))
        if ((guessrow-1) == row) and ((guesscolumn-1) == column):
                found = True
                print("You win!!! Woooo!")
                print("It took you " + str(tries) + " goes.")
        else:
                print("Sorry, try again.")
                tries += 1
                grid[guessrow-1][guesscolumn-1] = "# "
                if loadSavedGame == "y" or loadSavedGame == "Y":
                        printGridsave(grid)
                else:
                        printGridnew(grid)
                saveGrid(grid, row, column)