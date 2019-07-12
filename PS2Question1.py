import random

first = 0
minimum = 0
random1 = 0

for i in range(100000):

	rand2 = random.randint(0,999)
	mini = 10
	
	for q in range(1000):

		heads = 0
		
		for z in range(10):
			if random.randint(0,1) == 1:
				heads += 1

		if q == 0:
			first += heads/10

		if q == rand2:
			random1 += heads/10

		if heads < mini:
			mini = heads

		if q == 999:
			minimum += mini/10

print("\n")
print("Average Heads for First(v_1): " + str(first/100000))
print("Average Heads for Random(v_rand): " + str(random1/100000))
print("Average Heads for Minimum(v_min): " + str(minimum/100000))