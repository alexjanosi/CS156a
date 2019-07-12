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

while error(u, v) >= 10 ** -14:
	du = edu(u, v)
	dv = edv(u, v)

	u = u - (0.1) * du
	v = v - (0.1) * dv
	iterations += 1

print("Iterations: " + str(iterations))
print("u: " + str(u))
print("v: " + str(v))