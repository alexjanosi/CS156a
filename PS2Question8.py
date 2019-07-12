import random
import numpy

N = int(input("Number of Points: "))
einfinal = 0

for l in range(1000):
	points = []
	for i in range(N):
		points.append([1, random.uniform(-1,1), random.uniform(-1,1), 0])

	def sign(x):
		if x < 0:
			return -1
		if x > 0:
			return 1
		if x == 0:
			return 0

	for q in range(N):
		points[q][3] = sign(points[q][1] * points[q][1] + points[q][2] * points[q][2] - 0.6)


	for r in range(int(N/10)):
		noise = random.randint(0, N - 1)
		points[noise][3] *= -1 

	points1 = []
	outputs = []
	for w in range(N):
		points1.append([1, points[w][1], points[w][2]])
		outputs.append([points[w][3]])

	trans = numpy.transpose(points1)
	left = numpy.matmul(trans, points1)
	inverse = numpy.linalg.inv(left)
	pointsinverse = numpy.matmul(inverse, trans)

	w2 = numpy.matmul(pointsinverse, outputs)
	w = [[w2[0][0]],[w2[1][0]],[w2[2][0]]]

	eintotal = 0
			
	for it in range(N):
		if 	sign(w[0][0] * points[it][0] + w[1][0] * points[it][1] + w[2][0] * points[it][2]) != points[it][3]:	
			eintotal += 1

	ein = eintotal/N
	einfinal += ein

print(str(einfinal/1000))