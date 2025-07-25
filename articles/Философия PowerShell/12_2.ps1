# 1. Загружаем библиотеку
Add-Type -AssemblyName System.Windows.Forms

# 2. Создаем главный объект - нашу форму (окно)
$mainForm = New-Object -TypeName System.Windows.Forms.Form

# 3. Настраиваем свойства формы
$mainForm.Text = "Мое первое приложение на PowerShell" # Заголовок окна
$mainForm.Width = 400  # Ширина в пикселях
$mainForm.Height = 300 # Высота в пикселях
$mainForm.StartPosition = "CenterScreen" # Позиция окна при запуске

# 4. Отображаем окно
# Метод ShowDialog() делает окно модальным - он блокирует консоль,
# пока окно не будет закрыто. Это стандартный способ запуска простых форм.
$mainForm.ShowDialog()