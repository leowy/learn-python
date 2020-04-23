from multiprocessing import Pipe, Process
import os
import time
import random


def proc_recv(pipe):
    while True:
        print('Process(%s) receive : %s' % (os.getpid(), pipe.recv()))


def proc_send(pipe, urls):
    print('Process(%s) is running ...' % os.getpid())
    for url in urls:
        pipe.send(url)
        print('Process(%s) send : %s ' % (os.getpid(), url))
        time.sleep(random.random())


if __name__ == '__main__':
    # 多进程之进程通信Pipe
    p = Pipe()
    recv = Process(target=proc_recv, args=(p[0],))
    send = Process(target=proc_send, args=(p[1], ['url' + str(i) for i in range(10)]))
    recv.start()
    send.start()
    send.join()
    recv.terminate()
