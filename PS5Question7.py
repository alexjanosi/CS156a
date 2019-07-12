import math

u = 1
v = 1
iterations = 0

def edv(u, v):
	dv = 2 * (u * math.exp(v) - 2 * v * math.exp(-u)) * (u * math.exp(v) - 2 * math.exp(-u))
	return dv

def edu(u, v):
	du = 2 * (math.exp(v) + 2 * v * math.exp(-u)) * (u * math.exp(v) - 2 * v * math.exp(-u))
	return du

def error(u, v):
	error = (u * math.exp(v) - 2 * v * math.exp(-u)) ** 2
	return error

for i in range(15):

	du = edu(u, v)
	u = u - (0.1) * du

	dv = edv(u, v)
	v = v - (0.1) * dv

print("Error: " + str(error(u,v)))