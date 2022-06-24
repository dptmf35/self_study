import time
import multiprocessing

def test() :
    time.sleep(1)
    print('Work Finished!')

# if __name__ == '__main__' :
#     start = time.time()
#
#     for i in range(10) :
#         test()
#
#     print(f'Run Time : {time.time() - start :.4f}') ---> normal

if __name__ == '__main__' :
    start =time.time()
    processes = []
    for i in range(10) : # 반복 스텝마다 프로세스 생성 및 실행
        p = multiprocessing.Process(target=test)
        p.start()
        processes.append(p)

    for process in processes :
        process.join() # 실행 완료된 쓰레드를 합침

    # threads = [None] * 10
    #
    # for i in range(10) : # 반복 스텝마다 프로세스 생성 및 실행
    #     threads[i] = threading.Thread(target=test, args=[i])
    #     threads[i].start()
    #
    # for i in range(10) :
    #     threads[i].join()


    print(f'Run Time : {time.time() - start :.4f}') # --> multi-thread