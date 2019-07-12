import random
import numpy

N = int(input("Number of Points: "))
eoutfinal = 0

for l in range(1000):

	def sign(x):
		if x < 0:
			return -1
		if x > 0:
			return 1
		if x == 0:
			return 0

	points2 = []
	for z in range(N):
		points2.append([1, random.uniform(-1,1), random.uniform(-1,1), 0])

	for e in range(N):
		points2[e][3] = sign(points2[e][1] * points2[e][1] + points2[e][2] * points2[e][2] - 0.6)

	for b in range(int(N/10)):
		noise = random.randint(0, N - 1)
		points2[noise][3] *= -1 

	for s in range(N):
		if sign(-1 - 0.05 * points2[s][1] + 0.08 * points2[s][2] + 0.13 * points2[s][1] * points2[s][2] + 1.5 * points2[s][1] * points2[s][1] + 1.5 * points2[s][2] * points2[s][2]) != points2[s][3]:
			eoutfinal += 1


print("Eout: " + str(eoutfinal/1000000))