# coding:utf-8

import paramiko

from kvm.common import OK, NO, defaultRule

class KVM_Benchmark_lib(object):

    def __init__(self, ssh, ssh1, rule=None):
        self.functionList = [
            self.fun1_1_1,  # 0
            self.fun1_1_2,  # 1
            self.fun1_1_3,  # 2
            self.fun1_1_4,  # 3
            self.fun1_1_5,  # 4
            self.fun1_1_6,  # 5
            self.fun1_1_7,  # 6
        ]

        # ssh对象，用于远程(ESXI)执行命令
        self.ssh = ssh

        #ssh对象,用于本地(server)执行命令
        self.ssh1 = ssh1

        # 检测规则列表
        self.rule = rule

        # 检测结果列表
        self.resultList = [3 for i in range(len(self.functionList))] #3=NOTKNOWN

        # 直接启动各项检查，调用run()函数
        self.run()

    def run(self):
        # 　根据规则检测数据库
        if not self.rule:
            self.rule = defaultRule
        for i in range(len(self.functionList)):
            if self.rule[i]:
                self.resultList[i] = self.functionList[i]()

    def getResult(self):
        # 返回结果
        return self.resultList


# Recommendations
    # 1、base ESXi install.
    def fun1_1_1(self):
        # Disable unused filesystems
        try:
            stdin, stdout, stderr = self.ssh.exec_command('cat /etc/libvirt/libvirtd.conf | grep listen_tls')
            result = stdout.read()
            if result.find('listen_tls = 0') != -1:
                stdin, stdout, stderr = self.ssh.exec_command('cat /etc/libvirt/libvirtd.conf | grep listen_tcp')
                result = stdout.read()
                if result.find('listen_tcp = 1') != -1:
                    stdin, stdout, stderr = self.ssh.exec_command('cat /etc/libvirt/libvirtd.conf | grep auth_tcp')
                    result = stdout.read()
                    if result.find('auth_tcp = "sasl"') != -1:
                        return OK
                    else:
                        return NO
                else:
                   return NO
            else:
                return NO
        except:
            return OK

    def fun1_1_2(self):
        pass

    def fun1_1_3(self):
        # Ensure mounting of jffs2 filesystems is disabled
        try:
            stdin, stdout, stderr = self.ssh.exec_command('getenforce')
            result = stdout.read()
            if result.find('Enforcing') != -1:
                return OK
            else:
                return NO
        except:
            return OK

    def fun1_1_4(self):
        # Ensure mounting of hfs filesystems is disabled
        try:
            stdin, stdout, stderr = self.ssh.exec_command('ps -wwC qemu-kvm -o label,command')
            lines = stdout.readlines()
            count = 0
            if len(lines) == 0:  # 执行命令结果为空
               ++count
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue
            stdin, stdout, stderr = self.ssh.exec_command('ll -aZ /var/lib/libvirt/images/')
            lines = stdout.readlines()
            if len(lines) == 0 and count == 1:  # 执行命令结果为空
                return OK
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue
            return reslines
        except:
            return OK

    def fun1_1_5(self):
        # Ensure mounting of hfsplus filesystems is disabled
        try:
            stdin, stdout, stderr = self.ssh.exec_command('cat /etc/libvirt/libvirtd.conf | grep audit_level')
            result = stdout.read()
            if result.find('audit_level == 1') != -1:
                stdin, stdout, stderr = self.ssh.exec_command('cat /etc/libvirt/libvirtd.conf | grep audit_logging')
                result = stdout.read()
                if result.find('audit_logging = 1') != -1:
                    return OK
                else:
                    return NO
            else:
                return NO
        except:
            return OK

    def fun1_1_6(self):
        list = []
        try:
            stdin, stdout, stderr = self.ssh.exec_command('ebtables –L')
            line = stdout.readline()
            while line:
                line = line.strip('\n')
                list.append(line)
                line = stdout.readline()
            for i in range(len(list)):
                if list[i].find('FORWARD') != -1:
                    if list[i+1].find('vnet') != -1 and list[i+1].find('DROP') != -1:
                        return OK
            return NO
        except:
            return OK

    def fun1_1_7(self):
        try:
            stdin, stdout, stderr = self.ssh.exec_command('qemu-img --help | grep version')
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue
            return reslines
        except:
            return OK

if __name__ == '__main__':
    #连接远程ESXI服务器
    #ssh = paramiko.SSHClient()
    # ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # ssh.connect(hostname='10.108.115.134', port=22, username='root', password='12345678')
    #连接本地服务器（server）
    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh1.connect(hostname='10.108.114.24', port=22, username='root', password='ics123')

    test = KVM_Benchmark_lib(ssh1, ssh1,  None)
    print(test.getResult())
