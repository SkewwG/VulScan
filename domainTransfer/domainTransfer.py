# -*- coding:utf-8 -*-
#!/usr/bin/env python
# -*- coding=utf-8
# 检测是否存在域传送漏洞
# author:ske
# usage:python domainTransfer.py xxx.com

import dns.resolver
import dns.zone
import sys

domain = sys.argv[1]
try:
    dnsResolver = dns.resolver.Resolver()
    dnsResolver.timeout = 10
    ns = dnsResolver.query(domain, 'NS')                # 查询NS
    isVul = False
    if ns:                                              # 如果目标域名有nameserver
        for domain_dns in ns:                           # 遍历每个nameserver
            xfr = dns.query.xfr(str(domain_dns), domain, timeout=10, lifetime=10)
            if dns.zone.from_xfr(xfr):
                isVul = True
                print('[+] dig @{} {} axfr'.format(domain_dns, domain))
        if not isVul:
            print('[-] {} 不存在域传送漏洞'.format(domain))
    else:
        print('[-] {} 没有nameserver'.format(domain))
except Exception as e:
    print('[-] {} Error:{}'.format(domain, e.args))
