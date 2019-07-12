import random

e1 = 0
e2 = 0
e = 0

n = 10000000

for i in range (n):
	e1t = random.uniform(0, 1)
	e1 += e1t
	e2t = random.uniform(0, 1)
	e2 += e2t
	et = min(e1t, e2t)
	e += et

print("e1: " + str(e1/n))
print("e2: " + str(e2/n))
print("e: " + str(e/n))
