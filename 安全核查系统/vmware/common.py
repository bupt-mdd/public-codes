# -*- coding: utf-8 -*-

OK = 1
NO = 2
NOTKNOWN = 3

# 1表示可以配置项可以核查；0表示配置项未实现，不能核查
defaultRule = [
    1,1,1,                  # 第一部分 3
    1,1,1,0,1,1,0,          # 第二部分 7
    1,1,1,                  # 第三部分 3
    0,0,1,0,                # 第四部分 4
    1,1,1,1,0,0,1,1,1,0,     # 第五部分 10
    0,0,0,0,                    # 第六部分 4　个
    1,1,1,1,0,0,                 # 第七部分 6
    1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,# 第八部分 50
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    1,1,0,1,1,1,1,1,1,1,
    1,
]

manualDefaultRule = [
    0,1,1,                  # 第一部分 3
    1,1,1,0,1,1,0,          # 第二部分 7
    1,1,1,                  # 第三部分 3
    0,0,1,0,                # 第四部分 4
    1,1,1,1,0,0,1,1,1,0,     # 第五部分 10
    0,0,0,0,                    # 第六部分 4　个
    1,1,1,1,0,0,                 # 第七部分 6
    1,1,1,1,1,1,1,1,1,0,0,0,0,0,1,1,1,1,1,1,# 第八部分 50
    1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
    1,1,0,1,1,1,1,1,1,1,
    1,
]

reportIndex = [
    '1.1','1.2','1.3',
    '2.1','2.2','2.3','2.4','2.5','2.6','2.7',
    '3.1','3.2','3.3',
    '4.1','4.2','4.3','4.4',
    '5.1','5.2','5.3','5.4','5.5','5.6','5.7','5.8','5.9','5.10',
    '6.1','6.2','6.3','6.4',
    '7.1','7.2','7.3','7.4','7.5','7.6',
    '8.1.1','8.1.2',
    '8.2.1','8.2.2','8.2.3','8.2.4','8.2.5','8.2.6','8.2.7',
    '8.3.1','8.3.2','8.3.3','8.3.4',
    '8.4.1','8.4.2','8.4.3','8.4.4','8.4.5','8.4.6','8.4.7','8.4.8','8.4.9','8.4.10',
    '8.4.11','8.4.12','8.4.13','8.4.14','8.4.15','8.4.16','8.4.17','8.4.18','8.4.19',
    '8.4.20','8.4.21','8.4.22','8.4.23','8.4.24','8.4.25','8.4.26','8.4.27','8.4.28',
    '8.4.29',
    '8.5.1',
    '8.6.1','8.6.2','8.6.3',
    '8.7.1','8.7.2','8.7.3','8.7.4',
    '9.1'
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
reportContent["1.1"] = {
    "title": u"""确保ESXI系统补丁的合理性""",
    "level": u"""Scored""",

    "description": u"""VMware Update Manager是一种用于vSphere主机和虚拟机的自动补丁管理的工具。 为补丁创建基准是确保所有主机都是在相同的补丁级别的好方法。
        通过及时更新ESXi补丁，可以减轻虚拟机监视器中的漏洞。 在EXSI主机上，一个
        受过教育的攻击者可以在尝试获取访问权限或者提升权限时利用已知的漏洞。""",

    "audit": u"""根据行业标准和内部指南，采用一个流程使ESXi主机保持最新的补丁程序。 VMware Update Manager是一种自动化的工具，对这些非常有帮助。 
        VMware还发布了有关安全补丁的Advisories，并提供了一个
        订阅电子邮件提醒的方式。 以下Power Shell代码段将提供所有已安装补丁的列表：
        Foreach ($VMHost in Get-VMHost ) {
        $ESXCli = Get-EsxCli -VMHost $VMHost;
        $ESXCli.software.vib.list() | Select-Object @{N="VMHost";E={$VMHost}}, Name,
        AcceptanceLevel, CreationDate, ID, InstallDate, Status, Vendor, Version;
        }""",
    "remediation": u"""利用VMware Update Manager在可利用时测试和应用补丁。""",
}

reportContent["1.2"] = {
    "title": u"""验证镜像配置文件和VIB接受级别""",
    "level": u"""Scored""",

    "description": u"""ESXi镜像配置文件支持四种VIB接受级别。 VIB（vSphere Installation Bundle）是打包到存档中的文件集合。 VIB包含一个
            用于验证信任级别的签名文件。
            验证ESXi映像配置文件仅允许签名的VIB。 无符号VIB表示
            ESXi主机上安装的未经测试的代码。
            ESXi映像配置文件支持四种接受级别：
            1. VMwareCertified - 由VMware创建，测试和签名的VIB
            2. VMwareAccepted - 由VMware合作伙伴创建但经过测试和签名的VIB
            VMware的
            3. PartnerSupported - 由经过认证的VMware合作伙伴创建，测试和签署的VIB
            4. CommunitySupported - 未经VMware或VMware伙伴测试的VIB。
            不支持社区支持的VIB，也没有数字签名。 为了保护ESXi主机的安全性和完整性不允许未签名的VIB
            （CommunitySupported）在主机上安装。""",

    "audit": u"""执行以下过程：
        1.使用ESXi Shell或vCLI连接到每个ESX / ESXi主机并执行命令“esxcli software acceptance get”验证接受程度是否为
        “VMware认证”，“VMware支持”或“PartnerSupported”。
        2.使用vCLI连接到每个ESX / ESXi主机，然后执行命令“esxcli softwore vib list“并验证每个VIB的接受程度是”VMware认证“，”VMware支持“或”合作伙伴支持
        """,

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Set the Software AcceptanceLevel for each host
        Foreach ($VMHost in Get-VMHost ) {
        $ESXCli = Get-EsxCli -VMHost $VMHost
        $ESXCli.software.acceptance.Set("PartnerSupported")
        }""",
}

reportContent["1.3"] = {
    "title": u"""验证主机上加载的未经授权的内核模块""",
    "level": u"""Scored""",

    "description": u"""默认情况下，ESXi主机不允许加载缺少有效数字的内核模块签名。 可以覆盖此功能，这将导致未经授权的内核要加载的模块。
        VMware为内核模块提供数字签名。 默认情况下，ESXi主机不会
        允许加载缺少有效数字签名的内核模块。 但是，这种行为
        可以被覆盖，允许加载未经授权的内核模块。 未经测试或
        ESXi主机上加载的恶意内核模块可能会使主机面临不稳定的风险
        和/或利用。""",

    "audit": u"""Each ESXi host should be monitored for unsigned kernel modules. To list all the loaded kernel modules from the ESXi Shell or vCLI run: "esxcli system module list". For each module, verify the signature by running: esxcli system module get -m <module>. Secure the host by disabling unsigned modules and removing the offending VIBs from the host.""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        #To disable a module: 
        $ESXCli = Get-EsxCli -VMHost MyHost 
        $ESXCli.system.module.set($false, $false, "MyModuleName")""",
}

reportContent["2.1"] = {
    "title": u"""配置NTP时间同步""",
    "level": u"""Scored""",

    "description": u"""应在每个VMware ESXi主机上配置并启用NTP（网络时间协议）同步。 验证每个主机的NTP时间服务器是否正确以确保系统事件日志的准确时间。
        通过确保所有系统使用相同的相对时间源（包括相关时间源）定位偏移），并且相对时间源可以与商定的相关联时间标准，您可以更轻松地跟踪和关联入侵者的行为
        查看相关的日志文件。 时间设置不正确会使检查变得困难关联日志文件以检测攻击，并使审计不准确。""",

    "audit": u"""Runningible to the """,

    "remediation": u"""执行以下操作从vSphere Web Client：
        1.选择主机。
        2.单击“管理” - >“设置” - >“系统” - >“时间配置”。
        3.单击“编辑...”按钮。
        4.单击“使用网络时间协议”。
        5.提供NTP服务器的名称和/或IP。 用逗号分隔服务器。
        6.如果NTP服务状态为“已停止”，请单击“开始”。
        7.将启动策略更改为“使用主机启动和停止”。
        8.单击“确定”。
        要实施建议的配置状态，请运行以下PowerCLI命令：
        # Set the NTP Settings for all hosts
        # If an internal NTP server is used replace pool.ntp.org with
        # the IP address of the internal NTP server
        $NTPServers = "pool.ntp.org", "pool2.ntp.org" Get-VMHost | Add-VmHostNtpServer
        $NTPServers""",
}

reportContent["2.2"] = {
    "title": u"""配置ESXi主机防火墙以限制对正在运行的服务的访问""",
    "level": u"""Scored""",

    "description": u"""ESXi防火墙默认启用，允许ping（ICMP）和DHCP/DNS客户端通信。 为了防止外部攻击，确认只允许授权的IP /网络访问主机上的服务。
        对ESXi主机上运行的服务的无限制访问可以使主机暴露于外部攻击和未经授权的访问。通过将ESXi防火墙配置为仅允许授权的网络访问来降低风险。""",

    "audit": u"""从vSphere Web Client执行以下操作：
        1.选择主机
        2.转到“管理” - >“设置” - >“系统” - >“安全配置文件”
        3.在“防火墙”部分中，选择“编辑...”。
        4.对于每个已启用的服务（例如，ssh，vSphere Web Access，http客户端），请检查是否
        提供了一系列允许的IP地址。
        此外，可以使用以下PowerCLI命令：
        # List all services for a host
        Get-VMHost HOST1 | Get-VMHostService
        # List the services which are enabled and have rules defined for specific IP ranges to
        access the service
        Get-VMHost HOST1 | Get-VMHostFirewallException | Where {$_.Enabled -and (-not
        $_.ExtensionData.AllowedHosts.AllIP)}
        # List the services which are enabled and do not have rules defined for specific IP
        ranges to access the service
        Get-VMHost HOST1 | Get-VMHostFirewallException | Where {$_.Enabled -and
        ($_.ExtensionData.AllowedHosts.AllIP)}""",

    "remediation": u"""从vSphere Web Client执行以下操作：
            1.选择主机
            2.转到“管理” - >“设置” - >“系统” - >“安全配置文件”
            3.在“防火墙”部分中，选择“编辑...”。
            4.对于每个启用的服务（例如，ssh，vSphere Web Access，http客户端）提供范围
            允许的IP地址。
            5.单击“确定”。""",
}

reportContent["2.3"] = {
    "title": u"""禁用管理对象浏览器（MOB）""",
    "level": u"""Scored""",

    "description": u"""托管对象浏览器（MOB）是一个基于Web的服务器应用程序，可以让您
        检查服务器端存在的对象。 这是当vCenter安装时自动安装和启动的。
        托管对象浏览器（MOB）提供了一种探索所使用的对象模型的方法
        VMkernel来管理主机; 它还可以更改配置。 这个
        interface主要用于调试vSphere SDK。 因为
        没有访问控制MOB也可以用作获取有关未授权访问的主机的信息的方法,存在未经授权访问获取主机信息的风险。""",

    "audit": u"""To determine if the MOB is enabled run the following command from the ESXi shell:
    vim-cmd proxysvc/service_list""",

    "remediation": u"""要实施建议的配置状态，请运行以下ESXi shell命令：
        vim-cmd proxysvc/remove_service "/mob" "httpsWithRedirect\"""",
}

reportContent["2.4"] = {
    "title": u"""不要将默认的自签名证书用于ESXi通信""",
    "level": u"""Scored""",

    "description": u"""默认证书不由受信任的证书颁发机构（CA）签名，应该替换为由受信任的CA颁发的有效证书。
        使用默认的自签名证书可能会增加与Man-in-The-Middle攻击相关的风险（MiTM）。 将默认的自签名证书替换为来自可信CA，或者是商业组织的证书。""",

    "audit": u"""查看ESXi主机提供的SSL证书的详细信息，并确定其是否由受信任的CA（商业或组织）发布。
        1.以具有管理员权限用户身份，直接从DCUI或SSH客户端登录ESXi Shell。
        2.在/etc/vmware/ ssl目录中，使用以下命令重命名现有证书：
            mv rui.crt orig.rui.crt
            mv rui.key orig.rui.key
        3.将要使用的证书复制到/etc/vmware/ssl。
        4.将新证书和密钥重命名为rui.crt和rui.key。
        5.安装新证书后重新启动主机。
        或者，您可以将主机置于维护模式，安装新证书，使用
        直接控制台用户界面（DCUI）重新启动管理代理程序，并设置主机退出维护模式。""",

    "remediation": u"""利用VMware的SSL证书自动化工具安装CA签名的SSL证书。 有关此工具的更多信息，请见http://kb.vmware.com/kb/2057340。""",
}

reportContent["2.5"] = {
    "title": u"""确保合适的SNMP配置""",
    "level": u"""Scored""",

    "description": u"""验证是否已配置SNMP（简单网络管理协议）以及所有设置是正确的。 如果未使用SNMP，则应禁用它。
            如果未使用SNMP，应保持禁用状态。 如果正在使用，适当的陷阱目的地应该配置。 如果未正确配置SNMP，则监控信息可以发送到恶意主机。""",

    "audit": u"""Perform the following from the ESXi Shell or vCLI:
    1. Run the following to determine if SNMP is being used: esxcli system snmp get
    2. If SNMP is not being used, make sure that it is disabled by running: esxcli system snmp set --enable false
    3. If SNMP is being used, refer to the vSphere Monitoring and Performance guide, chapter 8 for steps to configure the required parameters.""",
    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Update the host SNMP Configuration (single host connection required)
        Get-VmHostSNMP | Set-VMHostSNMP -Enabled:$true -ReadOnlyCommunity '<secret>'""",
}

reportContent["2.6"] = {
    "title": u"""防止意外使用dvfilter网络API""",
    "level": u"""Scored""",

    "description": u"""如果未使用，请确认未配置dvfilter API。 如果您使用的是虚拟安全性利用此API然后配置的设备可能是必要的。
        如果您没有使用使用dvfilter网络API的产品（例如VMSafe），那么
        不应将主机配置为向VM发送网络信息。 如果启用了API，
        攻击者可能会尝试将VM连接到它，从而可能提供对VM的访问
        主机上其他VM的网络。 如果您使用的是使用此API的产品，那么
        验证主机是否已正确配置。""",

    "audit": u"""the following PowerCLI command may be used:# List Net.DVFilterBindIpAddress for each host Get-VMHost | Select Name, @{N="Net.DVFilterBindIpAddress";E={$_ | Get-VMHostAdvancedConfiguration Net.DVFilterBindIpAddress | Select -ExpandProperty Values}}""",

    "remediation": u"""从vSphere Web Client执行以下操作：
            1.选择主机，然后单击“管理” - >“设置” - >“系统” - >“高级系统”
            设置”。
            2.在过滤器中输入Net.DVFilterBindIpAddress。
            3.验证Net.DVFilterBindIpAddress是否为空值。
            4.如果正在使用设备，请确保将此参数的值设置为
            适当的IP地址.Page |20
            5.确保突出显示属性，然后单击铅笔图标。
            6.输入正确的IP地址。
            7.单击“确定”。
            要实施建议的配置状态，请运行以下PowerCLI命令：
            # Set Net.DVFilterBindIpAddress to null on all hosts
            Get-VMHost HOST1 | Foreach { Set-VMHostAdvancedConfiguration -VMHost $_ -Name
            Net.DVFilterBindIpAddress -Value "" }""",
}

reportContent["2.7"] = {
    "title": u"""从ESXi服务器中删除过期或已撤销的SSL证书""",
    "level": u"""Not Scored""",

    "description": u"""从ESXi服务器中删除过期或已撤销的SSL证书。
        在vCenter Server系统上保留过期或已撤销的证书可能会危害
        你的环境。 默认情况下，每个ESXi主机都没有检查可用的证书吊销列表
        （CRL）。 必须手动检查和删除已撤销的证书。 更换证书将避免让用户习惯点击
        浏览器警告。 警告可能表示的是中间人攻击，并且
        只有检查证书和指纹才能防止此类攻击。""",

    "audit": u"""使用“verify-ssl-certificates”PowerCLI脚本中调用的脚本来评估
        是否存在已撤消ESXi服务器上的SSL证书。 如果找到撤销的证书，请替换为具有有效证书的SSL证书。""",

    "remediation": u"""将自签名证书替换为来自可信CA（商业CA或组织CA）的证书. 证书可以通过多种方式替换：
        1.从ESXi Shell替换默认ESXi证书和密钥
        2.使用vifs命令替换默认ESXi证书和密钥
        3.使用HTTPS PUT替换默认ESXi证书和密钥
        如果您不小心删除了默认的自签名证书和密钥，或者您更改了
        主机名，您可以从ESXi Shell生成新的自签名证书和密钥。
        请参阅为ESXi生成新的自签名证书。""",
}

reportContent["3.1"] = {
    "title": u"""配置集中位置以收集ESXi主机核心转储""",
    "level": u"""Scored""",

    "description": u"""要配置集中位置以收集ESXi主机核心转储，请使用“ESXi转储收集器“.VMware vSphere网络转储收集器服务允许从遇到严重故障的主机收集诊断信息。
        当主机崩溃时，对结果核心转储的分析对于能够进行分析是至关重要的确定崩溃的原因以确定解决方案。 安装集中式转储
        collector有助于确保核心文件成功保存并在恐慌的ESXi主机事件中可用。""",

    "audit": u"""Run the following ESXi shell command to determine if the host is configured as prescribed:
    esxcli system coredump network get""",

    "remediation": u"""要实施建议的配置状态，请运行以下ESXi shell命令：
        # Configure remote Dump Collector Server 
        esxcli system coredump network set -v [VMK#] -i [DUMP_SERVER] -o [PORT] 
        # Enable remote Dump Collector 
        esxcli system coredump network set -e true""",
}

reportContent["3.2"] = {
    "title": u"""为所有ESXi主机配置持久日志记录""",
    "level": u"""Scored""",

    "description": u"""系统日志是审计和诊断目的所必需的。 如果您不存储系统永久记录，例如在数据存储上，它们会在重新启动后消失。确保设置持久日志记录可以防止重启时丢失日志。
        ESXi可以配置为在内存文件系统中存储日志文件。 这发生在
        host的Syslog.global.LogDir属性设置为非持久性位置，例如
        作为/刮擦。 完成此操作后，任何时候都只会存储一天的日志。
        此外，每次重新启动时都会重新初始化日志文件。 这带来了安全风险
        登录主机的用户活动仅暂时存储，不会保留
        重新启动。 这也可能使审计复杂化并使监控事件变得更加困难
        诊断问题。 应始终将ESXi主机日志记录配置为持久性数据存储""",

    "audit": u"""the following PowerCLI command may be used: # List Syslog.global.logDir for each host Get-VMHost | 
    Select Name, @{N="Syslog.global.logDir";E={$_ | Get-VMHostAdvancedConfiguration Syslog.global.logDir | 
    Select -ExpandProperty Values}}""",

    "remediation": u"""从vSphere Web Client执行以下操作：
        1.选择主机，然后转到“管理” - >“设置” - >“高级系统设置”。
        2.在过滤器中输入Syslog.global.LogDir。
        3.将Syslog.global.LogDir设置为所需的数据存储路径。
        4.确保突出显示属性，然后单击铅笔图标。
        或者，运行以下PowerCLI命令： 
        # Set Syslog.global.logDir for each host
        Get-VMHost | Foreach { Set-VMHostAdvancedConfiguration -VMHost $_ -Name
        Syslog.global.logDir -Value "<NewLocation>" }""",
}

reportContent["3.3"] = {
    "title": u"""配置ESXi主机的远程日志记录""",
    "level": u"""Scored""",

    "description": u"""默认情况下，ESXI日志存储在本地临时卷或ramdisk上。 保存日志进一步配置ESXI主机的集中式日志记录。
        远程日志记录到中央日志主机可为ESXi日志提供安全的集中式存储。 通过
        将主机日志文件收集到中央主机上，您可以更轻松地监控所有主机
        单一工具。 您还可以进行聚合分析和搜索以查找此类内容
        协调对多个主机的攻击。 登录到安全的集中式日志服务器也很有帮助
        防止日志篡改，并提供长期审计记录。 方便远程
        logging提供vSphere Syslog Collector""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # List Syslog.global.logHost for each host Get-VMHost | Select Name, @{N="Syslog.global.logHost";E={$_ | Get-VMHostAdvancedConfiguration Syslog.global.logHost | Select -ExpandProperty Values}}""",

    "remediation": u"""执行以下操作：
        1.安装/启用syslog主机（即vSphere Syslog Collector）。
        2.从vSphere Web Client中选择主机。
        3.单击“管理” - >“设置” - >“系统” - >“高级系统设置”。
        4.在过滤器中输入Syslog.global.logHost。
        5.确保突出显示Syslog.global.logHost，然后单击铅笔图标。
        6.将Syslog.global.logHost设置为syslog的主机名或IP地址服务器。
        7.单击“确定”。
        要实施建议的配置状态，请运行以下PowerCLI命令：
        # Set Syslog.global.logHost for each host
        Get-VMHost | Foreach { Set-VMHostAdvancedConfiguration -VMHost $_ -Name
        Syslog.global.logHost -Value "<NewLocation>" }""",
}

reportContent["4.1"] = {
    "title": u"""为本地管理员访问创建非root用户帐户""",
    "level": u"""Scored""",

    "description": u"""创建至少一个指定的用户帐户并使用此帐户代替共享的“root”帐户。
        默认情况下，每个ESXi主机都有一个用于本地管理的“root”管理员帐户
        并将主机连接到vCenter Server。 避免共享公共根
        帐户建议在每个主机上创建至少一个指定的用户帐户和
        为其分配完整的管理员权限并使用此帐户代替共享的“root”帐户。设置
        “root”帐户的高度复杂密码，并将其保存在安全的位置。 限制
        使用“root”但不删除“root”帐户。""",

    "audit": u"""执行以下操作：
        1.使用vSphere Client直接连接ESXi主机。
        2.以root或其他授权用户身份登录。
        3.选择“本地用户和组”选项卡，然后查看本地用户。
        4.确保至少有一个拥有以下内容的用户：
            已授予此用户Shell访问权限。
            选择“权限”选项卡并验证授予用户的“管理员”角色。
        5.对每个ESXi主机重复此操作。""",

    "remediation": u"""无法使用vSphere Web Client创建本地ESXi用户帐户，必须使用vSphere Client。
        1.使用vSphere Client直接连接ESXi主机。
        2.以root用户身份登录。
        3.选择“本地用户和组”选项卡
        4.添加本地用户，请务必授予对该用户的shell访问权限。
        5.选择“权限”选项卡。
        6.为用户分配“管理员”角色。
        7.对每个ESXi主机重复此操作。""",
}

reportContent["4.2"] = {
    "title": u"""为密码复杂性建立密码策略""",
    "level": u"""Scored""",

    "description": u"""需要使用不容易猜到的密码，且密码产生器产生的密码是复杂的。
        ESXi使用pam_passwdqc.so插件来设置密码强度和复杂性。 
        使用不容易猜到的密码并且产生复杂的密码是很重要的。
        注意：ESXi对root密码没有任何限制。 密码强度和
        复杂性规则仅适用于非root用户。""",

    "audit": u"""执行以下操作：
        1.以具有管理员权限的用户身份登录ESXi shell。
        2.打开/etc/pam.d/passwd
        3.找到以下行：
        password requisite /lib/security/$ISA/pam_passwdqc.so retry=N
        min=N0,N1,N2,N3,N4
        4.确认N小于或等于5
        5.确认N0设置为禁用
        6.确认N1设置为禁用
        7.确认N2设置为禁用
        8.确认N3设置为禁用
        9.确认N4设置为14或更高
        以上所述要求所有密码长度为14个或更多，并由
        来自四个不同字符集的至少一个字符组成。 此外，最多5次登录允许尝试。""",

    "remediation": u"""执行以下操作：
        1.以具有管理员权限的用户身份登录ESXi shell。
        2.打开/etc/pam.d/passwd
        3.找到以下行：
        password requisite /lib/security/$ISA/pam_passwdqc.so retry=N
        min=N0,N1,N2,N3,N4
        4.确认N小于或等于5
        5.确认N0设置为禁用
        6.确认N1设置为禁用
        7.确认N2设置为禁用
        8.确认N3设置为禁用
        9.确认N4设置为14或更高
        以上所述要求所有密码长度为14个或更多，并由
        来自四个不同字符集的至少一个字符组成。 此外，最多5次登录允许尝试。""",
}

reportContent["4.3"] = {
    "title": u"""使用Active Directory进行本地用户身份验证""",
    "level": u"""Scored""",

    "description": u"""可以将ESXi配置为使用Active Directory等目录服务来管理用户和团体。 建议使用目录服务。
        将ESXi主机加入Active Directory（AD）域，无需创建和
        维护多个本地用户帐户。 使用AD进行用户身份验证可简化ESXi
        主机配置，确保密码复杂性和重用策略得到执行
        降低安全漏洞和未经授权的访问风险。""",

    "audit": u"""Execute the following PowerCLI command: # Check each host and their domain membership status Get-VMHost | Get-VMHostAuthentication | Select VmHost, Domain, DomainMembershipStatus""",

    "remediation": u"""从vSphere Web Client：
            1.选择主机，然后转到“管理” - >“设置” - >“系统” - >“身份验证”
            服务”。
            2.单击“加入域”按钮。
            3.提供域名以及具有该域名的AD用户的用户凭据
            将计算机加入域的权限。
            4.单击“确定”。
            要实施建议的配置状态，请运行以下PowerCLI命令：
            # Join the ESXI Host to the Domain
            Get-VMHost HOST1 | Get-VMHostAuthentication | Set-VMHostAuthentication -Domain
            domain.local -User Administrator -Password Passw0rd -JoinDomain""",
}

reportContent["4.4"] = {
    "title": u"""验证“ESX管理员”组的活动目录组成员""",
    "level": u"""Not Scored""",

    "description": u"""vSphere使用的AD组由esxAdminsGroup属性定义。 默认情况下，这个属性设置为“ESX Admins”。 
        “ESX Admins”组的所有成员都被授予完整的对域中所有ESXi主机的管理访问权限。 监视AD以创建这个组对高度信任的用户和组进行制。
        由esxAdminsGroup属性设置的组中，具有成员身份的未授权用户将具有对所有ESXi主机的完全管理访问权限。 
        鉴于此，这样的用户可以损害所有ESXi主机的机密性，可用性和完整性和他们影响的各自数据和流程""",

    "audit": u"""从Active Directory，监视由高级主机设置（Config.HostAgent.plugins.hostsvc.esxAdminsGroup）定义的组名的成员身份。 和任何
        默认组一样，请考虑更改此名称以避免可能的漏洞利用并仅验证授权用户和组帐户是该组的成员。如果不希望对AD ESX管理员组进行完全管理员访问，
        则可以禁用使用高级主机设置（Config.HostAgent.plugins.hostsvc.esxAdminsGroupAutoAdd）的行为：""",

    "remediation": u"""1.验证esxAdminsGroup属性的设置（默认情况下为“ESX Admins”）。
        2.检查该Microsoft Active Directory组的成员列表。
        3.从该组中删除任何未经授权的用户。""",
}

reportContent["5.1"] = {
    "title": u"""禁用DCUI以防止本地管理控制""",
    "level": u"""Scored""",

    "description": u"""可以禁用直接控制台用户界面（DCUI）以防止来自主机的任何本地管理。 禁用DCUI后，任何ESXi主机的管理都将通过vCenter完成.DCUI允许进行低级主机配置，
	    例如配置IP地址，主机名和root密码以及诊断功能，例如启用ESXi shell，查看日志 文件，重新启动代理和重置配置。 vCenter Server不会跟踪从DCUI执行的操作。 即使启用
		了锁定模式，作为DCUI.Access列表成员的用户也可以在DCUI中执行管理任务，从而绕过RBAC并审核通过vCenter提供的控制。 可以禁用DCUI访问。 禁用它会阻止所有本地活动，
		从而强制在vCenter Server中执行操作，以便对它们进行集中审核和监视。如果主机与vCenter Server隔离，则禁用DCUI可能会产生潜在的“锁定”情况。 从“锁定”方案中恢复需
		要重新安装ESXi。 考虑启用DCUI并改为启用锁定模式，并使用DCUI.Access列表限制允许访问DCUI的用户。""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # List DCUI settings for all hosts Get-VMHost | Get-VMHostService | Where { $_.key -eq "DCUI" }""",

    "remediation": u"""1.从vSphere Web Client中选择主机。
                       2.选择“管理” - >“设置” - >“系统” - >“安全配置文件”
                       3.向下滚动到“服务”
                       4.单击“编辑...”
                       5.选择“直接控制台UI”
                       6.单击“停止”。
                       7.更改启动策略“手动启动和停止”
                       8.单击“确定”""",
}

reportContent["5.2"] = {
    "title": u"""除非诊断或故障排除需要，否则请禁用ESXi Shell""",
    "level": u"""Scored""",

    "description": u"""只应在运行诊断或故障排除时启用ESXi shell。 否则，应在每个主机上禁用它.ESXi Shell是一个交互式命令行环境，可从直接控制台用户界面（DCUI）或SSH远程访问。 
	   访问此模式需要服务器的root密码。 可以为各个主机打开和关闭ESXi Shell。 从ESXi Shell执行的活动绕过vCenter RBAC和审计控制。 只有在需要进行故障排除/解决无法通过
	   vSphere Web Client或vCLI / PowerCLI修复的问题时，才应打开ESXi shell。 您可以使用vSphere Web Client启用对ESXi Shell的本地和远程（SSH）访问，并设置空闲超时和可用
	   性超时。""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # Check if ESXi Shell is running and set to start Get-VMHost | Get-VMHostService | Where { $_.key -eq "TSM" } | Select VMHost, Key, Label, Policy, Running, Required""",

    "remediation": u"""1.从vSphere Web Client中选择主机。
                       2.选择“管理” - >“设置” - >“系统” - >“安全配置文件”
                       3.向下滚动到“服务”
                       4.单击“编辑...”
                       5.选择“ESXi Shell”
                       6.单击“停止”
                       7.更改启动策略“手动启动和停止”
                       此外，以下PowerCLI命令将实现建议的配置状态：# Set ESXi Shell to start manually rather than automatic for all hosts
                                                                     Get-VMHost | Get-VMHostService | Where { $_.key -eq "TSM" } | Set-VMHostService -
                                                                     Policy Off""",
}

reportContent["5.3"] = {
    "title": u"""禁用SSH""",
    "level": u"""Scored""",

    "description": u"""禁用每个ESXi主机的Secure Shell（SSH）以防止远程访问ESXi shell。 仅在需要进行故障排除或诊断时启用。启用ESXi shell后，可以通过DCUI直接从主机控制台访问，
	    也可以使用SSH远程访问。 对主机的远程访问应仅限于vSphere Client，远程命令行工具（vCLI / PowerCLI）以及已发布的API。 在正常情况下，应禁用使用SSH远程访问主机。""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # Check if SSH is running and set to start Get-VMHost | Get-VMHostService | Where { $_.key -eq "TSM-SSH" } | Select VMHost, Key, Label, Policy, Running, Required""",

    "remediation": u"""1.从vSphere Web Client中选择主机。
                       2.选择“管理” - >“设置” - >“系统” - >“安全配置文件”
                       3.向下滚动到“服务”。
                       4.单击“编辑...”
                       5.选择“SSH”。
                       6.确保将“启动策略”设置为“手动启动和停止”。
                       此外，可以使用以下PowerCLI命令：# Set SSH to start manually rather than automatic for all hosts
                                                       Get-VMHost | Get-VMHostService | Where { $_.key -eq "TSM-SSH" } | Set-VMHostService -
                                                       Policy Off""",
}

reportContent["5.4"] = {
    "title": u"""限制CIM访问""",
    "level": u"""Scored""",

    "description": u"""不要为基于CIM的硬件监视工具或其他第三方应用程序提供管理员级别访问权限（即root权限）。当用户使用您为CIM应用程序创建的服务帐户登录主机时，该用户仅具有系统管
	           理和CIM交互或只读访问权限。创建特定于每个CIM应用程序的服务帐户，并为每个应用程序提供最少的访问权限。 公共信息模型（CIM）系统提供了一个界面，该界面使用一组标准API实
			   现远程应用程序的硬件级管理。 要确保CIM接口保持安全，请仅提供这些应用程序所需的最低访问权限。 不要将CIM和其他第三方工具配置为以root用户身份或其他管理员帐户运行。 
			   而是使用具有有限权限集的专用服务帐户。 如果CIM或其他第三方被授予不需要的管理员级别访问权限，则可能会使用它们来破坏主机的安全性。""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # List all user accounts on the Host -Host Local connection required- Get-VMHostAccount""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：# Create a new host user account -Host Local connection requiredNew-VMHostAccount -ID ServiceUser -Password <password> -UserAccount""",
}

reportContent["5.5"] = {
    "title": u"""启用锁定模式以限制远程访问""",
    "level": u"""Scored""",

    "description": u"""锁定模式禁用对ESXi主机的本地访问。 所有管理都必须从VCenter完成以确保在使用锁定模式时应用适当的权限和角色。
        启用锁定模式会禁用对要求从vCenter Server远程管理主机的ESXi主机的直接访问。
        锁定限制ESXi主机对vCenter服务器的访问。 这样做是为了确保在vCenter中实现的角色和访问控制
        始终强制执行，用户无法通过直接登录主机来绕过它们。 通过强迫所有
        通过vCenter Server进行交互，无意中获得某人提升权限的风险或执行未正确审计的任务将大大减少。
        注意：锁定模式不适用于使用授权密钥登录的用户。 当你
        使用授权密钥文件进行root用户身份验证，不会阻止root用户
        即使主机处于锁定模式，也可以使用SSH访问主机。 请注意，列出的用户
        允许每个主机的DCUI.Access列表覆盖锁定模式并登录到
        DCUI。 默认情况下，“root”用户是DCUI.Access列表中列出的唯一用户""",

    "audit": u"""从vSphere Web客户端：
        1.选择主机
        2.选择“管理” - >“设置” - >“系统” - >“安全配置文件”。
        3.向下滚动到“锁定模式”。
        4.单击“编辑...”。
        5.确保选中“启用锁定模式”复选框。
        此外，可以使用以下PowerCLI命令：
        ＃检查是否启用了锁定模式
        Get-VMHost | Select Name,@{N="Lockdown";E={$_.Extensiondata.Config.adminDisabled}}""",

    "remediation": u"""Additionally, the following PowerCLI command may be used: # To check if 
    Lockdown mode is enabled Get-VMHost | Select Name,@{N="Lockdown";E={$_.Extensiondata.Config.adminDisabled}}
    从vSphere Web客户端：
        1.选择主机
        2.选择“管理” - >“设置” - >“系统” - >“安全配置文件”。
        3.向下滚动到“锁定模式”。
        4.单击“编辑...”。
        5.选择“启用锁定模式”复选框。
        6.单击“确定”。
        要实施建议的配置状态，请运行以下PowerCLI
        命令：
        # Enable lockdown mode for each host
        Get-VMHost | Foreach { $_.EnterLockdownMode() }""",
}

reportContent["5.6"] = {
    "title": u"""从SSH authorized_keys文件中删除密钥""",
    "level": u"""Scored""",

    "description": u"""对于日常操作，ESXi主机应与Secure Shell一起处于具有已禁用的（SSH）服务锁定模式。 锁定模式不会阻止root用户使用登录
        授权密钥。 使用授权密钥文件进行root用户身份验证时，root即使主机处于锁定状态，也不会阻止用户使用SSH访问主机模式。
        ESXi主机附带SSH，可配置为使用公钥认证验证远程用户。 要启用公钥验证，请复制远程用户
        公钥到ESXi主机上的/ etc / ssh / keys-root / authorized_keys文件中。在authorized_keys文件中存在远程用户的公钥将用户标识为
        信任，意味着用户被授予访问主机的权限，而无需提供密码。注意：锁定模式不适用于使用授权密钥登录的root用户。
        使用授权密钥文件进行root用户身份验证时，root用户即使主机处于锁定模式，也不被阻止使用SSH访问主机""",

    "audit": u"""要检查添加到authorized_keys文件的SSH密钥：
        1.以root用户或授权的管理员用户身份登录ESXi shell。
        2.验证/ etc / ssh / keys-root / authorized_keys文件是否为空。""",

    "remediation": u"""要检查添加到authorized_keys文件的SSH密钥：
        1.以root用户或授权的管理员用户身份登录ESXi shell。
        2.验证/ etc / ssh / keys-root / authorized_keys文件的内容。""",
}

reportContent["5.7"] = {
    "title": u"""设置超时以自动终止空闲ESXi Shell和SSH会话""",
    "level": u"""Scored""",

    "description": u"""设置超时以自动终止任何空闲ESXi shell和SSH会话。如果用户忘记注销其SSH会话，则空闲连接将无限期保留，从而增加某人获得
	    对主机的特权访问的可能性.ESXiShellInteractiveTimeOut允许您 自动终止空闲的shell会话。""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # List UserVars.ESXiShellInteractiveTimeOut for each host Get-VMHost | Select Name, @{N="UserVars.ESXiShellInteractiveTimeOut";E={$_ | Get-VMHostAdvancedConfiguration UserVars.ESXiShellInteractiveTimeOut | Select -ExpandProperty Values}}""",

    "remediation": u"""从vSphere Web客户端：
         1.选择主机。
         2.单击“管理” - >“设置” - >“系统” - >“高级系统设置”。
         3.在筛选器中键入ESXiShellInteractiveTimeOut。
         4.单击属性以突出显示它。
         5.单击铅笔图标进行编辑。
         6.将属性设置为所需的值（300或更小）。
         7.单击“确定”。
		 此外，以下PowerCLI命令将实现建议的配置状态：# Set Remove UserVars.ESXiShellInteractiveTimeOut to 300 on all hosts
                                                     Get-VMHost | Foreach { Set-VMHostAdvancedConfiguration -VMHost $_ -Name 
                                                     UserVars.ESXiShellInteractiveTimeOut -Value 300 }""",
}

reportContent["5.8"] = {
    "title": u"""为Shell服务设置超时""",
    "level": u"""Scored""",

    "description": u"""为了限制允许服务运行的时间，请设置超时以自动停止ESXi shell和SSH会话的服务。当在主机上启用ESXi Shell或SSH服务时，
	    它们将无限期运行。 要避免这些服务保持运行，请设置ESXiShellTimeOut。 ESXiShellTimeOut定义了一个时间窗口，在该窗口之后将自动终止ESXi Shell和SSH服务。""",

    "audit": u"""Additionally, the following PowerCLI command may be used: # List UserVars.ESXiShellTimeOut in minutes for each host Get-VMHost | Select Name, @{N="UserVars.ESXiShellTimeOut";E={$_ | Get-VMHostAdvancedConfiguration UserVars.ESXiShellTimeOut | Select -ExpandProperty Values}}""",

    "remediation": u"""从vSphere Web客户端：
          1.选择主机，然后单击“管理” - >“设置” - >“系统” - >“高级系统设置”。
          2.在筛选器中键入ESXiShellTimeOut。
          3.单击属性以突出显示它。
          4.单击铅笔图标进行编辑。
          5.将属性设置为3600秒（1小时）或更短。
          6.单击“确定”。
          要实施建议的配置状态，请运行以下PowerCLI命令：# Set UserVars.ESXiShellTimeOut to 3660 on all hosts
                                                        Get-VMHost | Foreach { Set-VMHostAdvancedConfiguration -VMHost $_ -Name 
                                                        UserVars.ESXiShellTimeOut -Value 3600 }""",
}

reportContent["5.9"] = {
    "title": u"""设置DCUI.Access以允许受信任的用户覆盖锁定模式""",
    "level": u"""Not Scored""",

    "description": u"""创建一个高度可信的用户列表，这些用户可以覆盖锁定模式并在主机被隔离时访问DCUI。当您使用DCUI禁用锁定模式时，
	    具有DCUI访问权限的所有用户都是 在主机上授予管理员角色。锁定会禁用直接主机访问，要求管理员从vCenter管理主机。
     	但是，如果主机与vCenter隔离，则管理员将被锁定，无法再管理主机。 避免可能被锁定在ESXi主机之外
        在锁定模式下运行时，将DCUI.Access设置为允许覆盖锁定模式并访问DCUI的高度可信用户列表。
		""",

    "audit": u"""Additionally, the following Power shell command may be used: Get-VMHost | Get-AdvancedSetting -Name DCUI.Access""",

    "remediation": u"""从vSphere Web客户端：
        1.选择主机。
        2.选择“管理” - >“设置” - >“系统” - >“高级系统设置”。
        3.在过滤器中键入DCUI.Access。
        4.单击属性以突出显示它。
        5.单击铅笔图标进行编辑。
        6.将DCUI.Access属性设置为以逗号分隔的用户列表允许覆盖锁定模式。
        7.单击“确定”""",
}

reportContent["5.10"] = {
    "title": u"""验证公开的配置文件的内容""",
    "level": u"""Not Scored""",

    "description": u"""监视公开的配置文件以验证未经授权的修改。
        虽然ESXi上的大多数配置都是通过API控制的，但是有一组有限的直接用于管理主机行为的配置文件。 这些特定文件是通过基于vSphere HTTPS的文件传输API公开。
        对这些文件的任何更改都应该与批准的管理操作相关联，例如授权配置更改。 篡改这些文件有可能造成未经授权的访问主机配置和虚拟机。
        警告：不要尝试监视未通过此文件传输API公开的文件，因为这会导致系统不稳定""",

    "audit": u"""1.打开Web浏览器。
        2.可以通过浏览到https：// <hostname> / host（如果禁用MOB，则不可用）来找到ESXi配置文件。""",

    "remediation": u"""在配置备份期间，将使用配置备份序列号。当
        恢复配置时将恢复编号。 
        当您运行Recovery CD（ESXi Embedded）或执行修复操作（ESXi Installable）时，该号码不会保留。
        您可以按如下方式备份和还原配置信息。
        1.使用vicfg-cfgbackup命令备份配置。
        2.运行Recovery CD或修复操作
        3.使用vicfg-cfgbackup命令恢复配置。
        还原配置时，必须确保主机上的所有虚拟机已停止""",
}

reportContent["6.1"] = {
    "title": u"""为iSCSI流量启用双向CHAP身份验证。""",
    "level": u"""Scored""",

    "description": u"""通过启用双向CHAP（也称为Mutual CHAP），可提供额外的安全级别使启动器能够验证目标。
        vSphere允许使用iSCSI目标和主机的双向身份验证。如果您创建一个专用网络或VLAN来为所有iSCSI设备提供服务，则选择不执行更严格的身份验证是有意义的。 
        通过不认证两者iSCSI目标和主机，可能存在攻击者可能发生的MiTM攻击冒充连接的任何一方窃取数据。 双向认证可以
        减轻这种风险。 如果iSCSI工具与一般网络流量隔离，则会减少漏洞利用。""",

    "audit": u"""执行以下操作：
        1.从vSphere Web Client中，导航到“主机”。
        2.单击主机。
        3.单击“管理” - >“存储” - >“存储适配器”。
        4.选择iSCSI适配器。
        5.在Adapter Details下，单击Properties选项卡。
        6.验证身份验证方法（使用双向CHAP）。
        此外，可以使用以下PowerCLI命令：
        # List Iscsi Initiator and CHAP Name if defined
        Get-VMHost | Get-VMHostHba | Where {$_.Type -eq "Iscsi"} | Select VMHost, Device,
        ChapType, @{N="CHAPName";E={$_.AuthenticationProperties.ChapName}}""",

    "remediation": u"""执行以下操作：
        1.从vSphere Web Client中，导航到“主机”。
        2.单击主机。
        3.单击“管理” - >“存储” - >“存储适配器”。
        4.选择要配置的iSCSI适配器或单击绿色加号以创建新的适配器。
        5.在Adapter Details下，单击Properties选项卡，然后单击Authentication中的“Edit”面板。
        6.指定身份验证方法：“使用双向CHAP”。
        7.指定传出的CHAP名称。
            确保您指定的名称匹配存储方面上配置的名称。
            将CHAP名称设置为iSCSI适配器名称，请选择“使用启动器”名称。
            将CHAP名称设置为iSCSI启动器名称以外的任何名称，取消选择“使用启动器名称”，在“名称”文本框中键入名称。
        8.输入要用作身份验证一部分的传出CHAP机密。使用相同的秘密作为你的存储方秘密。
        9.指定传入的CHAP凭据。确保你的传出和传入的秘密不符合。
        10.单击“确定”。
        11.单击倒数第二个符号以重新扫描iSCSI适配器。
        要实施建议的配置状态，请运行以下PowerCLI命令：
        # Set the Chap settings for the Iscsi Adapter 
        Get-VMHost | Get-VMHostHba | Where {$_.Type -eq "Iscsi"} | Set-VMHostHba # Use desired parameters here""",
}

reportContent["6.2"] = {
    "title": u"""确保CHAP身份验证机密的唯一性""",
    "level": u"""Not Scored""",

    "description": u"""CHAP（质询握手身份验证协议）要求客户端和主机知道建立连接的密码（密码）。 设置CHAP时，确保每个主机都连接一个唯一的秘密。
	    每个主机的相互认证秘密应该不同; 如果可能，对于每个对服务器进行身份验证的客户端，秘密也应该不同。 这可确保在单个主机受到攻击时，攻击者无法
	    创建另一个任意主机并对存储设备进行身份验证。 使用单个共享密钥，一台主机的泄露可以允许攻击者对存储设备进行身份验证。""",

    "audit": u"""# List Iscsi Initiator and CHAP Name if defined Get-VMHost | Get-VMHostHba | Where {$_.Type -eq "Iscsi"} | Select VMHost, Device, ChapType, @{N="CHAPName";E={$_.AuthenticationProperties.ChapName}}""",

    "remediation": u"""执行以下操作：
         1.从vSphere Web Client中，导航到“主机”。
         2.单击主机。
         3.单击“管理” - >“存储” - >“存储适配器”。
         4.选择要配置的iSCSI适配器或单击绿色加号以创建新的适配器。
         5.在Adapter Details下，单击Properties选项卡，然后单击Authentication中的“Edit”面板。
         6.指定身份验证方法。
           没有
           如果目标需要，使用单向CHAP
           使用单向CHAP，除非目标禁止
           使用单向CHAP
           使用双向CHAP。
         7.指定传出的CHAP名称。
             确保您指定的名称与存储端配置的名称相匹配。
           要将CHAP名称设置为iSCSI适配器名称，请选择“使用启动器名称”。
           要将CHAP名称设置为iSCSI启动器名称以外的任何名称，请取消选择“使用启动器名称”，然后在“名称”文本框中键入名称。
         8.输入要用作身份验证一部分的传出CHAP机密。使用与存储端密码相同的秘密。
         9.如果使用双向CHAP进行配置，请指定传入的CHAP凭据。
             确保您的传出和传入的秘密不匹配。
         10.单击“确定”。
         11.单击倒数第二个符号以重新扫描iSCSI适配器""",
}

reportContent["6.3"] = {
    "title": u"""适当地屏蔽和分区SAN资源""",
    "level": u"""Not Scored""",

    "description": u"""使用分区和LUN屏蔽来隔离SAN活动。 例如，为测试定义的区域应该在SAN内独立管理，这样它们就不会干扰网络中的活动生产区。 
        同样，您可以为不同的部门设置不同的区域。分区必须考虑已在SAN设备上设置的任何主机组。 LUN屏蔽是一个使LUN可供某些主机使用且其他主机不可用的进程
        分区在SAN拓扑中提供访问控制。 区域划分定义了哪些HBA可以连接到哪些目标。 当配置SAN分区时，区域外的设备对于区域内设备是不可见的。
        分区具有以下效果：
            减少提供给主机的目标和LUN的数量。
            可以防止非ESXi系统访问特定存储系统，破坏VMFS数据。
            可用于分隔不同的环境，例如，来自a生产环境的测试。""",

    "audit": u"""每个SAN交换机和磁盘阵列的分区和屏蔽功能都是特定于供应商的是用于管理LUN屏蔽的工具。""",

    "remediation": u"""对于ESXi主机，请使用单启动器分区或单启动器单目标分区。该后者是一种优选的分区实践。 
        使用限制性更强的分区可以防止出现问题SAN上可能出现的配置错误。
        有关详细说明和最佳分区实践，请联系存储阵列或交换机供应商。 供应商是每个SAN交换机和磁盘阵列的分区和屏蔽功能具体。""",
}

reportContent["6.4"] = {
    "title": u"""在删除之前将VMDK文件清零""",
    "level": u"""Not Scored""",

    "description": u"""在删除之前清零VMDK有助于防止用户重建磁盘的原始内容。
        有助于防止VMDK文件中的敏感数据被物理磁盘读取删除后，虚拟磁盘应在删除前清零。 这将使它更多难重建VMDK文件的内容。
        在删除之前，CLI命令'vmkfstools -writezeroes'可用于将零写入VMDK文件的全部内容。""",

    "audit": u"""Not applicable（不适用）""",

    "remediation": u"""当删除包含敏感数据的VMDK文件时：
        1.关闭或停止虚拟机。
        2.在删除来自数据存储区的数据之前，在该文件上发出CLI命令“vmkfstools -writezeroes”。""",
}

reportContent["7.1"] = {
    "title": u"""确保将vSwitch Forged Transmits策略设置为reject""",
    "level": u"""Scored""",

    "description": u"""设置vSwitch Forged Transmits策略设置为拒绝每个vSwitch。如果虚拟机操作系统更改了MAC地址，操作系统
	  可以随时发送带有模拟源MAC地址的帧。 这允许操作系统通过模拟由接收网络授权的网络适配器来对网络中的设备进行恶意攻击。 
	  伪造传输应默认设置为接受。 这意味着虚拟交换机不会比较源和有效MAC地址。 为防止MAC地址模拟，所有虚拟交换机都应将伪造传
	  输设置为拒绝。 可以在vSwitch和/或Portgroup级别设置Reject Forged Transmit。 您可以在端口组级别覆盖开关级别设置。
	  这将阻止VM更改其有效MAC地址。 这将影响需要此功能的应用程序。 像这样的应用程序的一个例子是Microsoft Clustering，
	  它要求系统有效地共享MAC地址。这也将影响第2层网桥的运行方式。 这也会影响需要特定MAC地址进行许可的应用程序。 
	  应对这些应用程序所连接的端口组进行例外处理。""",

    "audit": u"""# List all vSwitches and their Security Settings Get-VirtualSwitch -Standard | Select VMHost, Name, ` @{N="MacChanges";E={if ($_.ExtensionData.Spec.Policy.Security.MacChanges) { "Accept" } Else { "Reject"} }}, ` @{N="PromiscuousMode";E={if ($_.ExtensionData.Spec.Policy.Security.PromiscuousMode) { "Accept" } Else { "Reject"} }},
    @{N="ForgedTransmits";E={if ($_.ExtensionData.Spec.Policy.Security.ForgedTransmits) { "Accept" } Else { "Reject"} }}""",

    "remediation": u"""1.在vSphere Web Client中，导航到主机。
        2.“主机和群集” - >“vCenter” - >主机。
        3.在“管理”选项卡上，单击“网络”，然后选择虚拟交换机。
        4.从列表中选择标准开关，然后单击铅笔图标以编辑设置。
        5.选择安全性。
        6.将Forged传输设置为“Reject”。
        7.单击“确定”。
        此外，可以使用以下ESXi shell命令：# esxcli network vswitch standard policy security set -v vSwitch2 -f false""",
}

reportContent["7.2"] = {
    "title": u"""确保将vSwitch MAC地址更改策略设置为拒绝""",
    "level": u"""Scored""",

    "description": u"""确保vSwitch中的MAC地址更改策略设置为拒绝。如果虚拟机操作系统更改了MAC地址，则可以随时发送带有模拟源MAC地址的帧。
	  这允许它通过模拟由接收网络授权的网络适配器来对网络中的设备进行恶意攻击。这将阻止VM更改其有效MAC地址。它将影响需要此功能的应用程序。
	  像这样的应用程序的一个例子是Microsoft Clustering，它要求系统有效地共享MAC地址。这也将影响第2层网桥的运行方式。这也会影响需要特定MAC地址
	  进行许可的应用程序。应对这些应用程序所连接的端口组进行例外处理。拒绝MAC更改可以在vSwitch和/或Portgroup级别设置。您可以在端口组级别
	  覆盖交换机级别设置。这将阻止VM更改其有效MAC地址。它将影响需要此功能的应用程序。像这样的应用程序的一个例子是Microsoft Clustering，它要求
	  系统有效地共享MAC地址。这也将影响第2层网桥的运行方式。这也会影响需要特定MAC地址进行许可的应用程序。应对这些应用程序所连接的端口组进行例外处理。""",

    "audit": u"""# List all vSwitches and their Security Settings Get-VirtualSwitch -Standard | Select VMHost, Name, ` @{N="MacChanges";E={if ($_.ExtensionData.Spec.Policy.Security.MacChanges) { "Accept" } Else { "Reject"} }}, ` @{N="PromiscuousMode";E={if ($_.ExtensionData.Spec.Policy.Security.PromiscuousMode) { "Accept" } Else { "Reject"} }}, ` @{N="ForgedTransmits";E={if ($_.ExtensionData.Spec.Policy.Security.ForgedTransmits) { "Accept" } Else { "Reject"} }}""",

    "remediation": u"""1.在vSphere Web Client中，导航到主机。
        2.“主机和群集” - >“vCenter” - >主机。
        3.在“管理”选项卡上，单击“网络”，然后选择虚拟交换机。
        4.从列表中选择标准开关，然后单击铅笔图标以编辑设置。
        5.选择安全性。
        6.将MAC地址更改设置为“拒绝”。
        7.单击“确定”。
        此外，执行以下操作以使用ESXi shell实施建议的配置状态：# esxcli network vswitch standard policy security set -v vSwitch2 -m false""",
}

reportContent["7.3"] = {
    "title": u"""确保将vSwitch Promiscuous Mode策略设置为reject""",
    "level": u"""Scored""",

    "description": u"""确保vSwitch中的混杂模式策略设置为拒绝。当为虚拟交换机启用混杂模式时，连接到dvPortgroup的所有虚拟机都有可能读取通过该网络的所有数据包。 
	    默认情况下，ESXi Server上会禁用混杂模式，这是推荐的设置。 但是，可能有合理的理由将其用于调试，监视或故障排除。 安全设备可能需要能够查看vSwitch上的所有
	    数据包。 应对这些应用程序所连接的dvPortgroup进行例外处理，以便对该dvPortgroup上的流量进行全时可见。 可以在vSwitch和/或Portgroup级别设置Promiscous模式。 
	    您可以在端口组级别覆盖交换机级别设置。如果将“混杂模式”参数设置为“拒绝”，则需要能够查看vSwitch上所有数据包的安全设备将无法正常运行。""",

    "audit": u"""# List all vSwitches and their Security Settings Get-VirtualSwitch -Standard | Select VMHost, Name, ` @{N="MacChanges";E={if ($_.ExtensionData.Spec.Policy.Security.MacChanges) { "Accept" } Else { "Reject"} }}, ` @{N="PromiscuousMode";E={if ($_.ExtensionData.Spec.Policy.Security.PromiscuousMode) { "Accept" } Else { "Reject"} }}, ` @{N="ForgedTransmits";E={if ($_.ExtensionData.Spec.Policy.Security.ForgedTransmits) { "Accept" } Else { "Reject"} }}""",

    "remediation": u"""1.在vSphere Web Client中，导航到主机。
       2.“主机和群集” - >“vCenter” - >主机。
       3.在“管理”选项卡上，单击“网络”，然后选择虚拟交换机。
       4.从列表中选择标准开关，然后单击铅笔图标以编辑设置。
       5.选择安全性。
       6.将混杂模式设置为“拒绝”。
       7.单击“确定”。
       此外，执行以下操作以通过ESXi shell实施建议的配置状态：# esxcli network vswitch standard policy security set -v vSwitch2 -p false""",
}

reportContent["7.4"] = {
    "title": u"""确保端口组未配置为本机VLAN的值""",
    "level": u"""Scored""",

    "description": u"""不要使用Native VLAN ID 1.ESXi不使用本机VLAN的概念。 端口组中指定VLAN的帧将具有标记，但端口组中未指定VLAN的帧不会被标记，因此最终将属于
	   物理交换机的本地VLAN。 例如，来自Cisco物理交换机的VLAN 1上的帧将是未标记的，因为这被视为本地VLAN。 但是，指定为VLAN 1的ESXi中的帧将标记为“1”; 因此，
	   来自ESXi的发往本机VLAN的流量将无法正确路由（因为它标记为“1”而不是未标记），来自本机VLAN的物理交换机的流量将不可见（因为 它没有标记）。 如果ESXi虚拟交换机
	   端口组使用本机VLAN ID，则交换机上的本地VLAN将无法看到来自这些VM的流量，因为交换机预计会出现未标记的流量。""",

    "audit": u"""# List all vSwitches, their Portgroups and VLAN IDs Get-VirtualPortGroup -Standard | Select virtualSwitch, Name, VlanID""",

    "remediation": u"""如果正在使用本机VLAN的默认值1，则应将ESXi Server虚拟交换机端口组配置为介于2和4094之间的任何值。否则，请确保端口组未配置为使用为此设置的任何值。 本地VLAN。
       1.从vSphere Web Client中选择主机。
       2.在Manage选项卡上，单击Networking，然后选择Virtual switches。
       3.从列表中选择标准开关。
       4.显示交换机的拓扑图，显示与该交换机关联的各种端口组。
       5.对于vSwitch上的每个端口组，验证并记录使用的VLAN ID。
       6.如果需要更改VLAN ID，请单击虚拟交换机拓扑图中端口组的名称。
       7.单击拓扑图标题下的“编辑设置”铅笔图标。
       8.在“属性”部分中，在“网络标签”文本字段中为端口组命名。
       9.选择现有的VLAN ID下拉菜单或键入新的。""",
}

reportContent["7.5"] = {
    "title": u"""确保端口组未配置为upstreamphysical交换机保留的VLAN值""",
    "level": u"""Not Scored""",

    "description": u"""确保端口组未配置为上游物理交换机保留的VLAN值。某些物理交换机为内部目的保留某些VLAN ID，并且通常禁止配置为这些值的流量。 例如，Cisco Catalyst交换机
	   通常保留VLAN 1001到1024和4094，而Nexus交换机通常保留3968到4047和4094.请查看特定交换机的文档。 使用保留的VLAN可能会导致网络上的拒绝服务。""",

    "audit": u"""# List all vSwitches, their Portgroups and VLAN IDs Get-VirtualPortGroup -Standard | Select virtualSwitch, Name, VlanID""",

    "remediation": u"""不应将所有端口组上的VLAN ID设置设置为物理交换机的保留值。
       1.从vSphere Web Client中选择主机。
       2.在Manage选项卡上，单击Networking，然后选择Virtual switches。
       3.从列表中选择标准开关。
       4.显示交换机的拓扑图，显示与该交换机关联的各种端口组。
       5.对于vSwitch上的每个端口组，验证并记录使用的VLAN ID。
       6.如果需要更改VLAN ID，请单击虚拟交换机拓扑图中端口组的名称。
       7.单击拓扑图标题下的“编辑设置”铅笔图标。
       8.在“属性”部分中，在“网络标签”文本字段中为端口组命名。
       9.选择现有的VLAN ID下拉菜单或键入新的。""",
}

reportContent["7.6"] = {
    "title": u"""确保端口组未配置为VLAN 4095，但虚拟GuestTagging（VGT）除外""",
    "level": u"""Scored""",

    "description": u"""除虚拟guest标记（VGT）外，请勿使用VLAN 4095.当端口组设置为VLAN 4095时，将激活VGT模式。 在此模式下，vSwitch将所有网络帧传递到guestVM，而不修改VLAN标记，
	    将其留给guest处理它们。 仅当guest虚拟机已使用时才应使用VLAN 4095专门配置为自己管理VLAN标记。 如果不正确地启用VGT，
	    则可能导致拒绝服务或允许guestVM与未授权VLAN上的流量进行交互。""",

    "audit": u"""# List all vSwitches, their Portgroups and VLAN IDs Get-VirtualPortGroup -Standard | Select virtualSwitch, Name, VlanID""",

    "remediation": u"""除非需要VGT，否则不应将所有端口组上的VLAN ID设置设置为4095。
        1.从vSphere Web Client中选择主机。
        2.在Manage选项卡上，单击Networking，然后选择Virtual switches。
        3.从列表中选择标准开关。
        4.出现交换机的拓扑图，显示各种端口组与该开关相关联。
        5.对于vSwitch上的每个端口组，验证并记录使用的VLAN ID。
        6.如果需要更改VLAN ID，请单击虚拟交换机拓扑图中端口组的名称。
        7.单击拓扑图标题下的“编辑设置”铅笔图标。
        8.在“属性”部分中，在“网络标签”文本字段中为端口组命名。
        9.选择现有的VLAN ID下拉菜单或键入新的。""",
}

reportContent["8.1.1    "] = {
    "title": u"""限制从VM到VMX文件的信息性消息""",
    "level": u"""Scored""",

    "description": u"""限制从虚拟机到VMX文件的信息性消息，以避免填充数据存储区并导致拒绝服务（DoS）。包含这些名称 - 值对的配置文件限制为1MB的大小。 对于大多数情况，此1MB容量应该足够，
	    但您可以根据需要更改此值。 如果配置文件中存储了大量自定义信息，则可能会增加此值。 默认限制为1MB; 即使.vmx文件中未列出sizeLimit参数，也会应用此限制。 如果数据存储区已填满，则VMX文件
	    的不受控制的大小可能导致拒绝服务。""",

    "audit": u"""Check virtual machine configuration file and verify that tools.setInfo.sizeLimit is set to 1048576.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "tools.setInfo.sizeLimit" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
            # Add the setting to all VMs
            Get-VM | New-AdvancedSetting -Name "tools.setInfo.sizeLimit" -value 1048576""",
}

reportContent["8.1.2"] = {
    "title": u"""限制控制台连接的共享""",
    "level": u"""Scored""",

    "description": u"""限制最大控制台连接数，以防止非管理员观察虚拟机屏幕。默认情况下，远程控制台会话可以一次由多个用户连接。激活多个会话时，每个终端窗口都会收到有关新会话的通知。
	   如果VM中的管理员在会话期间使用VMware远程控制台登录，则VM中的非管理员可以连接到控制台并观察管理员的操作。此外，这可能导致管理员失去对虚拟机的控制台访问权限。例如，如果跳转框用
	   于打开控制台会话，并且管理员失去与该框的连接，则控制台会话保持打开状态。允许两个控制台会话允许通过共享会话进行调试。为了获得最高安全性，一次只允许一个远程控制台会话。只允许与
	   VM建立一个远程控制台连接。在第一个会话断开连接之前，其他尝试将被拒绝。""",

    "audit": u"""Check virtual machine configuration file and verify that RemoteDisplay.maxConnections is set to 1.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "RemoteDisplay.maxConnections" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
            # Add the setting to all VMs
            Get-VM | New-AdvancedSetting -Name "RemoteDisplay.maxConnections" -value 1""",
}
reportContent["8.2.1"] = {
    "title": u"""断开未经授权的设备 - 软盘设备""",
    "level": u"""Scored""",

    "description": u"""任何启用或连接的设备都代表潜在的攻击通道。 没有虚拟机权限的用户和进程可以连接或断开硬件设备，例如网络适配器和CD-ROM驱动器。 攻击者可以使用此功能来破坏虚拟机安全性。
	   删除不必要的硬件设备有助于防止攻击。确保没有设备连接到虚拟机（如果不需要）。 例如，串行和并行端口很少用于数据中心环境中的虚拟机，而CD / DVD驱动器通常仅在软件安装期间临时连接。 对于
	   不常用的不常用设备，参数不应存在或其值必须为FALSE。如果以后需要这些设备中的任何一个，则需要关闭虚拟机以反向更改。""",

    "audit": u"""The following parameters should either NOT be present or should be set to FALSE, unless Floppy drives are required: floppyX.present
        Additionally, the following PowerCLI command may be used:
        # Check for Floppy Devices attached to VMs
        Get-VM | Get-FloppyDrive | Select Parent, Name, ConnectionState""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Remove all Floppy drives attached to VMs
        Get-VM | Get-FloppyDrive | Remove-FloppyDrive""",
}

reportContent["8.2.2"] = {
    "title": u"""断开未经授权的设备 - CD / DVD设备""",
    "level": u"""Scored""",
    "description": u"""任何启用或连接的设备都代表潜在的攻击通道。 没有虚拟机权限的用户和进程可以连接或断开硬件设备，例如网络适配器和CD-ROM驱动器。 攻击者可以使用此功能来破坏虚拟机安全性。 
	   删除不必要的硬件设备有助于防止攻击。确保没有设备连接到虚拟机（如果不需要）。 例如，串行和并行端口很少用于数据中心环境中的虚拟机，而CD / DVD驱动器通常仅在软件安装期间临时连接。 
	   对于不常用的不常用设备，参数不应存在或其值必须为FALSE。如果以后需要这些设备中的任何一个，则需要关闭虚拟机以反向更改。""",
    "audit": u"""The following parameters should either NOT be present or should be set to FALSE, unless CD-ROM is required: ideX:Y.present
        Additionally, the following PowerCLI command may be used:
        # Check for CD/DVD Drives attached to VMs Get-VM | Get-CDDrive""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
            # Remove all CD/DVD Drives attached to VMs
            Get-VM | Get-CDDrive | Remove-CDDrive""",
}
reportContent["8.2.3"] = {
    "title": u"""断开未经授权的设备 - 并行设备 """,
    "level": u"""Scored""",
    "description": u"""任何启用或连接的设备都代表潜在的攻击通道。 没有虚拟机权限的用户和进程可以连接或断开硬件设备，例如网络适配器和CD-ROM驱动器。 攻击者可以使用此功能来破坏虚拟机安全性。 
	   删除不必要的硬件设备有助于防止攻击。确保没有设备连接到虚拟机（如果不需要）。 例如，串行和并行端口很少用于数据中心环境中的虚拟机，而CD / DVD驱动器通常仅在软件安装期间临时连接。 
	   对于不常用的不常用设备，参数不应存在或其值必须为FALSE。如果以后需要这些设备中的任何一个，则需要关闭虚拟机以反向更改。""",
    "audit": u"""The following parameters should either NOT be present or should be set to FALSE, unless Parallel ports are required: parallelX.present
        Additionally, the following PowerCLI command may be used:
        # In this Example you will need to add the functions from this post:
        http://blogs.vmware.com/vipowershell/2012/05/working-with-vm-devices-in-powercli.html
        # Check for Parallel ports attached to VMs Get-VM | Get-ParallelPort""",
    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # In this Example you will need to add the functions from this post:
        http://blogs.vmware.com/vipowershell/2012/05/working-with-vm-devices-in-powercli.html
        # Remove all Parallel Ports attached to VMs
        Get-VM | Get-ParallelPort | Remove-ParallelPort""",
}

reportContent["8.2.4"] = {
    "title": u"""断开未经授权的设备 - 串行设备""",
    "level": u"""Scored""",

    "description": u"""任何启用或连接的设备都代表潜在的攻击通道。 没有虚拟机权限的用户和进程可以连接或断开硬件设备，例如网络适配器和CD-ROM驱动器。 攻击者可以使用此功能来破坏虚拟机安全性。 
	    删除不必要的硬件设备有助于防止攻击。确保没有设备连接到虚拟机（如果不需要）。 例如，串行和并行端口很少用于数据中心环境中的虚拟机，而CD / DVD驱动器通常仅在软件安装期间临时连接。 
	    对于不常用的不常用设备，参数不应存在或其值必须为FALSE。如果以后需要这些设备中的任何一个，则需要关闭虚拟机以反向更改。""",

    "audit": u"""The following parameters should either NOT be present or should be set to FALSE, unless Serial ports are required: serialX.present
        Additionally, the following PowerCLI command may be used:
        # In this Example you will need to add the functions from this post:
        http://blogs.vmware.com/vipowershell/2012/05/working-with-vm-devices-in-powercli.html
        # Check for Serial ports attached to VMs
        Get-VM | Get-SerialPort""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # In this Example you will need to add the functions from this post:
        http://blogs.vmware.com/vipowershell/2012/05/working-with-vm-devices-in-powercli.html
        # Remove all Serial Ports attached to VMs
        Get-VM | Get-SerialPort | Remove-SerialPort""",
}

reportContent["8.2.5"] = {
    "title": u"""断开未经授权的设备 - USB设备""",
    "level": u"""Scored""",

    "description": u"""任何启用或连接的设备都代表潜在的攻击通道。 没有虚拟机权限的用户和进程可以连接或断开硬件设备，例如网络适配器和CD-ROM驱动器。 攻击者可以使用此功能来破坏虚拟机安全性。 
	   删除不必要的硬件设备有助于防止攻击。 如果不需要，请确保没有设备连接到虚拟机。 例如，串行和并行端口很少用于数据中心环境中的虚拟机，而CD / DVD驱动器通常仅在软件安装期间临时连接。 
	   对于不常用的不常用设备，参数不应存在或其值必须为FALSE。如果以后需要这些设备中的任何一个，则需要关闭虚拟机以反向更改。""",

    "audit": u"""The following parameters should either NOT be present or should be set to FALSE, unless USB controllers are required: usb.present
        Additionally, the following PowerCLI command may be used:
        # Check for USB Devices attached to VMs
        Get-VM | Get-USBDevice""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Remove all USB Devices attached to VMs
        Get-VM | Get-USBDevice | Remove-USBDevice""",
}

reportContent["8.2.6"] = {
    "title": u"""防止未经授权删除和修改设备""",
    "level": u"""Scored""",

    "description": u"""防止未经授权删除和修改设备。在虚拟机中，没有root或管理员权限的用户和进程可以连接或断开设备（如网络适配器和CD-ROM驱动器），并可以修改设备设置。 
	   使用虚拟机设置编辑器或配置编辑器删除不需要或未使用的硬件设备。 如果要再次使用该设备，可以防止虚拟机中的用户或正在运行的进程从客户机操作系统中连接，断开连接或修改设备。 
	   默认情况下，虚拟机中具有非管理员权限的恶意用户可以：•
           - 连接断开连接的CD-ROM驱动器，并访问驱动器中剩余介质上的敏感信息
           - 断开网络适配器以将虚拟机与其网络隔离，这是一种拒绝服务
           - 修改设备上的设置
       使用VMware工具在guest操作系统内阻止设备交互。""",

    "audit": u"""Check virtual machine configuration file and verify that isolation.device.edit.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.device.edit.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.device.edit.disable" -value $true""",
}

reportContent["8.2.7"] = {
    "title": u"""防止未经授权的设备连接。""",
    "level": u"""Scored""",

    "description": u"""防止未经授权的设备连接。在虚拟机中，没有root或管理员权限的用户和进程可以连接或断开设备（如网络适配器和CD-ROM驱动器），并可以修改设备设置。 
	    使用虚拟机设置编辑器或配置编辑器删除不需要或未使用的硬件设备。 如果要再次使用该设备，可以防止虚拟机中的用户或正在运行的进程从客户机操作系统中连接，
        断开连接或修改设备。 默认情况下，虚拟机中具有非管理员权限的流氓用户可以：
            •连接已断开连接的CD-ROM驱动器，并访问驱动器中剩余介质上的敏感信息
            •断开网络适配器以将虚拟机与其网络隔离，这是一种拒绝服务
            •修改设备上的设置
        使用VMware工具在guest操作系统内阻止设备交互""",

    "audit": u"""Check virtual machine configuration file and verify that isolation.device.connectable.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.device.connectable.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.device.connectable.disable" -value $true""",
}

reportContent["8.3.1"] = {
    "title": u"""禁用VM内不必要或多余的功能""",
    "level": u"""Not Scored""",

    "description": u"""通过禁用支持虚拟机上运行的应用程序或服务不需要的不必要的系统组件来减少潜在攻击媒介的数量。通过禁用不需要的不必要的系统组件来支持系统上运行的应用程序或服务，
	    可以减少 可以攻击的部件数量。 虚拟机通常不需要与普通物理服务器一样多的服务或功能; 所以在虚拟化时，您应该评估是否真正需要特定的服务或功能。 在VM中运行的任何服务都提供了潜在的攻击途径。""",

    "audit": u"""Verify the following are disabled:
        1. Unused services in the operating system. For example, if the system runs a file
        server, make sure to turn off any Web services.
        2. Unused physical devices, such as CD/DVD drives, floppy drives, and USB adaptors.
        This is described in the Removing Unnecessary Hardware Devices section in the
        ESXI Configuration Guide.
        3. Screen savers. X-Windows if using a Linux, BSD, or Solaris guest operating system.""",

    "remediation": u"""其中一些步骤包括：
        1.禁用操作系统中未使用的服务。 例如，如果系统运行文件服务器，请确保关闭所有Web服务。
        2.断开未使用的物理设备，例如CD / DVD驱动器，软盘驱动器和USB适配器。 “ESXI配置指南”中的“删除不必要的硬件设备”部分对此进行了描述。
        3.关闭所有屏幕保护程序。 如果使用Linux，BSD或Solaris客户机操作系统，除非必要，否则不要运行X Window系统。""",
}

reportContent["8.3.2"] = {
    "title": u"""尽量减少VM控制台的使用 """,
    "level": u"""Not Scored""",

    "description": u"""仅在需要时授予对虚拟机控制台的访问权限。 使用自定义角色提供细粒度权限。通过VM控制台，您可以连接到虚拟机的控制台，实际上可以查看物理服务器上的监视器将显示的内容。 
	    VM控制台还提供电源管理和可移动设备连接控制，这可能允许恶意用户关闭虚拟机。 此外，它还会对服务控制台产生性能影响，尤其是在同时打开许多VM控制台会话的情况下。""",

    "audit": u"""Instead of VM console, use native remote management services, such as terminal services
        and ssh, to interact with virtual machines. Grant VM console access only when necessary.
        1. From the vSphere Client, select an object in the inventory.
        2. Click the Permissions tab to view the user and role pair assignments for that object.
        3. Next, navigate to Administration\Roles section of vCenter.
        4. Select the role in question and choose edit to see which effective privileges are enabled.
        5. Only Authorized users should have a role which allows them a privilege under the Virtual Machine\Interaction section of the role editor.""",

    "remediation": u"""默认情况下，vCenter角色“虚拟机高级用户”和“虚拟机管理员”具有“Virtual Machine.Interaction.Console Interaction”权限。 不允许未经授权的个人在虚拟机或虚拟机文件夹上拥有这些角色。
         1.在vSphere Client中，导航到vCenter的Administration \ Roles部分。
         2.创建自定义角色，然后选择编辑以仅启用所需的最低有效权限。
         3.接下来，选择清单中的对象。
         4.单击“权限”选项卡以查看该对象的用户和角色对分配。
         5.删除所有默认的“管理员”或“高级用户”角色，并根据需要分配新的自定义角色。""",
}
reportContent["8.3.3"] = {
    "title": u"""使用安全协议进行虚拟串行端口访问""",
    "level": u"""Not Scored""",

    "description": u"""虚拟串行端口允许虚拟机通过网络进行通信。 这样做允许您将虚拟串行端口连接重定向到ESXi主机上的TCP / IP连接。 如果需要虚拟串行端口，请确保它们配置为使用安全协议。串行端口是用于将外围设备连接到虚拟机的接口。 
	    它们通常用于物理系统，以提供与服务器控制台的直接低级连接。 串行端口允许调试级别访问，这通常没有强大的控制，如日志记录或权限。""",

    "audit": u"""Check that no clear text protocols are configured:
        tcp - an unencrypted TCP connection (IPv4 or IPv6)
        tcp4 - an unencrypted TCP connection (IPv4 only)
        tcp6 - an unencrypted TCP connection (IPv6 only)
        telnet telnet over TCP without SSL. The virtual machine and remote system can
        negotiate and use SSL if the remote system supports the telnet authentication
        option. If not, the connection uses unencrypted text (plain text)
        Only these secure protocols should be configured:   
        ssl - the equivalent of TCP+SSL
        tcp+ssl - SSL over TCP over IPv4 or IPv6
        tcp4+ssl - SSL over TCP over IPv4
        tcp6+ssl - SSL over TCP over IPv6
        telnet over TCP with SSL. The virtual machine and remote system can negotiate and
        use SSL if the remote system supports the telnet authentication option. If not, the
        connection uses unencrypted text (plain text)
        telnets - telnet over SSL over TCP. In this case, SSL negotiation begins immediately
        and you cannot use the telnet authentication option.""",

    "remediation": u"""使用安全网络协议配置虚拟串行端口通信：
      ssl - 相当于TCP + SSL
      tcp+ ssl - 基于TCP over IPv4或IPv6的SSL
      tcp4+ ssl - 基于TCP的IPv4 over SSL
      tcp6+ ssl - 基于TCP的TCP over SSL
      使用SSL通过TCP进行telnet。 如果远程系统支持telnet身份验证选项，则虚拟机和远程系统可以协商并使用SSL。 如果没有，连接使用未加密的文本（纯文本）
      telnet - 通过TCP通过SSL进行telnet。 在这种情况下，SSL协商会立即开始，您无法使用telnet身份验证选项。""",
}

reportContent["8.3.4"] = {
    "title": u"""尽可能使用模板部署VM""",
    "level": u"""Not Scored""",

    "description": u"""使用强化的基本操作系统模板映像创建其他特定于应用程序的模板，并使用特定于应用程序的模板来部署虚拟机。通过在模板中捕获强化的基本操作系统映像（未安装应用程序），
	    可以确保所有 您的虚拟机是使用已知的基准安全级别创建的。 然后，您可以使用此模板创建其他特定于应用程序的模板，也可以使用应用程序模板来部署虚拟机。 将操作系统和应用程序手动安装到VM中
	    会导致由于人为或进程错误而导致配置错误的风险。确保应用程序不依赖于要部署的虚拟机的特定信息。""",

    "audit": u"""Verify that new virtual machine deployments are completed using hardened, patched, and
        properly configured OS templates.""",

    "remediation": u"""提供用于VM创建的模板，其中包含经过强化，修补和正确配置的操作系统部署。 如果可能，也可以在模板中预先部署应用程序，尽管应该注意应用程序不依赖于要部署的VM特定信息。 
	    在vSphere中，您可以将模板转换为虚拟机并快速返回，这使得更新模板非常容易。""",
}

reportContent["8.4.1"] = {
    "title": u"""通过dvfilter网络API控制对VM的访问""",
    "level": u"""Not Scored""",

    "description": u"""正确配置受dvfilter网络API保护的VM。必须明确配置VM以接受dvfilter网络API的访问。 仅配置将由API专门访问的VM。 攻击者可能通过使用dvFilter API来破坏VM。不正确地配置此选项
	     可能会对使用vmsafe API的工具的功能产生负面影响。 它还可以防止VM连接到网络。""",

    "audit": u"""If a VM is supposed to be protected:
         Verify that the following in its VMX file: ethernet0.filter1.name = dvfilter1 where ethernet0 is the network adapter interface of the virtual machine
        that is to be protected, filter1 is the number of the filter that is being used, and dvfilter1 is the name of the particular data path kernel module that is protecting the
        VM.
         Ensure that the name of the data path kernel is set correctly.
        If a VM is not supposed to be protected:
         Verify that the following is not in its VMX file: ethernet0.filter1.name = dvfilter1 where ethernet0 is the network adapter interface of the virtual machine
        that is to be protected, filter1 is the number of the filter that is being used, and dv-filter1 is the name of the particular data path kernel module that is protecting the VM.""",

    "remediation": u"""如果VM应该受到保护：
           在其VMX文件中配置以下内容：ethernet0.filter1.name = dvfilter1其中ethernet0是要保护的虚拟机的网络适配器接口，filter1是正在使用的过滤器的编号，dvfilter1是名称 正在保护VM的特定数据路径内核模块。
           确保正确设置数据路径内核的名称。
                     如果VM不应受保护：
           从其VMX文件中删除以下内容：ethernet0.filter1.name = dvfilter1其中ethernet0是要保护的虚拟机的网络适配器接口，filter1是正在使用的过滤器的编号，dvfilter1是名称 正在保护VM的特定数据路径内核模块。""",
}

reportContent["8.4.2"] = {
    "title": u"""控制VMsafe代理地址""",
    "level": u"""Not Scored""",

    "description": u"""正确配置虚拟机配置文件中的vmsafe.agentAddress选项.VMsafe CPU /内存API允许安全虚拟机检查和修改其他VM上的内存和CPU寄存器的内容，以便检测和防止恶意软件攻击。 但是，攻击者可能会利用此内省通道来破坏VM; 因此，您应该监控未经授权使用此API。 必须明确配置VM以接受VMsafe CPU /内存API的访问。
        这涉及三个参数来执行以下操作：
            1.启用API
            2.在内省vSwitch上设置安全虚拟设备使用的IP地址
            3.设置该IP地址的端口号。
        如果VM受此类产品保护，请确保正确设置后两个参数。 这应仅针对您希望获得此保护的特定VM执行。
		错误地配置此选项可能会对使用VMsafe API的工具的功能产生负面影响。""",

    "audit": u"""If the VM is not being protected by a VMsafe CPU/memory product, then check virtual
        machine configuration file and verify that vmsafe.agentAddress is not present.
        If it is being protected by a VMsafe CPU/Memory product then make sure the
        vmsafe.agentAddress is set to the correct value.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "vmsafe.agentAddress" | Select Entity, Name, Value""",

    "remediation": u"""如果VM未受VMsafe CPU /内存产品保护，请检查虚拟机配置文件并验证vmsafe.agentAddress是否存在。如果它受VMsafe CPU /内存产品保护，请确保将其设置为正确的值""",
}

reportContent["8.4.3"] = {
    "title": u"""控制VMsafe代理端口""",
    "level": u"""Not Scored""",

    "description": u"""正确配置虚拟机配置文件中的vmsafe.agentPort选项.VMsafe CPU /内存API允许安全虚拟机检查和修改其他VM上的内存和CPU寄存器的内容，以便检测和防止恶意软件攻击。
	    但是，攻击者可能会利用此内省通道来破坏VM;因此，您应该监控未经授权使用此API。必须明确配置VM以接受VMsafe CPU /内存API的访问。
        这涉及三个参数来执行以下操作：
            1.启用API
            2.在内省vSwitch上设置安全虚拟设备使用的IP地址
            3.设置该IP地址的端口号。
        如果VM受此类产品保护，请确保正确设置后两个参数。这应仅针对您希望获得此保护的特定VM执行。
        错误地配置此选项可能会对使用VMsafe API的工具的功能产生负面影响。""",

    "audit": u"""If the VM is not being protected by a VMsafe CPU/memory product, then check virtual
        machine configuration file and verify that vmsafe.agentPort is not present. If it is being
        protect by a VMsafe CPU/Memory product, make sure this is set to the correct value
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "vmsafe.agentPort"| Select Entity, Name, Value""",

    "remediation": u"""如果VM未受VMsafe CPU /内存产品保护，请检查虚拟机配置文件并验证vmsafe.agentPort不存在。
        如果VMsafe CPU /内存产品正在保护它，请确保将vmsafe.agentPort设置为正确的值。""",
}

reportContent["8.4.4"] = {
    "title": u"""控制VMsafe代理配置""",
    "level": u"""Not Scored""",

    "description": u"""正确配置虚拟机配置文件中的vmsafe.enable选项。它应该不存在或设置为FALSE.VMsafe CPU /内存API允许安全虚拟机检查和修改其他VM上的内存和CPU寄存器的内容，
	    以便检测和防止恶意软件攻击。但是，攻击者可能会利用此内省通道来破坏VM;因此，您应该监控未经授权使用此API。必须明确配置VM以接受VMsafe CPU /内存API的访问。
        这涉及三个参数来执行以下操作：
            1.启用API
            2.在内省vSwitch上设置安全虚拟设备使用的IP地址
            3.设置该IP地址的端口号。
        如果VM受此类产品保护，请确保正确设置后两个参数。这应仅针对您希望获得此保护的特定VM执行。
        错误地配置此选项可能会对使用vmsafe API的工具的功能产生负面影响。""",

    "audit": u"""If the VM is not being protected by a VMsafe CPU/memory product, then check virtual
        machine configuration file and verify that vmsafe.enable is either not present, or set to FALSE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "vmsafe.enable"| Select Entity, Name, Value""",

    "remediation": u"""如果VM未受VMsafe CPU /内存产品保护，请检查虚拟机配置文件并将vmsafe.enable设置为FALSE。""",
}

reportContent["8.4.5"] = {
    "title": u"""禁用自动登录""",
    "level": u"""Scored""",

    "description": u"""禁用不需要的自动登录以减少漏洞的可能性。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.ghi.autologon.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.autologon.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.ghi.autologon.disable" -value
        $true""",
}
reportContent["8.4.6"] = {
    "title": u"""禁用BIOS BBS""",
    "level": u"""Scored""",

    "description": u"""禁用BIOS BBS以减少漏洞的可能性。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值。""",

    "audit": u"""Check virtual machine configuration file and verify that isolation.bios.bbs.disable is
        set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.bios.bbs.disable"| Select Entity, Name,
        Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.bios.bbs.disable" -value $true""",
}

reportContent["8.4.7"] = {
    "title": u"""禁用guest主机交互协议处理程序。""",
    "level": u"""Scored""",

    "description": u"""禁用guest主机交互协议句柄以减少漏洞的机会。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.ghi.protocolhandler.info.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.protocolhandler.info.disable"
        | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.ghi.protocolhandler.info.disable" -value $true""",
}

reportContent["8.4.8"] = {
    "title": u"""禁用Unity任务栏 """,
    "level": u"""Disable unexposed Unity Taskbar feature.""",

    "description": u"""禁用未公开的Unity任务栏功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.unity.taskbar.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.taskbar.disable" | Select
        Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.unity.taskbar.disable" -value $true""",
}

reportContent["8.4.9"] = {
    "title": u"""禁用Unity Active""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Unity Active功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.unityActive.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.unityActive.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.unityActive.disable" -value $True""",
}

reportContent["8.4.10"] = {
    "title": u"""禁用Unity窗口内容""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Unity窗口内容功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.unity.windowContents.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.windowContents.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.unity.windowContents.disable" -value $True""",
}

reportContent["8.4.11"] = {
    "title": u"""禁用Unity推送更新""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Unity推送更新功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.unity.push.update.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.push.update.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.unity.push.update.disable" -value $true""",
}

reportContent["8.4.12"] = {
    "title": u"""禁用拖放版本获取 """,
    "level": u"""Scored""",

    "description": u"""禁用未曝光的拖放版本获取功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.vmxDnDVersionGet.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.vmxDnDVersionGet.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.vmxDnDVersionGet.disable" -value $true""",
}
reportContent["8.4.13"] = {
    "title": u"""禁用拖放版本集""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的拖放版本集功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.guestDnDVersionSet.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.guestDnDVersionSet.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.guestDnDVersionSet.disable" -value $true""",
}

reportContent["8.2.2"] = {
    "title": u"""Unix""",
    "level": u"""Scored""",

    "description": u"""Run""",

    "audit": u"""Runningible""",

    "remediation": u"""Configuration""",
}

reportContent["8.4.14"] = {
    "title": u"""禁用Shell操作""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Shell操作功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。一些自动化工具和流程可能会停止运行""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.ghi.host.shellAction.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.ghi.host.shellAction.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.ghi.host.shellAction.disable" -value $true""",
}

reportContent["8.4.15"] = {
    "title": u"""禁用请求磁盘拓扑 """,
    "level": u"""Scored""",

    "description": u"""禁用未曝光的请求磁盘拓扑功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。一些自动化工具和流程可能会停止运行""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.dispTopoRequest.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.dispTopoRequest.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.dispTopoRequest.disable" -value $true""",
}

reportContent["8.4.16"] = {
    "title": u"""禁用垃圾文件夹状态""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的“废纸篓文件夹状态”功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.trashFolderState.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.trashFolderState.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.trashFolderState.disable" -value $true""",
}

reportContent["8.4.17"] = {
    "title": u"""禁用访客主机交互托盘图标""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Guest Host Interaction Tray Icon功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.ghi.trayicon.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.trayicon.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.ghi.trayicon.disable" -value $true""",
}

reportContent["8.4.18"] = {
    "title": u"""禁用Unity""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Unity功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 这些功能的代码路径未在ESX中实现。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，这些都是针对那些坚持任何文档设置的客户记录的，无论是否在代码中实现，都必须具有价值。一些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that isolation.tools.unity.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.unity.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.unity.disable" -value $true""",
}

reportContent["8.4.19"] = {
    "title": u"""禁用Unity Interlock""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Unity Interlock功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.unityInterlockOperation.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.unityInterlockOperation.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.unityInterlockOperation.disable" -value $true""",
}

reportContent["8.4.20"] = {
    "title": u"""禁用GetCreds""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的GetCreds功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.getCreds.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.getCreds.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.getCreds.disable" -value $true""",
}

reportContent["8.4.21"] = {
    "title": u"""禁用主机guest文件系统服务器""",
    "level": u"""Scored""",

    "description": u"""禁用未暴露的主机guest文件系统服务器。某些自动化操作（如自动工具升级）将组件用于称为主机guest文件系统（HGFS）的虚拟机管理程序，攻击者可能会使用此组件在guest操作系统内传输文件。
	    这些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。明确禁用这些功能可以减少漏洞的可能性，因为它可以减少
	    guest虚拟机影响主机的方式。请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些。这将导致VMX进程不响应来自工具进程的命令。它还可能对自动化工具升级等操作产生负面影响。
		将isolation.tools.hgfsServerSet.disable设置为TRUE将禁用guest虚拟机的HGFS服务器与主机的注册。使用HGFS与客户机操作系统之间传输文件的API（例如某些VIX命令或VMware Tools自动升级实用程序）将无法运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.hgfsServerSet.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.hgfsServerSet.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.hgfsServerSet.disable" -value $true""",
}

reportContent["8.4.22"] = {
    "title": u"""禁用guest主机交互启动菜单""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的Guest Host Interaction启动菜单功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.ghi.launchmenu.change is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.ghi.launchmenu.change" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.ghi.launchmenu.change" -value $true""",
}

reportContent["8.4.23"] = {
    "title": u"""禁用memSchedFakeSampleStats""",
    "level": u"""Scored""",

    "description": u"""禁用未曝光的memSchedFakeSampleStats功能。某些VMX参数不适用于vSphere，因为VMware虚拟机可在vSphere和托管虚拟化平台（如Workstation和Fusion）上运行。 ESXi中未实现这些功能的代码路径。 
	    明确禁用这些功能可以减少漏洞的可能性，因为它可以减少guest虚拟机影响主机的方式。 请注意，对于坚持任何文档设置的组织，无论是否在代码中实现，都必须具有值，因此引用这些设置。某些自动化工具和流程可能会停止运行。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.memSchedFakeSampleStats.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.memSchedFakeSampleStats.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.memSchedFakeSampleStats.disable" -value $true""",
}

reportContent["8.4.24"] = {
    "title": u"""禁用VM控制台复制操作""",
    "level": u"""Scored""",

    "description": u"""禁用VM控制台复制和粘贴操作。默认情况下禁用复制和粘贴操作; 但是，通过明确禁用此功能，它将使审计控制能够检查此设置是否正确。这是默认设置，因此功能保持不变。 如果需要复制和粘贴操作，
	    则必须使用vSphere Client启用它们。""",

    "audit": u"""Check virtual machine configuration and verify that isolation.tools.copy.disable
        option is missing or set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.copy.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.copy.disable" -value $true""",
}
reportContent["8.4.25"] = {
    "title": u"""禁用VM控制台拖放操作""",
    "level": u"""Scored""",

    "description": u"""禁用VM控制台拖放操作。默认情况下禁用复制和粘贴操作; 但是，通过明确禁用此功能，它将使审计控制能够检查此设置是否正确。这是默认设置，因此功能保持不变。""",

    "audit": u"""Check virtual machine configuration and verify that isolation.tools.dnd.disable is
        missing or set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.dnd.disable" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.dnd.disable" -value $true""",
}

reportContent["8.4.26"] = {
    "title": u"""禁用VM控制台GUI选项""",
    "level": u"""Scored""",

    "description": u"""禁用VM控制台和粘贴GUI选项。默认情况下禁用复制和粘贴操作; 但是，通过明确禁用此功能，它将使审计控制能够检查此设置是否正确。这是默认设置，因此功能保持不变。""",

    "audit": u"""Check virtual machine configuration and verify that
        isolation.tools.setGUIOptions.enable option is missing or set to FALSE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.setGUIOptions.enable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.setGUIOptions.enable" -value $false""",
}

reportContent["8.4.27"] = {
    "title": u"""禁用VM控制台粘贴操作""",
    "level": u"""Scored""",

    "description": u"""禁用VM控制台粘贴操作。默认情况下禁用复制和粘贴操作; 但是，通过明确禁用此功能，它将使审计控制能够检查此设置是否正确。这是默认设置，因此功能保持不变。 如果需要复制和粘贴操作，则必须使用vSphere Web Client启用它们。""",

    "audit": u"""Check virtual machine configuration and verify that isolation.tools.paste.disable is
        missing or set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.paste.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.paste.disable" -value $true""",
}

reportContent["8.4.28"] = {
    "title": u"""通过VNC协议控制对VM控制台的访问 """,
    "level": u"""Scored""",

    "description": u"""通过VNC协议最大限度地减少对虚拟机的访问。通过VM控制台，您可以连接到虚拟机的控制台，实际上可以查看物理服务器上的监视器将显示的内容。 该控制台也可通过VNC协议使用。 设置此访问权限还涉及在虚拟机将运行的每个ESXi服务器上设置防火墙规则。
	    配置VM设置并打开防火墙意味着需要配置和监视多个步骤。""",

    "audit": u"""Check virtual machine configuration and verify that RemoteDisplay.vnc.enabled is
        missing or set to FALSE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "RemoteDisplay.vnc.enabled" | Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "RemoteDisplay.vnc.enabled" -value $false""",
}

reportContent["8.4.29"] = {
    "title": u"""禁用虚拟机上的所有VGA模式。""",
    "level": u"""Not Scored""",

    "description": u"""为虚拟机视频卡启用仅VGA模式。许多服务器级虚拟机只需要标准VGA控制台（通常是Unix / Linux服务器或Windows Server Core系统）。 启用此设置将删除除禁用3D之外的其他不必要的图形功能。 这减少了可用于恶意攻击的潜在攻击面。将此设置配置为True将不允许任何高级图形功能工作。 
	     只有字符单元格控制台模式可用。 使用此设置会使mks.enable3d无效。""",

    "audit": u"""Check that the virtual machine advanced setting of "svga.vgaonly" is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "svga.vgaOnly" | Select Entity, Name, Value""",

    "remediation": u"""检查虚拟机高级设置“svga.vgaonly”是否设置为TRUE。
        要使用vSphere Client修改虚拟机的高级设置，请执行以下操作：
            1.确保虚拟机已关闭并已关闭电源。
            2.右键单击虚拟机。
            3.单击“编辑设置...”以打开“虚拟机属性”窗口。
            4.单击“选项”选项卡。
            5.从左侧列表中，单击“高级”>“常规”。
            6.在右侧的“配置参数”框中，单击“配置参数...”。
            7.单击“添加行”。
            8.在新行上，单击“名称”列下的并指定配置选项名称。
            9.在新行上，单击“值”列下的并指定配置值。
            10.启动虚拟机以使设置生效。
        此外，可以使用以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "svga.vgaOnly" -value $true""",
}

reportContent["8.5.1"] = {
    "title": u"""防止虚拟机接管资源 """,
    "level": u"""Not Scored""",

    "description": u"""使用限制，共享和预留来防止虚拟机接管资源。默认情况下，ESXi主机上的所有虚拟机均等地共享资源。 通过使用ESXi的资源管理功能（例如共享和限制），您可以控制虚拟机使用的服务器资源。 
	    拒绝服务可能导致一台虚拟机消耗大量主机资源，而同一主机上的其他虚拟机无法执行其预期功能。 您可以使用此机制来防止这种情况发生。""",

    "audit": u"""Use shares or reservations to guarantee resources to critical VMs. Use limits to constrain
        resource consumption by virtual machines that have a greater risk of being exploited or
        attacked, or that run applications that are known to have the potential to greatly consume resources.
        Additionally, the following PowerCLI command may be used:
        # List all Resource shares on all VMs
        Get-VM | Get-VMResourceConfiguration""",

    "remediation": u"""使用共享或预留来保证关键VM的资源。
        使用限制来限制具有更大被利用或攻击风险的虚拟机的资源消耗，或者运行已知可能极大地消耗资源的应用程序。""",
}

reportContent["8.6.1"] = {
    "title": u"""避免使用非永久性磁盘""",
    "level": u"""Scored""",

    "description": u"""虚拟机磁盘默认情况下创建为Dependent，并受快照影响。为确保虚拟机磁盘不受快照影响，磁盘模式可以设置为Independent.Disks设置为Independent模式可以是Independent Persistent或Independent Nonpersistent.Disks with独立持久模式将其数据永久写入磁盘。
	    独立非永久性磁盘会在系统重新引导时丢失对磁盘所做的任何更改，并且可以屏蔽对系统的任何攻击痕迹。
        非持久磁盘模式的安全问题是，成功的攻击者可以通过简单的关闭或重新启动来撤消或删除他们在计算机上的任何痕迹。为防范此风险，应按如下方式配置生产虚拟机：
            1.未启用独立设置
            2.独立持久
            3.独立非远程登录
        如果没有VM上的持续活动记录，管理员可能永远不会知道他们是否受到攻击或被黑客攻击。因此不要使用非持久模式，该模式允许在重新引导VM时进入已知状态。""",

    "audit": u"""If remote logging of events and activity is not configured for the guest, scsiX:Y.mode should be either:
        1. Not present. This is the default.
        2. Not set to independent nonpersistent
        Additionally, the following PowerCLI command may be used:
        #List the VM's and their disk types
        Get-VM | Get-HardDisk | Select Parent, Name, Filename, DiskType, Persistence""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        #Alter the parameters for the following cmdlet to set the VM Disk Type:
        Get-VM | Get-HardDisk | Set-HardDisk""",
}

reportContent["8.6.2"] = {
    "title": u"""禁用虚拟磁盘收缩""",
    "level": u"""Scored""",

    "description": u"""如果重复执行虚拟磁盘收缩，则会导致虚拟磁盘不可用，从而导致拒绝服务。您可以通过禁用虚拟磁盘来防止虚拟磁盘收缩。清除虚拟磁盘会回收其中未使用的空间。如果磁盘中有空白空间，则此过程会减少虚拟磁盘在主驱动器上占用的空间量。
	    普通用户和进程（即没有root或管理员权限的用户和进程）在虚拟机中具有调用此过程的能力。但是，如果重复执行此操作，则在执行此收缩时虚拟磁盘可能变得不可用，从而有效地导致拒绝服务。在大多数数据中心环境中，磁盘收缩未完成，因此您应禁用此功能。重复磁盘收缩会使虚拟磁盘不可用。 guest虚拟机中的非管理用户可以使用此功能。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.diskShrink.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.diskShrink.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.diskShrink.disable" -value $true""",
}

reportContent["8.6.3"] = {
    "title": u"""禁用虚拟磁盘擦除""",
    "level": u"""Scored""",

    "description": u"""如果重复执行虚拟磁盘擦除，则会导致虚拟磁盘不可用，从而导致拒绝服务。您可以通过禁用虚拟磁盘擦除来阻止虚拟磁盘擦除。擦除虚拟磁盘会回收其中所有未使用的空间。如果磁盘中有空白空间，则此过程会减少虚拟磁盘在主驱动器上占用的空间量。普通用户和进程（即没有root或管理员权限的用户和进程）在虚拟机中具有调用此过程的能力。
	    但是，如果重复这样做，则在执行擦除时虚拟磁盘可能变得不可用，从而有效地导致拒绝服务。在大多数数据中心环境中，磁盘擦除未完成，因此您应禁用此功能。重复擦除磁盘可能会使虚拟磁盘不可用。 guest虚拟机中的非管理用户可以使用此功能。禁用此功能时，如果数据存储空间不足，则无法擦除虚拟机磁盘。""",

    "audit": u"""Check virtual machine configuration file and verify that isolation.tools.diskWiper.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.diskWiper.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.diskWiper.disable" -value $true""",
}

reportContent["8.7.1"] = {
    "title": u"""禁用VM的VIX消息""",
    "level": u"""Scored""",

    "description": u"""VIX API是一个用于编写脚本和程序以操作虚拟机的库。 如果您未在您的环境中使用自定义VIX编程，则应禁用某些功能以减少漏洞的可能性。 从VM向主机发送消息的能力是这些功能之一。访客将无法再通过VIX API发送消息。""",

    "audit": u"""Check virtual machine configuration file and verify that
        isolation.tools.vixMessage.disable is set to TRUE.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "isolation.tools.vixMessage.disable"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "isolation.tools.vixMessage.disable" -value $true""",
}

reportContent["8.7.2"] = {
    "title": u"""限制VM日志文件的数量""",
    "level": u"""Scored""",

    "description": u"""配置VM设置以防止不受控制的日志记录。您可以使用日志设置来限制日志文件的总大小和数量。通常，只有在重新引导主机时才会创建新的日志文件，因此文件可能会变得非常大。您可以通过限制日志文件的最大大小来确保更频繁地创建新日志文件。
       如果要限制日志记录数据的总大小，VMware建议保存10个日志文件，每个文件限制为1,000KB。数据存储可能使用2MB或4MB的块大小进行格式化，因此大小限制远低于此大小将导致不必要的存储利用率。每次将条目写入日志时，都会检查日志的大小;如果超过限制，则将
	   下一个条目写入新日志。如果已存在最大日志文件数，则在创建新日志文件时，将删除最旧的日志文件。可以通过编写大量日志条目来尝试避免这些限制的拒绝服务攻击。但是每个日志条目限制为4KB，因此没有日志文件比配置的限制大4KB。第二个选项是禁用虚拟机的
	   日志记录。禁用虚拟机的日志记录会使故障排除具有挑战性并且难以支持。您不应该考虑禁用日志记录，除非日志文件轮换方法证明不足。由于数​​据存储区被填满，不受控制的日志记录可能导致拒绝服务。更极端的策略是完全禁用虚拟机的日志记录。禁用日志记录会使
	   故障排除具有挑除非日志文件轮换方法证明不足，否则不要考虑禁用日志记录。""",

    "audit": u"""Check virtual machine configuration file and verify that log.keepOld is set to 10.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "log.keepOld"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "log.keepOld" -value "10\"""",
}

reportContent["8.7.3"] = {
    "title": u"""不要向guests发送主机信息""",
    "level": u"""Scored""",

    "description": u"""配置VMware Tools以禁止将主机信息发送给guest虚拟机。通过使VM能够获取有关物理主机的详细信息，攻击者可能会使用此信息来通知对主机的进一步攻击。 如果设置为TRUE，则VM可以获取有关物理主机的详细信息。 参数的默认值为FALSE。 
	    除非特定VM需要此信息进行性能监视，否则此设置不应为TRUE。您无法从guest虚拟机内部检索有关主机的性能信息，有时这对故障排除很有用。""",

    "audit": u"""Check virtual machine configuration file and verify that tools.guestlib.enableHostInfo is set to FALSE. 
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "tools.guestlib.enableHostInfo"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "tools.guestlib.enableHostInfo" -value $false""",
}

reportContent["8.7.4"] = {
    "title": u"""限制VM日志文件大小 """,
    "level": u"""Scored""",

    "description": u"""配置VM设置以防止不受控制的日志记录。虚拟机将故障排除信息写入存储在VMFS卷上的虚拟机日志文件中。虚拟机用户和进程可能会故意滥用日志记录，或者无意中滥用日志文件中的大量数据。随着时间的推移，日志文件可能会占用足够的文件系统空间来导致拒绝服务。
	    您可以使用日志设置来限制日志文件的总大小和数量。通常，只有在重新引导主机时才会创建新的日志文件，因此文件可能会变得非常大。您可以通过限制日志文件的最大大小来确保更频繁地创建新日志文件。如果要限制日志记录数据的总大小，VMware建议保存10个日志文件，每个文件限
	    制为1,000KB（1,024,000字节）。数据存储可能使用2MB或4MB的块大小进行格式化，因此大小限制远低于此大小将导致不必要的存储利用率。每次将条目写入日志时，都会检查日志的大小;如果超过限制，则将下一个条目写入新日志。如果已存在最大日志文件数，则在创建新日志文件时，
	    将删除最旧的日志文件。可以通过编写大量日志条目来尝试避免这些限制的拒绝服务攻击。但是每个日志条目限制为4KB，因此没有日志文件比配置的限制大4KB。第二个选项是禁用虚拟机的日志记录。禁用虚拟机的日志记录会使故障排除具有挑战性并且难以支持。除非日志文件轮换方法证明不足，
	    否则不应考虑禁用日志记录。由于数据存储被填满，不受控制的日志记录可能导致拒绝服务。更极端的策略是完全禁用虚拟机的日志记录。禁用日志记录会使故障排除具有挑除非日志文件轮换方法证明不足，否则不要考虑禁用日志记录。""",

    "audit": u"""Check virtual machine configuration file and verify that log.rotateSize is set to 1024000.
        Additionally, the following PowerCLI command may be used:
        # List the VMs and their current settings
        Get-VM | Get-AdvancedSetting -Name "log.rotateSize"| Select Entity, Name, Value""",

    "remediation": u"""要实施建议的配置状态，请运行以下PowerCLI命令：
        # Add the setting to all VMs
        Get-VM | New-AdvancedSetting -Name "log.rotateSize" -value "1024000\"""",
}

reportContent["9.1"] = {
    "title": u"""禁止共享root帐号""",
    "level": u"""Scored""",

    "description": u"""默认情况下，每个ESXi主机有一个“root”的帐号，用于本地管理和主机连接。为了避免共享一个公共根帐号，建议至少创建一个用户帐号，并将其分配给全部管理员权限，并使用此帐户代替共享的“root”帐号；即使为AD域控主机，也应当增加一个本地帐号。""",

    "audit": u"""1.	通过命令行方式连接主机。
        2.	检查帐号清单：Get-VMHostAccount""",

    "remediation": u"""无""",
}
