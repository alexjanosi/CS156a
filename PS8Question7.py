from sklearn import svm
import numpy as np
import random
import time
start_time = time.time()

train = open("train.txt", "r")

x = []
for line in train:
	fields = line.strip().split()
	for l in range(int(len(fields)/3)):
		x.append([float(fields[1 + 3 * l]), float(fields[2 + 3 * l]), float(fields[0 + 3 * l])])

train.close()

first = [0, 0]
second = [0, 0]
third = [0, 0]
fourth = [0, 0]
fifth = [0, 0]
for b in range(100):
	random.shuffle(x)
	maxi = []
	for i in [0.0001, 0.001, 0.01, 0.1, 1]:
		y2 = []
		x2 = []
		for z in range(len(x)):
			if (x[z][2] == 1):
				y2.append(1)
				x2.append([x[z][0], x[z][1]])
			elif (x[z][2] == 5):
				y2.append(-1)
				x2.append([x[z][0], x[z][1]])

		disagree = 0

		for c in range(10):
			x3 = x2[c * int(len(x2)/10): (c + 1) * int(len(x2)/10)]
			y3 = y2[c * int(len(y2)/10): (c + 1) * int(len(y2)/10)]
			x4 = []
			y4 = []
			for p in range(len(x2)):
				if x2[p] not in x3:
					x4.append(x2[p])
					y4.append(y2[p])

			clf = svm.SVC(kernel='poly', C=i, degree=2, gamma=1, coef0=1)
			clf.fit(x4, y4)
			y5 = clf.predict(x3)
			disagree += (np.sum(y3 * y5 < 0)) / len(x3)

		maxi.append(disagree/10)

	first[1] += maxi[0]
	second[1] += maxi[1]
	third[1] += maxi[2]
	fourth[1] += maxi[3]
	fifth[1] += maxi[4]

	test = 1
	index = 0
	for j in range(len(maxi)):
		if maxi[j] < test:
			index = j
			test = maxi[j]

	if index == 0:
		first[0] += 1
	elif index == 1:
		second[0] += 1
	elif index == 2:
		third[0] +=1
	elif index == 3:
		fourth[0] +=1
	elif index == 4:
		fifth[0] += 1


print("C = 0.0001 wins " + str(first[0]) +" times with an average error of " + str(first[1]/100))
print("C = 0.001 wins " + str(second[0]) +" times with an average error of " + str(second[1]/100))
print("C = 0.01 wins " + str(third[0]) +" times with an average error of " + str(third[1]/100))
print("C = 0.1 wins " + str(fourth[0]) +" times with an average error of " + str(fourth[1]/100))
print("C = 1 wins " + str(fifth[0]) +" times with an average error of " + str(fifth[1]/100))
print("%s seconds to run" % (time.time() - start_time))