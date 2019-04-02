Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost | Select Name,@{N="Lockdown";E={$_.Extensiondata.Config.adminDisabled}}
