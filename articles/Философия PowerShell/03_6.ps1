# Создать новую папку и сразу же перейти в нее
$newFolder = New-Item -Path C:\Temp\MyNewFolder -ItemType Directory
Set-Location -Path $newFolder.FullName