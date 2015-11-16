O = 0
X = 0
import math
win = 0
def detWin(sym):
	if sym&7 == 7 or sym&56 == 56 or sym&448 == 448 or sym&292 == 292 or sym&81 == 81:
		print(sym, "wins! ")
		return 1
	elif X|O == 511:
		print("Its a draw! ")
		return 1
	else:
		return 0
def printBoard(a, b):


	board = list(map(int, str(bin(X|O)[2:][::-1])))
	for j in range(9):
		if j!=2 and j!=5 and j!=8:
			print(str(board[j]), end=" | ")
		elif j==2 or j==5:
			print(" " + str(board[j]) + " \n-----------")
		else:
			print(" " + str(board[j]))
	print(board)
while win == 0:
	O = 261
	X = 48
	#O += 2**int(input("Enter O square: "))
	printBoard(X, O)
	win = 1
	#if win == 0:
	#	X += 2**int(input("Enter O square: "))
	#	printBoard(X)
	#	win = detWin(X)
	#	print(X)


