from sklearn import svm
import numpy as np

train = open("train.txt", "r")

x = []
y = []
for line in train:
	fields = line.strip().split()
	for l in range(int(len(fields)/3)):
		x.append([float(fields[1 + 3 * l]), float(fields[2 + 3 * l])])
		y.append(float(fields[0 + 3 * l]))

train.close()

for i in range(1, 11, 2):
	y2 = []
	for z in y:
		if (z == i):
			y2.append(1)
		else:
			y2.append(-1)

	clf = svm.SVC(kernel='poly', C=0.01, degree=2, gamma=1, coef0=1)
	clf.fit(x, y2)
	y3 = clf.predict(x)

	wrong = np.sum(y2 * y3 < 0)

	print("Ein for " + str(i) + " versus all: " + str(wrong/len(y2)))
