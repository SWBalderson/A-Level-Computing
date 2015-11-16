name = ""
score = 0
q1Choice = ["w", "r", "w"]	#These should have the multiple choice options written in them
q2Choice = ["r", "w", "w", "w"]
q3Choice = ["r", "w", "w", "w"]
q4Choice = ["w", "w", "r", "w"]
q5Choice = ["w", "r"]
q1ansCorrect = 1 #These should be the index of the array that pertain to the choice array
q2ansCorrect = 0 
q3ansCorrect = 0
q4ansCorrect = 2
q5ansCorrect = 1
####################################################################################### HEADER
name = input("\nPlease enter your name: ")
print("\nHi, welcome to the quiz %s! \n" % name)
####################################################################################### Q1
for i in range(len(q1Choice)):
	print(str(i+1) + ": " + q1Choice[i])	#Prints available answers defined above
q1ans = input("Type the number of your answer: ")
if (int(q1ans)-1) == q1ansCorrect:	#Verifies answer
	print("\nWell Done! \n")
	score += 1					#Adds 1 to score
else:
	print("\nWrong answer... The correct answer was %s" % q1Choice[q1ansCorrect] + "\n")	#Prints back correct answer
####################################################################################### Q2
for i in range(len(q2Choice)):
	print(str(i+1) + ": " + q2Choice[i])
q2ans = input("Type the number of your answer: ")
if (int(q2ans)-1) == q2ansCorrect:
	print("\nWell Done! \n")
	score += 1
else:
	print("\nWrong answer... The correct answer was %s" % q2Choice[q2ansCorrect] + "\n")
####################################################################################### Q3
for i in range(len(q3Choice)):
	print(str(i+1) + ": " + q3Choice[i])
q3ans = input("Type the number of your answer: ")
if (int(q3ans)-1) == q3ansCorrect:
	print("\nWell Done! \n")
	score += 1
else:
	print("\nWrong answer... The correct answer was %s" % q3Choice[q3ansCorrect] + "\n")
####################################################################################### Q4
for i in range(len(q4Choice)):
	print(str(i+1) + ": " + q4Choice[i])
q4ans = input("Type the number of your answer: ")
if (int(q4ans)-1) == q4ansCorrect:
	print("\nWell Done! \n")
	score += 1
else:
	print("\nWrong answer... The correct answer was %s" % q4Choice[q4ansCorrect] + "\n")
####################################################################################### Q5
for i in range(len(q5Choice)):
	print(str(i+1) + ": " + q5Choice[i])
q5ans = input("Type the number of your answer: ")
if (int(q5ans)-1) == q5ansCorrect:
	print("\nWell Done! \n")
	score += 1
else:
	print("\nWrong answer... The correct answer was %s" % q5Choice[q5ansCorrect] + "\n")
####################################################################################### FOOTER
print("\nCongratulations %s, you've finished! \n\nYour score is %s" % (name, score))
if score > 3:
	print("\nWell Done!" * 5)