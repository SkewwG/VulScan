# coding:utf-8
# elasticsearch未授权检测脚本
# author：ske
# usage: python3 elasticsearch_unauth.py ip port
# 默认端口9200
# http://localhost:9200/_plugin/head/ web管理界面
# http://localhost:9200/_cat/indices
# http://localhost:9200/_river/_search 查看数据库敏感信息
# http://localhost:9200/_nodes 查看节点数据

import sys
from elasticsearch import Elasticsearch
import requests
import json

ip = sys.argv[1]
port = int(sys.argv[2]) # 9200
try:
    es = Elasticsearch("{}:{}".format(ip, port), timeout=5)  # 连接Elasticsearch,延时5秒
    es.indices.create(index='unauth_text')
    print('[+] 成功连接 ：{}'.format(ip))
    print('[+] {} -> 成功创建测试节点unauth_text'.format(ip))
    es.index(index="unauth_text", doc_type="test-type", id=2, body={"text": "text"})
    print('[+] {} -> 成功往节点unauth_text插入数据'.format(ip))
    ret = es.get(index="unauth_text", doc_type="test-type", id=2)
    print('[+] {} -> 成功获取节点unauth_text数据 : {}'.format(ip, ret))
    es.indices.delete(index='unauth_text')
    print('[+] {} -> 清除测试节点unauth_text数据'.format(ip))
    print('[ok] {} -> 存在ElasticSearch未授权漏洞'.format(ip))

    print('尝试获取节点信息：↓')
    text = json.loads(requests.get(url='http://{}:{}/_nodes'.format(ip, port), timeout=5).text)
    nodes_total = text['_nodes']['total']
    nodes = list(text['nodes'].keys())
    print('[ok] {} -> [{}] : {}'.format(ip, nodes_total, nodes))

except Exception as e:
    error = e.args
    print('[-] -> {}  error : {}'.format(ip, error))
