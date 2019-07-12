import numpy

file_out = open('ps6out.txt', 'r')

x2 = []
y2 = []
for line2 in file_out:
	fields2 = line2.strip().split()
	x2.append([float(fields2[0]), float(fields2[1])])
	y2.append(float(fields2[2]))

file_out.close()

xtest = []
for i in range(len(x2)):
	xtest.append([1, x2[i][0], x2[i][1], x2[i][0]**2, x2[i][1]**2, x2[i][0] * x2[i][1], \
		abs(x2[i][0] - x2[i][1]), abs(x2[i][0] + x2[i][1])])

file_in = open('ps6in.txt', 'r')

xstart = []
y = []
for line in file_in:
	fields = line.strip().split()
	xstart.append([float(fields[0]), float(fields[1])])
	y.append(float(fields[2]))

file_in.close()

x = []
for i in range(len(xstart)):
	x.append([1, xstart[i][0], xstart[i][1], xstart[i][0]**2, xstart[i][1]**2, xstart[i][0] * xstart[i][1], \
		abs(xstart[i][0] - xstart[i][1]), abs(xstart[i][0] + xstart[i][1])])

xtest = []
for i in range(len(x2)):
	xtest.append([1, x2[i][0], x2[i][1], x2[i][0]**2, x2[i][1]**2, x2[i][0] * x2[i][1], \
		abs(x2[i][0] - x2[i][1]), abs(x2[i][0] + x2[i][1])])


def sign(x):
		if x < 0:
			return -1
		if x > 0:
			return 1
		if x == 0:
			return 0

for k in range(4, 9):
	x3 = []
	y3 = []
	for z in range(25, 35):
		test = []
		for q in range(k):
			test += [x[z][q]]
		x3.append(test)
		y3.append(y[z])

	left = numpy.matmul(numpy.transpose(x3), x3)
	leftinv = numpy.linalg.inv(left)
	w = numpy.matmul(leftinv, numpy.matmul(numpy.transpose(x3), y3))

	x4 = []
	y4 = []
	for t in range(25):
		test1 = []
		for r in range(k):
			test1 += [x[t][r]]
		x4.append(test1)
		y4.append(y[t])

	eintotal = 0
	for it in range(len(x4)):
		if 	sign(numpy.inner(w, x4[it])) != y4[it]:	
			eintotal += 1

	insample = (eintotal / len(x))

	print("Classification Error for k = " + str(k - 1) + ": " + str(insample))

	xtest2 = []
	for z in range(len(xtest)):
		test3 = []
		for q in range(k):
			test3 += [xtest[z][q]]
		xtest2.append(test3)

	wrong = 0
	for iter2 in range(len(xtest)):
		if 	sign(numpy.inner(w, xtest2[iter2])) != y2[iter2]:	
			wrong += 1
	
	disagree = (wrong / len(xtest))

	print("Out-Of-Sample Error for k = " + str(k - 1) + ": " + str(disagree))
