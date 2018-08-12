# coding:utf-8
# mongodb未授权检测脚本
# author：ske
# usage: python3 mongodb_unauth.py ip port
# 默认端口28017和27017

from pymongo import MongoClient
import sys

ip = sys.argv[1]
port = int(sys.argv[2])

try:
    conn = MongoClient(ip, port, socketTimeoutMS=5000)  # 连接MongoDB,延时5秒
    dbs = conn.database_names()
    print('[ok] -> {}:{}  database_names : {}'.format(ip, port, dbs))
    conn.close()
except Exception as e:
    error = e.args
    print('[-] -> {}:{}  error : {}'.format(ip, port, error))
