# coding:utf-8
# elasticsearch未授权批量检测脚本
# author：ske
# usage: python3 elasticsearch_unauth_multi.py /root/unAuth/elasticsearch/us.txt 30
# 默认端口9200
# es_ok_ip存放可以对es增删改查的IP， es_ok_nodes存放泄露节点的IP

import threading
from queue import Queue
import sys
from elasticsearch import Elasticsearch
import requests
import json

port = 9200        # 检测其他端口，请修改此处
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
                self.check_elasticsearch(ip)
                self.get_node(ip)

    # 检测是否可以对es增删改查操作
    def check_elasticsearch(self, ip):
        try:
            es = Elasticsearch("{}:{}".format(ip, port), timeout=5)  # 连接Elasticsearch,延时5秒
            es.indices.create(index='unauth_text')
            es.index(index="unauth_text", doc_type="test-type", id=2, body={"text": "text"})
            es.get(index="unauth_text", doc_type="test-type", id=2)
            es.indices.delete(index='unauth_text')
            print('[ok] -> [{}] {} -> 存在ElasticSearch未授权漏洞'.format(self.num, ip))
            self.save_ip(ip, port)
        except Exception as e:
            error = e.args
            print('[-] -> [{}] {}  error : {}'.format(self.num, ip, error))

    def save_ip(self, ip, port):
        with open('es_ok_ip.txt', 'at') as f:
            f.writelines('{}:{}\n'.format(ip, port))

    # 获取节点信息
    def get_node(self, ip):
        try:
            text = json.loads(requests.get(url='http://{}:{}/_nodes'.format(ip, port), timeout=5).text)
            nodes_total = text['_nodes']['total']
            nodes = list(text['nodes'].keys())
            print('[ok] -> [{}] {} -> [{}] : {}'.format(self.num, ip, nodes_total, nodes))
            self.save_nodes(ip, port, nodes)
        except Exception as e:
            error = e.args
            print('[-] -> [{}] {}  error : {}'.format(self.num, ip, error))

    def save_nodes(self, ip, port, nodes):
        with open('es_ok_nodes.txt', 'at') as f:
            f.writelines('{}:{} -> {}\n'.format(ip, port, nodes))

def scan_thread():
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
    path = sys.argv[1]  # /root/unAuth/elasticsearch/us.txt
    thread_num = int(sys.argv[2])
    get_ip()
    scan_thread()