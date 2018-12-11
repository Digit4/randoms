import numpy as np
import time,sys

SIZE = 1000

l1 = range(SIZE)
l2 = range(SIZE)

a1 = np.arange(SIZE)
a2 = np.arange(SIZE)

#python Lists
start = time.time()
result = [x + y for x, y in zip(l1, l2)]
#print("python took : " + str((time.time() - start)) * 1000 + "and returned "+ str(result))

#numpy arrays
start1 = time.time()
result1 = a1 + a2
print("numpy took : "+ str((time.time() - start1) * 1000) + "and returned "+ str(result1))
