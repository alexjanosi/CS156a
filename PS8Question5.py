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

test = open("test.txt", "r")

xtest = []
ytest = []
for line2 in test:
	fields = line2.strip().split()
	for l in range(int(len(fields)/3)):
		xtest.append([float(fields[1 + 3 * l]), float(fields[2 + 3 * l])])
		ytest.append(float(fields[0 + 3 * l]))

xt2 = []
yt2 = []
for w in range(len(ytest)):
		if (ytest[w] == 1):
			yt2.append(1)
			xt2.append(xtest[w])
		elif (ytest[w] == 5):
			yt2.append(-1)
			xt2.append(xtest[w])

test.close()

for i in [0.0001, 0.001, 0.01, 1]:
	y2 = []
	x2 = []
	for z in range(len(y)):
		if (y[z] == 1):
			y2.append(1)
			x2.append(x[z])
		elif (y[z] == 5):
			y2.append(-1)
			x2.append(x[z])


	clf = svm.SVC(kernel='poly', C=i, degree=2, gamma=1, coef0=1)
	clf.fit(x2, y2)
	y3 = clf.predict(x2)
	wrong = np.sum(y2 * y3 < 0)

	print("Ein for C = " + str(i) + " and Q = " + str(deg) + " is " + str(wrong/len(y2)))

	print("Support vectors for C = " + str(i) + " and Q = " + str(deg) + " is " + str(len(clf.support_)))

	y4 = clf.predict(xt2)
	outwrong = np.sum(y4 * yt2 < 0)

	print("Eout for C = " + str(i) + " and Q = " + str(deg) + " is " + str(outwrong/len(yt2)))
