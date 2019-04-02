#coding:utf-8

import docker.common
import paramiko
from docker.lib import Docker_Benchmark_lib
import json

class Docker_Benchmark_Main(object):

    def __init__(self, server, user, password, port):
        self.server = server
        self.user = user
        self.password= password
        self.port = port
        self.ssh = paramiko.SSHClient()
        self.result = ''

        if not self.connect():
            self.connectOK = False
        else:
            self.connectOK = True

        self.run()

    def run(self):
        if self.connectOK:
            docker = Docker_Benchmark_lib(ssh=self.ssh)
            self.result = docker.getResult()
            pass
        else:
            pass

    def connect(self):
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.server, username=self.user, password=self.password, port=self.port)
            return True
        except Exception as e:
            return False

    def get_result(self):
        return self.result

    def get_json_result(self):
        if self.get_result()==None:
            return None
        container = self.get_result()
        ret_json = json.dumps(container, indent=7)
        return ret_json