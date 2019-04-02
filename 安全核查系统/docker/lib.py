# coding:utf-8

import paramiko
import os
import json

class Docker_Benchmark_lib(object):
    def __init__(self, ssh):
        self.ssh = ssh
        self.containers_id = self.get_containers_id()
        self.run()

    def get_conf(self, str, tar):
        ind1 = str.find(tar)
        ind2 = str.find(" ", ind1)
        return str[ind1:ind2].strip()

    def run(self):
        for c_id in self.containers_id:

            self.resultList = []

            stdin, stdout, stderr = self.ssh.exec_command("uname -r")
            result = stdout.read().strip().decode()
            result_split = result.split(".")
            tmp = {"check_point": "1.2", "result": True, "config": ""}
            tmp["config"] = result
            if int(result_split[0]) < 3:
                tmp["result"] = False
            elif int(result_split[0])==3 and int(result_split[1])<10:
                tmp["result"] = False
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /usr/bin/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.7", "result": True, "config": ""}
            tmp["config"] = result
            if not result:
                tmp["result"] = False
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /var/lib/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.8", "result": True, "config": ""}
            tmp["config"] = result
            if not result:
                tmp["result"] = False
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /etc/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.9", "result": True, "config": ""}
            tmp["config"] = result
            if not result:
                tmp["result"] = False
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("systemctl show -p FragmentPath docker.service")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.10", "result": True, "config": ""}
            if "docker.service" not in result:
                tmp["result"] = False
            else:
                stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep docker.service")
                result = stdout.read().strip().decode()
                if not result:
                    tmp["result"] = False
                tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("systemctl show -p FragmentPath docker.socket")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.11", "result": True, "config": ""}
            if "docker.socket" not in result:
                tmp["result"] = False
            else:
                stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep docker.socket")
                result = stdout.read().strip().decode()
                if not result:
                    tmp["result"] = False
                tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /etc/default/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.12", "result": True, "config": ""}
            if not result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /etc/docker/daemon.json")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.13", "result": True, "config": ""}
            if not result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /usr/bin/docker-containerd")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.14", "result": True, "config": ""}
            if not result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("auditctl -l | grep /usr/bin/docker-runc")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "1.15", "result": True, "config": ""}
            if not result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("ps -ef | grep dockerd")
            ch2_result = stdout.read().strip().decode()
            tmp = {"check_point": "2.1", "result": True, "config": ""}
            if "--icc=false" in ch2_result:
                tmp["config"] = "--icc=false"
            elif "--icc=true" in ch2_result:
                tmp["config"] = "--icc=true"
                tmp["result"] = False
            else:
                tmp["result"] = False
            self.resultList.append(tmp)

            tmp = {"check_point": "2.2", "result": True, "config": ""}
            if "--log-level" in ch2_result:
                conf = self.get_conf(ch2_result, "--log-level")
                if '--log-level="info"' not in conf:
                    tmp["result"] = False
                tmp["config"] = conf
            self.resultList.append(tmp)

            tmp = {"check_point": "2.3", "result": True, "config": ""}
            if "--iptables=false" in ch2_result:
                tmp["result"] = False
                tmp["config"] = "--iptables=false"
            elif "--iptables=true" in ch2_result:
                tmp["config"] = "--iptables=true"
            self.resultList.append(tmp)

            tmp = {"check_point": "2.4", "result": True, "config": ""}
            if "--insecure-registry" in ch2_result:
                tmp["result"] = False
                tmp["config"] = self.get_conf(ch2_result, "--insecure-registry")
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("docker info | grep -e \"^Storage Driver:\s*aufs\s*$\"")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "2.5", "result": True, "config": ""}
            if result:
                tmp["result"] = False
                tmp["config"] = result
            self.resultList.append(tmp)

            tmp = {"check_point": "2.6", "result": True, "config": ""}
            if '--tlsverify' not in ch2_result or '--tlscacert' \
                    not in ch2_result or '--tlscert' not in ch2_result or '--tlskey' \
                    not in ch2_result:
                tmp["result"] = False
                tmp["config"] = tmp["config"] + self.get_conf(ch2_result, '--tlsverify') + \
                                self.get_conf(ch2_result, '--tlscacert') + \
                                self.get_conf(ch2_result, '--tlscert') + self.get_conf(ch2_result, '--tlskey')
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("ps -p $(docker inspect --format='{{ .State.Pid }}' %s) -o pid,user" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "2.8", "result": True, "config": ""}
            if "root" in result:
                tmp["result"] = False
                tmp["config"] = result
            elif '--userns-remap' in ch2_result:
                tmp["config"] = self.get_conf(ch2_result, '--userns-remap')
            else:
                tmp["result"] = False
                tmp["config"] = result
            self.resultList.append(tmp)

            tmp = {"check_point": "2.10", "result": True, "config": ""}
            if '--storage-opt' in ch2_result or 'dm.basesize' in ch2_result:
                tmp["result"] = False
            tmp["config"] = ch2_result
            self.resultList.append(tmp)

            tmp = {"check_point": "2.13", "result": True, "config": ""}
            if '--disable-legacy-registry' not in ch2_result:
                tmp["result"] = False
            else:
                tmp["config"] = ch2_result
            self.resultList.append(tmp)

            tmp = {"check_point": "2.14", "result": True, "config": ""}
            if '--live-restore' not in ch2_result:
                tmp["result"] = False
            else:
                tmp["config"] = self.get_conf(ch2_result, '--live-restore')
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("docker node ls | grep Leader")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "2.16", "result": True, "config": result}
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("netstat -lt | grep -i 2377")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "2.17", "result": True, "config": result}
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("systemctl show -p FragmentPath docker.service")
            result = stdout.read().strip().decode()
            path = result[result.find("=") + 1:]
            tmp = {"check_point": "3.1", "result": True, "config": ""}
            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G " + path)
            result = stdout.read().strip().decode()
            if 'root:root' not in result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a " + path)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.2", "result": True, "config": ""}
            if int(result) < 644:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("systemctl show -p FragmentPath docker.socket")
            result = stdout.read().strip().decode()
            path = result[result.find("=")+1:]
            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G " + path)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.3", "result": True, "config": ""}
            if 'root:root' not in result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a " + path)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.4", "result": True, "config": ""}
            if int(result) < 644:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.5", "result": True, "config": ""}
            if 'root:root' not in result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.6", "result": True, "config": ""}
            if int(result) < 755:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /var/run/docker.sock")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.15", "result": True, "config": ""}
            if 'root:docker' not in result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /var/run/docker.sock")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.16", "result": True, "config": ""}
            if int(result) < 660:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/docker/daemon.json")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.17", "result": True, "config": ""}
            if 'root:root' not in result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/docker/daemon.json")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.18", "result": True, "config": ""}
            if int(result) < 644:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %U:%G /etc/default/docker | grep -v root:root")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.19", "result": True, "config": ""}
            if 'root:root' not in result:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("stat -c %a /etc/default/docker")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "3.20", "result": True, "config": ""}
            if int(result) < 644:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("docker ps --quiet | xargs docker inspect --format {{ .Config.User }} %s" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "4.1", "result": True, "config": ""}
            if not result:
                tmp["config"] = 'root'
            else:
                tmp["config"] = result
            self.resultList.append(tmp)

            stdin, stdout, stderr = self.ssh.exec_command("echo $DOCKER_CONTENT_TRUST")
            result = stdout.read().strip().decode()
            tmp = {"check_point": "4.5", "result": True, "config": ""}
            if len(result)==0 or int(result)!=1:
                tmp["result"] = False
            tmp["config"] = result
            self.resultList.append(tmp)

            # 5.4 Ensure privileged containers are not used
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{.HostConfig.Privileged}}' %s" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.4", "result": True, "config": ""}
            if result:  # 存在结果
                if result != "false":
                    tmp["result"] = False
                tmp["config"] = "Privileged=" + result
            self.resultList.append(tmp)

            #  5.5 Ensure sensitive host system directories are not mounted on containers
            stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{.Mounts}}' %s 2>/dev/null" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.5", "result": False, "config": ""}
            if result:  # 存在结果
                if result == "" or result == "[]" or not (
                        "{ /dev" in result or "{ /boot" in result or "{ /etc" in result
                        or "{ /lib" in result or "{ /proc" in result or "{ /sys" in result or "{ /usr" in result):
                    tmp["result"] = True
                tmp["config"] = "Volumes=" + result
            self.resultList.append(tmp)

            # 5.6 Do not run ssh within containers
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker exec %s ps -el 2>/dev/null | grep -c sshd | awk '{print $1}'" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.6", "result": False, "config": ""}
            if result:  # 存在结果
                if result == "" or result == "0":
                    tmp["result"] = True
                tmp["config"] = "容器中运行的ssh进程数：" + result
            self.resultList.append(tmp)

            # 5.7 Do not map privileged ports within containers
            stdin, stdout, stderr = self.ssh.exec_command("docker port %s | awk '{print $0}' | cut -d ':' -f2" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.7", "result": True, "config": ""}
            if result:  # 存在结果
                tmpcmd = result.split('\n')
                for t in tmpcmd:
                    if t.isdigit() and int(t) <= 1024:
                        tmp["result"] = False
                tmp["config"] = "Ports=" + result.replace('\n', ' ')
            self.resultList.append(tmp)

            # # 5.8 Open only needed ports on container
            # tmp = {"check_point": "8", "result": "true", "config": "", "judge": True}
            # stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{ .NetworkSettings.Ports }}' %s" % c_id)
            # result = stdout.read().strip()
            # tmp["config"] = "NetworkPort="+result
            # self.resultList.append(tmp)

            # 5.9 Do not share the host's network namespace
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{.HostConfig.NetworkMode}}' %s" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.9", "result": False, "config": ""}
            if result:  # 存在结果
                if not result == "host":
                    tmp["result"] = True
                tmp["config"] = "NetworkMode=" + result
            self.resultList.append(tmp)

            # 5.10 Limit memory usage for container
            stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{.HostConfig.Memory}}' %s" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.10", "result": False, "config": ""}
            if result:  # 存在结果
                if not result == "0":
                    tmp["result"] = True
                tmp["config"] = "Memory=" + result
            self.resultList.append(tmp)

            # 5.11 Set container CPU priority appropriately
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.CpuShares }}' %s" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.11", "result": False, "config": ""}
            if result:  # 存在结果
                if not (result == "0" or result == "1024"):
                    tmp["result"] = True
                tmp["config"] = "CpuShares=" + result
            self.resultList.append(tmp)

            # 5.12 Mount container's root filesystem as read only
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.ReadonlyRootfs }}' %s" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.12", "result": False, "config": ""}
            if result:  # 存在结果
                if result == "true":
                    tmp["result"] = True
                tmp["config"] = "ReadonlyRootfs=" + result
            self.resultList.append(tmp)

            # 5.13 Bind incoming container traffic to a specific host interface
            stdin, stdout, stderr = self.ssh.exec_command("docker port %s | awk '{print $3}' | cut -d ':' -f1" % c_id)
            result = stdout.read().strip().decode().replace('\n', ' ')
            tmp = {"check_point": "5.13", "result": True, "config": ""}
            if result:  # 存在结果
                if "0.0.0.0" in result:
                    tmp["result"] = False
                tmp["config"] = "HostInterface=" + result
            self.resultList.append(tmp)

            # 5.14 Set the 'on-failure' container restart policy to 5
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.RestartPolicy.Name }}' %s " % c_id)
            result = stdout.read().strip().decode()
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.RestartPolicy.MaximumRetryCount }}' %s " % c_id)
            result1 = stdout.read().strip().decode()
            tmp = {"check_point": "5.14", "result": False, "config": ""}
            if result and result1:
                if result == "no" or result == "":  # 存在结果
                    tmp["result"] = True
                elif result == "on-failure":
                    if result1 <= "5":
                        tmp["result"] = True
                tmp["config"] = "RestartPolicyName=" + result + " MaximumRetryCount=" + result1
            self.resultList.append(tmp)

            # 5.15 Ensure the host's process namespace is not shared
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.PidMode }}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.15", "result": True, "config": ""}
            if result:  # 存在结果
                if result == "host":
                    tmp["result"] = False
                tmp["config"] = "PidMode=" + result
            self.resultList.append(tmp)

            # 5.16 - Ensure the host's IPC namespace is not shared
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.IpcMode }}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.16", "result": True, "config": ""}
            if result:  # 存在结果
                if result == "host":
                    tmp["result"] = False
                tmp["config"] = "IpcMode=" + result
            self.resultList.append(tmp)

            # 5.17 Ensure host devices are not directly exposed to containers
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.Devices }}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.17", "result": False, "config": ""}
            if result:  # 存在结果
                if result == "" or result == "[]" or result == "<no value>":
                    tmp["result"] = True
                tmp["config"] = "Devices=" + result
            self.resultList.append(tmp)

            # # 5.18 Ensure the default ulimit is overwritten at runtime, only if needed
            # stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{ .HostConfig.Ulimits }}' %s " % c_id)
            # result = stdout.read().strip()
            # tmp = {"check_point": "18", "result": False, "config": "", "judge": True}
            # if result:  # 存在结果
            #     if not (result == "" or result == "[]" or result == "<no value>"):
            #         tmp["result"] = True
            #     tmp["config"] = "Ulimits="+result
            # self.resultList.append(tmp)

            # 5.19 - Ensure mount propagation mode is not set to shared
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{range $mnt := .Mounts}} {{json $mnt.Propagation}} {{end}}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.19", "result": False, "config": ""}
            if result:  # 存在结果
                if "shared" not in result:
                    tmp["result"] = True
                tmp["config"] = "Propagation=" + result
            self.resultList.append(tmp)

            # 5.20 - Ensure the host's UTS namespace is not shared
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.UTSMode }}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.20", "result": True, "config": ""}
            if result:  # 存在结果
                if result == "host":
                    tmp["result"] = False
                tmp["config"] = "UTSMode=" + result
            self.resultList.append(tmp)

            # 5.21 - Ensure the default seccomp profile is not Disabled
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.SecurityOpt }}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.21", "result": False, "config": ""}
            if result:  # 存在结果
                if "seccomp:unconfined" not in result:
                    tmp["result"] = True
                tmp["config"] = "SecurityOpt=" + result
            self.resultList.append(tmp)

            # 5.22 - Ensure docker exec commands are not used with privileged option
            tmp = {"check_point": "5.22", "result": "true", "config": ""}
            self.resultList.append(tmp)

            # 5.23 - Ensure docker exec commands are not used with user option
            tmp = {"check_point": "5.23", "result": "true", "config": ""}
            self.resultList.append(tmp)

            # 5.24 - Ensure cgroup usage is confirmed
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.CgroupParent }}x' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.24", "result": False, "config": ""}
            if result:  # 存在结果
                if result == "x":
                    tmp["result"] = True
                tmp["config"] = "CgroupParent=" + result
            self.resultList.append(tmp)

            # # 5.25 - Ensure the container is restricted from acquiring additional privileges
            # stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{ .HostConfig.SecurityOpt }}' %s " % c_id)
            # result = stdout.read().strip()
            # tmp = {"check_point": "25", "result": False, "config": "", "judge": True}
            # if result:  # 存在结果
            #     if "no-new-privileges" in result:
            #         tmp["result"] = True
            #     tmp["config"] = "SecurityOpt="+result
            # self.resultList.append(tmp)

            # # 5.26 - Ensure container health is checked at runtime
            # stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{ .State.Health.Status }}' %s 2>/dev/null 1>&2" % c_id)
            # result = stdout.read().strip()
            # tmp = {"check_point": "26", "result": False, "config": "", "judge": True}
            # if result:  # 存在结果
            #     if result != '':
            #         tmp["result"] = True
            #     tmp["config"] = "Health="+result
            # self.resultList.append(tmp)

            # # 5.27 - Ensure docker commands always get the latest version of the image
            # tmp = {"check_point": "27", "result": "False", "config": "", "judge": True}
            # self.resultList.append(tmp)

            # 5.28 - Ensure PIDs cgroup limit is used
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.PidsLimit }}' %s " % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.28", "result": False, "config": ""}
            if result:  # 存在结果
                if result != "0" and (result.isdigit() and (result) > 0):
                    tmp["result"] = True
                tmp["config"] = "PidsLimit=" + result
            self.resultList.append(tmp)

            # 5.29 - Ensure Docker's default bridge docker0 is not used
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker network inspect --format='{{ range $k, $v := .Containers }} "
                "{{ $k }} {{ end }}' %s 2>/dev/null"
                "|sed -e 's/^ //' -e  's/  /\n/g' 2>/dev/null" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.29", "result": False, "config": ""}
            if result:  # 存在结果
                if len(result) < 1:
                    tmp["result"] = True
            self.resultList.append(tmp)

            # 5.30 - Ensure the host's user namespaces is not shared
            stdin, stdout, stderr = self.ssh.exec_command(
                "docker inspect --format '{{ .HostConfig.UsernsMode }}' %s 2>/dev/null" % c_id)
            result = stdout.read().strip().decode()
            tmp = {"check_point": "5.30", "result": True, "config": ""}
            if result:  # 存在结果
                if "host" in result:
                    tmp["result"] = False
                tmp["config"] = "UsernsMode=" + result
            self.resultList.append(tmp)

            # # 5.31 - Ensure the Docker socket is not mounted inside any containers
            # stdin, stdout, stderr = self.ssh.exec_command("docker inspect --format '{{ .Mounts }}' %s 2>/dev/null" % c_id)
            # result = stdout.read().strip()
            # tmp = {"check_point": "31", "result": True, "config": "", "judge": True}
            # if result:  # 存在结果
            #     if "docker.sock" in result:
            #         tmp["result"] = False
            #     tmp["config"] = "Volumes=" + result
            # self.resultList.append(tmp)

            self.containers_id[c_id] = self.resultList

    def getResult(self):
        return self.containers_id

    def get_containers_id(self):
        containers_id = {}
        stdin, stdout, stderr = self.ssh.exec_command("docker ps --quiet --all --no-trunc")
        temp = stdout.read()
        result = temp.decode()
        if result:
            for c in result.strip().split('\n'):
                containers_id[str(c)] = {}
        return containers_id

