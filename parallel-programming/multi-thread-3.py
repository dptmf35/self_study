import time
from concurrent import futures

def test(x) :
    sum_ = 0
    for i in range(x[0], x[1]) :
        sum_ *= i
    print('Work Finished !')
    return sum_

if __name__ == '__main__' :
    start =time.time()

    want_range = 10000

    with futures.ThreadPoolExecutor() as e :
        sub = [(i, i+999) for i in range(1, 10000, 1000)]
        result = e.map(test ,sub)

    print(sum(result))

    print(f'Run Time : {time.time() - start :.4f}') # --> multi-thread