# -*- coding: utf-8 -*-

import socket

socket.setdefaulttimeout(0.1)

def main(IP):
    name = ""
    type = ""
    protocolType = ""
    protocolPort = ""
    serviceType = "MYSQL"
    servicePort = "3306"

    device = ["", IP, "", "", "", "", ""]

    try:
        # get host, will raise error if not found
        # name = socket.gethostbyaddr(IP)[0]
        device[0] = r"ipaddr-" + IP

        # type, protocolType, protocolPort
        device[2] = type
        device[3] = protocolType
        device[4] = protocolPort

        # find if there is MSSQL Service running
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn = s.connect_ex((IP, int(servicePort)))
        if conn == 0:
            s.close()
            device[5], device[6] = serviceType, servicePort
        else:
            # if not found
            return None

        # all OK, return device
        return device

    except Exception as e:
        # if host not found
        return None


#测试连接
def test(configure):
    import paramiko
    try:
        server = configure['SERVER']
        user = configure['USER']
        password = configure['PWD']
        port = configure['PORT']
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname=server, username=user, password=password, port=str(port))
        return "True"
    except:
        return "False"
