import random
import math

average = 0
for i in range(1000000):
	x1 = random.uniform(-1, 1)
	x2 = random.uniform(-1, 1)
	y1 = math.sin(math.pi * x1)
	y2 = math.sin(math.pi * x2)

	a = (x1**2 * y1 + x2**2 * y2) / (x1**4 + x2**4)
	average += a

ahat = round(average/1000000, 2)

print("g(x) = {}x^2".format(ahat))

bias = 0

for j in range(-1000, 1000):
		bias += ((ahat * j/1000 * j/1000) - math.sin(math.pi * j/1000)) ** 2

bias /= 2000

print("bias: " + str(bias))		

variance = 0

for z in range(100000):
	x1 = random.uniform(-1, 1)
	x2 = random.uniform(-1, 1)

	y1 = math.sin(math.pi * x1)
	y2 = math.sin(math.pi * x2)

	a = (x1**2 * y1 + x2**2 * y2) / (x1**4 + x2**4)
	
	for w in range(-1000, 1000):
		variance += ((a * w/1000 * w/1000)  - (ahat * w/1000 * w/1000)) ** 2

variance /= 2000 * 100000

print("var: " + str(variance))

print("E_out: " + str(bias + variance))