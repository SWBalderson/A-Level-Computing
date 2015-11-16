grid = []
go = 0
import random
for i in range(3):				#Creates Blank Grid
	grid.append([])
	for j in range(3):
		grid[i].append(" ")
def printGrid(mygrid):			#Function that prints the grid nicely
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
	global go
	for i in range(3):				#Uses the "sym" variable so the number of options are halved
		if go > 8:
			print("Draw! ")
			return True
		elif mygrid[i] == [sym,sym,sym]:	#Horizontal line
			print(sym + " wins! ")
			return True
		elif mygrid[0][i] == sym and mygrid[1][i] == sym and mygrid[2][i] == sym:	#Vertical Line
			print(sym + " wins!")
			return True
		elif mygrid[0][0] == sym and mygrid[1][1] == sym and mygrid[2][2] == sym:	#Diagonal Line
			print(sym + " wins! ")
			return True
		elif mygrid[0][2] == sym and mygrid[1][1] == sym and mygrid[2][0] == sym:	#Digonal Line
			print(sym + " wins! ")
			return True
		else:
			return False
def question(mygrid, sym):		#Handles user input
	printGrid(grid)
	global go
	try:														#In case of str input
		Row = int(input(" %s: Enter Row: " % sym))-1
		Col = int(input(" %s: Enter Column: " % sym))-1
		if Row < 3 and Col < 3 and mygrid[Row][Col] == " ":		#Error management
			mygrid[Row][Col] = sym
			go += 1
		else: 
			print("Error: You chose an invalid square ")
	except ValueError:											#"Try" leads to here		
		print("Error: That wasn't a number ")	
def computerInput(mygrid):		#SinglePlayer mode
	global go					#Basically replicates a human
	choose = False
	while choose == False:
		Row = random.randint(0,2)
		Col = random.randint(0,2)
		if mygrid[Row][Col] == " ":
			mygrid[Row][Col] = "O"
			go += 1
			choose = True
end = False						#Main program
if input("Would you like to play with a computer? y/n ") == "y":
	while end == False:
		question(grid, "X")
		end = detectEnd(grid, "X")
		if end == False:
			computerInput(grid)
			end = detectEnd(grid, "O")
		print(grid)
else:	
	while end == False:
		question(grid, "X")
		end = detectEnd(grid, "X")
		if end == False:
			question(grid, "O")
			end = detectEnd(grid, "O")

print("Thanks for Playing! ")
printGrid(grid)


for i in range(3):
	if board[i] =x, board[i+3)=x, board(i+6]=x:












