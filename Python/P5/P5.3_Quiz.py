import time
score = 0
questions = [
"best A-level subject", 
"best base", 
"best cookie type", 
"mode of names in the LVI computing class", 
"best operating system"
]
questionChoices = [
["Music", "Biology", "Art", "Computing"],
["Denary", "Binary", "Hexadecimal"],
["Oreos", "Choco Chip", "Hobnobs"],
["Ashby", "Adam", "Tom", "James", "Simon"],
["UNIX", "DOS"]
] 
questionAnswers = [3, 1, 1, 1, 0]
name = input("\nPlease enter your name: ")
print("\nHi, welcome to the quiz %s! \n" % name)
time.sleep(3)
for i in range(len(questionAnswers)):
	print("Question %s is: \nWhat is the %s?: \n" % (str(i+1), questions[i]))
	
	for j in range(len(questionChoices[i])):
		print(str(j+1) + ": " + questionChoices[i][j])
	usrIn = input("\nWhat is your answer: ")
	if  usrIn == str(questionAnswers[i]+1) or usrIn == questionChoices[i][questionAnswers[i]]:
		print("\nCorrect!\n")
		score += 1
	else:
		print("\nWrong! The correct answer is %s\n" % str(questionChoices[i][questionAnswers[i]]))

print("\nCongratulations %s, you've finished! \n\nYour score is %s" % (name, score))
if score > 3:
	print("\nWell Done!" * 5)