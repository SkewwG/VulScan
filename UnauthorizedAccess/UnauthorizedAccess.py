# 未授权访问漏洞测试
import requests

# test url : http://www.china-nfh.com/admin/left.aspx

Login_url = input('Login_url:')
Suffix = input('Suffix:')

url = r'http://www.china-nfh.com'

url += '/admin/left.aspx'

response = requests.get(url)
ret = response.status_code
print(ret)