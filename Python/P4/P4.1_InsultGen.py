import random

adj = []
adv = []
noun = []



file = open('Column_1.txt', 'rt')

while True:
	line = file.readline()
	if line:
		adj.append(line.strip())
	else:
		break

file.close()

file = open('Column_2.txt', 'rt')

while True:
	line = file.readline()
	if line:
		adv.append(line.strip())
	else:
		break

file.close()

file = open('Column_3.txt', 'rt')

while True:
	line = file.readline()
	if line:
		noun.append(line.strip())
	else:
		break

file.close()

print("You " + adj[random.randint(0, len(adj))] + " " + adj[random.randint(0, len(adj))] + " " + adv[random.randint(0, len(adv))] + " " + noun[random.randint(0, len(noun))])
input("Would you like another insult sire? ")
while True:
	input("Would you like another insult sire? ")
	if input:
		print("OK you " + adj[random.randint(0, len(adj))] + " " + adj[random.randint(0, len(adj))] + " " + adv[random.randint(0, len(adv))] + " " + noun[random.randint(0, len(noun))])
	else:
		break

print ("Good bye")


