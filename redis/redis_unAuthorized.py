# coding:utf-8
# 未授权
import redis
import sys

ip = sys.argv[1]
r = redis.Redis(host=ip, port=6379)
r.set('name', 'test')
print(r.get('name'))