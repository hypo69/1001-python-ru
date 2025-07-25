# --- 1. Создание главного окна ---
$mainForm = New-Object -TypeName System.Windows.Forms.Form
$mainForm.Text = "CPU-Монитор на PowerShell"
$mainForm.Size = New-Object -TypeName System.Drawing.Size(800, 600) # Задаем размер через объект Size
$mainForm.StartPosition = "CenterScreen"
$mainForm.FormBorderStyle = "FixedSingle" # Запрещаем изменять размер окна
$mainForm.MaximizeBox = $false # Отключаем кнопку "Развернуть"

# --- 2. Создание области для графика (Chart) ---
$chart = New-Object -TypeName System.Windows.Forms.DataVisualization.Charting.Chart
$chart.Location = New-Object -TypeName System.Drawing.Point(20, 20)
$chart.Size = New-Object -TypeName System.Drawing.Size(740, 400)
$chart.Anchor = "Top, Left, Right" # "Привязываем" график к краям окна

# --- 2.1 Настройка внутреннего содержимого графика ---
# ChartArea - это "холст", на котором рисуется график.
$chartArea = New-Object -TypeName System.Windows.Forms.DataVisualization.Charting.ChartArea
$chartArea.AxisX.MajorGrid.Enabled = $false # Отключаем вертикальную сетку
$chartArea.AxisY.MajorGrid.LineDashStyle = "Dot" # Делаем горизонтальную сетку пунктирной
$chartArea.AxisY.Minimum = 0 # Ось Y всегда начинается с 0
$chartArea.AxisY.Maximum = 100 # и заканчивается на 100 (%)
$chart.ChartAreas.Add($chartArea)

# Series - это сам набор данных (линия, столбцы и т.д.)
$chartSeries = New-Object -TypeName System.Windows.Forms.DataVisualization.Charting.Series
$chartSeries.Name = "CPU"
$chartSeries.ChartType = "Line" # Тип графика - линия
$chartSeries.BorderWidth = 3 # Толщина линии
$chart.Series.Add($chartSeries)

# --- 3. Создание метки для текущего значения CPU ---
$cpuLabel = New-Object -TypeName System.Windows.Forms.Label
$cpuLabel.Text = "0 %"
$cpuLabel.Location = New-Object -TypeName System.Drawing.Point(20, 450)
$cpuLabel.Font = New-Object -TypeName System.Drawing.Font("Segoe UI", 36, "Bold") # Задаем шрифт, размер, стиль
$cpuLabel.AutoSize = $true

# --- 4. Создание кнопок "Старт" и "Стоп" ---
$startButton = New-Object -TypeName System.Windows.Forms.Button
$startButton.Text = "Старт"
$startButton.Location = New-Object -TypeName System.Drawing.Point(550, 460)
$startButton.Size = New-Object -TypeName System.Drawing.Size(100, 40)
$startButton.Font = New-Object -TypeName System.Drawing.Font("Segoe UI", 12)

$stopButton = New-Object -TypeName System.Windows.Forms.Button
$stopButton.Text = "Стоп"
$stopButton.Location = New-Object -TypeName System.Drawing.Point(660, 460)
$stopButton.Size = New-Object -TypeName System.Drawing.Size(100, 40)
$stopButton.Font = New-Object -TypeName System.Drawing.Font("Segoe UI", 12)
$stopButton.Enabled = $false # Изначально кнопка "Стоп" неактивна

# --- 5. Создание метки-статуса ---
$statusLabel = New-Object -TypeName System.Windows.Forms.Label
$statusLabel.Text = "Готов к запуску..."
$statusLabel.Location = New-Object -TypeName System.Drawing.Point(20, 530)
$statusLabel.AutoSize = $true
$statusLabel.Anchor = "Bottom, Left" # Привязываем к левому нижнему углу

# --- 6. Добавление всех элементов на форму ---
$mainForm.Controls.AddRange(@($chart, $cpuLabel, $startButton, $stopButton, $statusLabel))

# --- 7. Отображение окна ---
[void]$mainForm.ShowDialog() # [void] подавляет вывод ненужной информации в консоль