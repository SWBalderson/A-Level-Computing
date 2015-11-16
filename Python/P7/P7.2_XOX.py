grid = [[], [], [], 0]
import random
def blankGridGen(mygrid):
	for i in range(3):			#Creates Blank Grid	
		for j in range(3):
			mygrid[i].append(" ")
def exportGrid(mygrid):			#Exports grid arrays and mygrid[4] to be imported when reopened
	f = open("saves.txt", "w+")
	for i in range(3):
		for j in range(3):
			f.write(str(mygrid[i][j]) + ",")
		f.write("\n")
	f.write(str(mygrid[3]))
	f.close()
def importGrid(mygrid):			#Imports grid from saves.txt and assigns first 3 lines
	f = open("saves.txt", "r")	#to arrays inside the grid array and assigns last line
	for i in range(3):			#to mygrid[4] so draws can still be measured
		save = f.readline()
		mygrid[i] = (save.rstrip(",\n").split(","))
	mygrid[3] = int(f.readline(3))
	f.close()
	detectEnd(grid, "X")
	detectEnd(grid, "O")
def printGrid(mygrid):			#Prints the grid nicely
	for i in range(3):
		for j in range(3):
			if j==1 or j==2:
				print("|  " + str(grid[i][j]), end="")
			else:
				print("   " + str(grid[i][j]), end="")
		if i <2: 
			print("\n-------------")
		else:
			print("")
def detectEnd(mygrid, sym):		#Goes through all possible winning options
	for i in range(3):			#Uses the "sym" variable so the number of options are halved
		if mygrid[3] > 8:												#If this is 8, the limit of
			print("Draw! ")												#turns has been reached, so
			return True													#the game is a draw
		elif mygrid[i] == [sym,sym,sym]:	#Horizontal line
			print(sym + " wins! ")
			return True
		elif mygrid[0][i] == sym and mygrid[1][i] == sym and mygrid[2][i] == sym:	#Vertical Line
			print(sym + " wins!")
			return True
		elif mygrid[0][0] == sym and mygrid[1][1] == sym and mygrid[2][2] == sym:	#Diagonal Line
			print(sym + " wins! ")
			return True
		elif mygrid[0][2] == sym and mygrid[1][1] == sym and mygrid[2][0] == sym:	#Diagonal Line
			print(sym + " wins! ")
			return True
		else:
			return False
def question(mygrid, sym):		#Handles user input
	printGrid(grid)
	try:														#In case of string input
		Row = int(input(" %s: Enter Row: " % sym))-1
		Col = int(input(" %s: Enter Column: " % sym))-1
		if Row < 3 and Col < 3 and mygrid[Row][Col] == " ":		#Error management
			mygrid[Row][Col] = sym
			mygrid[3] += 1
		else: 
			print("Error: You chose an invalid square ")
	except ValueError:											#"Try" statement leads to here		
		print("Error: That wasn't a number ")	
def computerInput(mygrid):		#SinglePlayer mode				
	choose = False
	while choose == False:
		Row = random.randint(0,2)
		Col = random.randint(0,2)
		if mygrid[Row][Col] == " ":
			mygrid[Row][Col] = "O"
			mygrid[3] += 1
			choose = True
			#Main program
if input("Are you playing from a savestate? y/n ") == "y":
	importGrid(grid)
else:
	blankGridGen(grid)
end = False
if input("Would you like to play with a computer? y/n ") == "y":
	while end == False:
		question(grid, "X")
		end = detectEnd(grid, "X")
		print(grid)
		if end == False:
			computerInput(grid)
			end = detectEnd(grid, "O")
			exportGrid(grid)	
			#print(grid)
else:	
	while end == False:
		question(grid, "X")
		end = detectEnd(grid, "X")
		if end == False:
			question(grid, "O")
			end = detectEnd(grid, "O")
			exportGrid(grid)
print("Thanks for Playing! ")
printGrid(grid)