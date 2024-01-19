from numba import cuda
import numpy as np
import math
import time


@cuda.jit
def matmul(a, b, c):
    # 矩阵乘法c=a*b
    # 最终row行col列
    row = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    col = cuda.threadIdx.y + cuda.blockIdx.y * cuda.blockDim.y

    tmp = 0
    for k in range(a.shape[1]):
        tmp += a[row, k] * b[k, col]
    c[row, col] = tmp


def main():
    # 初始化
    m = 6000
    n = 4800
    p = 9000

    a = np.random.random((m, n))
    b = np.random.random((n, p))

    start = time.perf_counter()
    a = cuda.to_device(a)
    b = cuda.to_device(b)
    c_gpu = cuda.device_array((m, p))

    # 配置
    threads_per_block = (16, 16)
    blocks_per_grid_x = int(a.shape[0] / threads_per_block[0])
    blocks_per_grid_y = int(b.shape[1] / threads_per_block[1])
    blocks_per_gird = (blocks_per_grid_x, blocks_per_grid_y)

    # 执行核函数
    matmul[blocks_per_gird, threads_per_block](a, b, c_gpu)

    # 数据拷贝
    cuda.synchronize()
    c_cpu = c_gpu.copy_to_host()

    print("gpu_time: ", time.perf_counter() - start, end='\n')

    # 验证正确性
    ccc_cpu = np.empty((m, p))
    start = time.perf_counter()
    np.matmul(a, b, ccc_cpu)
    if np.allclose(c_cpu, ccc_cpu):
        print("correct")
    print("time_cpu: ", time.perf_counter() - start, end='\n')


if __name__ == "__main__":
    main()
