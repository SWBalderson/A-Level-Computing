import time
score = 0
questionData = [															
				["best A-level Subject", ["Music", "Biology", "Art", "Computing"], 3],
				["best base", ["Denary", "Binary", "Hexadecimal"], 1],
				["best cookie type", ["Oreos", "Choco Chip", "Hobnobs"], 1],
				["mode of names in the LVI computing class", ["Ashby", "Adam", "Tom", "James", "Simon"], 1],
				["best os", ["UNIX", "DOS"], 0]]
				#All variables go here in this format: [[{Q1}, [{choice list1}], {index of ans}],["Q", ["a", "b"],"1".....]]]
name = input("\nPlease enter your name: ")
print("\nHi, welcome to the quiz %s! \n" % name)
time.sleep(2)																		#Wait for 2 seconds to allow reading time
for i in range(len(questionData)):													#For each question
	print("Question %s is: \nWhat is the %s?: \n" % (str(i+1), questionData[i][0]))	#Print question
	for j in range(len(questionData[i][1])):										#Print question choices
		print(str(j+1) + ": " + questionData[i][1][j])
	usrIn = input("\nWhat is your answer: ")										#Makes variable usrIn taking input
	if  usrIn == str(questionData[i][2]+1):											#Verifies answer
		print("\nCorrect!\n")
		score += 1																	#Adds one to score counter
	else:
		print("\nWrong! The correct answer is %s\n" % questionData[i][1][questionData[i][2]])
	#time.sleep(1)																	#Wait for 1 second to allow reading time
if score > 3:																		#Checks final score
	print("\nCongratulations %s, you've finished! \n\nYour score was %s/%s" % (name, score,len(questionData)))
	print("\nWell Done!" * 5)
else:
	print("Disappointing %s; your score was %s/%s..." % (name, score, len(questionData)))