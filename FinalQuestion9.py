import numpy as np 

def transform(x1, x2):
	return [1, x1, x2, x1 * x2, x1**2, x2**2]


train = open("trainfinal.txt", "r")

x3 = []
y = []
for line in train:
	fields = line.strip().split()
	for l in range(int(len(fields)/3)):
		x3.append([1, float(fields[1 + 3 * l]), float(fields[2 + 3 * l])])
		y.append(float(fields[0 + 3 * l]))

train.close()

test = open("testfinal.txt", "r")

xtest2 = []
ytest = []
for line2 in test:
	fields = line2.strip().split()
	for l in range(int(len(fields)/3)):
		xtest2.append([1, float(fields[1 + 3 * l]), float(fields[2 + 3 * l])])
		ytest.append(float(fields[0 + 3 * l]))

test.close()

x = []
xtest = []
for k in range(len(x3)):
	x.append(transform(x3[k][1], x3[k][2]))

for q in range(len(xtest2)):
	xtest.append(transform(xtest2[q][1], xtest2[q][2]))

Ein = []
Eout = []
Einz = []
Eoutz = []

for i in range(10):
	y2 = []
	x2 = []
	xtest3 = []
	ytest3 = []
	z2 = []
	ztest2 = []
	for z in range(len(y)):
		if (y[z] == i):
			y2.append(1)
			x2.append(x3[z])
			z2.append(x[z])
		else:
			y2.append(-1)
			x2.append(x3[z])
			z2.append(x[z])

	for l in range(len(ytest)):
		if (ytest[l] == i):
			ytest3.append(1)
			xtest3.append(xtest2[l])
			ztest2.append(xtest[l])
		else:
			ytest3.append(-1)
			xtest3.append(xtest2[l])
			ztest2.append(xtest[l])

	left = np.matmul(np.transpose(x2), x2)
	summ = np.add(left, np.identity(3))
	inv = np.linalg.inv(summ)
	w = np.matmul(inv, np.matmul(np.transpose(x2), y2))

	Ein.append(format((np.sum(np.dot(x2, w) * y2 < 0) / len(x2)), '.3f'))
	Eout.append(format((np.sum(np.dot(xtest3, w) * ytest3 < 0) /len(xtest3)), '.3f'))

	left = np.matmul(np.transpose(z2), z2)
	summ = np.add(left, np.identity(6))
	inv = np.linalg.inv(summ)
	w = np.matmul(inv, np.matmul(np.transpose(z2), y2))

	Einz.append(format((np.sum(np.dot(z2, w) * y2 < 0) / len(z2)),'.3f'))
	Eoutz.append(format((np.sum(np.dot(ztest2, w) * ytest3 < 0) /len(xtest3)), '.3f'))		

print("Ein with no transform: " + str(Ein))
print("Eout with no transform: " + str(Eout))
print("Ein with transform: " + str(Einz))
print("Eout with transform: " + str(Eoutz))