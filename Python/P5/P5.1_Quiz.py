import time
name = ""
score = 0
answers = []

print("")
print("-----------------------------------------------------------------------")
print("")

name = input("Hi! What is your name? ")

print("")
print("-----------------------------------------------------------------------")
print("")

print("Hi " + name + ", enjoy the quiz! ")
print("")
print("In this quiz there are 5 multiple choice questions, ")
print("To answer a quistion, type the letter of the answer and hit enter! ")

print("")
print("-----------------------------------------------------------------------")
print("")

time.sleep(3)

print("OK!, here's question 1: ")
print("What is the best A-level subject ")
print("a) Computing \nb) Art \nc) Biology \nd) Music ")

Q1 = input("Enter your answer: ")
print("")
if Q1 == "a" or Q1 == "b)":
	print("Well done! ")
	score += 1
else:
	print("Better luck next time... ")
answers.append(Q1)
print("")
print("-----------------------------------------------------------------------")
print("")

time.sleep(3)

print("Here comes question 2: ")
print("What is the best number base: ")
print("a) Denary \nb) Binary \nc) Hexadecimal ")

Q2 = input("Enter your answer: ")
print("")
if Q2 == "b" or Q2 == "b)":
	print("That's right! ")
	score += 1
else:
	print("Damn, unlucky... ")
answers.append(Q2)
print("")
print("-----------------------------------------------------------------------")
print("")

time.sleep(3)

print("Alright, here is question 3: ")
print("What is the mode of names in the LVI Computing Class: ")
print("a) Ashby \nb) Adam \nc) Tom \nd) James \ne) Simon ")

Q3 = input("Now type your answer: ")
print("")
if Q3 == "b" or Q3 == "b)":
	print("Wow, you got it right! ")
	score += 1
else:
	print("Dude, that was an easy one! ")
answers.append(Q3)
print("")
print("-----------------------------------------------------------------------")
print("")

time.sleep(3)

print("OK, nearly done. ")
print("What is the coolest operating system: ")
print("a) DOS \nb) UNIX ")

Q4 = input("Type the answer now: ")
print("")
if Q4 == "b" or Q4 == "b)":
	print("That wasn't exactly difficult, was it ")
	score += 1
else:
	print("Dude are you serious... :O ")
answers.append(Q4)
print("")
print("-----------------------------------------------------------------------")
print("")

time.sleep(3)

print("Finally, the last question: ")
print("Who is the coolest teacher? ")
print("a) Mr. Balderson \nb) Anybody else ")

Q5 = input("OK, so what's your answer? ")
print("")
if Q5 == "a" or Q5 == "a)":
	print("Obviously... ")
	score += 1
else:
	print("Get out. ")
answers.append(Q5)
print("")
print("-----------------------------------------------------------------------")
print("")

time.sleep(3)

print("OK " + name + ", your answers were: ")
for s in range(len(answers)):
	print("Q" + str(s+1) + ": " + answers[s])
print("So your score is " + str(score))
 x1
if score > 3:
	for s in range(5):
		print("Well done!")