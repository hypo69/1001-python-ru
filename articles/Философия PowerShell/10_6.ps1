# PowerShell может запросить подтверждение на установку из "недоверенного" репозитория.
# Это нормально для PSGallery.
Install-Module -Name "BurntToast" -Scope CurrentUser
# -Scope CurrentUser устанавливает модуль только для вас и не требует прав администратора.