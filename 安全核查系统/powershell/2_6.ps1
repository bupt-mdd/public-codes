Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost | Select Name, @{N="Net.DVFilterBindIpAddress";E={$_ | GetVMHostAdvancedConfiguration Net.DVFilterBindIpAddress | Select -ExpandProperty Values}}
