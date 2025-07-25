$yesterday = (Get-Date).AddDays(-1)
Get-WinEvent -LogName System | Where-Object { ($_.TimeCreated -ge $yesterday) -and ($_.LevelDisplayName -ne "Information") }