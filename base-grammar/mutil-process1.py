import multiprocessing
import os


def run_task(str):
    print('child process %s is running ... , data is %s ' % (os.getpid(), str))


if __name__ == '__main__':
    # 多进程
    for i in range(5):
        p = multiprocessing.Process(target=run_task, args=(str(i),))
        p.start()
        p.join()
