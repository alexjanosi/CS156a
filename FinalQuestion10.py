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

for i in [0.01, 1]:
	y2 = []
	x2 = []
	xtest3 = []
	ytest3 = []
	for z in range(len(y)):
		if (y[z] == 1):
			y2.append(1)
			x2.append(x[z])
		elif (y[z] == 5):
			y2.append(-1)
			x2.append(x[z])

	for l in range(len(ytest)):
		if (ytest[l] == 1):
			ytest3.append(1)
			xtest3.append(xtest[l])
		elif (ytest[l] == 5):
			ytest3.append(-1)
			xtest3.append(xtest[l])

	left = np.matmul(np.transpose(x2), x2)
	summ = np.add(left,np.multiply(i, np.identity(6)))
	inv = np.linalg.inv(summ)
	w = np.matmul(inv, np.matmul(np.transpose(x2), y2))

	inputerr = np.sum(np.dot(x2, w) * y2 < 0)
	print("Ein for " + str(i) + " is " + str(inputerr/len(x2)))
	wrong = np.sum(np.dot(xtest3, w) * ytest3 < 0) 
	print("Eout for " + str(i) + " is " + str(wrong/len(xtest3)))
