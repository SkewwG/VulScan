# -*- coding:utf-8 -*-
# author:ske
# python3 zookeeper_unauth.py 107.191.40.46 2181

from kazoo.client import KazooClient
import sys

# 检测是否存在未授权漏洞
def check_zookeeper():
    try:
        zk = KazooClient(hosts='{}:{}'.format(ip, port))
        zk.start()
        chidlrens = zk.get_children('/')
        if len(chidlrens) > 0:
            print('[ok] -> {}:{}   {}'.format(ip, port, chidlrens))
        zk.stop()
    except Exception as e:
        zk.stop()
        error = e.args
        print('[-] error: {}'.format(error))

if __name__ == '__main__':
    ip = sys.argv[1]
    port = sys.argv[2]
    check_zookeeper()
