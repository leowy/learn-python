from multiprocessing import Process, Queue
import os
import time
import random


def proc_write(q, urls):
    print('Process(%s) is running .' % os.getpid())
    for url in urls:
        print('Put %s to queue ...' % url)
        q.put(url)
        time.sleep(random.random() * 3)


def proc_read(q):
    print('Process(%s) is running .' % os.getpid())
    while True:
        url = q.get(True)
        print('Get %s from queue ...' % url)


if __name__ == '__main__':
    # 多线程 之 线程通信 Queue
    queue = Queue()
    proc_write1 = Process(target=proc_write, args=(queue, ['url1', 'url2', 'url3']))
    proc_write2 = Process(target=proc_write, args=(queue, ['url4', 'url5', 'url6']))
    proc_reader = Process(target=proc_read, args=(queue,))
    proc_write1.start()
    proc_write2.start()
    proc_reader.start()
    proc_write1.join()
    proc_write2.join()
    proc_reader.terminate()
