Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost | Get-VMHostHba | Where {$_.Type -eq "Iscsi"} | Select VMHost, Device,
ChapType, @{N="CHAPName";E={$_.AuthenticationProperties.ChapName}}
