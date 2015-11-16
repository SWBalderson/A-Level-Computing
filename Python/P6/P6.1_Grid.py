import random
grid = []	
tries = 0	#Assign variables
guess = 0
for i in range(10):
	grid.append([])	#Fill empty array with 10 arrays
	for j in range(10):
		grid[i].append("O")	#Fill 10 arrays with 10 "O"s
realCol = random.randint(0,9)
realRow = random.randint(0,9)
while guess == 0:
	guessCol = int(input("Guess a column:"))
	guessRow = int(input("Guess a row: "))
	if guessRow == realRow and guessCol == realCol:
		print("-" * 18 + "Correct Answer" + "-" * 18)
		guess += 1
	else:
		tries += 1
		print("Wrong answer")
		grid[guessRow-1][guessCol-1] = ("x")
		for i in grid:
			print(i)
		exit = input("Would you like to exit? ")
		print(realCol)	#Debug
		print(realRow)	#Debug
		if exit == "y":
			break
grid[realRow][realCol] = ("X")
for i in grid:
	print(i)
print("\nYou took %s tries to get the right answer." % (tries+1))