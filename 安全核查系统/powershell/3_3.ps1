Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost | Select Name, @{N="Syslog.global.logHost";E={$_ | GetVMHostAdvancedConfiguration Syslog.global.logHost | Select -ExpandProperty Values}}
