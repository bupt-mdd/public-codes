# coding: utf-8

from flask import Flask, request
import vmware.interface_scan as VMware_scan
import vmware.interface_check as VMware_check
import kvm.interface_check as KVM_check
import openstack.interface_check as Openstack_check
import kubernetes.interface_check as Kubernetes_check
import docker.interface_check as Docker_check

app = Flask(__name__)

@app.route('/test')
def test_page():
    return "用于测试tests"

@app.route('/testConn', methods={'GET', 'POST'})
def test_connection():
    if request.method == 'POST':
        ip_addr = request.form['ip_addr']
        service_type = request.form['service_type']
        user = request.form['user']
        pwd = request.form['pwd']
        port = int(request.form['port'])
        strings = test_Account(service_type, ip_addr, user, pwd, port)
        return strings
    if request.method == 'GET':
        ip_addr = request.form['ip_addr']
        service_type = request.form['service_type']
        user = request.form['user']
        pwd = request.form['pwd']
        port = int(request.form['port'])
        strings = test_Account(service_type, ip_addr, user, pwd, port)
        return strings

# 测试账户密码正确性
def test_Account(type, ip_addr, user, pwd, PORT):
    if type == 'VMware':
        configure = {
        'SERVER' : ip_addr,
        'USER' : user,
        'PORT' : PORT or 22,
        'PWD' : pwd,
        }
        return VMware_scan.test(configure)
    elif type == 'openstack':
        openstackConfigure = {
            'SERVER': ip_addr,
            'PORT': PORT,
            'USER': user,
            "PWD": pwd,
        }
        return VMware_scan.test(openstackConfigure)
    elif type == 'KVM':
        configure = {
        'SERVER' : ip_addr,
        'USER' : user,
        'PORT' : PORT or 22,
        'PWD' : pwd,
        }
        return VMware_scan.test(configure)
    elif type == 'kubernetes':
        configure = {
            'SERVER': ip_addr,
            'USER': user,
            'PWD': pwd,
            'PORT': PORT
        }
        return VMware_scan.test(configure)
    elif type == 'Docker':
        configure = {
            'SERVER': ip_addr,
            'USER': user,
            'PWD': pwd,
            'PORT': PORT
        }
        return VMware_scan.test(configure)
    else:
        return False

@app.route('/check', methods={'GET', 'POST'})
def benchmark_mark():
    if request.method == 'POST':
        ip_addr = request.form['ip_addr']
        service_type = request.form['service_type']
        user = request.form['user']
        pwd = request.form['pwd']
        port = int(request.form['port'])
        nodetype = ""
        if service_type == "kubernetes":
            nodetype = request.form['type']
        strings = benchmark(service_type, ip_addr, user, pwd, port, nodetype)
        return strings
    if request.method == 'GET':
        ip_addr = request.form['ip_addr']
        return ip_addr
        service_type = request.form['service_type']
        user = request.form['user']
        pwd = request.form['pwd']
        port = int(request.form['port'])
        nodetype = ""
        if service_type == "kubernetes":
            nodetype = request.form['type']
        strings = benchmark(service_type, ip_addr, user, pwd, port, nodetype)
        return strings

# 工具自动化配置核查
def benchmark(type, ip_addr, user, pwd, PORT, nodetype):
    if type == "VMware":
        return VMware_check.main(rule=None, server=ip_addr, port=PORT or 22, user=user, password=pwd)
    elif type == "openstack":
        instance = Openstack_check(serverIP=ip_addr, port=PORT, userName=user, password=pwd)
        instance.run()
        return instance.getResult()
    elif type == "KVM":
        return KVM_check.main(rule=None, server=ip_addr, port=PORT or 22, user=user, password=pwd)
    elif type == "kubernetes":
        return Kubernetes_check.main(server=ip_addr, user=user, password=pwd, port=PORT, type=nodetype)
    elif type == "Docker":
        return Docker_check.main(server=ip_addr, user=user, password=pwd, port=PORT)
    else:
        return None

@app.route('/manualCheck', methods={'GET', 'POST'})
def manual_check():
    if request.method == 'POST':
        service_type = request.form['type']
        method = 'POST'
        strings = manualCheck(service_type,method)
        return strings

    if request.method == 'GET':
        service_type = request.form['type']
        method = 'GET'
        strings = manualCheck(service_type, method)
        return strings

# 人工手动核查
def manualCheck(service_type,method):
    if method == 'POST':
        if service_type == "VMware":
            strings = VMware_check.manualCheck()
            return strings
        elif service_type == 'KVM':
            strings = KVM_check.manualCheck()
            return strings
    if method == 'GET':
        if service_type == "VMware":
            strings = VMware_check.manualCheck()
            return strings
        elif service_type == 'KVM':
            strings = KVM_check.manualCheck()
            return strings

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5050)
