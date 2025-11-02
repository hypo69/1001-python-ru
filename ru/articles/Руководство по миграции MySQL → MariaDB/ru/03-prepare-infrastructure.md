# ГЛАВА 3: Подготовка инфраструктуры

> **Цель главы:** Подготовить систему к установке MariaDB

[← Предыдущая глава](./02-backup.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./04-install-mariadb.md)

---

## Содержание главы

1. [Остановка MySQL сервисов](#1-остановка-mysql-сервисов)
2. [Удаление или отключение MySQL](#2-удаление-или-отключение-mysql)
3. [Добавление репозитория MariaDB](#3-добавление-репозитория-mariadb)
4. [Установка зависимостей](#4-установка-зависимостей)
5. [Подготовка файловой системы](#5-подготовка-файловой-системы)
6. [Настройка системных лимитов](#6-настройка-системных-лимитов)
7. [Настройка сети и firewall](#7-настройка-сети-и-firewall)
8. [Проверка готовности системы](#8-проверка-готовности-системы)

---

## 1. Остановка MySQL сервисов

### 1.1 Проверка активных подключений

```bash
# Список активных подключений
mysql -u root -p -e "SHOW PROCESSLIST;"

# Количество подключений
mysql -u root -p -e "SHOW STATUS LIKE 'Threads_connected';"

# Детальная информация
mysql -u root -p -e "
SELECT 
    user,
    host,
    db,
    command,
    time,
    state
FROM information_schema.processlist
WHERE command != 'Sleep'
ORDER BY time DESC;"
```

### 1.2 Оповещение приложений

```bash
#!/bin/bash
# notify_maintenance.sh

echo "[$(date)] Setting MySQL to read-only mode..."

# Установить режим read-only
mysql -u root -p -e "SET GLOBAL read_only = ON;"
mysql -u root -p -e "SET GLOBAL super_read_only = ON;"

echo "MySQL now in read-only mode"
echo "Waiting 30 seconds for applications to complete..."

# Подождать завершения активных транзакций
sleep 30

# Проверить активные транзакции
ACTIVE_TRX=$(mysql -u root -p -N -e "
    SELECT COUNT(*) 
    FROM information_schema.innodb_trx;")

if [ "$ACTIVE_TRX" -gt 0 ]; then
    echo "⚠️  Warning: $ACTIVE_TRX active transactions still running"
    mysql -u root -p -e "SELECT * FROM information_schema.innodb_trx\G"
else
    echo "✅ No active transactions"
fi
```

### 1.3 Graceful shutdown

```bash
#!/bin/bash
# graceful_shutdown.sh

echo "[$(date)] Stopping MySQL gracefully..."

# Остановка сервиса
sudo systemctl stop mysql

# Ждать завершения
sleep 5

# Проверка остановки
if systemctl is-active --quiet mysql; then
    echo "❌ MySQL still running, forcing stop..."
    sudo systemctl kill mysql
    sleep 3
fi

# Проверка процессов
if ps aux | grep -v grep | grep mysqld; then
    echo "❌ MySQL processes still exist!"
    exit 1
else
    echo "✅ MySQL stopped successfully"
fi

# Проверка портов
if sudo netstat -tlnp | grep 3306; then
    echo "❌ Port 3306 still in use!"
else
    echo "✅ Port 3306 is free"
fi
```

### 1.4 Финальный snapshot данных

```bash
#!/bin/bash
# final_snapshot.sh

SNAPSHOT_DIR="/backup/mysql_final_snapshot"
DATE=$(date +%Y%m%d_%H%M%S)

echo "[$(date)] Creating final snapshot..."

# Создать snapshot данных
sudo rsync -av --progress \
    /var/lib/mysql/ \
    "$SNAPSHOT_DIR/data_$DATE/"

# Snapshot логов
sudo rsync -av \
    /var/log/mysql/ \
    "$SNAPSHOT_DIR/logs_$DATE/"

echo "[$(date)] Snapshot completed: $SNAPSHOT_DIR"
```

---

## 2. Удаление или отключение MySQL

### 2.1 Вариант A: Полное удаление (чистая установка)

```bash
#!/bin/bash
# remove_mysql.sh

echo "⚠️  WARNING: This will remove MySQL completely!"
read -p "Are you sure? (yes/no): " CONFIRM

if [ "$CONFIRM" != "yes" ]; then
    echo "Aborted"
    exit 1
fi

# Ubuntu/Debian
sudo apt remove --purge mysql-server mysql-client mysql-common -y
sudo apt autoremove -y
sudo apt autoclean -y

# Удаление конфигов (опционально - ОСТОРОЖНО!)
read -p "Remove configs? This will delete /etc/mysql/ (yes/no): " REMOVE_CONF
if [ "$REMOVE_CONF" = "yes" ]; then
    sudo rm -rf /etc/mysql/
fi

# Удаление данных (ОЧЕНЬ ОСТОРОЖНО!)
read -p "Remove data? This will delete /var/lib/mysql/ (yes/no): " REMOVE_DATA
if [ "$REMOVE_DATA" = "yes" ]; then
    sudo rm -rf /var/lib/mysql/
fi

# Удаление пользователя и группы
sudo deluser mysql 2>/dev/null
sudo delgroup mysql 2>/dev/null

echo "✅ MySQL removed"
```

**⚠️ КРИТИЧЕСКИ ВАЖНО:** 
- НЕ удаляйте `/var/lib/mysql/` если планируете in-place upgrade
- Убедитесь, что бэкапы созданы и проверены!

### 2.2 Вариант B: Отключение без удаления

```bash
#!/bin/bash
# disable_mysql.sh

echo "[$(date)] Disabling MySQL without removal..."

# Остановить и отключить автозапуск
sudo systemctl stop mysql
sudo systemctl disable mysql

# Переименовать исполняемые файлы (для безопасности)
sudo mv /usr/bin/mysql /usr/bin/mysql.disabled
sudo mv /usr/sbin/mysqld /usr/sbin/mysqld.disabled

echo "✅ MySQL disabled"
echo "To re-enable: mv /usr/bin/mysql.disabled /usr/bin/mysql"
```

### 2.3 Вариант C: In-place upgrade (рекомендуется)

```bash
#!/bin/bash
# prepare_inplace_upgrade.sh

echo "[$(date)] Preparing for in-place upgrade..."

# Только остановить MySQL, НЕ удалять
sudo systemctl stop mysql
sudo systemctl disable mysql

# Создать маркер
sudo touch /var/lib/mysql/.mariadb_upgrade_in_progress

# НЕ удалять:
# - /var/lib/mysql/ (данные)
# - /etc/mysql/ (конфиги)
# - Пакеты MySQL

echo "✅ Ready for in-place upgrade"
echo "MariaDB will migrate data automatically"
```

---

## 3. Добавление репозитория MariaDB

### 3.1 Автоматическая настройка (рекомендуется)

```bash
#!/bin/bash
# setup_mariadb_repo.sh

echo "[$(date)] Setting up MariaDB repository..."

# Официальный скрипт MariaDB Foundation
curl -LsS https://r.mariadb.com/downloads/mariadb_repo_setup | sudo bash

if [ $? -eq 0 ]; then
    echo "✅ MariaDB repository configured"
    apt-cache policy mariadb-server
else
    echo "❌ Repository setup failed!"
    exit 1
fi
```

### 3.2 Ручная настройка (Ubuntu 22.04)

```bash
#!/bin/bash
# manual_repo_setup.sh

# Установить prerequisites
sudo apt install -y \
    software-properties-common \
    dirmngr \
    apt-transport-https \
    ca-certificates \
    gnupg

# Добавить GPG ключ
sudo mkdir -p /etc/apt/keyrings
curl -o /etc/apt/keyrings/mariadb-keyring.pgp \
    'https://mariadb.org/mariadb_release_signing_key.pgp'

# Добавить репозиторий MariaDB 10.11 (LTS)
sudo tee /etc/apt/sources.list.d/mariadb.list << EOF
# MariaDB 10.11 LTS Repository
deb [signed-by=/etc/apt/keyrings/mariadb-keyring.pgp] https://mirror.mephi.ru/mariadb/repo/10.11/ubuntu jammy main
EOF

# Обновить списки пакетов
sudo apt update

echo "✅ MariaDB repository added"
```

### 3.3 Выбор версии MariaDB

| Версия | Статус | Поддержка до | Использование |
|--------|--------|--------------|---------------|
| **10.6** | LTS | 2026-07 | Production (стабильная) |
| **10.11** | LTS | 2028-02 | **Рекомендуется** |
| **11.0** | Stable | 2024-06 | Short-term |
| **11.4** | LTS | 2029-05 | Production (новейшая) |

**Рекомендация:** Используйте MariaDB 10.11 для максимальной стабильности и долгосрочной поддержки.

```bash
# Для установки конкретной версии
sudo apt install mariadb-server-10.11
```

---

## 4. Установка зависимостей

### 4.1 Системные зависимости

```bash
#!/bin/bash
# install_dependencies.sh

echo "[$(date)] Installing system dependencies..."

sudo apt update

# Основные зависимости
sudo apt install -y \
    software-properties-common \
    dirmngr \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release \
    wget \
    curl

# Дополнительные утилиты
sudo apt install -y \
    mytop \
    percona-toolkit \
    sysbench \
    htop \
    iotop \
    nethogs \
    net-tools \
    rsync \
    gzip \
    pigz

echo "✅ Dependencies installed"
```

---

## 5. Подготовка файловой системы

### 5.1 Создание структуры каталогов

```bash
#!/bin/bash
# prepare_filesystem.sh

echo "[$(date)] Preparing filesystem..."

# Основные директории
sudo mkdir -p /var/lib/mysql
sudo mkdir -p /var/log/mariadb
sudo mkdir -p /var/run/mysqld
sudo mkdir -p /etc/mysql/mariadb.conf.d

# Установить владельца
sudo chown -R mysql:mysql /var/lib/mysql 2>/dev/null || true
sudo chown -R mysql:mysql /var/log/mariadb
sudo chown -R mysql:mysql /var/run/mysqld

# Установить права
sudo chmod 750 /var/lib/mysql
sudo chmod 755 /var/log/mariadb
sudo chmod 755 /var/run/mysqld

echo "✅ Filesystem prepared"
```

### 5.2 Оптимизация файловой системы

```bash
# Для production рекомендуется XFS или ext4

# Проверить текущую ФС
df -Th /var/lib/mysql

# Для XFS (лучшая производительность)
sudo mkfs.xfs -f /dev/sdb1
sudo mount -o noatime,nodiratime,nobarrier /dev/sdb1 /var/lib/mysql

# Для ext4
sudo tune2fs -o journal_data_writeback /dev/sdb1
sudo mount -o noatime,nodiratime,data=writeback /dev/sdb1 /var/lib/mysql

# Добавить в /etc/fstab
echo "/dev/sdb1 /var/lib/mysql xfs noatime,nodiratime,nobarrier 0 0" | \
    sudo tee -a /etc/fstab
```

### 5.3 Настройка swap (если требуется)

```bash
#!/bin/bash
# configure_swap.sh

# Проверить текущий swap
free -h

# Если swap отсутствует или мал, создать swap файл
SWAP_SIZE="8G"  # Измените на нужный размер

sudo fallocate -l $SWAP_SIZE /swapfile
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile

# Добавить в /etc/fstab
echo '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab

# Настроить swappiness (меньше = меньше swap)
sudo sysctl vm.swappiness=10
echo 'vm.swappiness=10' | sudo tee -a /etc/sysctl.conf

echo "✅ Swap configured: $SWAP_SIZE"
free -h
```

---

## 6. Настройка системных лимитов

### 6.1 Увеличение лимитов для MySQL

```bash
#!/bin/bash
# configure_limits.sh

# Создать файл лимитов
sudo tee /etc/security/limits.d/mysql.conf << EOF
# MySQL/MariaDB system limits
mysql soft nofile 65535
mysql hard nofile 65535
mysql soft nproc 65535
mysql hard nproc 65535
mysql soft memlock unlimited
mysql hard memlock unlimited
EOF

echo "✅ System limits configured"
```

### 6.2 Настройка systemd лимитов

```bash
#!/bin/bash
# configure_systemd_limits.sh

# Создать override для MariaDB service
sudo mkdir -p /etc/systemd/system/mariadb.service.d/

sudo tee /etc/systemd/system/mariadb.service.d/limits.conf << EOF
[Service]
LimitNOFILE=infinity
LimitMEMLOCK=infinity
LimitNPROC=infinity
EOF

# Перезагрузить systemd
sudo systemctl daemon-reload

echo "✅ Systemd limits configured"
```

### 6.3 Оптимизация kernel параметров

```bash
#!/bin/bash
# optimize_kernel.sh

sudo tee -a /etc/sysctl.conf << EOF

# === MariaDB Kernel Optimization ===

# Увеличить лимит файловых дескрипторов
fs.file-max = 2097152

# Сетевые оптимизации
net.core.somaxconn = 4096
net.core.netdev_max_backlog = 5000
net.ipv4.tcp_max_syn_backlog = 4096

# TCP настройки
net.ipv4.tcp_fin_timeout = 15
net.ipv4.tcp_keepalive_time = 300
net.ipv4.tcp_keepalive_probes = 5
net.ipv4.tcp_keepalive_intvl = 15

# Shared memory
kernel.shmmax = 68719476736
kernel.shmall = 4294967296

# Swappiness (меньше = меньше swap)
vm.swappiness = 10

EOF

# Применить настройки
sudo sysctl -p

echo "✅ Kernel parameters optimized"
```

---

## 7. Настройка сети и firewall

### 7.1 Firewall (UFW)

```bash
#!/bin/bash
# configure_firewall_ufw.sh

echo "[$(date)] Configuring UFW firewall..."

# Разрешить SSH (важно!)
sudo ufw allow 22/tcp

# Разрешить MariaDB только с определенных сетей
sudo ufw allow from 192.168.1.0/24 to any port 3306 proto tcp comment 'MariaDB'

# Или с конкретных хостов
sudo ufw allow from 192.168.1.100 to any port 3306 proto tcp comment 'App Server 1'
sudo ufw allow from 192.168.1.101 to any port 3306 proto tcp comment 'App Server 2'

# Включить firewall
sudo ufw --force enable

# Проверить правила
sudo ufw status numbered

echo "✅ Firewall configured"
```

### 7.2 Firewall (iptables)

```bash
#!/bin/bash
# configure_firewall_iptables.sh

# Разрешить MariaDB с определенной сети
sudo iptables -A INPUT -p tcp -s 192.168.1.0/24 --dport 3306 \
    -m conntrack --ctstate NEW,ESTABLISHED -j ACCEPT

# Блокировать все остальные подключения к порту 3306
sudo iptables -A INPUT -p tcp --dport 3306 -j DROP

# Сохранить правила
sudo iptables-save | sudo tee /etc/iptables/rules.v4

echo "✅ iptables configured"
```

---

## 8. Проверка готовности системы

### 8.1 Комплексная проверка

```bash
#!/bin/bash
# system_readiness_check.sh

echo "===== MariaDB Migration Readiness Check ====="

# 1. Дисковое пространство
echo -e "\n1. Disk Space:"
df -h /var/lib/mysql

AVAILABLE_GB=$(df -BG /var/lib/mysql | tail -1 | awk '{print $4}' | sed 's/G//')
if [ "$AVAILABLE_GB" -lt 50 ]; then
    echo "⚠️  Warning: Less than 50GB available"
else
    echo "✅ Sufficient disk space ($AVAILABLE_GB GB)"
fi

# 2. Память
echo -e "\n2. Memory:"
free -h

TOTAL_RAM_GB=$(free -g | grep Mem | awk '{print $2}')
if [ "$TOTAL_RAM_GB" -lt 4 ]; then
    echo "⚠️  Warning: Less than 4GB RAM"
else
    echo "✅ Sufficient RAM ($TOTAL_RAM_GB GB)"
fi

# 3. Порт 3306
echo -e "\n3. Port 3306:"
if sudo netstat -tlnp | grep -q ':3306'; then
    echo "❌ Port 3306 is ALREADY IN USE!"
    sudo netstat -tlnp | grep ':3306'
else
    echo "✅ Port 3306 is available"
fi

# 4. Репозиторий MariaDB
echo -e "\n4. MariaDB Repository:"
if apt-cache policy mariadb-server | grep -q 'mariadb.org'; then
    echo "✅ MariaDB repository configured"
    apt-cache policy mariadb-server | grep -A1 "Candidate:"
else
    echo "❌ MariaDB repository NOT found"
fi

# 5. Бэкапы
echo -e "\n5. Backup Verification:"
BACKUP_COUNT=$(find /backup/mysql -name "*.sql.gz" -type f 2>/dev/null | wc -l)
if [ "$BACKUP_COUNT" -gt 0 ]; then
    echo "✅ Found $BACKUP_COUNT backup(s)"
    ls -lht /backup/mysql/*.sql.gz 2>/dev/null | head -3
else
    echo "❌ No backups found in /backup/mysql/"
fi

# 6. Системные лимиты
echo -e "\n6. System Limits:"
if [ "$(ulimit -n)" -ge 65535 ]; then
    echo "✅ Open files limit OK ($(ulimit -n))"
else
    echo "⚠️  Warning: Open files limit too low ($(ulimit -n))"
fi

# 7. MySQL статус
echo -e "\n7. MySQL Status:"
if systemctl is-active --quiet mysql 2>/dev/null; then
    echo "⚠️  WARNING: MySQL is still running!"
    echo "Run: sudo systemctl stop mysql"
else
    echo "✅ MySQL is stopped"
fi

# 8. Зависимости
echo -e "\n8. Dependencies:"
MISSING=0
for pkg in curl wget rsync gzip; do
    if ! command -v $pkg &> /dev/null; then
        echo "❌ Missing: $pkg"
        MISSING=$((MISSING + 1))
    fi
done

if [ $MISSING -eq 0 ]; then
    echo "✅ All dependencies installed"
fi

echo -e "\n===== Check Complete ====="

# Финальная рекомендация
echo -e "\nSystem Status:"
if [ "$AVAILABLE_GB" -ge 50 ] && [ "$TOTAL_RAM_GB" -ge 4 ] && \
   [ "$BACKUP_COUNT" -gt 0 ] && [ $MISSING -eq 0 ]; then
    echo "✅ System is READY for MariaDB installation"
    exit 0
else
    echo "⚠️  System has warnings. Review above and fix issues."
    exit 1
fi
```

---

## Чек-лист выполнения главы

### ✅ Обязательные действия

- [ ] MySQL сервис остановлен
- [ ] MySQL отключен/удален (выбран метод)
- [ ] Репозиторий MariaDB добавлен
- [ ] Зависимости установлены
- [ ] Файловая система подготовлена
- [ ] Системные лимиты настроены
- [ ] Firewall настроен
- [ ] Проверка готовности пройдена
- [ ] Порт 3306 свободен
- [ ] Достаточно дискового пространства (минимум 50GB)
- [ ] Достаточно RAM (минимум 4GB)

### 📋 Конфигурации

| Параметр | Значение | Статус |
|----------|----------|--------|
| Open files limit | 65535 | ☐ |
| Swap size | 8GB | ☐ |
| vm.swappiness | 10 | ☐ |
| Firewall rules | Configured | ☐ |
| MariaDB repo | Added | ☐ |

---

## Следующий шаг

После успешной подготовки системы переходите к:

**[→ ГЛАВА 4: Установка MariaDB Server](./04-install-mariadb.md)**

В следующей главе:
- Установка пакетов MariaDB
- Первый запуск
- Базовая конфигурация
- Настройка root доступа
