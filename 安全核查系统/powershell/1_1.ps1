Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Foreach ($VMHost in Get-VMHost ) {
$ESXCli = Get-EsxCli -VMHost $VMHost;
$ESXCli.software.vib.list() | Select-Object @{N="VMHost";E={$VMHost}}, Name,
AcceptanceLevel, CreationDate, ID, InstallDate, Status, Vendor, Version;
}

