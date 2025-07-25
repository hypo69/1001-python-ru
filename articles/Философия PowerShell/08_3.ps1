function Get-RemoteServiceStatus {
    [CmdletBinding(SupportsShouldProcess = $true, ConfirmImpact = 'Medium')]
    <#
    .SYNOPSIS
        Получает статус службы на удаленном или локальном компьютере.
    .DESCRIPTION
        Эта функция использует Invoke-Command для подключения к удаленной машине и
        получения информации о конкретной службе.
    .PARAMETER ComputerName
        Имя компьютера, к которому нужно подключиться. По умолчанию - локальный компьютер.
    .PARAMETER ServiceName
        Имя службы, статус которой нужно проверить.
    .EXAMPLE
        Get-RemoteServiceStatus -ComputerName SERVER01 -ServiceName Spooler
    .EXAMPLE
        'SERVER01', 'SERVER02' | Get-RemoteServiceStatus -ServiceName WinRM
    #>
    param (
        [Parameter(ValueFromPipeline = $true,
                   ValueFromPipelineByPropertyName = $true,
                   Position = 0)]
        [string]$ComputerName = $env:COMPUTERNAME,

        [Parameter(Mandatory = $true,
                   Position = 1)]
        [string]$ServiceName
    )

    # Блоки Begin, Process, End
    begin {
        Write-Verbose "Начинаем обработку. Целевая служба: $ServiceName"
    }

    process {
        foreach ($computer in $ComputerName) {
            Write-Verbose "Подключаемся к $computer..."

            if ($PSCmdlet.ShouldProcess($computer, "Получение статуса службы '$ServiceName'")) {
                try {
                    $result = Invoke-Command -ComputerName $computer -ScriptBlock {
                        # $using:ServiceName - передача локальной переменной в удаленный сеанс
                        Get-Service -Name $using:ServiceName -ErrorAction Stop
                    }
                    # Возвращаем кастомный объект с нужной информацией
                    [PSCustomObject]@{
                        ComputerName = $computer
                        ServiceName  = $result.Name
                        Status       = $result.Status
                        DisplayName  = $result.DisplayName
                    }
                }
                catch {
                    Write-Error "Не удалось получить статус службы на $computer. Ошибка: $_"
                }
            }
        }
    }

    end {
        Write-Verbose "Обработка завершена."
    }
}