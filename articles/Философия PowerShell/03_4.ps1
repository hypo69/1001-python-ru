# Получим содержимое папки C:\Windows
$items = Get-ChildItem -Path C:\Windows

# Посмотрим, сколько объектов каждого типа мы получили
$items | Group-Object -Property {$_.GetType().Name}