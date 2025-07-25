# --- Код из Части 13 (создание формы и элементов) ---
# ... (весь код по созданию $mainForm, $chart, $labels, $buttons) ...

# --- НОВАЯ ЧАСТЬ: Логика приложения ---

# 1. Создание таймера
$timer = New-Object -TypeName System.Windows.Forms.Timer
$timer.Interval = 1000 # Интервал в миллисекундах (1000 мс = 1 секунда)

# 2. Создание обработчика события Tick для таймера
$timer.add_Tick({
    # Этот блок кода будет выполняться каждую секунду, пока таймер запущен

    # 2.1 Получаем текущее значение загрузки CPU
    $cpuValue = (Get-Counter -Counter "\Processor(_Total)\% Processor Time").CounterSamples.CookedValue
    # Округляем до целого числа
    $cpuValue = [math]::Round($cpuValue)

    # 2.2 Обновляем большую текстовую метку
    $cpuLabel.Text = "$cpuValue %"

    # 2.3 Добавляем новую точку на график
    # .Points - это коллекция точек данных для нашего ряда
    $chart.Series["CPU"].Points.AddY($cpuValue)

    # 2.4 Управляем количеством точек на графике, чтобы он не переполнялся
    # Если точек стало больше 60, удаляем самую старую (первую)
    if ($chart.Series["CPU"].Points.Count -gt 60) {
        $chart.Series["CPU"].Points.RemoveAt(0)
    }
})

# 3. Программирование логики кнопки "Старт"
$startButton.add_Click({
    # Запускаем таймер
    $timer.Start()

    # Обновляем состояние интерфейса
    $startButton.Enabled = $false
    $stopButton.Enabled = $true
    $statusLabel.Text = "Мониторинг запущен..."
})

# 4. Программирование логики кнопки "Стоп"
$stopButton.add_Click({
    # Останавливаем таймер
    $timer.Stop()

    # Обновляем состояние интерфейса
    $startButton.Enabled = $true
    $stopButton.Enabled = $false
    $statusLabel.Text = "Остановлено. Готов к запуску..."
})

# 5. Дополнительная логика: что делать при закрытии окна?
# Если пользователь закроет окно, а таймер будет работать,
# процесс PowerShell может остаться "висеть" в памяти.
# Поэтому при закрытии формы нам нужно убедиться, что таймер остановлен.
$mainForm.add_FormClosing({
    $timer.Stop()
})

# --- Конец новой части ---

# --- Отображение окна ---
[void]$mainForm.ShowDialog()