# coding:utf-8
# mongodb未授权批量检测脚本
# author：ske
# usage: python3 mongodb_unauth_multi.py /root/unAuth/mongodb/us.txt 10
# 默认端口27017和28017

import threading
from queue import Queue
import sys
from pymongo import MongoClient

port = 27017        # 检测其他端口，请修改此处
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
                self.check_mongodb(ip)

    def check_mongodb(self, ip):
        try:
            conn = MongoClient(ip, port, socketTimeoutMS=5000)  # 连接MongoDB,延时5秒
            dbs = conn.database_names()
            print('[ok] -> [{}] {}:{}  database_names : {}'.format(self.num, ip, port, dbs))
            conn.close()
            self.save(ip, port)
        except Exception as e:
            error = e.args
            print('[-] -> [{}] {}:{}  error : {}'.format(self.num, ip, port, error))

    def save(self, ip, port):
        with open('mongodb_success.txt', 'at') as f:
            f.writelines('{}:{}\n'.format(ip, port))

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
    path = sys.argv[1]  # /root/unAuth/mongodb/us.txt
    thread_num = int(sys.argv[2])
    get_ip()
    scan_thread()