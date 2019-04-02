Connect-VIServer -Server $args[0] -User $args[1] -Password $args[2]
Get-VirtualSwitch -Standard | Select VMHost, Name, `
@{N="MacChanges";E={if ($_.ExtensionData.Spec.Policy.Security.MacChanges) { "Accept" }
Else { "Reject"} }}, `
@{N="PromiscuousMode";E={if ($_.ExtensionData.Spec.Policy.Security.PromiscuousMode) {
"Accept" } Else { "Reject"} }},@{N="ForgedTransmits";E={if ($_.ExtensionData.Spec.Policy.Security.ForgedTransmits) {
"Accept" } Else { "Reject"} }}
