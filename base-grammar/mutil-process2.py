from multiprocessing import Pool
import os
import time
import random


def run_task(str):
    print('subprocess %s is running ...., data is %s ' % (os.getpid(), str))
    time.sleep(random.random())
    print('subprocess %s is end .' % os.getpid())


if __name__ == '__main__':
    # 多进程之进程池
    print('Current process %s.' % os.getpid())
    p = Pool(processes=3)
    for i in range(5):
        p.apply_async(func=run_task, args=([str(i), ]))
    print('waiting for all subprocesses done ...')
    p.close()
    p.join()
