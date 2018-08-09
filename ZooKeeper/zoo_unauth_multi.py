# coding:utf-8
# 检验zookeeper是否存在未授权
# author:ske

import threading
from queue import Queue
from kazoo.client import KazooClient
import sys

event = threading.Event()
event.set()
q = Queue(-1)

class multi_thread(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q

    def run(self):
        while event.is_set():                                               #is_set()查看信号，由于之前设置了Flag为True，所以为真
            if self.q.empty():                                              #如果队列空了就跳出循环，终止
                event.clear()
            else:                                                           #如果队列不为空
                ip = self.q.get()
                self.check_zookeeper(ip)

    def check_zookeeper(self, ip):
        try:
            zk = KazooClient(hosts='{}:2181'.format(ip))
            zk.start()
            chidlrens = zk.get_children('/')
            if len(chidlrens) > 0:
                print('[ok] -> [{}] {}:2181   {}'.format(self.num, ip, chidlrens))
                self.save(ip)
            zk.stop()
        except Exception as e:
            zk.stop()
            error = e.args
            print('[-] -> [{}]  error: {}'.format(self.num, error))

    def save(self, ip):
        with open('success.txt', 'at') as f:
            f.writelines(ip + '\n')

def scan_thread():                                                         #参数是队列
    threads = []
    for num in range(1,thread_num+1):
        t = multi_thread(num,q)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def get_ip():
    with open(path, 'rt') as f:
        for ip in f.readlines():
            q.put(ip.strip())

if __name__ == '__main__':
    path = sys.argv[1]  # /root/unAuth/zookeeper/us.txt
    thread_num = int(sys.argv[2])
    get_ip()
    scan_thread()