myname = input("What is your name?: ")

print("Hi " + myname)
if myname != "1":
	subject = input("What is your favourite subject?: ")

	if subject == "Computing" or subject == "computing":
		print("You have chosen wisely!")
	else:
		print("wrong")
	score = int(input("What was your test result? "))
	if score == 100:
		print("Well done! Full marks!")
	elif score >= 90:
		print("An A, well done")
	elif score >= 80:
		print("B, not too bad")
	elif score >= 70:
		print("C?!?, you need to try harder!")
	elif score < 70:
		print("You failed")
else:
	score = int(input("What was your test result? "))
	if score == 100:
		print("Well done! Full marks!")
	elif score >= 90:
		print("An A, well done")
	elif score >= 80:
		print("B, not too bad")
	elif score >= 70:
		print("C?!?, you need to try harder!")
	elif score < 70:
		print("You failed")
	