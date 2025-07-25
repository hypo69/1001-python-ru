# Получаем объект службы
$serviceName = "Spooler"
$serviceObject = Get-Service -Name $serviceName -ErrorAction SilentlyContinue

# -ErrorAction SilentlyContinue нужен, чтобы скрипт не остановился с ошибкой, если служба вообще не найдена

if ($serviceObject -eq $null) {
    # Условие 1: Служба не существует
    Write-Host "Служба '$serviceName' не найдена на этом компьютере." -ForegroundColor Red
}
elsif ($serviceObject.Status -eq "Running") {
    # Условие 2: Служба найдена и запущена
    Write-Host "Служба '$serviceName' находится в состоянии: $($serviceObject.Status)." -ForegroundColor Green
}
else {
    # Условие 3: Служба найдена, но не запущена (Stopped, Paused и т.д.)
    Write-Host "ВНИМАНИЕ! Служба '$serviceName' не запущена. Текущий статус: $($serviceObject.Status)." -ForegroundColor Yellow
}