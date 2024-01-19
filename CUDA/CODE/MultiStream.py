from numba import cuda
import numpy as np
import math
import time

@cuda.jit
def gpu_cal(x, y, result, n):
    idx = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    if idx < n:  # 大于数据数量的
        result[idx] = x[idx] * y[idx]


def main():
    n = 20000000
    x = np.arange(n).astype(np.int32)
    y = x * 2

    # cpu
    start = time.perf_counter()
    cpu_result = np.empty(n)
    for i in range(n):
        cpu_result[i] = x[i] * y[i]
    print("cpu时间: ", time.perf_counter() - start)

    # 默认流
    start = time.perf_counter()
    x_device = cuda.to_device(x)
    y_device = cuda.to_device(y)
    result_device = cuda.device_array(n)
    final_result = np.empty(n)

    threads_per_block = 1024
    blocks_per_grid = math.ceil(n / threads_per_block)  # 向上取整

    gpu_cal[blocks_per_grid, threads_per_block](x_device, y_device, result_device, n)
    cuda.synchronize()
    final_result[:] = result_device.copy_to_host()
    print("默认流时间: ", time.perf_counter() - start)

    # 多流
    StreamNum = 5
    SegementSize = n // StreamNum  # 数据分流后每个流的数据量

    StreamList = []
    for i in range(StreamNum):
        StreamList.append(cuda.stream())

    threads_per_block = 1024
    # 每个stream处理的数据量变为原来的1/5
    blocks_per_grid = math.ceil(SegementSize / threads_per_block)
    result_device_stream = cuda.device_array(SegementSize)
    final_result = np.empty(n)

    start = time.perf_counter()
    # 启动多个stream
    for i in range(StreamNum):
        x_device = cuda.to_device(x[i * SegementSize: (i + 1) * SegementSize], stream=StreamList[i])
        y_device = cuda.to_device(y[i * SegementSize: (i + 1) * SegementSize], stream=StreamList[i])

        gpu_cal[blocks_per_grid, threads_per_block, StreamList[i]](
            x_device,
            y_device,
            result_device_stream,
            SegementSize
        )

        final_result[i*SegementSize:(i+1)*SegementSize] = result_device_stream.copy_to_host()

    cuda.synchronize()
    print("多流时间: ", time.perf_counter() - start)


if __name__ == "__main__":
    main()
