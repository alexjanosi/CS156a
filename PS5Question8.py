import math
import random

N = 100
epoch = 0
disagree = 0

def gradient(x, w):
	sum1 = [0, 0, 0]
	
	temp = [x[3] * x[0], x[3] * x[1], x[3] * x[2]]
	for j in range(3):
		temp[j] /= -1 * (1 + math.exp(-1 * (x[3] * (x[0] * w[0] + x[1] * w[1] + x[2] * w[2]))))
		sum1[j] += temp[j]	
	
	return sum1

def sign(x):
	if x < 0:
		return -1
	if x > 0:
		return 1
	if x == 0:
		return 0

for i in range(100):

	x1 = random.uniform(-1, 1)
	x2 = random.uniform(-1, 1)
	y1 = random.uniform(-1, 1)
	y2 = random.uniform(-1, 1)

	slope = (y2 - y1)/(x2 - x1)
	b = y1 - slope * x1

	points = []
	for k in range(N):
		x1 = random.uniform(-1, 1)
		x2 = random.uniform(-1, 1)
		if x2 < x1 * slope + b:
			points.append([1, x1, x2, -1])
		else:
			points.append([1, x1, x2, 1])

	w = [0, 0, 0]
	wb = [20, 20, 20]

	while math.sqrt((wb[0] - w[0])**2 + (wb[1] - w[1])**2 + (wb[2] - w[2])**2) >= 0.01:
		
		wb = w[:]

		random.shuffle(points)
		for m in range(N):
			ein = gradient(points[m], w)
		
			for i in range(3):
				ein[i] *= 0.01
				w[i] += ein[i]

		epoch += 1

	points2 = []
	for m in range(1000):
			points2.append([1, [random.uniform(-1,1), random.uniform(-1,1)], 0])

	for n in points2:
		if n[1][1]  < n[1][0] * slope + b:
			n[2] = -1
		else:
			n[2] = 1

	wrong = 0

	for iter2 in range(len(points2)):
		wrong += math.log(1 + math.exp(points2[iter2][2] * 
			(w[0] + w[1] * points2[iter2][1][0] + w[2] * points2[iter2][1][1])))
	
	disagree += (wrong/len(points2))


print("Epochs: " + str(epoch/100))
print("Eout: " + str(disagree/100))