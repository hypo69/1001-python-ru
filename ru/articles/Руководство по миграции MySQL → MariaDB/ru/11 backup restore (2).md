
# ГЛАВА 11: Резервное копирование и восстановление

> **Цель главы:** Настроить надежную систему резервного копирования

[← Предыдущая глава](./10-replication-clustering.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./12-monitoring-maintenance.md)

---

## Содержание

1. [Стратегия резервного копирования](#1-стратегия-резервного-копирования)
2. [Автоматизация с mariabackup](#2-автоматизация-с-mariabackup)
3. [Инкрементальные бэкапы](#3-инкрементальные-бэкапы)
4. [Point-in-time recovery](#4-point-in-time-recovery)
5. [Тестирование восстановления](#5-тестирование-восстановления)
6. [Disaster recovery](#6-disaster-recovery)

---

## 1. Стратегия резервного копирования

### 1.1 Правило 3-2-1

```plaintext
3 копии данных
2 различных типа носителей
1 копия off-site (удаленная)
```

### 1.2 Типы бэкапов

| Тип | Частота | Retention | Метод |
|-----|---------|-----------|-------|
| **Полный** | Воскресенье 02:00 | 4 недели | mariabackup |
| **Инкрементальный** | Ежедневно 02:00 | 7 дней | mariabackup |
| **Логический** | Ежедневно 03:00 | 7 дней | mariadb-dump |
| **Binary logs** | Постоянно | 7 дней | Копирование |

---

## 2. Автоматизация с mariabackup

### 2.1 Создание backup пользователя

```sql
CREATE USER 'backup'@'localhost' IDENTIFIED BY 'BackupPass123!';
GRANT RELOAD, PROCESS, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'backup'@'localhost';
GRANT SELECT ON mysql.* TO 'backup'@'localhost';
FLUSH PRIVILEGES;
```

### 2.2 Скрипт полного бэкапа

```bash
#!/bin/bash
# mariabackup_full.sh

BACKUP_DIR="/backup/mariabackup"
DATE=$(date +%Y%m%d_%H%M%S)
FULL_BACKUP="$BACKUP_DIR/full_$DATE"
LOG_FILE="$BACKUP_DIR/backup.log"

mkdir -p "$FULL_BACKUP"

echo "[$(date)] Starting full backup..." | tee -a "$LOG_FILE"

mariabackup \
    --backup \
    --target-dir="$FULL_BACKUP" \
    --user=backup \
    --password=BackupPass123! \
    --parallel=4 \
    --compress \
    --compress-threads=4 \
    2>&1 | tee -a "$LOG_FILE"

if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "[$(date)] Backup completed: $FULL_BACKUP" | tee -a "$LOG_FILE"
    
    # Создать маркер успешного бэкапа
    echo "$DATE" > "$BACKUP_DIR/last_full_backup.txt"
    
    # Архивирование (опционально)
    # tar -czf "${FULL_BACKUP}.tar.gz" -C "$BACKUP_DIR" "full_$DATE"
    # rm -rf "$FULL_BACKUP"
else
    echo "[$(date)] Backup FAILED!" | tee -a "$LOG_FILE"
    exit 1
fi
```

---

## 3. Инкрементальные бэкапы

### 3.1 Скрипт инкрементального бэкапа

```bash
#!/bin/bash
# mariabackup_incremental.sh

BACKUP_DIR="/backup/mariabackup"
DATE=$(date +%Y%m%d_%H%M%S)

# Найти последний полный бэкап
LAST_FULL=$(cat "$BACKUP_DIR/last_full_backup.txt")
BASE_DIR="$BACKUP_DIR/full_$LAST_FULL"

if [ ! -d "$BASE_DIR" ]; then
    echo "❌ No full backup found! Run full backup first."
    exit 1
fi

INCR_DIR="$BACKUP_DIR/incr_$DATE"

echo "[$(date)] Starting incremental backup based on: $BASE_DIR"

mariabackup \
    --backup \
    --target-dir="$INCR_DIR" \
    --incremental-basedir="$BASE_DIR" \
    --user=backup \
    --password=BackupPass123! \
    --parallel=4 \
    --compress

if [ $? -eq 0 ]; then
    echo "[$(date)] Incremental backup completed: $INCR_DIR"
    echo "$DATE" > "$BACKUP_DIR/last_incr_backup.txt"
else
    echo "[$(date)] Incremental backup FAILED!"
    exit 1
fi
```

### 3.2 Восстановление из инкрементальных бэкапов

```bash
#!/bin/bash
# restore_incremental.sh

BACKUP_DIR="/backup/mariabackup"
FULL_BACKUP="$BACKUP_DIR/full_20251101_020000"
INCR_BACKUP="$BACKUP_DIR/incr_20251102_020000"

echo "[$(date)] Preparing full backup..."
mariabackup --prepare --apply-log-only --target-dir="$FULL_BACKUP"

echo "[$(date)] Applying incremental backup..."
mariabackup \
    --prepare \
    --apply-log-only \
    --target-dir="$FULL_BACKUP" \
    --incremental-dir="$INCR_BACKUP"

echo "[$(date)] Final prepare..."
mariabackup --prepare --target-dir="$FULL_BACKUP"

echo "[$(date)] Stopping MariaDB..."
sudo systemctl stop mariadb

echo "[$(date)] Backing up current data..."
sudo mv /var/lib/mysql /var/lib/mysql.old

echo "[$(date)] Restoring backup..."
mariabackup --copy-back --target-dir="$FULL_BACKUP"

sudo chown -R mysql:mysql /var/lib/mysql

echo "[$(date)] Starting MariaDB..."
sudo systemctl start mariadb

echo "✅ Restore completed!"
```

---

## 4. Point-in-time recovery

### 4.1 Сохранение binary logs

```bash
#!/bin/bash
# backup_binlogs.sh

BINLOG_DIR="/var/log/mysql"
BACKUP_DIR="/backup/binlogs"
DATE=$(date +%Y%m%d)

# Flush текущих binlogs
mariadb -u root -p -e "FLUSH BINARY LOGS;"

# Копировать старые binlogs
mkdir -p "$BACKUP_DIR/$DATE"
find "$BINLOG_DIR" -name "mariadb-bin.[0-9]*" -type f -mtime +1 \
    -exec cp {} "$BACKUP_DIR/$DATE/" \;

echo "Binary logs backed up to: $BACKUP_DIR/$DATE"
```

### 4.2 Восстановление на определенное время

```bash
#!/bin/bash
# point_in_time_recovery.sh

BINLOG_DIR="/backup/binlogs/20251101"
STOP_DATETIME="2025-11-01 14:30:00"

# 1. Восстановить из полного бэкапа
# (используйте restore_incremental.sh)

# 2. Применить binlogs до нужного времени
for binlog in "$BINLOG_DIR"/mariadb-bin.*; do
    echo "Applying: $binlog"
    mariadb-binlog \
        --stop-datetime="$STOP_DATETIME" \
        "$binlog" | mariadb -u root -p
done

echo "✅ Point-in-time recovery to $STOP_DATETIME completed"
```

---

## 5. Тестирование восстановления

### 5.1 Ежемесячный тест восстановления

```bash
#!/bin/bash
# test_restore_monthly.sh

TEST_DATE=$(date +%Y%m%d)
LATEST_BACKUP=$(ls -t /backup/mariabackup/full_* | head -1)

echo "=== Monthly Restore Test: $TEST_DATE ==="
echo "Using backup: $LATEST_BACKUP"

# 1. Создать тестовый контейнер
docker run -d --name mariadb-restore-test \
    -e MYSQL_ROOT_PASSWORD=testpass \
    -v "$LATEST_BACKUP":/backup \
    mariadb:10.11

# 2. Восстановить бэкап
docker exec mariadb-restore-test bash -c "
    systemctl stop mariadb
    rm -rf /var/lib/mysql/*
    mariabackup --copy-back --target-dir=/backup
    chown -R mysql:mysql /var/lib/mysql
    systemctl start mariadb
"

# 3. Проверить данные
RECORD_COUNT=$(docker exec mariadb-restore-test \
    mariadb -u root -ptestpass -N -e \
    'SELECT COUNT(*) FROM production_db.users;')

echo "Restored record count: $RECORD_COUNT"

# 4. Очистка
docker stop mariadb-restore-test
docker rm mariadb-restore-test

# 5. Отчет
cat > "/backup/test_reports/restore_test_$TEST_DATE.txt" << EOF
Restore Test Report
Date: $TEST_DATE
Backup: $LATEST_BACKUP
Record Count: $RECORD_COUNT
Status: SUCCESS
EOF

echo "✅ Test completed"
```

---

## 6. Disaster recovery

### 6.1 Disaster Recovery Plan

```plaintext
=== MariaDB Disaster Recovery Plan ===

RTO (Recovery Time Objective): 4 часа
RPO (Recovery Point Objective): 1 час

Шаги восстановления:

1. ОЦЕНКА (15 минут)
   - Определить масштаб проблемы
   - Найти последний валидный бэкап
   - Уведомить команду

2. ПОДГОТОВКА (30 минут)
   - Подготовить новый сервер (если нужно)
   - Загрузить бэкапы
   - Проверить целостность

3. ВОССТАНОВЛЕНИЕ (2 часа)
   - Восстановить из полного бэкапа
   - Применить инкрементальные бэкапы
   - Применить binlogs (point-in-time)

4. ПРОВЕРКА (1 час)
   - Проверить данные
   - Тест подключений
   - Smoke tests приложений

5. ПЕРЕКЛЮЧЕНИЕ (30 минут)
   - Обновить DNS/конфиги
   - Переключить трафик
   - Мониторинг
```

### 6.2 Скрипт автоматического DR

```bash
#!/bin/bash
# disaster_recovery.sh

BACKUP_SERVER="backup.company.com"
BACKUP_USER="backup"
LATEST_BACKUP_DIR="/backups/mariadb/latest"

echo "=== DISASTER RECOVERY INITIATED ==="
echo "Timestamp: $(date)"

# 1. Остановить проблемный сервер (если работает)
sudo systemctl stop mariadb

# 2. Загрузить последний бэкап с backup сервера
echo "[$(date)] Downloading latest backup..."
rsync -avz --progress \
    "$BACKUP_USER@$BACKUP_SERVER:$LATEST_BACKUP_DIR/" \
    /tmp/restore_backup/

# 3. Подготовить бэкап
echo "[$(date)] Preparing backup..."
mariabackup --prepare --target-dir=/tmp/restore_backup/

# 4. Восстановить
echo "[$(date)] Restoring data..."
sudo rm -rf /var/lib/mysql/*
mariabackup --copy-back --target-dir=/tmp/restore_backup/
sudo chown -R mysql:mysql /var/lib/mysql

# 5. Запустить MariaDB
echo "[$(date)] Starting MariaDB..."
sudo systemctl start mariadb

# 6. Проверка
echo "[$(date)] Verification..."
mariadb -u root -p -e "SELECT COUNT(*) FROM production_db.users;"

echo "✅ DISASTER RECOVERY COMPLETED"
echo "Please verify all data and applications"
```

---

## Автоматизация (Cron)

```bash
# Добавить в crontab

# Полный бэкап каждое воскресенье в 2:00
0 2 * * 0 /usr/local/bin/mariabackup_full.sh

# Инкрементальный ежедневно в 2:00 (кроме воскресенья)
0 2 * * 1-6 /usr/local/bin/mariabackup_incremental.sh

# Binary logs каждый час
0 * * * * /usr/local/bin/backup_binlogs.sh

# Ротация старых бэкапов
0 3 * * * find /backup/mariabackup -type d -mtime +30 -exec rm -rf {} \;

# Ежемесячный тест восстановления
0 4 1 * * /usr/local/bin/test_restore_monthly.sh
```

---

## Чек-лист

### ✅ Обязательные действия

- [ ] Стратегия бэкапов определена
- [ ] mariabackup настроен
- [ ] Полные бэкапы автоматизированы
- [ ] Инкрементальные бэкапы настроены
- [ ] Binary logs сохраняются
- [ ] Тестирование восстановления регулярное
- [ ] Disaster Recovery Plan документирован
- [ ] Off-site копии настроены

### 🔄 Проверки

- [ ] Последний бэкап успешен
- [ ] Тест восстановления пройден
- [ ] Достаточно места для бэкапов
- [ ] RTO/RPO соблюдаются

---

## Следующий шаг

**[→ ГЛАВА 12: Мониторинг и обслуживание](./12-monitoring-maintenance.md)**

В следующей главе:
- Prometheus + Grafana
- Alerting
- Регулярное обслуживание
- Performance monitoring