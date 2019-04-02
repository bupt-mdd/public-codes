# coding:utf-8

OK = 1
NO = 2
NOTKNOWN = 3

# 1表示可以配置项可以核查；0表示配置项未实现，不能核查
defaultRule = [
    1, 0, 1, 1, 1, 1, 1,
]

ManualRule = [
    1, 0, 1, 0, 1, 1, 0,
]

reportIndex = [
    '1.1.1', '1.1.2', '1.1.3', '1.1.4', '1.1.5', '1.1.6', '1.1.7',
]
# print('87个配置项')

# 报表内容字典，自定义编号作为索引，值为另一个字典
# 每一项报表条目包括：标题，等级，描述，检测方法，修复建议
reportContent = dict()
for i in reportIndex:
    reportContent[i] = {
        "title": u"""Title""",
        "level": u"""Level""",
        "description": u"""Description""",
        "audit": u"""Audit""",
        "remediation": u"""Remediation""",

    }

# ==============================================================================
# 此处开始为每一项的详细信息
# 注意：使用三重引号可以控制格式，主要是换行，空格的处理将按照HTML默认处理，换行在生成HTML是会特殊处理成<br />
# 注意：所有字符串都要用Unicode编码，即字符串前面加'u'字符，例如：u"""字符串"""
reportContent["1.1.1"] = {
    "title": u"""使用SASL对KVM进行远程管理要求项""",
    "level": u"""Scored""",

    "description": u"""默认情况下，通常使用SSH对KVM平台进行远程管理。这种情况下，KVM宿主机的账户密码将透漏给第三方，如果第三方使用该信息对KVM宿主机进行恶意操作或攻击，会导致KVM的敏感数据泄露或损坏。同时，无法对KVM平台进行账户管理。使用SASL远程管理的方式，可对远程管理KVM的用户进行身份验证，同时提供加密通道保证传输安全。(SASL) 提供了安全认证和数据加密，但是允许与传统或外部认证和授权服务集成。""",
    "audit": u"""1.	输入more /etc/libvirt/libvirtd.conf | grep listen_tls
2.	查看输出项：是否有listen_tls = 0项
3.	输入more /etc/libvirt/libvirtd.conf | grep listen_tcp
4.	查看输出项：是否有listen_tcp = 1项
5.	输入more /etc/libvirt/libvirtd.conf | grep auth_tcp
6.	查看输出项：是否有auth_tcp = "sasl"项""",
    "remediation": u"""N/A""",

}

reportContent["1.1.2"] = {
    "title": u"""开启nwfilter要求项""",
    "level": u"""Scored""",

    "description": u"""nwfilter全称network filtering，为虚拟化系统管理员提供对了一种网络流量的过滤规则，系统管理员可以通过配置过滤参数，实施和管理对虚拟机网络流量的接受和转发。由于过滤规则不能绕过直接进入虚拟机内，它使得一个filter对虚拟用户的访问控制具有强制性。Network filtering子系统允许每一个虚拟机的网络过滤表可以被单独配置。
开启nwfilter，控制VM的进入进出流量，不同于IP tables，nwfilter直接针对VM进行控制。network filtering部署在KVM Server上可以实现：虚拟网络隔离、入侵防护、批量管理等功能。""",
    "audit": u"""1.	输入virsh nwfilter-list，查看已存在的nwfilter,并且找到自己定义的策略：
(UUID)0247f98a-9736-e0ab-29a6-23fd0ac75258  (Name)mysecfilter(此处为自己定义的策略名) 
2.输入，查看interface接口，查看是否引用了nwfilter。
输入virsh edit test1，输出如下
<interface type=’network’>
<mac address=’54:52:00:5b:1a:cd’/>
<source network=’default’/>
<target dev=’vnet0’/>
<model type=’virtio’/>
<filterref filter=’mysecfilter’/>
</interface>
 3.filterref filter参数与virsh nwfilter-list输出的条目名称相同即判定合格。""",
    "remediation": u"""N/A""",

}

reportContent["1.1.3"] = {
    "title": u"""KVM启用selinux要求项""",
    "level": u"""Scored""",

    "description": u"""启用selinux，为KVM提供强制访问控制。普通的linux采用自由访问控制策略（Discretionary Acces Control ,DAC)策略来限制资源访问。这种策略比较简单薄弱，只要满足规定的权限（文件所有者和文件属性等）就可以使用资源，这很容易引起安全隐患，而且很难支持很多安全特性。
selinux基于强制访问策略（Mandatory Access Control ，MAC）限制资源访问的，应用程序必须同时满足DAC策略和MAC策略才能使用资源。DAC先于MAC生效，如果DAC本身不通过，那么MAC在这个过程没有参与，如果DAC通过，则selinux将对其进行进一步访问控制检查。（注：不做强制要求，业务优先，在不影响业务的情况下，可以开启。）""",
    "audit": u"""1.	输入getenforce,输出项为Enforcing合规""",
    "remediation": u"""N/A""",

}

reportContent["1.1.4"] = {
    "title": u"""KVM检查sVirt是否开启要求项""",
    "level": u"""Scored""",

    "description": u"""sVirt为KVM提供强制访问控制，sVirt是基于selinux的，sVirt可以给VM相应的进程、存储等打标签，实现MAC。在只使用dac策略虚拟化环境中，因为运行客户机的进程运行身份都是一样的，而且每个客户机都是使用相同的物理设备，当一台客户机被攻陷后，攻击者很可能利用它发起对宿主机的攻击。
svir使用基于进程的机制和约束为客户机提供了一个额外的安全保护层，它的一般的工作方式是这样的：在rhel系统中使用libvirt的守护进程（libvirtd）在后头管理客户机，在启动客户机之前，libvirt动态选择一个带有两个分类标志的随机mcs标签如（s0:c1,c2），将客户机使用的所有存储资源都打上相应的标签（svirt_image_t:s0:c1,c2)，然后用该标签启动客户机。当客户机试图使用磁盘资源而标签不一致的时候，则禁止访问，返回错误提示。""",
    "audit": u"""1.	输入ps -wwC qemu-kvm -o label,command，输出：
LABEL                                  COMMAND
system_u:system_r:svirt_t:s0:c372,c978 /usr/libexec/qemu-kvm 
2.	输入ll -aZ /var/lib/libvirt/images/，查看输出：
 -rw-------. qemu qemu unconfined_u:object_r:svirt_image_t:s0:c256,c965 test1.img
3.显示system_u:system_r:svirt_t:s0:c372,c978，其中type为svirt_t，标签为c372,c978，type项和标签值同时存在时，该项合格。""",
    "remediation": u"""N/A""",

}

reportContent["1.1.5"] = {
    "title": u"""KVM开启libvirt审计安全基线要求项""",
    "level": u"""Scored""",

    "description": u"""开启libvirt审计，对KVM的hypervisor层操作进行审计。开启libvirt审计后，它允许系统管理员、审计员，甚至其他应用程序访问虚拟化环境中详细的变更历史，包括客户机生命周期操作，以及主机资源到客户机的分配变化。通过审计虚拟化环境的详细数据可以及时发现潜在风险，提高虚拟化环境的安全性。""",
    "audit": u"""1.输入more  /etc/libvirt/libvirtd.conf | grep audit_level，输出audit_level = 1
    2.	输入more  /etc/libvirt/libvirtd.conf | grep audit_logging，输出：audit_logging = 1""",
    "remediation": u"""N/A""",

}

reportContent["1.1.6"] = {
    "title": u"""KVM开启ebtables安全基线要求项""",
    "level": u"""Scored""",

    "description": u"""ebtables即是以太网桥防火墙，以太网桥工作在数据链路层，ebtables来过滤数据链路层数据包，相当于给网桥设备设置防火墙。开启ebtables，当VM客户端MAC地址变化时，ebtables将根据规则对该VM所发出的流量进行操作，可以丢弃该流量，防止MAC冒用。""",
    "audit": u"""1.输入ebtables -L，输出为：
Bridge table: filter
Bridge chain: INPUT, entries: 0, policy: ACCEPT
Bridge chain: FORWARD, entries: 1, policy: ACCEPT
-s ! 54:52:0:5b:1a:cd -i vnet0 -j DROP 
Bridge chain: OUTPUT, entries: 0, policy: ACCEPT
2.由于网络方式选择桥接，所以规则在FORWARDchain才管用，-s ! 54:52:0:5b:1a:cd -i vnet0 -j DROP 为规则，其中54:52:0:5b:1a:cd，为VM的MAC地址，vnet0为VM所使用的虚拟网卡，DROP为操作项。当这三个参数均被填写且有效时，满足要求。""",
    "remediation": u"""N/A""",

}

reportContent["1.1.7"] = {
    "title": u"""KVM安全系统补丁安全基线要求项""",
    "level": u"""Scored""",

    "description": u"""在系统运行过程中，应保持KVM主机已安装的补丁与行业标准或内部指导要求保持一致，降低系统被攻击者通过漏洞攻击的风险。""",
    "audit": u"""1.输入qemu-img --help | grep version
2.已安装补丁列表完全包含行业标准或内部指导要求的补丁则符合要求。""",
    "remediation": u"""N/A""",

}
