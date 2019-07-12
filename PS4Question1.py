import math

for i in range(500000):
	if i > 3200 * math.log(81920 * (i**10) + 80):
		print(i)
		break
