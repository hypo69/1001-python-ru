$oneHourAgo = (Get-Date).AddHours(-1)
Get-Process | Where-Object { $_.StartTime -gt $oneHourAgo }