value = 0
maximum = 0
amount = 0

for i in range(1, 36):
	weights = (10 * (i - 1)) + (i * (36 - i - 1)) + (36 - i)
	if weights > maximum:
		value = i
		maximum = weights
		amount = 2
for q in range(1, 36):
	if (q % 2 == 1):
		weights = (10 * (q - 1)) + (q * ((37 - q)/2 - 1)) + ((37 - q)/2 * ((35 - q)/2 - 1)) + ((35 - q)/2)
	else:
		weights = (10 * (q - 1)) + (q * ((36 - q)/2 - 1)) + ((36 - q)/2 * ((36 - q)/2 - 1)) + ((36 - q)/2)
	if weights > maximum:
		value = q
		maximum = weights
		amount = 3

print("The maximum is " + str(maximum) + " with " + str(amount) \
 + " hidden layers with a first hidden layer of " + str(value) + " units")