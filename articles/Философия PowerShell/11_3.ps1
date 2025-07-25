$computers = "SERVER01", "SERVER02", "LAB03"
Invoke-Command -ComputerName $computers -ScriptBlock {
    [PSCustomObject]@{
        OS = (Get-CimInstance Win32_OperatingSystem).Caption
        PSVersion = $PSVersionTable.PSVersion.ToString()
    }
} | Select-Object PSComputerName, OS, PSVersion