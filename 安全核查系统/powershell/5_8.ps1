Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost | Select Name, @{N="UserVars.ESXiShellTimeOut";E={$_ | GetVMHostAdvancedConfiguration UserVars.ESXiShellTimeOut | Select -ExpandProperty Values}}
