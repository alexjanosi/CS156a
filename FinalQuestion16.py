from sklearn import svm
from sklearn.cluster import KMeans
import numpy as np
import random

ein9 = 0

for i in range(1000):
	x = []
	y = []
	for i in range(100):
		x.append([random.uniform(-1,1), random.uniform(-1,1)])
	for k in range(100):
		y.append(np.sign(x[k][1] - x[k][0] + 0.25 * np.sin(np.pi * x[k][0])))

	x2 = []
	y2 = []
	for i in range(100):
		x2.append([random.uniform(-1,1), random.uniform(-1,1)])
	for k in range(100):
		y2.append(np.sign(x2[k][1] - x2[k][0] + 0.25 * np.sin(np.pi * x2[k][0])))

	for k in [9]:
		kmeans = KMeans(n_clusters=k).fit(x)
		centers = kmeans.cluster_centers_

		phi = []
		for i in range(len(x)):
			row = []
			for q in range(k):
				row.append(np.exp(-1.5 * np.linalg.norm(x[i] - centers[q])))
			phi.append(row)

		left = np.linalg.inv(np.matmul(np.transpose(phi), phi))
		right = np.matmul(np.transpose(phi), y)
		w = np.matmul(left, right)

		Ein = np.sum(np.matmul(phi, w) * y < 0) / len(y)

		if Ein == 0:
			ein9 += 1

print("Number of time: " + str(ein9/1000))
