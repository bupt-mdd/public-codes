# -*- coding: utf-8 -*-

import socket
socket.setdefaulttimeout(0.1)
#测试连接
def test(configure):
    import paramiko
    try:
        server = configure['SERVER']
        port = configure['PORT']
        user = configure['USER']
        password = configure['PWD']
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server, port=port, username=user, password=password)
        return "True"
    except:
        return "False"

if __name__ == '__main__':
    configure = {
        'SERVER': '10.108.114.253',
        'PORT': 3306,
        'USER': "root",
        "PWD": "hxm12345",
    }
    test(configure)