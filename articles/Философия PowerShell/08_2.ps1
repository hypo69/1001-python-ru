function Show-Greeting {
    param (
        $Name # Простейшее объявление параметра
    )
    Write-Host "Hello, $Name!"
}

# Вызов функции с параметром
Show-Greeting -Name "Alex"