# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding=utf-8
# 批量检测是否存在域传送漏洞
# author:ske
# usage:python domainTransfer.py domain.txt 10

import threading
from queue import Queue
import sys
import dns.resolver
import dns.zone

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
                domain = self.q.get()
                self.check_domainTransfer(domain)

    def check_domainTransfer(self, domain):
        try:
            dnsResolver = dns.resolver.Resolver()
            dnsResolver.timeout = 10
            ns = dnsResolver.query(domain, 'NS')  # 查询NS
            isVul = False
            results = []
            if ns:  # 如果目标域名有dns服务器
                for domain_dns in ns:  # 遍历每个dns服务器
                    xfr = dns.query.xfr(str(domain_dns), domain, timeout=10, lifetime=10)
                    if dns.zone.from_xfr(xfr):
                        isVul = True
                        results.append('[+] dig @{} {} axfr'.format(domain_dns, domain))
                        print('[+] -> [{}] :  dig @{} {} axfr'.format(self.num, domain_dns, domain))
                if isVul:
                    self.save(results)
                else:
                    print('[-] -> [{}] : {} 不存在域传送漏洞'.format(self.num, domain))
            else:
                print('[-] -> [{}] : {} 没有dns服务器'.format(self.num, domain))
        except Exception as e:
            print('[-] -> [{}] : {} Error:{}'.format(self.num, domain, e.args))

    def save(self, results):
        with open('success.txt', 'at') as f:
            for result in results:
                f.writelines(result + '\n')

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