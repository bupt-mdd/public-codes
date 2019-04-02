#coding:utf-8

import paramiko
from vmware import common
from vmware.lib import VMware_Benchmark_lib
import json

class VMware_Benchmark_Main(object):
    server = "10.108.115.134"
    port = 22
    user = "root"
    password = "12345678"

    ssh = None
    ssh1 = None
    connectOK = True
    rule = None
    result = None   #返回结果lisr

    def __init__(self, rule=None, server='10.108.115.134', port=22, user='root', password='12345678'):

        self.server = server
        self.port = port
        self.user = user
        self.password = password

        if not self.connect():
            self.connectOK = False
        else:
            self.rule = rule
        # 启动检测函数
        self.run()

    def run(self):
        if self.connectOK:
            #　如果可以连接ssh　，　执行基线检测函数
            vmwareLib = VMware_Benchmark_lib(self.ssh, self.ssh1, self.rule,self.server,self.user,self.password)
            self.result = vmwareLib.getResult()
            pass
        else:
            pass

    def connect(self):
        try:
            self.ssh = paramiko.SSHClient()
            self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh.connect(hostname=self.server,
                        port=self.port,
                        username=self.user,
                        password=self.password)

            self.ssh1 = paramiko.SSHClient()
            self.ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.ssh1.connect(hostname='127.0.0.1',
                             port=22,
                             username='ics',
                             password='123456')

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
        res = common.reportContent #字典类型（dict）
        jsonData = []
        for i in range(len(resInd)):
            res[common.reportIndex[i]]['checkRes'] = resInd[i]
            if resInd[i] == common.NOTKNOWN:   #纯人工核查(checkTpye=3)
                jsonData.append(
                    {"index": common.reportIndex[i], "checkType": 3, "data": res[common.reportIndex[i]]}  # 索引是配置项的下标，数据是配置项的内容
                )
            elif resInd[i] == common.NO or resInd[i] == common.OK: #命令（自动化）核查(checkType=1)
                jsonData.append(
                    {"index": common.reportIndex[i], "checkType": 1, "data": res[common.reportIndex[i]]}  # 索引是配置项的下标，数据是配置项的内容
                )
            else: #半自动化（有命令参与）的人工核查(checkType=2)
                jsonData.append(
                    {"index": common.reportIndex[i], "checkType": 2, "data": res[common.reportIndex[i]]}  # 索引是配置项的下标，数据是配置项的内容
                )
        resJSON = json.dumps(jsonData, ensure_ascii=False, indent=7)
        return resJSON


# 测试　main
if __name__ == "__main__":
    #vmwareBenchmark = VMware_Benchmark_Main(server='10.108.115.134')
    vmwareBenchmark = VMware_Benchmark_Main(server='10.108.115.134', port = 22, user = 'root', password = '12345678')
    result = vmwareBenchmark.getResult()
    resultJson = vmwareBenchmark.getJsonResult()
    print(result)
    print(resultJson)
    #print mysqlBM.getJsonResult()
