import random

tries = 1
grid = []
row = 0
column = 0
def createGrid(mygrid):
        for i in range(10):
                line = []
                for j in range(10):
                        line.append("  ")
                        grid.append(line)

def saveExport(mygrid, myrow, mycolumn):
        fw = open('savestate.txt', 'wt')
        fw.write(str(row) + '\n')

        for i in range(len(mygrid)):
                for j in range(len(mygrid[i])):
                        fw.write(mygrid[i][j] + ",")
                fw.write("\n")
        fw.close()

def saveImport(mygrid):
        fr = open('savestate.txt', 'rt')
        while True:
                fline = fr.readline()
                if fline:
                        linearray = fline.split(",")
                        mygrid.append(linearray)
                else:
                        break
        fr.close()

def printGrid(mygrid):
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

print(str(row+1))
print(str(column+1))

imp = input("Would you like to open your savestate? y/n ")
if imp == "y" or imp == "Y":
        saveImport(grid)
else:
        createGrid(grid)
        row = random.randint(0,9)
        column = random.randint(0,9)

while True:
        guessrow = int(input("Which row?: "))-1
        guesscolumn = int(input("Which column?: "))-1
        tries += 1
        grid[guessrow][guesscolumn] = "# "
        print(grid)
        if guessrow == row and guesscolumn == column:
                grid[row][column] = "X "
                printGrid(grid)
                print("You win!!! Woooo!")
                print("It took you %s goes!" % tries)
                break





