#coding:utf-8

import paramiko
from kubernetes.lib import Kubernetes_Benchmark_lib
import json

class Kubernetes_Benchmark_Main(object):
    #
    # ssh = None
    # connectOK = True
    # result = None   #返回结果lisr

    def __init__(self, server, user, password, port, nodetype):

        self.server = server
        self.user = user
        self.password = password
        self.port = port
        self.nodetype = nodetype
        self.ssh = paramiko.SSHClient()
        self.result=''

        if not self.connect():
            self.connectOK = False
        else:
            self.connectOK = True

        # 启动检测函数
        self.run()

    def run(self):
        if self.connectOK:
            #　如果可以连接ssh　，　执行基线检测函数
            k8s = Kubernetes_Benchmark_lib(ssh=self.ssh, check_type=self.nodetype)
            self.result = k8s.getResult()
            pass
        else:
            pass

    def connect(self):
        try:
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.server, username=self.user, password=self.password, port=str(self.port))
            return True
        except Exception as e:
            print('error:', e)
            return False

    def getResult(self):
        # 返回检测结果
        return self.result

    def getJsonResult(self):
        if self.getResult() == None:  # 没有结果
            return None
        resInd = self.getResult() #结果list
        jsonData = []

        for i in range(len(resInd)):
            # print resInd[i][0], resInd[i][1]
            jsonData.append(
                {"index": resInd[i][0], "result": resInd[i][1], "config": resInd[i][2]} #索引是配置项的下标，数据是配置项的内容
            )
        # resJSON = json.dumps(jsonData,indent = 7).decode('unicode-escape')
        resJSON = json.dumps(jsonData, indent=7)
        return resJSON
