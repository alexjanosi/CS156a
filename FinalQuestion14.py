from sklearn import svm
from sklearn.cluster import KMeans
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

	x2 = []
	y2 = []
	for i in range(100):
		x2.append([random.uniform(-1,1), random.uniform(-1,1)])
	for k in range(100):
		y2.append(np.sign(x2[k][1] - x2[k][0] + 0.25 * np.sin(np.pi * x2[k][0])))

	yout = clf.predict(x2)
	Eout = np.sum(y2 * yout < 0) / len(y2)

	kmeans = KMeans(n_clusters=9).fit(x)
	centers = kmeans.cluster_centers_

	phi = []
	for i in range(len(x)):
		row = []
		for k in range(9):
			row.append(np.exp(-1.5 * np.linalg.norm(x[i] - centers[k])**2))
		phi.append(row)

	left = np.linalg.inv(np.matmul(np.transpose(phi), phi))
	right = np.matmul(np.transpose(phi), y)
	w = np.matmul(left, right)

	phi = []
	for i in range(len(x2)):
		row = []
		for k in range(9):
			row.append(np.exp(-1.5 * np.linalg.norm(x2[i] - centers[k])**2))
		phi.append(row)

	Eout1 = np.sum(np.matmul(phi, w) * y2 < 0) / len(y2)

	if (Eout < Eout1):
		wrong += 1


print(wrong/1000)