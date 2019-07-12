import random
from operator import add

N = int(input("Number of Points: "))
iterations = 0
disagree = 0

for q in range(1000):
	points = []
	for i in range(N):
		points.append([1, [random.uniform(-1,1), random.uniform(-1,1)], 0])

	# creates random list of points with default first and last value

	point1 = [random.uniform(-1,1), random.uniform(-1,1)]
	point2 = [random.uniform(-1,1), random.uniform(-1,1)]
	slope = (point2[1] - point1[1])/(point2[0] - point1[0])
	intercept = point1[1] - slope * point1[0]

	# creates the target function

	for j in points:
		if j[1][1]  < j[1][0] * slope + intercept:
			j[2] = -1
		else:
			j[2] = 1

	# updates the y value of each point set		

	def sign(x):
		if x < 0:
			return -1
		if x > 0:
			return 1
		if x == 0:
			return 0



	w = [0, 0, 0]

	misclass = points

	while len(misclass) != 0:
		iter = random.randint(0, len(misclass) - 1)
		w = list(map(add, w, [q * misclass[iter][2] for q in [misclass[iter][0], misclass[iter][1][0], misclass[iter][1][1]]]))
		iterations += 1
		misclass = []
		for z in range(len(points)):
			if sign(w[0] * points[z][0] + w[1] * points[z][1][0] + w[2] * points[z][1][1]) != points[z][2]:
				misclass.append(points[z])

	# main PLA algorithm that checks to see if each point is misclassified and changes the weight if so

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
		if 	sign(w[0] * points2[iter2][0] + w[1] * points2[iter2][1][0] + w[2] * points2[iter2][1][1]) != points2[iter2][2]:	
			wrong += 1
	
	disagree += (wrong/len(points2))

	# generating random points to see if hypothesis agrees with target function		
			

print("Average Iterations: " + str(iterations/1000))
print("Average Disagreement: " + str(disagree/1000))