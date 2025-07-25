# Найти все Windows-серверы, принадлежащие IT-отделу
$serverObjects | Where-Object { ($_.OS -eq "Windows") -and ($_.Owner -eq "IT-Dept") }