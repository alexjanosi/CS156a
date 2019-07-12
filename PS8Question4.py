from sklearn import svm
import numpy as np

sup1 = 0
sup2 = 0
train = open("train.txt", "r")

x = []
y = []
for line in train:
	fields = line.strip().split()
	for l in range(int(len(fields)/3)):
		x.append([float(fields[1 + 3 * l]), float(fields[2 + 3 * l])])
		y.append(float(fields[0 + 3 * l]))

train.close()

for i in range(2):
	y2 = []
	for z in y:
		if (z == i):
			y2.append(1)
		else:
			y2.append(-1)

	clf = svm.SVC(kernel='poly', C=0.01, degree=2, gamma=1, coef0=1)
	clf.fit(x, y2)

	if sup1 == 0:
		sup1 = len(clf.support_)
	else:
		sup2 = len(clf.support_)

	print("Support vectors for " + str(i) + " versus all: " + str(len(clf.support_)))

print("Difference: " + str(sup1 - sup2))