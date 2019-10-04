# Name: Shane Mckisson
# Period 2
# Dice Rolling Simulator

import random

tS = 1

c1 = 0
c2 = 0
c3 = 0
c4 = 0
c5 = 0
c6 = 0

rolls = int(input("How many rolls? "))
randNum = 0

while tS <= rolls:
	rR = random.randint(1,6)
	print("Roll number: " + str(tS))
	print("Result: " + str(rR))
	tS += 1

	if rR == 1:
		c1 += 1

	elif rR == 2:
		c2 += 1

	elif rR == 3:
		c3 += 1

	elif rR == 4:
		c4 += 1

	elif rR == 5:
		c5 += 1

	elif rR == 6:
		c6 += 1

print("Total number of ones: " + str(c1))
print("Total number of twos: " + str(c2))
print("Total number of threes: " + str(c3))
print("Total number of fours: " + str(c4))
print("Total number of fives: " + str(c5))
print("Total number of sixes: " + str(c6))

p1 = (c1 / rolls) * 100
print("Percentage of ones: " + str(p1) + "%")
p2 = (c2 / rolls) * 100
print("Percentage of twos: " + str(p2) + "%")
p3 = (c3 / rolls) * 100
print("Percentage of threes: " + str(p3) + "%")
p4 = (c4 / rolls) * 100
print("Percentage of fours: " + str(p4) + "%")
p5 = (c5 / rolls) * 100
print("Percentage of fives: " + str(p5) + "%")
p6 = (c6 / rolls) * 100
print("Percentage of sixes: " + str(p6) + "%")