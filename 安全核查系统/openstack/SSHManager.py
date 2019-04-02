#coding:utf-8

import paramiko
import operator

class SSHManager(object):

    serverIP = "10.108.114.24"
    port = "2222"
    userName = "root"
    password = "123456"

    ssh = None

    def init(self, serverIP, port, userName, password):
        self.serverIP = serverIP
        self.port = port
        self.userName = userName
        self.password = password

        return self.connect()

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.serverIP,
                        port=self.port,
                        username=self.userName,
                        password=self.password)

            return True
        except Exception as e:
            #print('error:', e)
            return False

    def ssh_cmd(self, cmd):
        result = ""
        try:
            stdin, stdout, stderr = self.ssh.exec_command(cmd)
            result = stdout.read()
        except:
            return "FFF"
        list = result.decode('gb2312').splitlines()
        if len(list) == 0:
            return ""
        else:
            return list[0]

    def closeSession(self):
        self.ssh.close()
        self.ssh = None
        self.serverIP = None
        self.port = None
        self.userName = None
        self.password = None