import time
from concurrent import futures

def test() :
    time.sleep(1)
    return 'Work Finished!'


if __name__ == '__main__' :
    start = time.time()

    with futures.ThreadPoolExecutor() as e :
        results = [e.submit(test) for i in range(10)]

    for f in futures.as_completed(results) :
        print(f.result())

    print(f'Run Time : {time.time() - start :.4f}')  # --> multi-thread

