from numba import cuda

@cuda.jit
def gpu_cal(data_num):
    idWithinGrid = cuda.threadIdx.x + cuda.blockIdx.x * cuda.blockDim.x
    gridStride = cuda.blockDim.x * cuda.gridDim.x
    # gird的thread总数是跨步数
    for i in range(idWithinGrid, data_num, gridStride):
        print(i)


def main():
    gpu_cal[2, 4](32)  # 2个block,每个block4个thread
    cuda.synchronize()


if __name__ == "__main__":
    main()
