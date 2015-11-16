O = [511, "O"]
X = [511, "X"]
win = 0
def detWin(sym):
	if sym[0]&504 == 504 or sym[0]&455 == 455 or sym[0]&63 == 63 or sym[0]&219 == 219 or sym[0]&430 == 430:
		print(sym[1], "wins! ")
		return 1
	elif X|O == 511:
		print("Its a draw! ")
		return 1
	else:
		return 0
def printBoard(sym):
	board = list(map(int, str(bin(sym[0])[2:][::-1])))
	print(board)
while win == 0:
	O[0] -= 2**int(input("Enter O square: "))
	printBoard(O)
	win = detWin(O)
	X[0] -= 2**int(input("Enter O square: "))
	printBoard(X)
	win = detWin(X) 


