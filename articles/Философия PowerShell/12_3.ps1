# --- Шаги 1 и 2 из предыдущего примера ---
Add-Type -AssemblyName System.Windows.Forms
$mainForm = New-Object -TypeName System.Windows.Forms.Form
$mainForm.Text = "Интерактивное приложение"
$mainForm.Width = 400
$mainForm.Height = 300
$mainForm.StartPosition = "CenterScreen"

# --- Создаем и настраиваем метку (Label) ---
$infoLabel = New-Object -TypeName System.Windows.Forms.Label
$infoLabel.Text = "Нажмите на кнопку, чтобы увидеть магию!"
$infoLabel.Location = New-Object -TypeName System.Drawing.Point(20, 30) # Координаты X, Y от левого верхнего угла
$infoLabel.AutoSize = $true # Автоматически подбирать размер под текст
$infoLabel.Font = "Arial, 12" # Задаем шрифт и размер

# --- Создаем и настраиваем кнопку (Button) ---
$actionButton = New-Object -TypeName System.Windows.Forms.Button
$actionButton.Text = "Нажми меня!"
$actionButton.Location = New-Object -TypeName System.Drawing.Point(120, 80)
$actionButton.Width = 150
$actionButton.Height = 40

# --- Добавляем созданные элементы на форму ---
# У каждой формы есть коллекция Controls, куда нужно добавлять дочерние элементы.
$mainForm.Controls.Add($infoLabel)
$mainForm.Controls.Add($actionButton)

# --- Отображаем окно ---
$mainForm.ShowDialog()