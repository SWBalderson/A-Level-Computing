positions = []
names = []
quant = 0
print("")
print("-----------------------------------------------------------------------")
print("")

quant = int(input("How many players would you like to play with?: "))

print("")
print("-----------------------------------------------------------------------")
print("")

for i in range(quant):
    name = input("Type in the name of player " + str(i+1) + ": ")
    names.append(name)
    print("")

print("-----------------------------------------------------------------------")
print("")

for i in range(quant):
    position = input("What position is " + names[i] + " in: ")
    positions.append(position)
    print("")

print("-----------------------------------------------------------------------")
print("")

print("Your player positions are as follows: ")
print("")    
for i in range(quant):
    print(names[i] + " is in " + positions[i])
print("")
print("-----------------------------------------------------------------------")