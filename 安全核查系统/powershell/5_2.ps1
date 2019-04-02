Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost | Get-VMHostService | Where { $_.key -eq "TSM" } | Select VMHost, Key, Label, Policy, Running, Required

