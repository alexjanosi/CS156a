import numpy

file_in = open('ps6in.txt', 'r')

xstart = []
y = []
for line in file_in:
	fields = line.strip().split()
	xstart.append([float(fields[0]), float(fields[1])])
	y.append(float(fields[2]))

file_in.close()

file_out = open('ps6out.txt', 'r')

x2 = []
y2 = []
for line2 in file_out:
	fields2 = line2.strip().split()
	x2.append([float(fields2[0]), float(fields2[1])])
	y2.append(float(fields2[2]))

file_out.close()

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

minimum = 1
for k in range(-1000, 3):
	left = numpy.matmul(numpy.transpose(x), x)
	middle = numpy.multiply(10**k, numpy.identity(8))
	left2 = numpy.add(left, middle)
	left2inv = numpy.linalg.inv(left2)
	w = numpy.matmul(left2inv, numpy.matmul(numpy.transpose(x), y))


	eintotal = 0
	for it in range(len(x)):
		if 	sign(numpy.inner(w, x[it])) != y[it]:	
			eintotal += 1

	insample = (eintotal / len(x))

	wrong = 0
	for iter2 in range(len(xtest)):
		if 	sign(numpy.inner(w, xtest[iter2])) != y2[iter2]:	
			wrong += 1
	
	disagree = (wrong / len(xtest))
	if disagree < minimum:
		minimum = disagree

print('Minimum: ' + str(minimum))
