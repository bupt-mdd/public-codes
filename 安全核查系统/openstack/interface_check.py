#coding:utf-8

from openstack.SSHManager import SSHManager

class OpenstackBenchmark(object):
    sshSession = None
    connectOK = None
    functionList = None
    result = None

    temp = 'FFF'

    def __init__(self, serverIP, port, userName, password):
        self.sshSession = SSHManager()
        if not self.sshSession.init(serverIP, port, userName, password):
            self.connectOK = False
        else:
            self.connectOK = True

        self.functionList = [
            self.fun1_1,
            self.fun1_2,
            self.fun1_3,
            self.fun1_4,
            self.fun1_5,
            self.fun1_6,
            self.fun1_7,
            self.fun2_1,
            self.fun3_1,
            self.fun3_2,
            self.fun3_3,
            self.fun3_4,
            self.fun4_1,
            self.fun4_2,
            self.fun4_3,
            self.fun4_4,
            self.fun5_1,
            self.fun5_2,
            self.fun5_3,
            self.fun5_4,
            self.fun5_5,
            self.fun5_6,
            self.fun5_7,
            self.fun5_8,
            self.fun5_9,
            self.fun5_10,
            self.fun5_11,
            self.fun5_12,
            self.fun5_13,
            self.fun6,
            self.fun7,
            self.fun8,
            self.fun9,
            self.fun10,
            self.fun11,
            self.fun12,
            self.fun13,
            self.fun14,
            self.fun15,
            self.fun16,
            self.fun17,
            self.fun18,
            self.fun19,
            self.fun20,
            self.fun21,
            self.fun22,
            self.fun23,
            self.fun24,
            self.fun25,
            self.fun26,
            self.fun27,
            self.fun28,
            self.fun29,
            self.fun30,
            self.fun31,
            self.fun32,
            self.fun33,

        ]

    def run(self):
        self.result = ''
        for i in range(len(self.functionList)):
            temp1 = self.functionList[i]()
            #print(temp1)
            if temp1 == 'FFF':
                self.result = ''
                break
            self.result = self.result + temp1

    def fun1_1(self):
        str1_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone.conf" ]  && echo "yes" || echo "no"')
        if str1_1 == "no":
            return 'F#' + '/etc/keystone/keystone.conf文件不存在#'
        elif str1_1 == 'FFF':
            return self.temp

        str1_1 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/keystone/keystone.conf | egrep "keystone keystone" 2>&1')
        if str1_1 == "keystone keystone":
            return 'T#' + '/etc/keystone/keystone.conf文件所属用户符合配置#'
        elif str1_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/keystone.conf文件所属用户不符合配置#'

    def fun1_2(self):
        str1_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone-paste.ini" ]  && echo "yes" || echo "no"')
        if str1_2 == "no":
            return 'F#' + '/etc/keystone/keystone-paste.ini文件不存在#'
        elif str1_2 == 'FFF':
            return self.temp

        str1_2 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/keystone/keystone-paste.ini | egrep "keystone keystone" 2>&1')
        if str1_2 == "keystone keystone":
            return 'T#' + '/etc/keystone/keystone-paste.ini文件所属用户符合配置#'
        elif str1_2 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/keystone-paste.ini文件所属用户不符合配置#'

    def fun1_3(self):
        str1_3 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/policy.json" ]  && echo "yes" || echo "no"')
        if str1_3 == "no":
            return 'F#' + '/etc/keystone/policy.json文件不存在#'
        elif str1_3 == 'FFF':
            return self.temp

        str1_3 = self.sshSession.ssh_cmd('stat -L -c "%U %G" /etc/keystone/policy.json | egrep "keystone keystone" 2>&1')
        if str1_3 == "keystone keystone":
            return 'T#' + '/etc/keystone/policy.json文件所属用户符合配置#'
        elif str1_3 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/policy.json文件所属用户不符合配置#'

    def fun1_4(self):
        str1_4 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/logging.conf" ]  && echo "yes" || echo "no"')
        if str1_4 == "no":
            return 'F#' + '/etc/keystone/logging.conf文件不存在#'
        elif str1_4 == 'FFF':
            return self.temp

        str1_4 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/keystone/logging.conf | egrep "keystone keystone" 2>&1')
        if str1_4 == "keystone keystone":
            return 'T#' + '/etc/keystone/logging.conf文件所属用户符合配置#'
        elif str1_4 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/logging.conf文件所属用户不符合配置#'

    def fun1_5(self):
        str1_5 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/ssl/certs/signing_cert.pem" ]  && echo "yes" || echo "no"')
        if str1_5 == "no":
            return 'F#' + '/etc/keystone/ssl/certs/signing_cert.pem文件不存在#'
        elif str1_5 == 'FFF':
            return self.temp

        str1_5 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/keystone/ssl/certs/signing_cert.pem | egrep "keystone keystone" 2>&1')
        if str1_5 == "keystone keystone":
            return 'T#' + '/etc/keystone/ssl/certs/signing_cert.pem文件所属用户符合配置#'
        elif str1_5 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/ssl/certs/signing_cert.pem文件所属用户不符合配置#'

    def fun1_6(self):
        str1_6 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/ssl/private/signing_key.pem" ]  && echo "yes" || echo "no"')
        if str1_6 == "no":
            return 'F#' + '/etc/keystone/ssl/private/signing_key.pem文件不存在#'
        elif str1_6 == 'FFF':
            return self.temp

        str1_6 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/keystone/ssl/private/signing_key.pem | egrep "keystone keystone" 2>&1')
        if str1_6 == "keystone keystone":
            return 'T#' + '/etc/keystone/ssl/private/signing_key.pem文件所属用户符合配置#'
        elif str1_6 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/ssl/private/signing_key.pem文件所属用户不符合配置#'

    def fun1_7(self):
        str1_7 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/ssl/certs/ca.pem" ]  && echo "yes" || echo "no"')
        if str1_7 == "no":
            return 'F#' + '/etc/keystone/ssl/certs/ca.pem文件不存在#' + 'E#'
        elif str1_7 == 'FFF':
            return self.temp

        str1_7 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/keystone/ssl/certs/ca.pem | egrep "keystone keystone" 2>&1')
        if str1_7 == "keystone keystone":
            return 'T#' + '/etc/keystone/ssl/certs/ca.pem文件所属用户符合配置#' + 'E#'
        elif str1_7 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/ssl/certs/ca.pem文件所属用户不符合配置#' + 'E#'

    def fun2_1(self):
        str2_1 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str2_1 == "no":
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str2_1 == 'FFF':
            return self.temp

        str2_1 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /opt/stack/horizon/openstack_dashboard/local/local_settings.py | egrep "root horizon" 2>&1')
        if str2_1 == "root horizon":
            return 'T#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件所属用户符合配置#' + 'E#'
        elif str2_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件所属用户不符合配置#' + 'E#'

    def fun3_1(self):
        str3_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/nova.conf" ]  && echo "yes" || echo "no"')
        if str3_1 == "no":
            return 'F#' + '/etc/nova/nova.conf文件不存在#'
        elif str3_1 == 'FFF':
            return self.temp

        str3_1 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/nova/nova.conf | egrep "root nova" 2>&1')
        if str3_1 == "root nova":
            return 'T#' + '/etc/nova/nova.conf文件所属用户符合配置#'
        elif str3_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/nova/nova.conf文件所属用户不符合配置#'

    def fun3_2(self):
        str3_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/api-paste.ini" ]  && echo "yes" || echo "no"')
        if str3_2 == "no":
            return 'F#' + '/etc/nova/api-paste.ini文件不存在#'
        elif str3_2 == 'FFF':
            return self.temp

        str3_2 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/nova/api-paste.ini | egrep "root nova" 2>&1')
        if str3_2 == "root nova":
            return 'T#' + '/etc/nova/api-paste.ini文件所属用户符合配置#'
        elif str3_2 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/nova/api-paste.ini文件所属用户不符合配置#'

    def fun3_3(self):
        str3_3 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/policy.json" ]  && echo "yes" || echo "no"')
        if str3_3 == "no":
            return 'F#' + '/etc/nova/policy.json文件不存在#'
        elif str3_3 == 'FFF':
            return self.temp

        str3_3 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/nova/policy.json | egrep "root nova" 2>&1')
        if str3_3 == "root nova":
            return 'T#' + '/etc/nova/policy.json文件所属用户符合配置#'
        elif str3_3 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/nova/policy.json文件所属用户不符合配置#'

    def fun3_4(self):
        str3_4 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/rootwrap.conf" ]  && echo "yes" || echo "no"')
        if str3_4 == "no":
            return 'F#' + '/etc/nova/rootwrap.conf文件不存在#' + 'E#'
        elif str3_4 == 'FFF':
            return self.temp

        str3_4 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/nova/rootwrap.conf | egrep "root nova" 2>&1')
        if str3_4 == "root nova":
            return 'T#' + '/etc/nova/rootwrap.conf文件所属用户符合配置#' + 'E#'
        elif str3_4 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/nova/rootwrap.conf文件所属用户不符合配置#' + 'E#'

    def fun4_1(self):
        str4_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str4_1 == "no":
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#'
        elif str4_1 == 'FFF':
            return self.temp

        str4_1 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/cinder/cinder.conf | egrep "root cinder" 2>&1')
        if str4_1 == "root cinder":
            return 'T#' + '/etc/cinder/cinder.conf文件所属用户符合配置#'
        elif str4_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/cinder.conf文件所属用户不符合配置#'

    def fun4_2(self):
        str4_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/api-paste.ini" ]  && echo "yes" || echo "no"')
        if str4_2 == "no":
            return 'F#' + '/etc/cinder/api-paste.ini文件不存在#'
        elif str4_2 == 'FFF':
            return self.temp

        str4_2 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/cinder/api-paste.ini | egrep "root cinder" 2>&1')
        if str4_2 == "root cinder":
            return 'T#' + '/etc/cinder/api-paste.ini文件所属用户符合配置#'
        elif str4_2 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/api-paste.ini文件所属用户不符合配置#'

    def fun4_3(self):
        str4_3 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/policy.json" ]  && echo "yes" || echo "no"')
        if str4_3 == "no":
            return 'F#' + '/etc/cinder/policy.json文件不存在#'
        elif str4_3 == 'FFF':
            return self.temp

        str4_3 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/cinder/policy.json | egrep "root cinder" 2>&1')
        if str4_3 == "root cinder":
            return 'T#' + '/etc/cinder/policy.json文件所属用户符合配置#'
        elif str4_3 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/policy.json文件所属用户不符合配置#'

    def fun4_4(self):
        str4_4 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/rootwrap.conf" ]  && echo "yes" || echo "no"')
        if str4_4 == "no":
            return 'F#' + '/etc/cinder/rootwrap.conf文件不存在#' + 'E#'
        elif str4_4 == 'FFF':
            return self.temp

        str4_4 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/cinder/rootwrap.conf | egrep "root cinder" 2>&1')
        if str4_4 == "root cinder":
            return 'T#' + '/etc/cinder/rootwrap.conf文件所属用户符合配置#' + 'E#'
        elif str4_4 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/rootwrap.conf文件所属用户不符合配置#' + 'E#'

    def fun5_1(self):
        str5_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-api-paste.ini" ]  && echo "yes" || echo "no"')
        if str5_1 == "no":
            return 'F#' + '/etc/glance/glance-api-paste.ini文件不存在#'
        elif str5_1 == 'FFF':
            return self.temp

        str5_1 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-api-paste.ini | egrep "root glance" 2>&1')
        if str5_1 == "root glance":
            return 'T#' + '/etc/glance/glance-api-paste.ini文件所属用户符合配置#'
        elif str5_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-api-paste.ini文件所属用户不符合配置#'

    def fun5_2(self):
        str5_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-api.conf" ]  && echo "yes" || echo "no"')
        if str5_2 == "no":
            return 'F#' + '/etc/glance/glance-api.conf文件不存在#'
        elif str5_2 == 'FFF':
            return self.temp

        str5_2 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-api.conf | egrep "root glance" 2>&1')
        if str5_2 == "root glance":
            return 'T#' + '/etc/glance/glance-api.conf文件所属用户符合配置#'
        elif str5_2 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-api.conf文件所属用户不符合配置#'

    def fun5_3(self):
        str5_3 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-manage.conf" ]  && echo "yes" || echo "no"')
        if str5_3 == "no":
            return 'F#' + '/etc/glance/glance-manage.conf文件不存在#'
        elif str5_3 == 'FFF':
            return self.temp

        str5_3 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-manage.conf | egrep "root glance" 2>&1')
        if str5_3 == "root glance":
            return 'T#' + '/etc/glance/glance-manage.conf文件所属用户符合配置#'
        elif str5_3 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-manage.conf文件所属用户不符合配置#'

    def fun5_4(self):
        str5_4 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/glance/etc/oslo-config-generator/glance-manage.conf" ]  && echo "yes" || echo "no"')
        if str5_4 == "no":
            return 'F#' + '/opt/stack/glance/etc/oslo-config-generator/glance-manage.conf文件不存在#'
        elif str5_4 == 'FFF':
            return self.temp

        str5_4 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /opt/stack/glance/etc/oslo-config-generator/glance-manage.conf | egrep "root glance" 2>&1')
        if str5_4 == "root glance":
            return 'T#' + '/opt/stack/glance/etc/oslo-config-generator/glance-manage.conf文件所属用户符合配置#'
        elif str5_4 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/opt/stack/glance/etc/oslo-config-generator/glance-manage.conf文件所属用户不符合配置#'

    def fun5_5(self):
        str5_5 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-registry-paste.ini" ]  && echo "yes" || echo "no"')
        if str5_5 == "no":
            return 'F#' + '/etc/glance/glance-registry-paste.ini文件不存在#'
        elif str5_5 == 'FFF':
            return self.temp

        str5_5 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-registry-paste.ini | egrep "root glance" 2>&1')
        if str5_5 == "root glance":
            return 'T#' + '/etc/glance/glance-registry-paste.ini文件所属用户符合配置#'
        elif str5_5 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-registry-paste.ini文件所属用户不符合配置#'

    def fun5_6(self):
        str5_6 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-registry.conf" ]  && echo "yes" || echo "no"')
        if str5_6 == "no":
            return 'F#' + '/etc/glance/glance-registry.conf文件不存在#'
        elif str5_6 == 'FFF':
            return self.temp

        str5_6 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-registry.conf | egrep "root glance" 2>&1')
        if str5_6 == "root glance":
            return 'T#' + '/etc/glance/glance-registry.conf文件所属用户符合配置#'
        elif str5_6 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-registry.conf文件所属用户不符合配置#'

    def fun5_7(self):
        str5_7 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-scrubber.conf" ]  && echo "yes" || echo "no"')
        if str5_7 == "no":
            return 'F#' + '/etc/glance/glance-scrubber.conf文件不存在#'
        elif str5_7 == 'FFF':
            return self.temp

        str5_7 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-scrubber.conf | egrep "root glance" 2>&1')
        if str5_7 == "root glance":
            return 'T#' + '/etc/glance/glance-scrubber.conf文件所属用户符合配置#'
        elif str5_7 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-scrubber.conf文件所属用户不符合配置#'

    def fun5_8(self):
        str5_8 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/glance/etc/oslo-config-generator/glance-scrubber.conf" ]  && echo "yes" || echo "no"')
        if str5_8 == "no":
            return 'F#' + '/opt/stack/glance/etc/oslo-config-generator/glance-scrubber.conf文件不存在#'
        elif str5_8 == 'FFF':
            return self.temp

        str5_8 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /opt/stack/glance/etc/oslo-config-generator/glance-scrubber.conf | egrep "root glance" 2>&1')
        if str5_8 == "root glance":
            return 'T#' + '/opt/stack/glance/etc/oslo-config-generator/glance-scrubber.conf文件所属用户符合配置#'
        elif str5_8 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/opt/stack/glance/etc/oslo-config-generator/glance-scrubber.conf文件所属用户不符合配置#'

    def fun5_9(self):
        str5_9 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-swift-store.conf" ]  && echo "yes" || echo "no"')
        if str5_9 == "no":
            return 'F#' + '/etc/glance/glance-swift-store.conf文件不存在#'
        elif str5_9 == 'FFF':
            return self.temp

        str5_9 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-swift-store.conf | egrep "root glance" 2>&1')
        if str5_9 == "root glance":
            return 'T#' + '/etc/glance/glance-swift-store.conf文件所属用户符合配置#'
        elif str5_9 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-swift-store.conf文件所属用户不符合配置#'

    def fun5_10(self):
        str5_10 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/policy.json" ]  && echo "yes" || echo "no"')
        if str5_10 == "no":
            return 'F#' + '/etc/glance/policy.json文件不存在#'
        elif str5_10 == 'FFF':
            return self.temp

        str5_10 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/policy.json | egrep "root glance" 2>&1')
        if str5_10 == "root glance":
            return 'T#' + '/etc/glance/policy.json文件所属用户符合配置#'
        elif str5_10 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/policy.json文件所属用户不符合配置#'

    def fun5_11(self):
        str5_11 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-cache.conf" ]  && echo "yes" || echo "no"')
        if str5_11 == "no":
            return 'F#' + '/etc/glance/glance-cache.conf文件不存在#'
        elif str5_11 == 'FFF':
            return self.temp

        str5_11 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/glance-cache.conf | egrep "root glance" 2>&1')
        if str5_11 == "root glance":
            return 'T#' + '/etc/glance/glance-cache.conf文件所属用户符合配置#'
        elif str5_11 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-cache.conf文件所属用户不符合配置#'

    def fun5_12(self):
        str5_12 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/schema-image.json" ]  && echo "yes" || echo "no"')
        if str5_12 == "no":
            return 'F#' + '/etc/glance/schema-image.json文件不存在#'
        elif str5_12 == 'FFF':
            return self.temp

        str5_12 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/schema-image.json | egrep "root glance" 2>&1')
        if str5_12 == "root glance":
            return 'T#' + '/etc/glance/schema-image.json文件所属用户符合配置#'
        elif str5_12 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/schema-image.json文件所属用户不符合配置#'

    def fun5_13(self):
        str5_13 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/schema.json" ]  && echo "yes" || echo "no"')
        if str5_13 == "no":
            return 'F#' + '/etc/glance/schema.json文件不存在#' + 'E#'
        elif str5_13 == 'FFF':
            return self.temp

        str5_13 = self.sshSession.ssh_cmd(
            'stat -L -c "%U %G" /etc/glance/schema.json | egrep "root glance" 2>&1')
        if str5_13 == "root glance":
            return 'T#' + '/etc/glance/schema.json文件所属用户符合配置#' + 'E#'
        elif str5_13 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/schema.json文件所属用户不符合配置#' + 'E#'

    def fun6(self):
        str6 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone.conf" ]  && echo "yes" || echo "no"')
        if str6 == 'no':
            return 'F#' + '/etc/keystone/keystone.conf文件不存在#' + 'E#'
        elif str6 == 'FFF':
            return self.temp

        str6 = self.sshSession.ssh_cmd('grep -c "^[ ]*hash_algorithm[ ]*=[ ]*SHA256" /etc/keystone/keystone.conf 2>/dev/null')
        if str6 == '1':
            return 'T#' + '身份令牌使用了SHA256哈希算法#' + 'E#'
        elif str6 == 'FFF':
            return self.temp
        else:
            return 'F#' + '身份令牌中并没有使用SHA256哈希算法#' + 'E#'

    def fun7(self):
        str7 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone.con" ]  && echo "yes" || echo "no"')
        if str7 == 'no':
            return 'F#' + '/etc/keystone/keystone.conf文件不存在#' + 'E#'
        elif str7 == 'FFF':
            return self.temp

        str7 = self.sshSession.ssh_cmd('grep -c "^[ ]*max_request_body_size[ ]*=[ ]*114688" /etc/keystone/keystone.conf 2>/dev/null')
        if str7 == '1':
            return 'T#' + '身份令牌使用了SHA256哈希算法#' + 'E#'
        elif str7 == 'FFF':
            return self.temp
        else:
            return 'F#' + '身份令牌中并没有使用SHA256哈希算法#' + 'E#'

    def fun8(self):
        str8_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone.conf" ]  && echo "yes" || echo "no"')
        str8_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone-paste.ini" ]  && echo "yes" || echo "no"')
        if str8_1 == 'yes':
            if str8_2 == 'no':
                return 'F#' + '/etc/keystone/keystone-paste.ini文件不存在#' + 'E#'
            elif str8_2 == 'FFF':
                return self.temp
        elif str8_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/keystone/keystone.conf文件不存在#' + 'E#'

        str8_1 = self.sshSession.ssh_cmd('grep -c "^[ ]*admin_token[ ]*=[ ]*[^ *#]\+" /etc/keystone/keystone.conf 2>/dev/null')
        str8_2 = self.sshSession.ssh_cmd('grep -c "^[ ]*filter[ ]*:[ ]*admin_token_auth" /etc/keystone/keystone-paste.ini 2>/dev/null')
        if str8_1 == '0':
            if str8_2 == '0':
                return 'T#' + '符合配置#' + 'E#'
            elif str8_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'keystone-paste.ini文件中的[filter:admin_token_auth]参数没有被删除#' + 'E#'
        elif str8_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'keystone.conf文件中的admin_token被设置#' + 'E#'

    def fun9(self):
        str9 = self.sshSession.ssh_cmd(
            '[ -f "/etc/keystone/keystone.conf" ]  && echo "yes" || echo "no"')
        if str9 == 'no':
            return 'F#' + '/etc/keystone/keystone.conf文件不存在#' + 'E#'
        elif str9 == 'FFF':
            return self.temp

        str9 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*insecure_debug[ ]*=[ ]*[Ff]alse" /etc/keystone/keystone.conf 2>/dev/null')
        if str9 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str9 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'insecure_debug值未设置为false#' + 'E#'

    def fun10(self):
        str10 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/nova.conf" ]  && echo "yes" || echo "no"')
        if str10 == 'no':
            return 'F#' + '/etc/nova/nova.conf文件不存在#' + 'E#'
        elif str10 == 'FFF':
            return self.temp

        str10 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_strategy[ ]*=[ ]*keystone" /etc/nova/nova.conf 2>/dev/null')
        if str10 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str10 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'nova身份认证未使用keystone#' + 'E#'

    def fun11(self):
        str11_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/nova.conf" ]  && echo "yes" || echo "no"')
        str11_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/nova.conf" ]  && echo "yes" || echo "no"')
        if str11_1 == 'yes':
            if str11_2 == 'no':
                return 'F#' + '/etc/nova/nova.conf文件不存在#' + 'E#'
            elif str11_2 == 'FFF':
                return self.temp
        elif str11_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/nova/nova.conf文件不存在#' + 'E#'

        str11_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_uri[ ]*=[ ]*https" /etc/nova/nova.conf 2>/dev/null')
        str11_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*insecure[ ]*=[ ]*[Ff]alse" /etc/nova/nova.conf 2>/dev/null')
        if str11_1 == '1':
            if str11_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str11_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'nova.conf文件中的insecure值未设置为false#' + 'E#'
        elif str11_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'nova.conf文件中的auth_uri未设置为以https://开头#' + 'E#'

    def fun12(self):
        str12 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str12 == 'no':
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'
        elif str12 == 'FFF':
            return self.temp

        str12 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_strategy[ ]*=[ ]*keystone" /etc/cinder/cinder.conf 2>/dev/null')
        if str12 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str12 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'Cinder身份认证未使用keystone#' + 'E#'

    def fun13(self):
        str13_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        str13_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str13_1 == 'yes':
            if str13_2 == 'no':
                return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'
            elif str13_2 == 'FFF':
                return self.temp
        elif str13_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'

        str13_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_uri[ ]*=[ ]*https" /etc/cinder/cinder.conf 2>/dev/null')
        str13_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*insecure[ ]*=[ ]*[Ff]alse" /etc/cinder/cinder.conf 2>/dev/null')
        if str13_1 == '1':
            if str13_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str13_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'cinder.conf文件中的insecure值未设置为false#' + 'E#'
        elif str13_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'cinder.conf文件中的auth_uri未设置为以https://开头#' + 'E#'

    def fun14(self):
        str14_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-api.conf" ]  && echo "yes" || echo "no"')
        str14_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-registry.conf" ]  && echo "yes" || echo "no"')
        if str14_1 == 'yes':
            if str14_2 == 'no':
                return 'F#' + '/etc/glance/glance-registry.conf文件不存在#' + 'E#'
            elif str14_2 == 'FFF':
                return self.temp
        elif str14_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-api.conf文件不存在#' + 'E#'

        str14_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_strategy[ ]*=[ ]*keystone" /etc/glance/glance-api.conf 2>/dev/null')
        str14_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_strategy[ ]*=[ ]*keystone" /etc/glance/glance-registry.conf 2>/dev/null')
        if str14_1 == '1':
            if str14_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str14_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'glance-registry.conf文件的auth_strategy未被设置成keystone#' + 'E#'
        elif str14_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'glance-api.conf文件的auth_strategy未被设置成keystone#' + 'E#'

    def fun15(self):
        str15_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-api.conf" ]  && echo "yes" || echo "no"')
        str15_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/glance/glance-registry.conf" ]  && echo "yes" || echo "no"')
        if str15_1 == 'yes':
            if str15_2 == 'no':
                return 'F#' + '/etc/glance/glance-registry.conf文件不存在#' + 'E#'
            elif str15_2 == 'FFF':
                return self.temp
        elif str15_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/glance/glance-api.conf文件不存在#' + 'E#'

        str15_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_uri[ ]*=[ ]*https" /etc/glance/glance-api.conf 2>/dev/null')
        str15_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*insecure[ ]*=[ ]*[Ff]alse" /etc/glance/glance-registry.conf 2>/dev/null')
        if str15_1 == '1':
            if str15_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str15_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'glance-registry.conf文件中的insecure值未设置为false#' + 'E#'
        elif str15_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'glance-api.conf文件中的auth_uri未设置为以https://开头#' + 'E#'

    def fun16(self):
        str16 = self.sshSession.ssh_cmd(
            '[ -f "/etc/neutron/neutron.conf" ]  && echo "yes" || echo "no"')
        if str16 == 'no':
            return 'F#' + '/etc/neutron/neutron.conf文件不存在#' + 'E#'
        elif str16 == 'FFF':
            return self.temp

        str16 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_strategy[ ]*=[ ]*keystone" /etc/neutron/neutron.conf 2>/dev/null')
        if str16 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str16 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'Neutron身份认证不是keystone#' + 'E#'

    def fun17(self):
        str8_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/neutron/neutron.conf" ]  && echo "yes" || echo "no"')
        str8_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/neutron/neutron.conf" ]  && echo "yes" || echo "no"')
        if str8_1 == 'yes':
            if str8_2 == 'no':
                return 'F#' + '/etc/neutron/neutron.conf文件不存在#' + 'E#'
            elif str8_2 == 'FFF':
                return self.temp
        elif str8_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/neutron/neutron.conf文件不存在#' + 'E#'

        str8_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*auth_uri[ ]*=[ ]*https" /etc/neutron/neutron.conf 2>/dev/null')
        str8_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*insecure[ ]*=[ ]*[Ff]alse" /etc/neutron/neutron.conf 2>/dev/null')
        if str8_1 == '1':
            if str8_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str8_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'neutron.conf文件中的insecure值未设置为false#' + 'E#'
        elif str8_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'neutron.conf文件中的auth_uri未设置为以https://开头#' + 'E#'

    def fun18(self):
        str18 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str18 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str18 == 'FFF':
            return self.temp

        str18 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*SESSION_COOKIE_HTTPONLY[ ]*=[ ]*off" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str18 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str18 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的SESSION_COOKIE_HTTPONLY参数未设置为off#' + 'E#'

    def fun19(self):
        str19 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str19 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str19 == 'FFF':
            return self.temp


        str19 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*DISABLE_PASSWORD_REVEAL[ ]*=[ ]*[Tt]rue" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str19 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str19 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的DISABLE_PASSWORD_REVEAL参数未设置为True#' + 'E#'

    def fun20(self):
        str20 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str20 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str20 == 'FFF':
            return self.temp

        str20 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*ENFORCE_PASSWORD_CHECK[ ]*=[ ]*[Tt]rue" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str20 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str20 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的ENFORCE_PASSWORD_CHECK参数未设置为True#' + 'E#'

    def fun21(self):
        str21 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str21 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str21 == 'FFF':
            return self.temp

        str21 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*PASSWORD_VALIDATOR[ ]*=[ ]*[^ *#]\+" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str21 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str21 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的PASSWORD_VALIDATOR参数未设置#' + 'E#'

    def fun22(self):
        str22 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str22 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str22 == 'FFF':
            return self.temp

        str22 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*DISALLOW_IFRAME_EMBED[ ]*=[ ]*[Tt]rue" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str22 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str22 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的DISALLOW_IFRAME_EMBED参数未设置为True#' + 'E#'

    def fun23(self):
        str23 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str23 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str23 == 'FFF':
            return self.temp

        str23 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*CSRF_COOKIE_SECURE[ ]*=[ ]*[Tt]rue" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str23 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str23 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的CSRF_COOKIE_SECURE参数未设置为True#' + 'E#'

    def fun24(self):
        str24 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str24 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str24 == 'FFF':
            return self.temp

        str24 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*SESSION_COOKIE_SECURE[ ]*=[ ]*[Tt]rue" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str24 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str24 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的SESSION_COOKIE_SECURE参数未设置为True#' + 'E#'

    def fun25(self):
        str25 = self.sshSession.ssh_cmd(
            '[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"')
        if str25 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str25 == 'FFF':
            return self.temp

        str25 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*SESSION_COOKIE_HTTPONLY[ ]*=[ ]*[Tt]rue" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null')
        if str25 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str25 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的SESSION_COOKIE_HTTPONLY参数未设置为True#' + 'E#'

    def fun26(self):
        str26 = self.sshSession.ssh_cmd(
            '''[ -f "/opt/stack/horizon/openstack_dashboard/local/local_settings.py" ]  && echo "yes" || echo "no"''')
        if str26 == 'no':
            return 'F#' + '/opt/stack/horizon/openstack_dashboard/local/local_settings.py文件不存在#' + 'E#'
        elif str26 == 'FFF':
            return self.temp

        str26 = self.sshSession.ssh_cmd(
            '''grep -c "^[ ]*SECURE_PROXY_SSL_HEADER[ ]*=[ ]*([ ]*'HTTP_X_FORWARDED_PROTO'[ ]*,[ ]*'https'[ ]*)" /opt/stack/horizon/openstack_dashboard/local/local_settings.py 2>/dev/null''')
        if str26 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str26 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'local_settings.py文件中的SECURE_PROXY_SSL_HEADER参数未设置为HTTP_X_FORWARDED_PROTO, https#' + 'E#'

    def fun27(self):
        str27_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/nova.conf" ]  && echo "yes" || echo "no"')
        if str27_1 == 'no':
            return 'F#' + '/etc/nova/nova.conf文件不存在#' + 'E#'
        elif str27_1 == 'FFF':
            return self.temp

        str27_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*api_insecure[ ]*=[ ]*[Ff]alse" /etc/nova/nova.conf 2>/dev/null')
        str27_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*api_servers[ ]*=[ ]*https" /etc/nova/nova.conf 2>/dev/null')
        if str27_1 == '1':
            if str27_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str27_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'nova.conf文件中的api_servers未设置成https://#' + 'E#'
        elif str27_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'nova.conf文件中的api_insecure未设置成false#' + 'E#'

    def fun28(self):
        str28 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str28 == 'no':
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'
        elif str28 == 'FFF':
            return self.temp

        str28 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*nova_api_insecure[ ]*=[ ]*[Ff]alse" /etc/cinder/cinder.conf 2>/dev/null')
        if str28 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str28 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'cinder.conf文件中的nova_api_insecure未设置为false#' + 'E#'

    def fun29(self):
        str29_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str29_1 == 'no':
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'
        elif str29_1 == 'FFF':
            return self.temp

        str29_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*glance_api_insecure[ ]*=[ ]*[Ff]alse" /etc/cinder/cinder.conf 2>/dev/null')
        str29_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*glance_api_servers[ ]*=[ ]*https" /etc/cinder/cinder.conf 2>/dev/null')
        if str29_1 == '1':
            if str29_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str29_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'cinder.conf文件中的未设置为以https://开头#' + 'E#'
        elif str29_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'cinder.conf文件中的未设置为false#' + 'E#'

    def fun30(self):
        str30 = self.sshSession.ssh_cmd(
            '[ -f "/etc/neutron/neutron.conf" ]  && echo "yes" || echo "no"')
        if str30 == 'no':
            return 'F#' + '/etc/neutron/neutron.conf文件不存在#' + 'E#'
        elif str30 == 'FFF':
            return self.temp

        str30 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*use_ssl[ ]*=[ ]*[Tt]rue" /etc/neutron/neutron.conf 2>/dev/null')
        if str30 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str30 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'neutron.conf文件中的use_ssl未设置为true#' + 'E#'

    def fun31(self):
        str31 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str31 == 'no':
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'
        elif str31 == 'FFF':
            return self.temp

        str31 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*nas_secure_file_permissions[ ]*=[ ]*[Aa]uto" /etc/cinder/cinder.conf 2>/dev/null')
        if str31 == '1':
            return 'T#' + '符合配置#' + 'E#'
        elif str31 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'lcinder.conf文件中的nas_secure_file_permissions未设置为auto#' + 'E#'

    def fun32(self):
        str32_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        str32_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        if str32_1 == 'yes':
            if str32_2 == 'no':
                return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'
            elif str32_2 == 'FFF':
                return self.temp
        elif str32_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'

        str32_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*osapi_max_request_body_size[ ]*=[ ]*114688" /etc/cinder/cinder.conf 2>/dev/null')
        str32_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*max_request_body_size[ ]*=[ ]*114688" /etc/cinder/cinder.conf 2>/dev/null')
        if str32_1 == '1':
            if str32_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str32_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'cinder.conf文件中的max_request_body_size未设置为114688#' + 'E#'
        elif str32_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'cinder.conf文件中的osapi_max_request_body_size未设置为114688#' + 'E#'

    def fun33(self):
        str33_1 = self.sshSession.ssh_cmd(
            '[ -f "/etc/cinder/cinder.conf" ]  && echo "yes" || echo "no"')
        str33_2 = self.sshSession.ssh_cmd(
            '[ -f "/etc/nova/nova.conf" ]  && echo "yes" || echo "no"')
        if str33_1 == 'yes':
            if str33_2 == 'no':
                return 'F#' + '/etc/nova/nova.conf文件不存在#' + 'E#'
            elif str33_2 == 'FFF':
                return self.temp
        elif str33_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + '/etc/cinder/cinder.conf文件不存在#' + 'E#'

        str33_1 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*api_class[ ]*=[ ]*[^ *#]\+" /etc/cinder/cinder.conf 2>/dev/null')
        str33_2 = self.sshSession.ssh_cmd(
            'grep -c "^[ ]*api_class[ ]*=[ ]*[^ *#]\+" /etc/nova/nova.conf 2>/dev/null')
        if str33_1 == '1':
            if str33_2 == '1':
                return 'T#' + '符合配置#' + 'E#'
            elif str33_2 == 'FFF':
                return self.temp
            else:
                return 'F#' + 'nova.conf文件中的api_class未设置#' + 'E#'
        elif str33_1 == 'FFF':
            return self.temp
        else:
            return 'F#' + 'cinder.conf文件中的api_class未设置#' + 'E#'

    def getResult(self):
        return self.result

if __name__ == '__main__':
    instance = OpenstackBenchmark(serverIP='10.108.114.24', port='2222', userName='root', password='123456')
    instance.run()
    print(instance.getResult())