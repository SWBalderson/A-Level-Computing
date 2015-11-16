import random
grid = []	
tries = 0	#Assign variables
guess = 0
for i in range(10):
	grid.append([])	#Fill empty array with 10 arrays
	for j in range(10):
		grid[i].append("O")	#Fill 10 arrays with 10 "O"s
#usrCol = input("Select the column of your ship: ")
#usrRow = input
realRow = random.randint(0,9)
realCol = random.randint(0,9)
while True:
	guessRow = int(input("Guess a row: "))-1
	guessCol = int(input("Guess a column:"))-1
	if guessRow == realRow and guessCol == realCol:
		print("-" * 18 + "Correct Answer" + "-" * 18)
		break
	else:
		tries += 1
		print("Wrong answer")
		grid[guessRow][guessCol] = ("x")
		for i in grid:
			print(i)
		exit = input("Would you like to exit? ")
		if exit == "y":
			break
		print("Row = " + str(realRow))	#Debug
		print("Column = " + str(realCol))	#Debug
		
grid[realRow][realCol] = ("X")
for i in grid:
	print("i")
print("\nYou took %s tries to get the right answer." % (tries+1))