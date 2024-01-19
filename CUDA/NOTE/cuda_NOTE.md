# cuda

## numba 

Numba可以与NumPy紧密结合，两者一起，常常能够得到近乎C语言的速度。尽管Numba不能直接优化pandas，但是我们可以将pandas中处理数据的`for`循环作为单独的函数提出来，再使用Numba加速。

```python
data = np.random.random((20000, 20000))

start = time.perf_counter()

@jit # 使用@前后深度从30s变为0.5s
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
```

---



![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-9f43550d78b3ba61cc24076dc9e89e2a_b.jpg)

引入gpu后的计算流程

1. 初始化，并将必要的数据拷贝到GPU设备的显存上。
2. CPU调用GPU函数，启动GPU多个核心同时进行计算。
3. CPU与GPU异步计算。
4. 将GPU计算结果拷贝回主机端，得到计算结果。

```python
from numba import cuda

print(cuda.gpus)


def cpu_print():
    print("hello cpu")


@cuda.jit()  # 核函数
def gpu_print():
    print("hello,gpu")


def main():
    gpu_print[1, 3]()  # 告诉gpu开始1个block3个thread并行执行gpu_print函数,每个线程执行一次
    cuda.synchronize()  # 同步,告诉cpu等待gpu核函数执行完成后在执行下面代码
    cpu_print()


if __name__ == "__main__":
    main()
```



- 使用`from numba import cuda`引入`cuda`库
- 在GPU函数上添加`@cuda.jit`装饰符，表示该函数是一个在GPU设备上运行的函数，GPU函数又被称为**核函数**。
- 主函数调用GPU核函数时，需要添加如`[1, 2]`这样的**执行配置**，这个配置是在告知GPU以多大的并行粒度同时进行计算。`gpu_print[1, 2]()`表示同时开启2个线程并行地执行`gpu_print`函数，函数将被并行地执行2次。下文会深入探讨如何设置执行配置。
- GPU核函数的启动方式是**异步**的：启动GPU函数后，CPU不会等待GPU函数执行完毕才执行下一行代码。必要时，需要调用`cuda.synchronize()`，告知CPU等待GPU执行完核函数后，再进行CPU端后续计算。这个过程被称为**同步**，也就是GPU执行流程图中的红线部分。如果不调用`cuda.synchronize()`函数，执行结果也将改变，"print by cpu.将先被打印。虽然GPU函数在前，但是程序并没有等待GPU函数执行完，而是继续执行后面的`cpu_print`函数，由于CPU调用GPU有一定的延迟，反而后面的`cpu_print`先被执行，因此`cpu_print`的结果先被打印了出来。



### thread层次结构

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-a56b9d023b7c16c159c1d6e965fca06f_b.jpg)

CUDA将核函数所定义的运算称为**线程（Thread）**，多个线程组成一个**块（Block）**，多个块组成**网格（Grid）**。这样一个grid可以定义成千上万个线程，也就解决了并行执行上万次操作的问题。例如，把前面的程序改为并行执行8次：可以用2个block，每个block中有4个thread。原来的代码可以改为`gpu_print[2, 4]()`，其中方括号中第一个数字表示整个grid有多少个block，方括号中第二个数字表示一个block有多少个thread

在实际使用中，我们一般将CPU代码中**互相不依赖**的的`for`循环适当替换成CUDA代码。

- 一个block中的thread数最好是32、128、256的倍数。*注意，限于当前硬件的设计，block大小不能超过1024。*
- grid的大小`gridDim`（执行配置中第一个参数），即一个grid中block的个数可以由总次数`N`除以`blockDim`，并向上取整。

例如，我们想并行启动1000个thread，可以将blockDim设置为128，`1000 ÷ 128 = 7.8`，向上取整为8。使用时，执行配置可以写成`gpuWork[8, 128]()`，CUDA共启动`8 * 128 = 1024`个

==在一维的情况下,一个thread的全局id是`cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x`==

CUDA的统一内存系统是当GPU运行到某块数据发现不在设备端时，再去主机端中将数据拷贝过来，当执行完核函数后，又将所有的内存拷贝回主存

```python
ary = np.arange(10)
device_ary = cuda.to_device(ary)  # 将主存的数据拷贝到显存

host_ary = device_ary.copy_to_host()  # 将显存的数据拷贝和主存
```



**Python Numba库可以调用CUDA进行GPU编程，CPU端被称为host，GPU端被称为device，运行在GPU上的函数被称为核函数，调用核函数时需要有执行配置，以告知CUDA以多大的并行粒度(几个block,每个block几个thread)来计算。使用GPU编程时要合理地将数据在主机和设备间互相拷贝。**

<img src="https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-a8afebcca9f881a4e5ed75da4606a01d_b.jpg" alt="img" style="zoom: 67%;" />

---

### 并行计算优化--网格跨度

==相当于为一个thread分配多个数据,不用开很多个thread,节约开启和销毁thread的成本==

仍然以`[2, 4]`的执行配置为例，该执行配置中整个grid只能并行启动8个线程，假如我们要并行计算的数据是32，会发现后面8号至31号数据共计24个数据无法被计算。

这个时候就需要网格跨度

<img src="https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-61acef065b0e0cb03e6f080de2d7ae94_1440w.webp" alt="img" style="zoom:50%;" />

我们可以在0号线程中，处理第0、8、16、24号数据，就能解决数据远大于执行配置中的线程总数的问题，用程序表示，就是在核函数里再写个for循环。以打印为例，代码如下

```python
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

```

跨步大小为网格中线程总数，用`gridDim.x * blockDim.x`来计算

网格跨度的优势:

1. 扩展性：可以解决数据量比线程数大的问题

2. 线程复用：**CUDA线程启动和销毁都有开销**，主要是线程内存空间初始化的开销；不使用网格跨步，CUDA需要启动大于计算数的线程，每个线程内只做一件事情，做完就要被销毁；使用网格跨步，线程内有`for`循环，每个线程可以干更多事情，所有线程的启动销毁开销更少。

### 多流

==主要是让拷贝数据和数据计算同时执行==

之前我们讨论的并行，都是线程级别的，即CUDA开启多个线程，并行执行核函数内的代码。GPU最多就上千个核心，同一时间只能并行执行上千个任务。当我们处理千万级别的数据，整个大任务无法被GPU一次执行，所有的计算任务需要放在一个队列中，排队顺序执行。CUDA将放入队列顺序执行的一系列操作称为**流（Stream）**。

由于异构计算的硬件特性，CUDA中以下操作是相互独立的，通过编程，是可以操作他们并发地执行的：

- 主机端上的计算
- 设备端的计算（核函数）
- 数据从主机和设备间相互拷贝
- 数据从设备内拷贝或转移
- 数据从多个GPU设备间拷贝或转移

即使我们把大量的数据放在多个线程上执行已经极大的提升了性能.但是在一个流里面,数据也是先经过从host拷贝到device,然后在计算.

但是,拷贝和计算是可以并行的,数据拷贝不占用计算资源，计算不占用数据拷贝的总线（Bus）资源，因此计算和数据拷贝完全可以并发执行.

因此,**多流**就是:把一个大任务中的上述几部分**拆分开**，放到多个流中，**每次只对一部分数据进行拷贝、计算和回写**，并把这个流程做成**流水线**

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-5f9da08f74205af9f1ba0909c80d6d8d_1440w.webp)

上图中第一行的Stream 0部分是我们之前的逻辑，没有使用多流技术，程序的三大步骤是顺序执行的：

1. 先从主机拷贝初始化数据到设备（Host To Device）
2. 在设备上执行核函数（Kernel）
3. 将计算结果从设备拷贝回主机（Device To Host）

当数据量很大时，每个步骤的耗时很长，后面的步骤必须等前面执行完毕才能继续，整体的耗时相当长。以2000万维的向量加法为例，向量大约有几十M大小，将整个向量在host和device间拷贝将占用占用上百毫秒的时间，有可能远比核函数计算的时间多得多。将程序改为多流后，每次只计算一小部分，流水线并发执行，会得到非常大的性能提升。

#### 多流规则

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-19179c7f309d613fa45a88e0ea5d78b6_1440w.webp)

某个流内的操作是**顺序**的，非默认流之间是**异步**的，默认流有**阻塞**作用(如果调用默认流，那么默认流会等非默认流**都执行完**才能执行；同样，默认流执行完，才能再次执行其他非默认流)。

```python
# 定义流
stream = numba.cuda.stream()

# 数据拷贝接受流
numba.cuda.to_device(obj, stream=0, copy=True, to=None)
numba.cuda.copy_to_host(self, ary=None, stream=0)


```

### 多维度thread,block

```python
# 一个二维配置，某个thread在矩阵中的位置可以表示为
col = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y
row = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x


# 配置
threads_per_block = (16, 16)
blocks_per_grid = (32, 32)
gpu_kernel[blocks_per_grid, threads_per_block]
```

利用多维度进行矩阵运算

<img src="https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-813d72431a98db16ade9c4b05a5dd889_720w.webp" alt="img" style="zoom:67%;" />

```python
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
    c_cpu = c_gpu.copy_to_host()
    cuda.synchronize()

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

```



### shared memory

==先前是直接从显存的global memory中读取数据进行运算,但是从global memory中读取速度较慢,特别是重复读取的情况下;现在是把数据读取到shared memory,然后再进行运算,运算单元是子矩阵==

<img src="https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-dade539536d886164b39d7c8f1379c54_720w.webp" alt="img" style="zoom:67%;" />

Shared Memory的读写访问速度会远高于Global Memory。内存优化一般主要利用Shared Memory技术

我们计算的时候,一般把内存读取总量当成了参与运算的数据总量.但实际上，由于寄存器数量限制，没法完全容纳全部的数据量，每个数据往往需要读很多次，特别是对于那些相同的数据,如果多次读取,数据流动会影响算术强度.因此实际的算术强度只可能比理论值更低.

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-a047c8b80fbe078abdee7d9285ddad5f_720w.webp)

没法无限制增加寄存器数量的情况下，一种折中的方案就是用一块速度比普通内存块，容量比寄存器大的特殊区域来做中间存储，也就是**共享内存**

我们就可以把需要重复利用的数据先加载到共享内存中，虽然从共享内存到**寄存器**仍然存在重复加载的问题，但由于它们之间的**速度极快**

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-60b1dc5f92485ab20854a12502670241_720w.webp)

而**矩阵运算**,身为常见的运算手段,尤其是神经网络中,就是典型的数据被多次读取的运算.

设矩阵 A, B, C 的尺寸分别为 `M x K`, `K x N`, `M x N`，计算 `C = A x B`.分析一下内存访问情况，C中的一个元素是A中一行和B中一列的点积.那么计算 C 的完整一行需要读取 `N `次 A 矩阵的对应行，于是计算完 C 需要读取 `N `次矩阵 A;同理，还需要读取 `M `次矩阵 B.

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-f3b771a4ee40742cd594f8da828fd695_720w.webp)

**根据前面的讨论，最理想的情况当然是让每个 block 将 A 的一个行条带和 B 的一个列条带全部加载到shared memory中**这样就可以减少很多次的从global memory中的读取.

但是,shared memory的容量有限,比较保险的方法就是分多次加载到shared memory中.

由于 block 的尺寸为 `32 x 32`，因此总共需要从 global memory 中读取 `M / 32 + N / 32` 次.相比原来少了不少.

![img](https://spasmodic.oss-cn-hangzhou.aliyuncs.com/v2-4bf85c3749f0f868a59cb6d92f7dbc20_720w.webp)

如果数据量不足够的话,用了shared memory相比没用,速度反而会下降.

==多流和shared memory是从“增大并行度”和“充分利用内存”两个方向对CUDA来进行优化==

```python
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
    
'''matmul time without shared memory:  513.9576281999999
matmul time with shared memory:  297.4433074000001'''
```

