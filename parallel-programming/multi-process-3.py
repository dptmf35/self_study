import time
from concurrent import futures

def test(x) :
    sum_ = 1
    print(x)
    for i in range(x[0], x[1]) :
        sum_ *= i
    print('Work Finished !')
    return sum_

if __name__ == '__main__' :
    start =time.time()
#
#     with futures.ProcessPoolExecutor() as e :
#         sub = [(i, i+999) for i in range(1, 10000, 1000)]
#         result = e.map(test ,sub)
#
#     print(list(result))
#
#     print(f'Run Time : {time.time() - start :.4f}') # --> multi-thread

    s = 1
    for i in range(1, 10000) :
        s *= i
    print(f'Run Time : {time.time() - start :.4f}')