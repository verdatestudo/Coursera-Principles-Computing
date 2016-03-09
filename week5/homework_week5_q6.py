
import math
import greedy_boss
from matplotlib import pyplot as plt

zzz = greedy_boss.greedy_boss(200,1000)
aaa = []

for value in zzz:
    print value

for x in range(10,101, 10):
    my_formula = (0.1 * x * (0.1 * x+1)) / 2 * 1000
    print x, my_formula
    aaa.append([x, my_formula])

xxx, yyy = zip(*zzz)
bbb, ccc = zip(*aaa)
plt.plot(xxx, yyy, lw=2)
plt.plot(bbb, ccc, lw=2)
plt.show()
