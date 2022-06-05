# Запуск окна
vmconnect.exe localhost "Ubuntu 18.04 LTS"
# Задержка
Wait-Event -Timeout 1
# Запуск виртуальной машины
Start-VM -Name "Ubuntu 18.04 LTS"