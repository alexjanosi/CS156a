import numpy as np 

train = open("trainfinal.txt", "r")

x = []
y = []
for line in train:
	fields = line.strip().split()
	for l in range(int(len(fields)/3)):
		x.append([1, float(fields[1 + 3 * l]), float(fields[2 + 3 * l])])
		y.append(float(fields[0 + 3 * l]))

train.close()

for i in [5, 6, 7, 8, 9]:
	y2 = []
	x2 = []
	for z in range(len(y)):
		if (y[z] == i):
			y2.append(1)
			x2.append(x[z])
		else:
			y2.append(-1)
			x2.append(x[z])

	left = np.matmul(np.transpose(x2), x2)
	summ = np.add(left, np.identity(3))
	inv = np.linalg.inv(summ)
	w = np.matmul(inv, np.matmul(np.transpose(x2), y2))

	wrong = np.sum(np.dot(x2, w) * y2 < 0) 

	print("Ein for " + str(i) + " versus all is " + str(wrong/len(x2)))

	