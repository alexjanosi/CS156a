import random
from operator import add
from sklearn import svm

N = int(input("Number of Points: "))
runs = 1000
actualruns = 0
disagree = 0
vectors = 0

for q in range(runs):
	points = []
	for i in range(N):
		points.append([1, [random.uniform(-1,1), random.uniform(-1,1)], 0])

	x = []
	for l in range(N):
		x.append([points[l][1][0], points[l][1][1]])

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

	y = []
	for k in range(N):
		y.append(points[k][2])
	check = set(y)
	if len(check) == 1:
		continue
	actualruns += 1

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
		w = list(map(add, w, [q * misclass[iter][2] for q in [misclass[iter][0],\
		 misclass[iter][1][0], misclass[iter][1][1]]]))
		misclass = []
		for z in range(len(points)):
			if sign(w[0] * points[z][0] + w[1] * points[z][1][0]\
			 + w[2] * points[z][1][1]) != points[z][2]:
				misclass.append(points[z])

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
		if 	sign(w[0] * points2[iter2][0] + w[1] * \
			points2[iter2][1][0] + w[2] * points2[iter2][1][1]) != points2[iter2][2]:	
			wrong += 1
	
	PLAdisagree = (wrong/len(points2))

	clf = svm.SVC(kernel='linear', C=999999999999999999999999999999999999)
	clf.fit(x,y)
	vectors += len(clf.support_)

	wrong2 = 0

	for iter3 in range(len(points2)):
		if 	clf.predict([[points2[iter3][1][0], points2[iter3][1][1]]]) != points2[iter3][2]:	
			wrong2 += 1
	
	SVMdisagree = (wrong2/len(points2))

	if PLAdisagree > SVMdisagree:
		disagree += 1

print("SVM is better than PLA " + str((disagree/actualruns) * 100) + "% of the time")
print("Number of support vectors: " + str(vectors/actualruns))