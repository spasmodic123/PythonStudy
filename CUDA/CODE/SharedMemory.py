import numpy as np
import math
import time
from numba import cuda, float32

# 每个block由block_size * block_size个元素
block_size = 32


@cuda.jit
def matmul(a, b, c):
    # c = a*b
    row = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    col = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y

    if row < c.shape[0] and col < c.shape[1]:
        tmp = 0
        for k in range(a.shape[1]):
            tmp += a[row, k] * b[k, col]
        c[row, col] = tmp


@cuda.jit
def matmul_shared_memory(a, b, c):
    # 声明shared memory的大小
    sa = cuda.shared.array((block_size, block_size), float32)
    sb = cuda.shared.array((block_size, block_size), float32)

    tx = cuda.threadIdx.x
    ty = cuda.threadIdx.y
    row = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    col = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y

    if row >= c.shape[0] and col >= c.shape[1]:
        return

    tmp = 0
    # 以shared memory的矩阵块为单位进行运算,切割成了多个矩阵块
    for m in range(math.ceil(a.shape[1] / block_size)):
        sa[tx, ty] = a[row, m * block_size]
        sb[tx, ty] = b[m * block_size, col]

        # 线程同步,这一个block的全部thread成功的将对应的数据读取到shared memory上才可以进行运算
        cuda.syncthreads()

        # 计算这一个shared memory矩阵块的点积
        for n in range(block_size):
            tmp += sa[tx, n] * sb[n, ty]

    # 线程同步,计算结束才读取
    c[row, col] = tmp


def main():
    # 初始化矩阵
    M = 20000
    N = 30000
    P = 10000

    a = np.random.random((M, N))
    b = np.random.random((N, P))

    a_device = cuda.to_device(a)
    b_device = cuda.to_device(b)
    c_devide = cuda.device_array((M, P))

    # 配置
    threads_per_block = (block_size, block_size)
    blocks_per_grid_x = math.ceil(a.shape[0] / block_size)
    blocks_per_grid_y = math.ceil((b.shape[1] / block_size))
    blocks_per_grid = (blocks_per_grid_x, blocks_per_grid_y)

    # 执行配置

    # 没有shared memory
    start = time.perf_counter()
    matmul[blocks_per_grid, threads_per_block](a_device, b_device, c_devide)
    # 同步
    cuda.synchronize()
    print("matmul time without shared memory: ", time.perf_counter() - start)

    # 有shared memory
    start = time.perf_counter()
    matmul_shared_memory[blocks_per_grid, threads_per_block](a_device, b_device, c_devide)
    cuda.synchronize()
    print("matmul time with shared memory: ", time.perf_counter() - start)


if __name__ == "__main__":
    main()
