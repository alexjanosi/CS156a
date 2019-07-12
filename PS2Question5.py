import random
import numpy
from operator import add

N = int(input("Number of Points: "))

einfinal = 0
disagree = 0
iterations = 0

for l in range(1000):
	points = []
	for i in range(N):
		points.append([1, random.uniform(-1,1), random.uniform(-1,1)])

	# creates random list of points with default first and last value

	point1 = [random.uniform(-1,1), random.uniform(-1,1)]
	point2 = [random.uniform(-1,1), random.uniform(-1,1)]
	slope = (point2[1] - point1[1])/(point2[0] - point1[0])
	intercept = point1[1] - (slope * point1[0])

	# creates the target function

	output = []

	for j in points:
		if j[2]  < j[1] * slope + intercept:
			output.append([-1])
		else:
			output.append([1])


	# creates output vector with appropriate values

	def sign(x):
		if x < 0:
			return -1
		if x > 0:
			return 1
		if x == 0:
			return 0

	trans = numpy.transpose(points)
	left = numpy.matmul(trans, points)
	inverse = numpy.linalg.inv(left)
	pointsinverse = numpy.matmul(inverse, trans)

	w2 = numpy.matmul(pointsinverse, output)
	w = [[w2[0][0]],[w2[1][0]],[w2[2][0]]]

	eintotal = 0
			
	for it in range(N):
		if 	sign(w[0][0] * points[it][0] + w[1][0] * points[it][1] + w[2][0] * points[it][2]) != output[it][0]:	
			eintotal += 1

	ein = eintotal/N
	einfinal += ein
	
	points1 = []
	for t in range(N):
		points1.append([1, [points[t][1], points[t][2]], output[t][0]])

	misclass = points1
	w1 = [w[0][0], w[1][0], w[2][0]]

	while len(misclass) != 0:
		iter = random.randint(0, len(misclass) - 1)
		w1 = list(map(add, w1, [q * misclass[iter][2] for q in [misclass[iter][0], misclass[iter][1][0], misclass[iter][1][1]]]))
		iterations += 1
		misclass = []
		for z in range(len(points)):
			if sign(w1[0] * points1[z][0] + w1[1] * points1[z][1][0] + w1[2] * points1[z][1][1]) != points1[z][2]:
				misclass.append(points1[z])


	points2 = []
	for m in range(1000):
			points2.append([1, [random.uniform(-1,1), random.uniform(-1,1)], 0])

	for n in points2:
		if n[1][1]  < n[1][0] * slope + intercept:
			n[2] = -1
		else:
			n[2] = 1

	wrong = 0

	for iter2 in range(len(points2)):
		if 	sign(w[0][0] * points2[iter2][0] + w[1][0] * points2[iter2][1][0] + w[2][0] * points2[iter2][1][1]) != points2[iter2][2]:	
			wrong += 1
	
	disagree += (wrong/len(points2))



print("E_in: " + str(einfinal/1000))
print("E_out: " + str(disagree/1000))
print("Iterations: " + str(iterations/1000))