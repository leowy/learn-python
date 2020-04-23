import threading
import time
import random


def run_task(urls):
    print('child thread (%s) is running ...' % threading.current_thread().name)
    for url in urls:
        print('%s ----> %s ' % (threading.current_thread().name, url))
        time.sleep(random.random())
    print('%s ended.' % threading.current_thread().name)


if __name__ == '__main__':
    # for i in range(5):
    t = threading.Thread(target=run_task, args=(['url1', 'url2', 'url3', 'url4'],))
    # t = threading.Thread(target=run_task, name='name' + str(i), args=([str(i)],))
    t.start()
    t.join()
