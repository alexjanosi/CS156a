from sklearn import svm
import numpy as np
import random

wrong = 0

for i in range(1000):
	x = []
	y = []
	for i in range(100):
		x.append([random.uniform(-1,1), random.uniform(-1,1)])
	for k in range(100):
		y.append(np.sign(x[k][1] - x[k][0] + 0.25 * np.sin(np.pi * x[k][0])))

	clf = svm.SVC(kernel='rbf',C=float("inf"),gamma=1.5)
	clf.fit(x,y)
	yin = clf.predict(x)
	Ein = np.sum(y * yin < 0) / len(y)
	if Ein != 0:
		wrong += 1

print(wrong/1000)

