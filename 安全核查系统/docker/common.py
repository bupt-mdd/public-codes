# -*- coding: utf-8 -*-

PASS = 1

WARN = 0
manual = [
    1, 1, 1, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 0, 0,
    0, 0, 1, 0, 0,
    0, 0, 0, 0, 1,
    1, 1, 0, 0, 0,
    1
]
reportIndex = [
    '1', '2', '3', '4', '5',
    '6', '7', '8', '9', '10',
    '11', '12', '13', '14', '15',
    '16', '17', '18', '19', '20',
    '21', '22', '23', '24', '25',
    '26', '27', '28', '29', '30',
    '31'
]

reportContent = dict()
for i in reportIndex:
    reportContent[i] = {
        "title": u'''Title''',
        "description": u'''Description''',
        "impact": u'''Impact''',
        "audit": u'''Audit''',
        "remediation": u'''Remediation'''
    }

reportContent['1'] = {
    "titile": u'''是否禁用 AppArmor Profile''',
    "description": u'''AppArmor是一个有效且易于使用的Linux应用程序安全系统。默认情况下，可以在很多Linux发行版上使用，例如Debian和Ubuntu。AppArmor通过强制执行安全策略（也称为AppArmor配置文件）来保护Linux操作系统和应用程序免受各种威胁。''',
    "impact": u'''容器（进程）具有AppArmor配置文件中定义的一组限制。 如果您的AppArmor配置文件配置错误，则容器可能无法完全按预期工作。''',
    "audit": u'''docker ps --quiet | xargs docker inspect --format '{{ .Id }}: AppArmorProfile={{ .AppArmorProfile }}'
                 运行以上命令，该命令应该为每个容器实例返回一个有效的AppArmor配置文件。''',
	"remediation": u'''如果AppArmor适用于您的Linux操作系统，请使用它。您可能必须遵循以下步骤：
                           1、验证是否已安装AppArmor。如果没有，请安装它。
                           2、为Docker容器创建或导入AppArmor配置文件。
                           3、将此配置文件置于强制模式。
                           4、使用自定义的AppArmor配置文件启动Docker容器。 例如运行以下命令：
                              docker run --interactive --tty --security-opt="apparmor:PROFILENAME" centos /bin/bash
                       或者，您可以保留docker的默认AppArmor配置文件。'''
}

reportContent['2'] = {
    "titile": u'''是否验证SELinux安全选项''',
    "description": u'''SELinux是一款高效且易于使用的Linux应用程序安全系统。默认可用于多种Linux发行版，如Red Hat和Fedora。SELinux提供强制访问控制（MAC）系统，极大地增强了默认的自主访问控制（DAC）模型。可以通过在Linux主机上启用SELinux来增加额外的安全层。''',
    "impact": u'''容器（进程）将具有SELinux策略中定义的一组限制。如果您的SELinux策略配置错误，则容器可能无法完全按预期工作。''',
    "audit": u'''docker ps --quiet | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}'
                 以上命令应返回当前为容器配置的所有安全选项。''',
    "remediation": u'''如果SELinux适用于您的Linux操作系统，请使用它。您可能必须遵循以下步骤：
                           1、设置SELinux状态。
                           2、设置SELinux策略。
                           3、为Docker容器创建或导入SELinux策略模板。
                           4、在启用SELinux的守护进程模式下启动Docker。例如运行以下命令：
                              docker daemon --selinux-enabled
                           5、使用安全选项启动Docker容器。 例如运行以下命令：
                              docker run --interactive --tty --security-opt label=level:TopSecret centos /bin/bash'''
}

reportContent['3'] = {
    "titile": u'''是否限制在容器内的Linux内核功能。''',
    "description": u'''默认情况下，Docker使用一组受限的Linux内核功能启动容器。这意味着可以为任何进程授予所需的功能，而不是root访问权限。使用Linux内核功能，对于几乎所有通常需要root权限的特定区域，进程不必以root身份运行。''',
    "impact": u'''通过添加或删除的Linux内核功能来限制容器内的使用功能。Docker支持添加和删除功能，允许使用非默认配置文件。这可以通过删除功能使Docker更安全，或通过添加功能使安全性更低。因此，建议删除除容器进程明确要求的功能之外的所有功能。''',
    "audit": u'''docker ps --quiet | xargs docker inspect --format '{{ .Id }}: CapAdd={{ .HostConfig.CapAdd }} CapDrop={{ .HostConfig.CapDrop }}'
                 验证添加和删除的Linux内核功能是否与每个容器实例的容器进程所需的功能一致。''',
    "remediation": u'''执行以下命令以添加所需的功能：
                       $> docker run --cap-add={"Capability 1","Capability 2"} <Run arguments> <Container Image Name or ID> <Command>
                       例如：
                       docker run --interactive --tty --cap-add={"NET_ADMIN","SYS_ADMIN"} centos:latest /bin/bash'''
}
reportContent['4'] = {
    "titile": u'''是否不使用特权容器''',
    "description": u'''使用--privileged标志为容器提供所有Linux内核功能，从而覆盖--cap-add和--cap-drop标志。确保不使用它。--privileged标志还解除了设备cgroup控制器强制执行的所有限制。换句话说，容器几乎可以完成主机可以执行的所有操作。此标志存在以允许特殊用例，例如在Docker中运行Docker。''',
    "impact": u'''除默认值之外的Linux内核功能将无法在容器内使用。'''
}
reportContent['5'] = {
    "titile": u'''是否没有将主机的敏感目录挂载在容器上。''',
    "description": u'''不应允许将下面的敏感主机系统目录作为容器卷挂载，尤其是在读写模式下(/,/boot,/dev,/etc,/lib,/proc,/sys,/usr)。如果敏感目录以读写模式挂载，则可以更改这些敏感目录中的文件。 这些更改可能会降低安全隐患或无理更改，从而使Docker主机处于受损状态。''',
    "impact": u'''None'''
}

reportContent['6'] = {
    "titile": u'''是否不在容器内运行ssh''',
    "description": u'''SSH服务器不应该在容器内运行。应使用SSH进入Docker主机，并使用nsenter工具从远程主机入容器。在容器内运行SSH会增加安全管理的复杂性。''',
    "impact": u'''None'''
}
reportContent['7'] = {
    "titile": u'''是否没有在容器内映射特权端口''',
    "description": u'''低于1024的TCP / IP端口号被视为特权端口。出于各种安全原因，不允许普通用户和进程使用它们。Docker允许将容器端口映射到特权端口。如果用户明确声明容器端口，则Docker允许将容器端口映射到主机上的特权端口。这是因为容器是使用NET_BIND_SERVICE Linux内核功能执行的，不会限制特权端口映射。特权端口接收和传输各种敏感和特权数据，因此允许容器使用它们会带来严重影响。''',
    "impact": u'''None'''
}
reportContent['8'] = {
    "titile": u'''是否只在容器上打开需要的端口''',
    "description": u'''容器镜像的Dockerfile定义了容器实例上默认打开的端口。端口列表可能与您在容器中运行的应用程序相关，也可能不相关。只能使用Dockerfile中为其镜像定义的端口运行容器，或者可以任意传递运行时参数以打开端口列表。打开不需要的端口会增加容器和容器化应用程序的攻击面。 建议不要打开不需要的端口。''',
    "impact": u'''None''',
    "audit": u'''通过执行以下命令列出容器的所有正在运行的实例及其端口映射：
                 docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ports={{ .NetworkSettings.Ports }}'
                 查看列表并确保映射的端口是容器真正需要的端口。''',
    "remediation": u'''修复容器镜像的Dockerfile以通过容器化应用程序露仅需要的端口。也可以完全忽略Dockerfile中定义的端口列表，方法是在启动容器时不要使用'-P'（大写）或'--publish all'标志。使用'-p'（小写）或'--publish'标志显式定义特定容器实例所需的端口。
                       例如：
                       docker run --interactive --tty --publish 5000 --publish 5001 --publish 5002 centos /bin/bash'''
}
reportContent['9'] = {
    "titile": u'''是否不共享主机的网络名称空间''',
    "description": u'''当容器中的网络模式设置为“--net = host”时，容器上的网络模式会跳过将容器放在单独的网络堆栈中的操作。实质上，这个行为告诉Docker不要配置容器中的网络。这在网络上意味着容器位于主Docker主机的“外部”，并且可以完全访问其网络接口。这有潜在危险。它允许容器进程像任何其他根进程一样打开低编号的端口。它还允许容器访问Docker主机上的D-bus等网络服务。因此，容器进程可能会发生意外情况，''',
    "impact": u'''None'''
}
reportContent['10'] = {
    "titile": u'''是否限制了容器的内存使用''',
    "description": u'''默认情况下，Docker主机上的所有容器均等地共享资源。 通过使用Docker主机的资源管理功能（例如内存限制），您可以控制容器可能占用的内存量。默认情况下，容器可以使用主机上的所有内存。 您可以使用内存限制机制来防止由于一个容器占用所有主机资源而导致的拒绝服务，以致同一主机上的其他容器无法执行其预期的功能。对内存没有限制可能会导致一个容器容易使整个系统不稳定并因此无法使用的问题。''',
    "impact": u'''如果您没有设置适当的限制，容器进程可能必须饿死（所有资源被其他容器进程占用导致该容器一直处于等待资源状态）。'''
}
reportContent['11'] = {
    "titile": u'''是否设置了容器的CPU使用优先级''',
    "description": u'''默认情况下，Docker主机上的所有容器均等共享资源。通过使用Docker主机的资源管理功能，例如CPU共享，您可以控制容器可能使用的主机CPU资源。''',
    "impact": u'''如果未设置正确的CPU共享，则如果主机上的资源不可用，容器进程可能必须饿死（长期等待资源分配而无法运行）。如果主机上的CPU资源是空闲的，则CPU共享不会对容器可能使用的CPU施加任何限制。'''
}
reportContent['12'] = {
    "titile": u'''是否让装载容器的根文件系统仅作为只读。''',
    "description": u'''应将容器的根文件系统视为“golden image”，并应避免对根文件系统的任何写入。应该明确定义一个用于写入的容器卷。''',
    "impact": u'''容器根文件系统不可写。 应该明确定义一个容器卷以进行写入。'''
}
reportContent['13'] = {
    "titile": u'''是否将传入的容器流量绑定到特定的主机接口''',
    "description": u'''默认情况下，Docker容器可以与外界建立连接，但外部世界无法连接到容器。每个传出连接似乎都源自主机的一个IP地址。仅允许通过主机上的特定外部接口联系容器服务。如果主机上有多个网络接口，则容器可以接受任何网络接口上公开端口上的连接，这可能是不安全的。很多时候，特定接口在外部暴露，并且在这些接口上运行诸如入侵检测，入侵防御，防火墙，负载平衡等服务以筛选传入的公共流量。 因此，不应接受任何接口上的传入连接，应该只允许来自特定外部接口的传入连接。''',
    "impact": u'''None'''
}
reportContent['14'] = {
    "titile": u'''是否将“on-failure”容器重启策略设置为5''',
    "description": u'''使用“docker run”命令中的“--restart”标志，可以指定一个在容器退出时应该或不应该重新启动的重启策略。您应该选择“on-failure”重启策略并将重启尝试次数限制为5次。''',
    "impact": u'''容器只会尝试重新启动5次。如果无限次地尝试重启容器，则可能导致主机上的拒绝服务。'''
}
reportContent['15'] = {
    "titile": u'''是否不共享主机的进程名称空间''',
    "description": u'''主机进程ID（PID）命名空间隔离容器进程ID号空间，这意味着不同PID名称空间中的进程可以具有相同的PID。这是容器和主机之间的进程级隔离。''',
    "impact": u'''容器进程无法看到主机系统上的进程。如果主机的PID命名空间与容器共享，它基本上允许容器内的进程查看主机系统上的所有进程。这打破了主机和容器之间进程级别隔离的好处。有权访问容器的人最终可以知道主机系统上运行的所有进程，甚至可以从容器内杀死主机系统进程。这可能是灾难性的。'''
}
reportContent['16'] = {
    "titile": u'''是否不共享主机的IPC名称空间''',
    "description": u'''IPC（POSIX / SysV IPC）命名空间提供命名共享内存段，信号量和消息队列的分离。因此，主机上的IPC命名空间不应与容器共享，并且应保持隔离状态。如果主机的IPC命名空间与容器共享，它基本上允许容器内的进程查看主机系统上的所有IPC。这打破了主机和容器之间IPC级隔离的好处。有权访问容器的人最终可以操纵主机IPC，这可能是灾难性的。''',
    "impact": u'''共享内存段用于加速进程间通信。它通常被高性能应用程序使用。如果将此类应用程序容器化为多个容器，则可能需要共享容器的IPC命名空间以实现高性能。在这种情况下，仍应仅共享特定于容器的IPC命名空间，而不是主机IPC命名空间'''
}
reportContent['17'] = {
    "titile": u'''是否没有直接将主机设备暴露给容器''',
    "description": u'''主机设备可以在运行时直接暴露给容器。 不要将主机设备直接暴露给容器，尤其是对于不受信任的容器。若您希望在主机中使用主机设备，可适当地使用共享权限：r-read only, w-writable, m-mknod allowed。''',
    "impact": u'''无法直接在容器中使用主机设备。'--device'选项将主机设备公开给容器，容器可以从主机移除块设备。'''
}
reportContent['18'] = {
    "titile": u'''是否在需要时在运行时覆盖默认的ulimit''',
    "description": u'''默认的ulimit是在Docker daemon程序级别设置的。如果需要，您可以在容器运行时重写默认的ulimit设置。''',
    "impact": u'''如果ulimits设置不正确，可能无法实现所需的资源控制，甚至可能导致系统无法使用。''',
    "audit": u'''docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Ulimits={{ .HostConfig.Ulimits }}'
                 上面的命令应该为每个容器实例返回Ulimits = <no value>，直到除非存在异常并且需要覆盖默认的ulimit设置。''',
    "remediation": u'''如果需要，仅覆盖默认的ulimit设置。例如，启动容器以覆盖默认的ulimit设置，如下所示：
                       docker run --ulimit nofile=1024:1024 --interactive --tty centos /bin/bash'''
}
reportContent['19'] = {
    "titile": u'''是否没有设置挂载传播模式来进行共享''',
    "description": u'''安装传播模式允许在容器上以共享，从属或私有模式安装卷。 在需要之前，请勿使用共享安装传播模式。在所有挂载中复制共享挂载，并且在任何挂载点进行的更改将传播到所有挂载。在共享模式下装入卷不会限制任何其他容器装入并对该卷进行更改。如果挂载的卷对更改敏感，这可能是灾难性的。''',
    "impact": u'''None'''
}
reportContent['20'] = {
    "titile": u'''是否没有共享主机的UTS名称空间''',
    "description": u'''UTS名称空间提供两个系统标识符的隔离：主机名和NIS域名。它用于设置主机名和该命名空间中正在运行的进程可见的域。在容器内运行的进程通常不需要知道主机名和域名。与主机共享UTS命名空间为容器提供了完全权限以更改主机的主机名，这是不安全的，不应该被允许。因此，不应与主机共享命名空间。''',
    "impact": u'''None'''
}
reportContent['21'] = {
    "titile": u'''是否没有禁用默认的seccomp配置文件''',
    "description": u'''Seccomp筛选为进程指定传入系统调用的筛选器提供了一种手段。默认的Docker seccomp配置文件基于白名单，并允许311个系统调用阻止其他所有配置。它不应该被禁用，除非它阻碍了你的容器应用程序的使用。''',
    "impact": u'''使用Docker 1.10和更高版本时，默认的seccomp配置文件会阻止系统调用，无论是否将--cap-add传递给容器。 在这种情况下，您应该创建自己的自定义seccomp配置文件。 您还可以通过在docker run上传递--security-opt = seccomp：unconfined来禁用默认的seccomp配置文件。'''
}
reportContent['22'] = {
    "titile": u'''是否不使用特权选项的docker exec命令''',
    "description": u'''不要使用--privileged选项执行docker exec。在docker exec中使用--privileged选项可为命令提供扩展的Linux功能。这可能是不安全和不安全的，尤其是当您运行具有已删除功能或具有增强限制的容器时。''',
    "impact": u'''None'''
}
reportContent['23'] = {
    "titile": u'''是否不使用用户选项的docker exec命令''',
    "description": u'''使用--user选项不要执行docker exec。在docker exec中使用--user选项会以该用户身份执行容器内的命令。这可能是不安全和不安全的，尤其是当运行具有已删除功能或具有增强限制的容器时。''',
    "impact": u'''None'''
}
reportContent['24'] = {
    "titile": u'''确认cgroup用法''',
    "description": u'''可以在容器运行时附加到特定的cgroup。确认cgroup的使用将确保容器在定义的cgroup下运行。容器在运行时，可以连接到预期使用的cgroup以外的其他cgroup，通过附加到与预期不同的cgroup，可能会向容器授予过多的权限和资源，因此可能是不安全的。''',
    "impact": u'''None'''
}
reportContent['25'] = {
    "titile": u'''是否限制容器获得额外的特权''',
    "description": u'''限制容器通过suid或sgid位获取额外的权限。进程可以在内核中设置no_new_priv位。它持续跨越fork，clone和execve。no_new_priv位确保进程或其子进程不通过suid或sgid位获得任何其他权限。这样很多危险的操作变得没有那么危险，因为不可能破坏特权二进制文件。''',
    "impact": u'''no_new_priv阻止像SELinux这样的LSM转换为不允许访问当前进程的进程标签。''',
    "audit": u'''docker ps --quiet | xargs docker inspect --format '{{ .Id }}: SecurityOpt={{ .HostConfig.SecurityOpt }}'
                 以上命令应返回当前为容器配置的所有安全选项。no-new-privileges 也应该是其中之一。''',
    "remediation": u'''如下所示启动容器：
                       docker run <run-options> --security-opt=no-new-privileges <IMAGE> <CMD>
                       例如：
                       docker run --rm -it --security-opt=no-new-privileges ubuntu bash'''
}
reportContent['26'] = {
    "titile": u'''是否在运行时检查容器的健康状况''',
    "description": u'''如果容器映像没有定义HEALTHCHECK指令，请在容器运行时使用--health-cmd参数来检查容器运行状况。''',
    "impact": u'''None''',
    "audit": u'''运行以下命令并确保所有容器都报告运行状况：
                 docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Health={{ .State.Health.Status }}' ''',
    "remediation": u'''使用--health-cmd和其他参数运行容器。例如，运行以下命令：
                       docker run -d --health-cmd='stat /etc/passwd || exit 1' nginx'''
}
reportContent['27'] = {
    "titile": u'''确保docker命令总是得到镜像的最新版本''',
    "description": u'''始终确保在存储库中使用最新版本的映像，而不是缓存的旧版本。已知多个docker命令（如docker拉出，docker运行等）存在一个问题，即默认情况下，即使在上游存储库中存在具有相同标签的镜像的更新版本，它们也会提取镜像的本地副本（如果存在）。这可能导致使用较旧且易受攻击的镜像。''',
    "impact": u'''None''',
    "audit": u'''步骤1：打开镜像库并列出要检查的镜像的版本历史记录。
                 步骤2：观察触发docker命令时的状态。例如，如果触发了docker pull <Image_ID>，请注意，如果它显示状态为Downloading，则表示镜像是最新的。如果它显示的状态为其他，则表示您正在获取镜像的缓存版本。
                 步骤3：将正在运行的镜像的版本与镜像库中报告的最新版本进行匹配，该版本告知您是在运行缓存版本还是最新版本。''',
    "remediation": u'''使用正确的版本固定机制（默认情况下分配的最新标记仍然容易受到缓存攻击），以避免提取缓存的旧版本。版本钉扎机制也应该用于基本镜像，包和整个镜像。您可以根据自己的要求自定义版本固定规则。'''

}
reportContent['28'] = {
    "titile": u'''是否使用pid cgroup限制''',
    "description": u'''在容器运行时使用--pids-limit选项.攻击者可以在容器内使用单个命令发射一个fork boom。这个fork boom可能会导致整个系统崩溃，需要重新启动主机才能使系统再次运行。 PIDs cgroup --pids-limit将通过限制在给定时间内容器内可能发生的fork数量来防止此类攻击。''',
    "impact": u'''根据需要设置PID限制值.不正确的值可能会导致容器无法使用。'''
}
reportContent['29'] = {
    "titile": u'''是否没有使用Docker的默认桥式docker0''',
    "description": u'''不要使用Docker的默认桥接docker0，使用docker的用户定义网络进行容器网络连接。Docker将在桥接模式下创建的虚拟接口连接到名为docker0的公共桥接器。此默认网络模型易受ARP欺骗和MAC泛洪攻击，因为未应用过滤。''',
    "impact": u'''必须管理用户定义的网络，防止受到ARP欺骗和MAC泛洪攻击'''
}
reportContent['30'] = {
    "titile": u'''是否不共享主机的用户名称空间''',
    "description": u'''不要将主机的用户命名空间与容器共享。用户命名空间确保容器内的根进程将映射到容器外部的非根进程。因此，与容器共享主机的用户命名空间不会将主机上的用户与容器上的用户隔离。''',
    "impact": u'''None'''
}
reportContent['31'] = {
    "titile": u'''是否没有在容器内安装Docker套接字''',
    "description": u'''docker套接字（docker.sock）不应该安装在容器内。如果docker socket安装在容器内，它将允许在容器内运行的进程执行docker命令来有效地完全控制主机。''',
    "impact": u'''None''',
    "audit": u'''docker ps --quiet | xargs docker inspect --format '{{ .Id }}: Volumes={{ .Mounts }}' | grep docker.sock
                 上面的命令将返回docker.sock已作为卷映射到容器的任何实例。''',
    "remediation": u'''确保没有容器将docker.sock挂载为卷。'''
}
