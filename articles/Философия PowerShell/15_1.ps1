# Обновленный обработчик события Tick для таймера
$timer.add_Tick({
    try {
        # Код, который может вызвать ошибку, помещаем в блок try
        $cpuValue = (Get-Counter -Counter "\Processor(_Total)\% Processor Time" -ErrorAction Stop).CounterSamples.CookedValue
        $cpuValue = [math]::Round($cpuValue)

        # Обновляем интерфейс только если данные успешно получены
        $cpuLabel.Text = "$cpuValue %"
        $chart.Series["CPU"].Points.AddY($cpuValue)

        if ($chart.Series["CPU"].Points.Count -gt 60) {
            $chart.Series["CPU"].Points.RemoveAt(0)
        }
        # Если все хорошо, убедимся, что статус-метка не показывает ошибку
        if ($statusLabel.ForeColor -eq "Red") {
             $statusLabel.Text = "Мониторинг запущен..."
             $statusLabel.ForeColor = "Black"
        }
    }
    catch {
        # Этот блок выполнится, если Get-Counter выдаст ошибку
        $statusLabel.Text = "Ошибка: Не удалось получить данные счетчика CPU. ($_)"
        $statusLabel.ForeColor = [System.Drawing.Color]::Red # Выделяем ошибку красным цветом
    }
})