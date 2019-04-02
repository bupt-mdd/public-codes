# coding:utf-8

import paramiko
PASS = "PASS"
WARN = "WARN"
INFO = "INFO"

class Kubernetes_Benchmark_lib(object):

    def __init__(self, ssh, check_type):
        self.masterFunctionList = [
            self.fun1_1_1,
            self.fun1_1_2,
            self.fun1_1_3,
            self.fun1_1_4,
            self.fun1_1_5,
            self.fun1_1_6,
            self.fun1_1_7,
            self.fun1_1_8,
            self.fun1_1_9,
            self.fun1_1_10,
            self.fun1_1_11,
            self.fun1_1_12,
            self.fun1_1_13,
            self.fun1_1_14,
            self.fun1_1_15,
            # self.fun1_1_16,
            # self.fun1_1_17,
            # self.fun1_1_18,
            # self.fun1_1_19,
            self.fun1_1_20,
            self.fun1_1_21,
            # self.fun1_1_22,
            # self.fun1_1_23,
            self.fun1_1_24,
            self.fun1_1_25,
            # self.fun1_1_26,
            # self.fun1_1_27,
            self.fun1_1_28,
            # self.fun1_1_29,
            # self.fun1_1_30,
            # self.fun1_1_31,
            self.fun1_1_32,
            self.fun1_1_33,
            # self.fun1_1_34,

            self.fun1_2_1,

            # self.fun1_3_1,
            self.fun1_3_2,
            self.fun1_3_3,
            # self.fun1_3_4,
            # self.fun1_3_5,

            self.fun1_4_1,
            self.fun1_4_2,
            self.fun1_4_3,
            self.fun1_4_4,
            self.fun1_4_5,
            self.fun1_4_6,
            self.fun1_4_7,
            self.fun1_4_8,
            self.fun1_4_9,
            self.fun1_4_10,

            # self.fun1_5_1,
            self.fun1_5_2,
            self.fun1_5_3,
            # self.fun1_5_4,
            self.fun1_5_5,
            self.fun1_5_6,
            # self.fun1_5_7,
            self.fun1_5_8
        ]

        self.nodeFunctionList = [
            self.fun2_1_1,
            self.fun2_1_2,
            self.fun2_1_3,
            # self.fun2_1_4,
            self.fun2_1_5,
            self.fun2_1_6,
            self.fun2_1_7,
            self.fun2_1_8,
            self.fun2_1_9,
            self.fun2_1_10,
            self.fun2_1_11,
            # self.fun2_1_12,
            self.fun2_1_13,

            self.fun2_2_1,
            self.fun2_2_2,
            self.fun2_2_3,
            self.fun2_2_4,
            self.fun2_2_5,
            self.fun2_2_6
        ]

        self.ssh = ssh

        self.checkType = check_type

        self.apiServer = self.apiservercmd()

        self.scheduler = self.schedulercmd()

        self.controllermanager = self.controllermanagercmd()

        self.etcd = self.etcdcmd()

        self.kubelet = self.kubeletcmd()
        # 检测结果列表
        self.resultList = []

        # 直接启动各项检查，调用run()函数
        self.run()

    def run(self):
        # 　根据规则检测数据库
        if self.checkType == 'master':
            for i in range(len(self.masterFunctionList)):
                self.resultList.append(self.masterFunctionList[i]())
        elif self.checkType == 'node':
            for i in range(len(self.nodeFunctionList)):
                self.resultList.append(self.nodeFunctionList[i]())

    def getResult(self):
        # 返回结果
        return self.resultList

    '''
          参考基线文档：CIS_VMware_ESXi_5.5_Benchmark_v1.2.0.pdf
          部分检测点暂未实现
    '''

    def apiservercmd(self):
        stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep kube-apiserver")
        return stdout.read().decode()

    def schedulercmd(self):
        stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep kube-scheduler")
        return stdout.read().decode()

    def controllermanagercmd(self):
        stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep kube-controller-manager")
        return stdout.read().decode()

    def etcdcmd(self):
        stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep etcd")
        return stdout.read().decode()

    def kubeletcmd(self):
        stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep kubelet")
        return stdout.read().decode()

    def getadmissoncontrol(self):
        result = self.apiServer
        start = result.find("--admission-control")
        end = result.find(" ", start)
        return result[start:end]

    def get_config_info(self, target, config):
        result = target
        newline = result.find("\n")
        start = result.find(config)
        end = result.find(" ", start)
        return result[start:end if end <= newline else newline]

    def fun1_1_1(self):
        tmp = self.get_config_info(self.apiServer, "--allow-privileged")
        return [1, PASS, tmp] if "--allow-privileged=false" in tmp else [1, WARN, tmp]

    def fun1_1_2(self):
        tmp = self.get_config_info(self.apiServer, "--anonymous-auth")
        return [2, PASS, tmp] if "--anonymous-auth=false" in tmp else [2, WARN, tmp]

    def fun1_1_3(self):
        tmp = self.get_config_info(self.apiServer, "--basic-auth-file")
        return [3, PASS, tmp] if "--basic-auth-file" not in tmp else [3, WARN, tmp]

    def fun1_1_4(self):
        tmp = self.get_config_info(self.apiServer, "--insecure-allow-any-token")
        return [4, PASS, tmp] if "--insecure-allow-any-token" not in tmp else [4, WARN, tmp]

    def fun1_1_5(self):
        tmp = self.get_config_info(self.apiServer, "--kubelet-https")
        return [5,PASS, tmp] if "--kubelet-https=true" in tmp or "--kubelet-https" not in tmp else [5, WARN, tmp]

    def fun1_1_6(self):
        tmp = self.get_config_info(self.apiServer, "--insecure-bind-address")
        return [6,PASS, tmp] if "--insecure-bind-address" not in tmp or "--insecure-bind-address=127.0.0.1" in tmp else\
            [6,WARN, tmp]

    def fun1_1_7(self):
        tmp = self.get_config_info(self.apiServer, "--insecure-port")
        return [7,PASS, tmp] if "--insecure-port=0" in tmp else [7,WARN, tmp]

    def fun1_1_8(self):
        tmp = self.get_config_info(self.apiServer, "--secure-port")
        if len(tmp) == 0:
            return [8,PASS, tmp]
        else:
            port = int(tmp[tmp.find("=") + 1:])
            return [8,PASS, tmp] if 1 <= port <= 65535 else [8,WARN, tmp]

    def fun1_1_9(self):
        tmp = self.get_config_info(self.apiServer, "--profiling")
        return [9,PASS, tmp] if "--profiling=false" in tmp else [9,WARN, tmp]

    def fun1_1_10(self):
        tmp = self.get_config_info(self.apiServer, "--repair-malformed-updates")
        return [10,PASS, tmp] if "--repair-malformed-updates=false" in tmp else [10,WARN, tmp]

    def fun1_1_11(self):
        return [11,PASS, self.getadmissoncontrol()] if "AlwaysAdmit" not in self.getadmissoncontrol() \
            else [11,WARN, self.getadmissoncontrol()]

    def fun1_1_12(self):
        return [12,PASS, self.getadmissoncontrol()] if "AlwaysPullImages" in self.getadmissoncontrol() \
            else [12,WARN, self.getadmissoncontrol()]

    def fun1_1_13(self):
        return [13,PASS, self.getadmissoncontrol()] if "DenyEscalatingExec" in self.getadmissoncontrol() \
            else [13,WARN, self.getadmissoncontrol()]

    def fun1_1_14(self):
        return [14,PASS, self.getadmissoncontrol()] if "SecurityContextDeny" in self.getadmissoncontrol() \
            else [14,WARN, self.getadmissoncontrol()]

    def fun1_1_15(self):
        return [15,PASS, self.getadmissoncontrol()] if "NamespaceLifecycle" in self.getadmissoncontrol() \
            else [15,WARN, self.getadmissoncontrol()]

    # def fun1_1_16(self):
    #     tmp = self.get_config_info(self.apiServer, "--audit-log-path")
    #     return [INFO, tmp]
    #
    # def fun1_1_17(self):
    #     tmp = self.get_config_info(self.apiServer, "--audit-log-maxage")
    #     return [PASS, tmp] if "--audit-log-maxage=30" in tmp else [INFO, tmp]
    #
    # def fun1_1_18(self):
    #     tmp = self.get_config_info(self.apiServer, "--audit-log-maxbackup")
    #     return [PASS, tmp] if "--audit-log-maxbackup=10" in tmp else [INFO, tmp]
    #
    # def fun1_1_19(self):
    #     tmp = self.get_config_info(self.apiServer, "--audit-log-maxsize")
    #     return [PASS, tmp] if "--audit-log-maxsize=100" in tmp else [INFO, tmp]

    def fun1_1_20(self):
        tmp = self.get_config_info(self.apiServer, "--authorization-mode")
        return [20,PASS, tmp] if "AlwaysAllow" not in tmp else [20,WARN, tmp]

    def fun1_1_21(self):
        tmp = self.get_config_info(self.apiServer, "--token-auth-file")
        return [21,PASS, tmp] if "--token-auth-file" not in tmp else [21,WARN, tmp]
    #
    # def fun1_1_22(self):
    #     tmp = self.get_config_info(self.apiServer, "--kubelet-certificate-authority")
    #     return [INFO, tmp] if "--kubelet-certificate-authority" in tmp else [WARN, tmp]
    #
    # def fun1_1_23(self):
    #     tmp1 = self.get_config_info(self.apiServer, "--kubelet-client-certificate")
    #     tmp2 = self.get_config_info(self.apiServer, "--kubelet-client-key")
    #     return [INFO, tmp1 + "\n" + tmp2] if "--kubelet-client-certificate" in tmp1 and "--kubelet-client-key" in tmp2 \
    #         else [WARN, tmp1 + "\n" + tmp2]

    def fun1_1_24(self):
        tmp = self.get_config_info(self.apiServer, "--service-account-lookup")
        return [24,PASS, tmp] if "--service-account-lookup=true" in tmp else [24,WARN, tmp]

    def fun1_1_25(self):
        return [25,PASS, self.getadmissoncontrol()] if "PodSecurityPolicy" in self.getadmissoncontrol() \
            else [25,WARN, self.getadmissoncontrol()]
    #
    # def fun1_1_26(self):
    #     tmp = self.get_config_info(self.apiServer, "--service-account-key-file")
    #     return [INFO, tmp] if "--service-account-key-file" in tmp else [WARN, tmp]
    #
    # def fun1_1_27(self):
    #     tmp = self.get_config_info(self.apiServer, "--etcd-certfile")
    #     tmp2 = self.get_config_info(self.apiServer, "--etcd-keyfile")
    #     return [INFO, tmp + "\n" + tmp2] if "--etcd-certfile" in tmp and "--etcd-keyfile" in tmp2 \
    #         else [WARN, tmp + "\n" + tmp2]

    def fun1_1_28(self):
        return [28,PASS, self.getadmissoncontrol()] if "ServiceAccount" in self.getadmissoncontrol() \
            else [28,WARN, self.getadmissoncontrol()]

    # def fun1_1_29(self):
    #     tmp = self.get_config_info(self.apiServer, "--tls-cert-file")
    #     tmp2 = self.get_config_info(self.apiServer, "--tls-private-key-file")
    #     return [INFO, tmp + "\n" + tmp2] if "--tls-cert-file" in tmp and "--tls-private-key-file" in tmp2 \
    #         else [WARN, tmp + "\n" + tmp2]
    #
    # def fun1_1_30(self):
    #     tmp = self.get_config_info(self.apiServer, "--client-ca-file")
    #     return [INFO, tmp] if "--client-ca-file" in tmp else [WARN, tmp]
    #
    # def fun1_1_31(self):
    #     tmp = self.get_config_info(self.apiServer, "--etcd-cafile")
    #     return [INFO, tmp] if "--etcd-cafile" in tmp else [WARN, tmp]

    def fun1_1_32(self):
        tmp = self.get_config_info(self.apiServer, "--authorization-mode")
        return [32,PASS, tmp] if "Node" in tmp else [32,WARN, tmp]

    def fun1_1_33(self):
        return [33,PASS, self.getadmissoncontrol()] if "NodeRestriction" in self.getadmissoncontrol() \
            else [33,WARN, self.getadmissoncontrol()]
    #
    # def fun1_1_34(self):
    #     tmp = self.get_config_info(self.apiServer, "--experimental-encryption-provider-config")
    #     return [INFO, tmp]

    def fun1_2_1(self):
        tmp = self.get_config_info(self.scheduler, "--profiling")
        return [35,PASS, tmp] if "--profiling=false" in tmp else [35,WARN, tmp]

    # def fun1_3_1(self):
    #     tmp = self.get_config_info(self.controllermanager, "--terminated-pod-gc-threshold")
    #     return [INFO, tmp]

    def fun1_3_2(self):
        tmp = self.get_config_info(self.controllermanager, "--profiling")
        return [37,PASS, tmp] if "--profiling=false" in tmp else [37,WARN, tmp]

    def fun1_3_3(self):
        tmp = self.get_config_info(self.controllermanager, "--use-service-account-credentials")
        return [38,PASS, tmp] if "--use-service-account-credentials=true" in tmp else [38,WARN, tmp]
    #
    # def fun1_3_4(self):
    #     tmp = self.get_config_info(self.controllermanager, "--service-account-private-key-file")
    #     return [INFO, tmp]
    #
    # def fun1_3_5(self):
    #     tmp = self.get_config_info(self.controllermanager, "--root-ca-file")
    #     return [INFO, tmp]

    def fun1_4_1(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/apiserver")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [41, WARN, "/etc/kubernetes/apiserver 文件不存在"]
        return [41, PASS, "/etc/kubernetes/apiserver 文件权限：" + tmp] if int(tmp) >= 644\
            else [41, WARN, "/etc/kubernetes/apiserver 文件权限：" + tmp]

    def fun1_4_2(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/apiserver")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [42, WARN, "/etc/kubernetes/apiserver 文件不存在"]
        return [42,PASS, "/etc/kubernetes/apiserver 文件所有者：" + tmp] if "root:root" in tmp \
            else [42,WARN, "/etc/kubernetes/apiserver 文件所有者：" + tmp]

    def fun1_4_3(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/config")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [43, WARN, "/etc/kubernetes/config 文件不存在"]
        return [43,PASS, "/etc/kubernetes/config 文件权限：" + tmp] if int(tmp) >= 644 \
            else [43,WARN, "/etc/kubernetes/config 文件权限：" + tmp]

    def fun1_4_4(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/config")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [44, WARN, "/etc/kubernetes/config 文件不存在"]
        return [44,PASS, "/etc/kubernetes/config 文件所有者：" + tmp] if "root:root" in tmp \
            else [44,WARN, "/etc/kubernetes/config 文件所有者：" + tmp]

    def fun1_4_5(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/scheduler")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [45, WARN, "/etc/kubernetes/scheduler 文件不存在"]
        return [45,PASS, "/etc/kubernetes/scheduler 文件权限：" + tmp] if int(tmp) >= 644 \
            else [45,WARN, "/etc/kubernetes/scheduler 文件权限：" + tmp]

    def fun1_4_6(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/scheduler")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [46, WARN, "/etc/kubernetes/scheduler 文件不存在"]
        return [46,PASS, "/etc/kubernetes/scheduler 文件所有者：" + tmp] if "root:root" in tmp \
            else [46,WARN, "/etc/kubernetes/scheduler 文件所有者：" + tmp]

    def fun1_4_7(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/etcd/etcd.conf")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [47, WARN, "/etc/etcd/etcd.conf 文件不存在"]
        return [47,PASS, "/etc/etcd/etcd.conf 文件权限：" + tmp] if int(tmp) >= 644 \
            else [47,WARN, "/etc/etcd/etcd.conf 文件权限：" + tmp]

    def fun1_4_8(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/etcd/etcd.conf")
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [48, WARN, "/etc/etcd/etcd.conf 文件不存在"]
        return [48,PASS, "/etc/etcd/etcd.conf 文件所有者：" + tmp] if "root:root" in tmp \
            else [48,WARN, "/etc/etcd/etcd.conf 文件所有者：" + tmp]

    def getetcddir(self, item):
        result = self.etcd
        result = result[result.find(item):]
        space = result.find("\n")
        end = result.find(" ")
        result = result[:space if space < end else end]
        return result[result.find("=") + 1:]

    def fun1_4_9(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a " + self.getetcddir("--data-dir"))
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [49, WARN, self.getetcddir("--data-dir") + " 文件不存在"]
        return [49,PASS, self.getetcddir("--data-dir") + " 权限：" + tmp] if int(tmp) >= 700 \
            else [49,WARN,self.getetcddir("--data-dir") + " 权限：" + tmp]

    def fun1_4_10(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G " + self.getetcddir("--data-dir"))
        tmp = stdout.read().decode().replace("\n", "")
        if tmp=='':
            return [50, WARN, self.getetcddir("--data-dir") + " 文件不存在"]
        return [50,PASS, self.getetcddir("--data-dir") + " 所有者：" + tmp] if "root:root" in tmp \
            else [50,WARN, self.getetcddir("--data-dir") + " 所有者：" + tmp]

    # def fun1_5_1(self):
    #     tmp = self.get_config_info(self.etcd, "--cert-file")
    #     tmp1 = self.get_config_info(self.etcd, "--key-file")
    #     return [INFO, tmp + "\n" + tmp1] if "--cert-file" in tmp and "--key-file" in tmp1 \
    #         else [WARN, tmp + "\n" + tmp1]

    def fun1_5_2(self):
        tmp = self.get_config_info(self.etcd, "--client-cert-auth")
        return [52,PASS, tmp] if "--client-cert-auth=true" in tmp else [52,WARN, tmp]

    def fun1_5_3(self):
        tmp = self.get_config_info(self.etcd, "--auto-tls")
        return [53,PASS, tmp] if "--auto-tls=false" in tmp else [53,WARN, tmp]
    #
    # def fun1_5_4(self):
    #     tmp = self.get_config_info(self.etcd, "--peer-cert-file")
    #     tmp1 = self.get_config_info(self.etcd, "--peer-key-file")
    #     return [INFO, tmp + "\n" + tmp1] if "--peer-cert-file" in tmp and "--peer-key-file" in tmp1 \
    #         else [WARN, tmp + "\n" + tmp1]

    def fun1_5_5(self):
        tmp = self.get_config_info(self.etcd, "--peer-client-cert-auth")
        return [55,PASS,tmp] if "--peer-client-cert-auth=true" in tmp else [55,WARN, tmp]

    def fun1_5_6(self):
        tmp = self.get_config_info(self.etcd, "--peer-auto-tls")
        return [56,PASS, tmp] if "--peer-auto-tls=false" in tmp else [56,WARN,tmp]

    # def fun1_5_7(self):
    #     tmp = self.get_config_info(self.etcd, "--wal-dir")
    #     return [INFO, tmp] if "--wal-dir" in self.etcd and self.getetcddir("--wal-dir") != self.getetcddir("--data-dir") \
    #         else [WARN, tmp]

    def fun1_5_8(self):
        tmp = self.get_config_info(self.etcd, "--max-wals")
        return [58,PASS, tmp] if "--max-wals=0" in tmp else [58,WARN, tmp]

    def fun2_1_1(self):
        tmp = self.get_config_info(self.kubelet, "--allow-privileged")
        return [59,PASS, tmp] if "--allow-privileged=false" in tmp else [59,WARN, tmp]

    def fun2_1_2(self):
        tmp = self.get_config_info(self.kubelet, "--anonymous-auth")
        return [60,PASS, tmp] if "--anonymous-auth=false" in tmp else [60,WARN, tmp]

    def fun2_1_3(self):
        tmp = self.get_config_info(self.kubelet, "--authorization-mode")
        return [61,WARN, tmp] if "AlwaysAllow" in tmp else [61,PASS, tmp]

    # def fun2_1_4(self):
    #     tmp = self.get_config_info(self.kubelet, "--client-ca-file")
    #     return [INFO, tmp] if "--client-ca-file" in tmp else [WARN, tmp]

    def fun2_1_5(self):
        tmp = self.get_config_info(self.kubelet, "--read-only-port")
        return [63,PASS, tmp] if "--read-only-port=0" in tmp else [63,WARN, tmp]

    def fun2_1_6(self):
        tmp = self.get_config_info(self.kubelet, "--streaming-connection-idle-timeout")
        return [64,WARN, tmp] if "--streaming-connection-idle-timeout=0" in tmp else [64,PASS, tmp]

    def fun2_1_7(self):
        tmp = self.get_config_info(self.kubelet, "--protect-kernel-defaults")
        return [65,PASS, tmp] if "--protect-kernel-defaults=true" in tmp else [65,WARN, tmp]

    def fun2_1_8(self):
        tmp = self.get_config_info(self.kubelet, "--make-iptables-util-chains")
        return [66,PASS, tmp] if "--make-iptables-util-chains=true" in tmp else [66,WARN, tmp]

    def fun2_1_9(self):
        tmp = self.get_config_info(self.kubelet, "--keep-terminated-pod-volumes")
        return [67,PASS, tmp] if "--keep-terminated-pod-volumes=false" in tmp else [67,WARN, tmp]

    def fun2_1_10(self):
        tmp = self.get_config_info(self.kubelet, "--hostname-override")
        return [68,PASS, tmp] if "--hostname-override" not in tmp else [68,WARN, tmp]

    def fun2_1_11(self):
        tmp = self.get_config_info(self.kubelet, "--event-qps")
        return [69,PASS, tmp] if "--event-qps=0" in tmp else [69,WARN, tmp]

    # def fun2_1_12(self):
    #     tmp = self.get_config_info(self.kubelet, "--tls-cert-file")
    #     tmp1 = self.get_config_info(self.kubelet, "--tls-private-key-file")
    #     return [INFO, tmp + "\n" + tmp1] if "--tls-cert-file" in tmp and "--tls-private-key-file" in tmp1 \
    #         else [WARN, tmp + "\n" + tmp1]

    def fun2_1_13(self):
        tmp = self.get_config_info(self.kubelet, "--cadvisor-port")
        return [71,PASS, tmp] if "--cadvisor-port=0" in tmp else [71,WARN, tmp]

    def fun2_2_1(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/config")
        if len(stderr.read()) != 0:
            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/kubelet.conf")
            tmp = stdout.read().decode()
            if tmp=='':
                return [72, WARN, "/etc/kubernetes/kubelet.conf 文件不存在"]
            return [72,PASS, "/etc/kubernetes/kubelet.conf 权限 : " + tmp.replace("\n", "")] if int(tmp) >= 644 \
                else [72,WARN, "/etc/kubernetes/kubelet.conf 权限 : " + tmp.replace("\n", "")]
        tmp = stdout.read().decode()
        if tmp=='':
            return [72, WARN, "/etc/kubernetes/config 文件不存在"]
        return [72,PASS, "/etc/kubernetes/config 权限 : " + tmp.replace("\n", "")] if int(tmp) >= 644 \
            else [72,WARN, "/etc/kubernetes/config 权限 : " + tmp.replace("\n", "")]

    def fun2_2_2(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/config")
        if len(stderr.read()) !=0:
            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/kubelet.conf")
            tmp = stdout.read().decode()
            if tmp=='':
                return [73,WARN, "/etc/kubernetes/kubelet.conf 文件不存在"]
            return [73,PASS, "/etc/kubernetes/kubelet.conf 所有者 : " + tmp.replace("\n")] if "root:root" in tmp \
                else [73,WARN, "/etc/kubernetes/kubelet.conf 所有者 : " + tmp.replace("\n", "")]
        tmp = stdout.read().decode()
        if tmp == '':
            return [73, WARN, "/etc/kubernetes/config 文件不存在"]
        return [73,PASS, "/etc/kubernetes/config 所有者 : " + tmp.replace("\n","")] if "root:root" in tmp \
            else [73,WARN, "/etc/kubernetes/config 所有者 : " + tmp.replace("\n","")]

    def fun2_2_3(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/kubelet")
        if len(stderr.read()) != 0:
            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/kubelet.conf")
            tmp = stdout.read().decode()
            if tmp=='':
                return [74,WARN, "/etc/kubernetes/kubelet.conf 文件不存在"]
            return [74,PASS, "/etc/kubernetes/kubelet.conf 权限 : " + tmp.replace("\n", "")] if int(tmp) >= 644 \
                else [74,WARN, "/etc/kubernetes/kubelet.conf 权限 : " + tmp.replace("\n", "")]
        tmp = stdout.read().decode()
        if tmp == '':
            return [74, WARN, "/etc/kubernetes/kubelet 文件不存在"]
        return [74,PASS, "/etc/kubernetes/kubelet 权限 : " + tmp.replace("\n", "")] if int(tmp) >= 644 \
            else [74,WARN, "/etc/kubernetes/kubelet 权限 : " + tmp.replace("\n", "")]

    def fun2_2_4(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/kubelet")
        if len(stderr.read()) != 0:
            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/kubelet.conf")
            tmp = stdout.read().decode()
            if tmp=='':
                return [75,WARN, "/etc/kubernetes/kubelet.conf 文件不存在"]
            return [75,PASS, "/etc/kubernetes/kubelet.conf 所有者 : " + tmp.replace("\n", "")] if "root:root" in tmp \
                else [75,WARN, "/etc/kubernetes/kubelet.conf 所有者 : " + tmp.replace("\n", "")]
        tmp = stdout.read().decode()
        if tmp == '':
            return [75, WARN, "/etc/kubernetes/kubelet 文件不存在"]
        return [75,PASS, "/etc/kubernetes/kubelet 所有者 : " + tmp.replace("\n", "")] if "root:root" in tmp \
            else [75,WARN, "/etc/kubernetes/kubelet 所有者 : " + tmp.replace("\n", "")]

    def fun2_2_5(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/kubernetes/proxy")
        tmp = stdout.read().decode()
        if tmp=='':
            return [76,WARN, "/etc/kubernetes/proxy 文件不存在"]
        return [76,PASS, "/etc/kubernetes/proxy 权限：" + tmp.replace("\n", "")] if int(tmp) >= 644 \
            else [76,WARN, "/etc/kubernetes/proxy 权限：" + tmp.replace("\n", "")]

    def fun2_2_6(self):
        stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/kubernetes/proxy")
        tmp = stdout.read().decode()
        if tmp=='':
            return [77,WARN, "/etc/kubernetes/proxy 文件不存在"]
        return [77,PASS, "/etc/kubernetes/proxy 所有者：" + tmp.replace("\n", "")] if "root:root" in tmp \
            else [77,WARN, "/etc/kubernetes/proxy 所有者：" + tmp.replace("\n", "")]
