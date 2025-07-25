$serviceName = "WinRM"
$computers = "SERVER01", "SERVER02"

Invoke-Command -ComputerName $computers -ScriptBlock {
    Get-Service -Name $using:serviceName
}