from numba import jit
import numpy as np
import time

data = np.random.random((20000, 20000))

start = time.perf_counter()

@jit
def origin_cal():
    all = 0
    for i in range(2000):
        for j in range(20000):
            all += np.tanh(data[i, j])

    return all


print(origin_cal())

end = time.perf_counter()
duration = end - start

print("time : ", duration)
