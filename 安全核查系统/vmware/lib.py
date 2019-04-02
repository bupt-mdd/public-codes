# coding:utf-8

import paramiko
from vmware.common import OK, NO, defaultRule

class VMware_Benchmark_lib(object):
    server = "10.108.115.134"
    user = "root"
    password = "12345678"
    def __init__(self, ssh, ssh1, rule=None, server="10.108.115.134", user="root", password="12345678"):
        self.functionList = [
            self.fun1_1,  # 0
            self.fun1_2,  # 1
            self.fun1_3,  # 2
            self.fun2_1,  # 3
            self.fun2_2,  # 4
            self.fun2_3,  # 5
            self.fun2_4,  # 6
            self.fun2_5,  # 7
            self.fun2_6,  # 8
            self.fun2_7,  # 9
            self.fun3_1,  # 10
            self.fun3_2,  # 11
            self.fun3_3,  # 12
            self.fun4_1,  # 13
            self.fun4_2,  # 14
            self.fun4_3,  # 15
            self.fun4_4,  # 16
            self.fun5_1,  # 17
            self.fun5_2,  # 18
            self.fun5_3,  # 19
            self.fun5_4,  # 20
            self.fun5_5,  # 21
            self.fun5_6,  # 22
            self.fun5_7,  # 23
            self.fun5_8,  # 24  1
            self.fun5_9,  # 25
            self.fun5_10,  # 26  1
            self.fun6_1,  # 27
            self.fun6_2,  # 28  1
            self.fun6_3,  # 29  1
            self.fun6_4,  # 30  1
            self.fun7_1,  # 31   1
            self.fun7_2,  # 32   1
            self.fun7_3,  # 33   1
            self.fun7_4,  # 34   1
            self.fun7_5,  # 35   1
            self.fun7_6,  # 36
            self.fun8_1_1,  # 37   1
            self.fun8_1_2,  # 38   1
            self.fun8_2_1,  # 39   1
            self.fun8_2_2,  # 40
            self.fun8_2_3,  # 41   1
            self.fun8_2_4,  # 42   1
            self.fun8_2_5,  # 43   1
            self.fun8_2_6,  # 44   1
            self.fun8_2_7,  # 45   1
            self.fun8_3_1,  # 46   1
            self.fun8_3_2,  # 47   1
            self.fun8_3_3,  # 48   1
            self.fun8_3_4,  # 49  1
            self.fun8_4_1,  # 50
            self.fun8_4_2,  # 51   1
            self.fun8_4_3,  # 52
            self.fun8_4_4,  # 53
            self.fun8_4_5,  # 54
            self.fun8_4_6,  # 555
            self.fun8_4_7,  # 56
            self.fun8_4_8,  # 57   1
            self.fun8_4_9,  # 58
            self.fun8_4_10,  # 59
            self.fun8_4_11,  # 60
            self.fun8_4_12,  # 61
            self.fun8_4_13,  # 62
            self.fun8_4_14,  # 63  1
            self.fun8_4_15,  # 64
            self.fun8_4_16,  # 65
            self.fun8_4_17,  # 66
            self.fun8_4_18,  # 67
            self.fun8_4_19,  # 68
            self.fun8_4_20,  # 69   1
            self.fun8_4_21,  # 70
            self.fun8_4_22,  # 71
            self.fun8_4_23,  # 72
            self.fun8_4_24,  # 73
            self.fun8_4_25,  # 74
            self.fun8_4_26,  # 75   1
            self.fun8_4_27,  # 76
            self.fun8_4_28,  # 77
            self.fun8_4_29,  # 78
            self.fun8_5_1,  # 79
            self.fun8_6_1,  # 80
            self.fun8_6_2,  # 81
            self.fun8_6_3,  # 82
            self.fun8_7_1,  # 83
            self.fun8_7_2,  # 84
            self.fun8_7_3,  # 85
            self.fun8_7_4,  # 86
            self.fun9_1,

        ]

        # ssh对象，用于远程(ESXI)执行命令
        self.ssh = ssh

        #ssh对象,用于本地(server)执行命令
        self.ssh1 = ssh1

        # 检测规则列表
        self.rule = rule

        self.server = server

        self.user = user

        self.password = password

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

    '''
          参考基线文档：CIS_VMware_ESXi_5.5_Benchmark_v1.2.0.pdf
          部分检测点暂未实现
    '''
# Recommendations
    # 1、base ESXi install.
    def fun1_1(self):
        #Keep ESXi system properly patched
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/1_1.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
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

    def fun1_2(self):
        # Verify Image Profile and VIB Acceptance Levels
        try:
            stdin, stdout, stderr = self.ssh.exec_command('esxcli software acceptance get')
            result = stdout.read()
            if result == 'VMware Certified' or result == 'VMware Supported' or result == 'PatnerSupported':
                return OK
            else:
                return NO
        except:
            return OK

    def fun1_3(self):
        # Verify no unauthorized kernel modules are loaded on the host
        try:
            stdin, stdout, stderr = self.ssh.exec_command('esxcli system module list')
            result = stdout.read()
            for module in result:
                stdin, stdout, stderr = ssh.exec_command('esxcli system module get -m ' + module)
                result = stdout.read()
                if result == '' or len(result) == 0:
                    return NO
            return OK

        except:
            return OK

    # related to ESXi communication
    def fun2_1(self):###
        #Configure NTP time synchronization
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password+ '} | &{Get-VMHost | Select Name, @{N="NTPSetting", E={$_ | Get-VMHostNtpServer}}}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('Start and stop with host') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun2_2(self):
        #Configure the ESXi host firewall to restrict access to services running on the host
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/2_2.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            if n==3 :
                return NO #不通过
            return OK  # 通过
        except:
            return OK

    def fun2_3(self):
        # Disable Managed Object Browser (MOB)
        try:
            stdin, stdout, stderr = self.ssh.exec_command('vim-cmd proxysvc/service_list')
            result = stdout.read()
            str = str(result, encoding="utf-8")
            res = str.find('serverNamespace = "/mob", \n      accessMode = "httpsWithRedirect", \n      pipeName = "/var/run/vmware/proxy-mob",')
            if res != -1:
                return NO
            return OK
        except:
            return OK

    def fun2_4(self):
        #Do not use default self-signed certificates for ESXi communication
        pass

    def fun2_5(self):
        # Ensure proper SNMP configuration
        try:
            stdin, stdout, stderr = self.ssh.exec_command('esxcli system snmp get')
            result = stdout.read()
            str = str(result, encoding="utf-8")
            res = str.find('Enable: false')
            if res != -1:
                return OK
        except:
            return OK

    def fun2_6(self):
        #Prevent unintended use of dvfilter network APIs
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/2_6.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].strip() == 'Net.DVFilterBindIpAddress :':  # 为空值
                    return OK #通过
                else:
                    continue
            return NO  # 不通过
        except:
            return OK

    def fun2_7(self):
        #Remove expired or revoked SSL certificates from the ESXi server
        pass

    # related to ESXi's logging capabilities
    def fun3_1(self):
        # Configure a centralized location to collect ESXi host core dumps
        try:
            stdin, stdout, stderr = self.ssh.exec_command('esxcli system coredump network get')
            result = stdout.read()
            str = str(result, encoding="utf-8")
            res = str.find('Enabled: true')
            if res != -1:
                return  OK
            return NO
        except:
            return OK

    def fun3_2(self):
        #Configure persistent logging for all ESXi host
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/3_2.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue
            n = len(reslines)
            for i in range(2, n):
                if reslines[i].strip() == 'Syslog.global.logDir :':  # 为空值
                    return OK   #通过
                elif reslines[i].strip().find("scratch"):
                    return NO
                else:
                    continue
            return OK  # 通过
        except:
            return OK

    def fun3_3(self):
        #Configure remote logging for ESXi hosts
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/3_3.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].strip() == 'Syslog.global.logHost :':  # 为空值
                    return NO #不通过
                else:
                    continue
            return OK  # 不通过
        except:
            return OK

    #related to ESXi access management.
    def fun4_1(self):
        #Create a non-root user account for local admin access
        pass

    def fun4_2(self):
        #Establish a password policy for password complexity
        pass

    def fun4_3(self):
        # Use Active Directory for local user authentication
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VMHost | Get-VMHostAuthentication | Select VmHost, Domain, DomainMembershipStatus}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue
            n = len(reslines)
            for i in range(2, n):
                if len(reslines[i].strip()) <= 15:
                    return NO
            return OK
        except:
            return OK

    def fun4_4(self):
        #Verify Active Directory group membership for the "ESX Admins" group
        pass

    #related to ESXi consoles
    def fun5_1(self):
        #Disable DCUI to prevent local administrative control
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/5_1.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('off') != -1 and reslines[i].find('Policy') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun5_2(self):
        #Disable ESXi Shell unless needed for diagnostics or troubleshooting
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/5_2.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('off') != -1 and reslines[i].find('Policy') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun5_3(self):
        #Disable SSH
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/5_3.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('off') != -1 and reslines[i].find('Policy') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun5_4(self):
        # Limit CIM Access
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VMHostAccount}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            result = stdout.read()
            if result != '':
                return OK
            return NO
        except:
            return OK

    def fun5_5(self):
        #Enable lockdown mode to restrict remote access
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/5_5.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('Lockdown') != -1 and reslines[i].find('true') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue
            return NO  # 不通过
        except:
            return OK

    def fun5_6(self):
        #Remove keys from SSH authorized_keys file
        pass

    def fun5_7(self):
        #Set a timeout to automatically terminate idle ESXi Shell and SSH sessions
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/5_7.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('300') != -1 and reslines[i].find('UserVars.ESXiShellInteractiveTimeOut') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun5_8(self):
        #Set a timeout for Shell Services
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/5_8.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('3600') != -1 and reslines[i].find('UserVars.ESXiShellTimeOut') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun5_9(self):
        # Set DCUI.Access to allow trusted users to override lockdown mode
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VMHost | Get-AdvancedSetting -Name DCUI.Access}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            result = stdout.read()
            if result != '':
                return OK
            return NO
        except:
            return OK

    def fun5_10(self):
        #Verify contents of exposed configuration files
        pass

    #related to ESXi disk an storage-related settings#########################################待定
    def fun6_1(self):
        #Enable bidirectional CHAP authentication for iSCSI traffic.
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/6_1.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('ChapType') != -1 and reslines[i].find('bidirectional') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun6_2(self):
        #Ensure uniqueness of CHAP authentication secrets
        pass

    def fun6_3(self):
        #Mask and zone SAN resources appropriately
        pass

    def fun6_4(self):
        #Zero out VMDK files prior to deletion
        pass

    #related to configuring vNetwork.
    def fun7_1(self):
        #Ensure that the vSwitch Forged Transmits policy is set to reject
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/7_1.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('Reject') != -1 and reslines[i].find('ForgedTransmits') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun7_2(self):
        #Ensure that the vSwitch MAC Address Change policy is set to reject
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/7_2.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('Reject') != -1 and reslines[i].find('MacChanges') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue
            return NO  # 不通过
        except:
            return OK

    def fun7_3(self):
        #Ensure that the vSwitch Promiscuous Mode policy is set to reject
        try:
            cmd = 'pwsh -f /usr/local/vmware_script/powershell/7_3.ps1 ' + self.server + ' ' + self.user + ' ' + self.password
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('Reject') != -1 and reslines[i].find('PromiscuousMode') != -1:  # 找到TRUE
                    return OK #通过
                else:
                    continue

            return NO  # 不通过
        except:
            return OK

    def fun7_4(self):
        # Ensure that port groups are not configured to the value of the native VLAN
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VirtualPortGroup -Standard | Select virtualSwitch, Name, VlanID}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            result = stdout.read()
            str = str(result, encoding="utf-8")
            res = str.find('1')
            if result != '' and res == -1:
                return OK
            return NO
        except:
            return OK

    def fun7_5(self):
        # Ensure that port groups are not configured to VLAN values reserved by upstream physical switches
        """
        try:
            stdin, stdout, stderr = self.ssh.exec_command(
                'pwsh -c "&{Connect-VIServer -Server 10.108.115.134 -User root -Password 12345678} | &{Get-VirtualPortGroup -Standard | Select virtualSwitch, Name, VlanID}"')
            result = stdout.read()
            if (result != ''):
                return OK
            return NO
        except:
            return OK
        """
        pass

    def fun7_6(self):
        #Ensure that port groups are not configured to VLAN 4095 except for Virtual Guest Tagging (VGT)
        pass

#Virtual Machines(settings related to guest virtual machines)
    #Communication
    def fun8_1_1(self):
        # Limit informational messages from the VM to the VMX file
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "tools.setInfo.sizeLimit" | Select Entity,Name,Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0: #执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('1048576') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK #通过
        except:
            return OK

    def fun8_1_2(self):
        # Limit sharing of console connections
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "RemoteDisplay.maxConnections" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('1') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    #Devices
    def fun8_2_1(self):
        # Disconnect unauthorized devices - Floppy Devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-FloppyDrive | Select parent,Name,ConnectionState}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('FALSE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_2_2(self):
        # Disconnect unauthorized devices - CD/DVD Devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-CDDrive}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('FALSE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_2_3(self):
        # Disconnect unauthorized devices - Parallel Devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-ParallelPort}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('FALSE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_2_4(self):
        # Disconnect unauthorized devices - Serial Devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-SerialPort}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('FALSE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_2_5(self):
        # Disconnect unauthorized devices - USB Devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-USBDevice}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('FALSE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_2_6(self):
        # Prevent unauthorized removal and modification of devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.device.edit.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('TRUE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_2_7(self):
        # Prevent unauthorized connection of devices
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.device.connectable.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('TRUE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    #Guest
    def fun8_3_1(self):
        pass

    def fun8_3_2(self):
        pass

    def fun8_3_3(self):
        pass

    def fun8_3_4(self):
        pass

    #Monitor
    def fun8_4_1(self):
        pass

    def fun8_4_2(self):
        # Control VMsafe Agent Address
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "vmsafe.agentAddress" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            else:
                return NO
        except:
            return OK

    def fun8_4_3(self):
        # Control VMsafe Agent Port
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "vmsafe.agentPort" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            else:
                return NO
        except:
            return OK

    def fun8_4_4(self):
        # Control VMsafe Agent Configuration
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "vmsafe.enable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('FALSE') != -1:  # 找到1048576
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_5(self):
        # Disable Autologon
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.autologon.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('TRUE') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_6(self):
        # Disable BIOS BBS
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.bios.bbs.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_7(self):
        # Disable Guest Host Interaction Protocol Handler
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.protocolhandler.info.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_8(self):
        # Disable Unity Taskbar
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.taskbar.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_9(self):
        # Disable Unity Active
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.unityActive.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_10(self):
        # Disable Unity Window Contents
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.windowContents.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_11(self):
        # Disable Unity Push Update
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.push.update.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_12(self):
        # Disable Drag and Drop Version Get
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.vmxDnDVersionGet.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_13(self):
        # Disable Drag  and Drop Version Set
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.guestDnDVersionSet.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_14(self):
        # Disable Shell and Action
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.ghi.host.shellAction.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_15(self):
        # Disable Request Disk Topology
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.dispTopoRequest.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_16(self):
        # Disable Trash Folder State
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.trashFolderState.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_17(self):
        # Disable Guest Host Interaction Tray Icon
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.trayicon.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_18(self):
        # Disable Unity
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_19(self):
        # Disable Unity Interlock
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.unityInterlockOperation.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_20(self):
        # Disable GetCreds
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.getCreds.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_21(self):
        # Disable Host Guest File System Server
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.hgfsServerSet.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_22(self):
        # Disable Guest Host Interaction Launch menu
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.launchmenu.change" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_23(self):
        # Disable memSchedFakeSampleStats
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.memSchedFakeSampleStats.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_24(self):
        # Disable VM Console Copy operations
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.copy.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_25(self):
        # Disable VM Console Drag and Drop operations
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.dnd.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_26(self):
        # Disable VM Console GUI Options
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.setGUIOptions.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('false') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_27(self):
        # Disable VM Console Paste operations
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.paste.disable" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_28(self):
        # Control access to VM console via VNC protocol
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "RemoteDisplay.vnc.enabled" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('false') != -1:  # 找到false
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_4_29(self):
        # Disable all but VGA mode on virtual machines
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "svga.vgaOnly" | Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    #Resources
    def fun8_5_1(self):
        #Prevent virtual machines from taking over resources
        pass

    #Storage
    def fun8_6_1(self):
        #Avoid using nonpersistent disks
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-HardDisk | Select Parent, Name, Filename, DiskType, Persistence}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue
            n = len(reslines)
            for i in range(4, n, 5):
                #print(reslines[i])
                if reslines[i].find('Persistent'):
                    continue
                else:
                    return NO
                    #print("不通过")
            return OK
            #print("通过")
        except:
            return OK


    def fun8_6_2(self):
        #Disable virtual disk shrinking
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.diskShrink.disable"| Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_6_3(self):
        #Disable virtual disk wiping
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.diskWiper.disable"| Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    #Tools
    def fun8_7_1(self):
        #Disable VIX messages from the VM
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "isolation.tools.vixMessage.disable"| Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('true') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_7_2(self):
        #Limit number of VM log files
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "log.keepOld"| Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('10') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_7_3(self):
        #Do not send host information to guests
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "tools.guestlib.enableHostInfo"| Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('false') != -1:  # 找到false
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun8_7_4(self):
        #Limit VM log file size
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VM | Get-AdvancedSetting -Name "log.rotateSize"| Select Entity, Name, Value}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            for i in range(2, n):
                if reslines[i].find('1024000') != -1:  # 找到TRUE
                    continue
                else:
                    return NO  # 不通过

            return OK  # 通过
        except:
            return OK

    def fun9_1(self):
        #ESXi按角色分配帐号安全基线要求项
        try:
            cmd = 'pwsh -c "&{Connect-VIServer -Server ' + self.server + ' -User ' + self.user + ' -Password ' + self.password + '} | &{Get-VMHostAccount}"'
            stdin, stdout, stderr = self.ssh1.exec_command(cmd)
            lines = stdout.readlines()
            if len(lines) == 0:  # 执行命令结果为空
                return OK
            reslines = []
            for line in lines:
                if line.strip():  # line不为空字符串
                    reslines.append(line)
                else:
                    continue

            n = len(reslines)
            flag = 0
            for i in range(2, n):
                if reslines[i].find('Administrator') != -1:  # 找到TRUE
                    flag = flag + 1
                else:
                    continue
            if flag >=2:
                return OK
            else:
                return NO
        except:
            return OK

if __name__ == '__main__':
    #连接远程ESXI服务器
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname='10.108.115.134', port=22, username='root', password='12345678')
    #连接本地服务器（server），在本地服务器上执行powercli命令
    ssh1 = paramiko.SSHClient()
    ssh1.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh1.connect(hostname='10.108.114.167', port=22, username='root', password='1202')
    #stdin, stdout, stderr = ssh1.exec_command('ls -al')
    ##for line in lines:
        #print(line)
    test = VMware_Benchmark_lib(ssh, ssh1,  None)
    print(test.getResult())
