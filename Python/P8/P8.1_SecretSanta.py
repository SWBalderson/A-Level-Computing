import random
p = []
num = int(input("How many people do you want: "))
for i in range(num):
    p.append(input("Type the name of person %s: "% str(i+1)))
random.shuffle(p)
for i in range(len(p)):
    if i<len(p)-1:
        print("Pair " + str(i+1) + " is " + p[i] + " to " + p[i+1])
print("Pair " + str(len(p)) + " is " + p[len(p)-1] + " to " + p[0])
