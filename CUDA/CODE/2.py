from numba import cuda

print(cuda.gpus)


def cpu_print():
    print("hello cpu")


@cuda.jit()  # 核函数
def gpu_print():
    print("hello,gpu")


def main():
    gpu_print[1, 3]()  # 告诉gpu开始用1个block3个thread并行执行gpu_print函数,每个线程执行一次
    cuda.synchronize()  # 同步,告诉cpu等待gpu核函数执行完成后在执行下面代码
    cpu_print()


if __name__ == "__main__":
    main()
