import math
from decimal import Decimal 

delta = 0.05
dvc = 50
N = 10000
overflow = 925.416

orignialvcbound = math.sqrt((8/N) * math.log(4*((2 * N)**dvc + 1)/delta))

rademachbound = math.sqrt((2/N) * math.log(2 *((N)**dvc + 1))) + math.sqrt(2/N * math.log(1/delta)) + 1/N

parrondo = (1/N) * (1 + math.sqrt(N * math.log((6 * ((N)**dvc + 1))/ delta) + 1))

devroye_overflow = (1/(2 * (N - 2))) * (2 + math.sqrt(2 * N * (overflow) - 4 * (overflow) + 4))

#devroye = (1/(2 * (N - 2))) * (2 + math.sqrt(2 * N * (math.log((4 * ((N)**(dvc * 2) + 1))/ delta)) \
# - 4 * (math.log((4 * ((N)**(dvc * 2) + 1))/ delta)) + 4))

print(orignialvcbound)
print(rademachbound)
print(parrondo)
print(devroye_overflow)
#print(devroye)