# Сначала сортируем по возрастанию времени создания, затем берем последние 5
Get-ChildItem -File | Sort-Object -Property CreationTime | Select-Object -Last 5