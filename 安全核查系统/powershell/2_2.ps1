Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VMHost $args[0] | Get-VMHostFirewallException | Where {$_.Enabled -and (-not $_.ExtensionData.AllowedHosts.AllIP)}

