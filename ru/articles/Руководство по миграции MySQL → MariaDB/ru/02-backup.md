# ГЛАВА 2: Создание полного резервного копирования

> **Цель главы:** Создать надежную точку восстановления перед началом миграции

[← Предыдущая глава](./01-inventory.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./03-prepare-infrastructure.md)

---

## Содержание главы

1. [Стратегия резервного копирования](#1-стратегия-резервного-копирования)
2. [Логическое резервное копирование (mysqldump)](#2-логическое-резервное-копирование)
3. [Физическое резервное копирование (XtraBackup)](#3-физическое-резервное-копирование)
4. [Бэкап конфигурационных файлов](#4-бэкап-конфигурационных-файлов)
5. [Проверка целостности бэкапов](#5-проверка-целостности-бэкапов)
6. [Организация хранения](#6-организация-хранения)
7. [Копирование на удаленное хранилище](#7-копирование-на-удаленное-хранилище)
8. [Документирование бэкапов](#8-документирование-бэкапов)

---

## 1. Стратегия резервного копирования

### 1.1 Правило 3-2-1

```plaintext
3 копии данных
2 различных типа носителей (например: локальный диск + S3)
1 копия off-site (удаленное хранилище)
```

### 1.2 Сравнение методов

| Метод | Скорость | Размер | Downtime | Точность | Рекомендация |
|-------|----------|--------|----------|----------|--------------|
| **mysqldump** | Медленная | Большой | Минимальный | 100% | ✅ Основной для миграции |
| **XtraBackup** | Быстрая | Средний | Нет | 100% | ✅ Дополнительный |
| **LVM snapshot** | Очень быстрая | Большой | Секунды | 99% | Для быстрого отката |
| **File copy** | Средняя | Большой | Полный | 100% | Только при остановке |

### 1.3 Рекомендуемая стратегия

```plaintext
Для миграции MySQL → MariaDB:

1. Логический дамп (mysqldump)
   - Для импорта в MariaDB
   - Максимальная совместимость
   
2. Физический бэкап (XtraBackup)
   - Для быстрого отката к MySQL
   - На случай проблем

3. Snapshot конфигов
   - Все файлы /etc/mysql/
   - Runtime переменные
```

---

## 2. Логическое резервное копирование (mysqldump)

### 2.1 Полный дамп всех баз данных

```bash
#!/bin/bash
# full_mysqldump.sh

BACKUP_DIR="/backup/mysql/dumps"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="$BACKUP_DIR/full_backup_$DATE.sql"
LOG_FILE="$BACKUP_DIR/backup.log"

mkdir -p "$BACKUP_DIR"

echo "[$(date)] Starting full database dump..." | tee -a "$LOG_FILE"

mysqldump \
    --user=root \
    --password \
    --all-databases \
    --routines \
    --triggers \
    --events \
    --single-transaction \
    --quick \
    --lock-tables=false \
    --master-data=2 \
    --flush-logs \
    --hex-blob \
    --default-character-set=utf8mb4 \
    --result-file="$BACKUP_FILE" \
    2>&1 | tee -a "$LOG_FILE"

if [ ${PIPESTATUS[0]} -eq 0 ]; then
    echo "[$(date)] Backup completed: $BACKUP_FILE" | tee -a "$LOG_FILE"
    
    # Сжатие
    gzip "$BACKUP_FILE"
    
    # Контрольная сумма
    md5sum "${BACKUP_FILE}.gz" > "${BACKUP_FILE}.gz.md5"
    
    # Размер
    ls -lh "${BACKUP_FILE}.gz" | tee -a "$LOG_FILE"
    
    echo "[$(date)] Backup successful!" | tee -a "$LOG_FILE"
else
    echo "[$(date)] BACKUP FAILED!" | tee -a "$LOG_FILE"
    exit 1
fi
```

### 2.2 Критические параметры mysqldump

```bash
--all-databases              # Все базы данных
--routines                   # Stored procedures и functions
--triggers                   # Триггеры
--events                     # Scheduled events
--single-transaction         # Для InnoDB без блокировок
--quick                      # Не буферизовать результаты
--lock-tables=false          # Не блокировать таблицы
--master-data=2              # Записать binlog позицию (комментарий)
--flush-logs                 # Создать новый binlog
--hex-blob                   # BLOB в HEX (безопасно)
--default-character-set      # Кодировка (utf8mb4 для emoji)
```

### 2.3 Раздельные дампы баз данных

```bash
#!/bin/bash
# separate_dumps.sh

BACKUP_DIR="/backup/mysql/separate"
DATE=$(date +%Y%m%d_%H%M%S)
OUTPUT_DIR="$BACKUP_DIR/$DATE"

mkdir -p "$OUTPUT_DIR"

# Получить список баз (исключая системные)
DATABASES=$(mysql -u root -p -N -e "SHOW DATABASES;" | \
    grep -Ev "^(information_schema|performance_schema|mysql|sys)$")

for DB in $DATABASES; do
    echo "[$(date)] Backing up database: $DB"
    
    mysqldump \
        --user=root \
        --password \
        --databases "$DB" \
        --routines \
        --triggers \
        --events \
        --single-transaction \
        --result-file="$OUTPUT_DIR/${DB}.sql"
    
    # Сжатие
    gzip "$OUTPUT_DIR/${DB}.sql"
    
    echo "[$(date)] Completed: $DB"
done

echo "[$(date)] All databases backed up to: $OUTPUT_DIR"
```

### 2.4 Дамп только структуры (схемы)

```bash
# Только CREATE TABLE, без данных
mysqldump \
    --user=root \
    --password \
    --all-databases \
    --no-data \
    --routines \
    --triggers \
    --events \
    > schema_only_$(date +%Y%m%d).sql
```

### 2.5 Оптимизация для больших баз

```bash
#!/bin/bash
# optimized_dump.sh

# Для баз >100GB используйте параллельный дамп
mysqldump \
    --user=root \
    --password \
    --all-databases \
    --single-transaction \
    --quick \
    --extended-insert \
    --max-allowed-packet=512M \
    --net-buffer-length=32K \
    | gzip -c > backup_$(date +%Y%m%d).sql.gz

# Или используйте mydumper для параллельности
mydumper \
    --user=root \
    --password=yourpass \
    --outputdir=/backup/mydumper_$(date +%Y%m%d) \
    --threads=4 \
    --compress \
    --build-empty-files \
    --routines \
    --events \
    --triggers
```

---

## 3. Физическое резервное копирование (XtraBackup)

### 3.1 Установка Percona XtraBackup

```bash
# Ubuntu/Debian
wget https://repo.percona.com/apt/percona-release_latest.$(lsb_release -sc)_all.deb
sudo dpkg -i percona-release_latest.$(lsb_release -sc)_all.deb
sudo apt update
sudo apt install percona-xtrabackup-80 -y

# Проверка установки
xtrabackup --version
```

### 3.2 Создание backup пользователя

```sql
CREATE USER 'xtrabackup'@'localhost' IDENTIFIED BY 'BackupPass123!';
GRANT RELOAD, LOCK TABLES, PROCESS, REPLICATION CLIENT ON *.* TO 'xtrabackup'@'localhost';
GRANT SELECT ON mysql.* TO 'xtrabackup'@'localhost';
FLUSH PRIVILEGES;
```

### 3.3 Полный физический бэкап

```bash
#!/bin/bash
# xtrabackup_full.sh

BACKUP_DIR="/backup/xtrabackup"
DATE=$(date +%Y%m%d_%H%M%S)
FULL_BACKUP="$BACKUP_DIR/full_$DATE"

mkdir -p "$FULL_BACKUP"

echo "[$(date)] Starting XtraBackup full backup..."

xtrabackup \
    --backup \
    --user=xtrabackup \
    --password=BackupPass123! \
    --target-dir="$FULL_BACKUP" \
    --parallel=4 \
    --compress \
    --compress-threads=4

if [ $? -eq 0 ]; then
    echo "[$(date)] XtraBackup completed: $FULL_BACKUP"
    
    # Создать архив
    tar -czf "${FULL_BACKUP}.tar.gz" -C "$BACKUP_DIR" "full_$DATE"
    
    # Удалить исходную папку
    rm -rf "$FULL_BACKUP"
    
    echo "[$(date)] Backup archived: ${FULL_BACKUP}.tar.gz"
else
    echo "[$(date)] XtraBackup FAILED!"
    exit 1
fi
```

### 3.4 Преимущества XtraBackup

```plaintext
✅ Горячий бэкап (без остановки MySQL)
✅ Не блокирует таблицы
✅ Быстрее mysqldump в 5-10 раз
✅ Поддержка инкрементальных бэкапов
✅ Point-in-time recovery
✅ Сжатие на лету
✅ Параллельное выполнение
```

---

## 4. Бэкап конфигурационных файлов

### 4.1 Полное резервное копирование конфигов

```bash
#!/bin/bash
# backup_configs.sh

BACKUP_DIR="/backup/mysql/configs"
DATE=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

echo "[$(date)] Backing up MySQL configuration files..."

# Основная конфигурация
sudo tar -czf "$BACKUP_DIR/mysql_configs_$DATE.tar.gz" \
    /etc/mysql/ \
    /etc/my.cnf 2>/dev/null || true

# Runtime переменные
mysql -u root -p -e "SHOW VARIABLES;" > "$BACKUP_DIR/variables_$DATE.txt"
mysql -u root -p -e "SHOW GLOBAL STATUS;" > "$BACKUP_DIR/status_$DATE.txt"

# Информация о версии
mysql -V > "$BACKUP_DIR/version_$DATE.txt"

# Список плагинов
mysql -u root -p -e "SHOW PLUGINS;" > "$BACKUP_DIR/plugins_$DATE.txt"

# Binary log позиция
mysql -u root -p -e "SHOW MASTER STATUS\G" > "$BACKUP_DIR/master_status_$DATE.txt"

echo "[$(date)] Configuration backup completed: $BACKUP_DIR"
```

### 4.2 Экспорт важных переменных

```bash
#!/bin/bash
# export_variables.sh

OUTPUT_FILE="mysql_variables_$(date +%Y%m%d).txt"

mysql -u root -p -e "
SELECT 
    VARIABLE_NAME,
    VARIABLE_VALUE
FROM performance_schema.global_variables
WHERE VARIABLE_NAME IN (
    'innodb_buffer_pool_size',
    'innodb_log_file_size',
    'max_connections',
    'table_open_cache',
    'query_cache_size',
    'tmp_table_size',
    'max_heap_table_size',
    'thread_cache_size',
    'key_buffer_size',
    'binlog_format',
    'gtid_mode',
    'server_id'
)
ORDER BY VARIABLE_NAME;
" > "$OUTPUT_FILE"

echo "Key variables exported to: $OUTPUT_FILE"
```

---

## 5. Проверка целостности бэкапов

### 5.1 Проверка SQL дампа

```bash
#!/bin/bash
# verify_dump.sh

BACKUP_FILE="$1"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: Backup file not found: $BACKUP_FILE"
    exit 1
fi

echo "Verifying backup: $BACKUP_FILE"

# Распаковка если .gz
if [[ "$BACKUP_FILE" == *.gz ]]; then
    gunzip -c "$BACKUP_FILE" > /tmp/verify_backup.sql
    VERIFY_FILE="/tmp/verify_backup.sql"
else
    VERIFY_FILE="$BACKUP_FILE"
fi

# Проверка структуры SQL
if grep -q "CREATE DATABASE" "$VERIFY_FILE" && \
   grep -q "CREATE TABLE" "$VERIFY_FILE"; then
    echo "✅ Backup file structure is valid"
else
    echo "❌ Backup file may be corrupted!"
    exit 1
fi

# Проверка размера
FILE_SIZE=$(stat -f%z "$VERIFY_FILE" 2>/dev/null || stat -c%s "$VERIFY_FILE")
if [ "$FILE_SIZE" -gt 1000 ]; then
    echo "✅ Backup file size OK: $(numfmt --to=iec $FILE_SIZE)"
else
    echo "⚠️  Warning: Backup file is very small: $FILE_SIZE bytes"
fi

# Проверка SQL синтаксиса (на sample)
head -1000 "$VERIFY_FILE" | mysql --batch --skip-column-names -e "SELECT 'OK';" 2>&1
if [ $? -eq 0 ]; then
    echo "✅ SQL syntax check passed"
else
    echo "❌ SQL syntax errors detected"
fi

# Очистка
if [ "$VERIFY_FILE" = "/tmp/verify_backup.sql" ]; then
    rm -f /tmp/verify_backup.sql
fi

echo "Verification complete"
```

### 5.2 Тестовое восстановление

```bash
#!/bin/bash
# test_restore.sh

BACKUP_FILE="$1"
TEST_DB="test_restore_$(date +%Y%m%d_%H%M%S)"

echo "Testing restore from: $BACKUP_FILE"

# Создать тестовую базу
mysql -u root -p -e "CREATE DATABASE $TEST_DB;"

# Попробовать восстановить первые 1000 строк
if [[ "$BACKUP_FILE" == *.gz ]]; then
    gunzip -c "$BACKUP_FILE" | head -1000 | mysql -u root -p "$TEST_DB"
else
    head -1000 "$BACKUP_FILE" | mysql -u root -p "$TEST_DB"
fi

if [ $? -eq 0 ]; then
    echo "✅ Test restore successful"
    mysql -u root -p -e "DROP DATABASE $TEST_DB;"
    exit 0
else
    echo "❌ Test restore FAILED!"
    exit 1
fi
```

### 5.3 Проверка контрольных сумм

```bash
#!/bin/bash
# verify_checksums.sh

BACKUP_DIR="/backup/mysql/dumps"

echo "Verifying checksums in: $BACKUP_DIR"

cd "$BACKUP_DIR" || exit 1

for file in *.sql.gz; do
    if [ -f "${file}.md5" ]; then
        echo "Checking: $file"
        md5sum -c "${file}.md5"
        
        if [ $? -eq 0 ]; then
            echo "✅ $file - OK"
        else
            echo "❌ $file - CHECKSUM MISMATCH!"
        fi
    else
        echo "⚠️  No checksum for: $file"
    fi
done
```

---

## 6. Организация хранения

### 6.1 Рекомендуемая структура каталогов

```plaintext
/backup/mysql/
├── dumps/                          # Логические дампы
│   ├── 20251101_120000/
│   │   ├── full_backup.sql.gz
│   │   ├── full_backup.sql.gz.md5
│   │   └── backup.log
│   └── 20251102_120000/
├── separate/                       # Раздельные дампы
│   └── 20251101_120000/
│       ├── production_db.sql.gz
│       ├── analytics_db.sql.gz
│       └── staging_db.sql.gz
├── xtrabackup/                     # Физические бэкапы
│   ├── full_20251101_120000.tar.gz
│   └── full_20251102_120000.tar.gz
├── configs/                        # Конфигурации
│   ├── mysql_configs_20251101.tar.gz
│   ├── variables_20251101.txt
│   └── status_20251101.txt
├── binlogs/                        # Binary logs
│   └── 20251101/
│       ├── mysql-bin.000001
│       └── mysql-bin.000002
└── scripts/                        # Скрипты
    ├── full_mysqldump.sh
    ├── xtrabackup_full.sh
    └── verify_dump.sh
```

### 6.2 Скрипт ротации бэкапов

```bash
#!/bin/bash
# rotate_backups.sh

BACKUP_DIR="/backup/mysql/dumps"
RETENTION_DAYS=30

echo "Rotating backups older than $RETENTION_DAYS days in $BACKUP_DIR..."

# Удалить бэкапы старше N дней
find "$BACKUP_DIR" -type f -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete
find "$BACKUP_DIR" -type f -name "*.md5" -mtime +$RETENTION_DAYS -delete

# Удалить пустые директории
find "$BACKUP_DIR" -type d -empty -delete

echo "Rotation completed"

# Показать оставшиеся бэкапы
echo -e "\nRemaining backups:"
du -sh "$BACKUP_DIR"/* | sort -h
```

---

## 7. Копирование на удаленное хранилище

### 7.1 Загрузка в AWS S3

```bash
#!/bin/bash
# s3_upload.sh

BACKUP_FILE="$1"
S3_BUCKET="s3://company-mysql-backups/production/"

if [ ! -f "$BACKUP_FILE" ]; then
    echo "Error: File not found: $BACKUP_FILE"
    exit 1
fi

echo "Uploading to S3: $BACKUP_FILE"

aws s3 cp "$BACKUP_FILE" "$S3_BUCKET" \
    --storage-class STANDARD_IA \
    --server-side-encryption AES256 \
    --metadata "created=$(date -Iseconds)"

if [ $? -eq 0 ]; then
    echo "✅ Backup uploaded to S3 successfully"
    echo "S3 URL: ${S3_BUCKET}$(basename $BACKUP_FILE)"
else
    echo "❌ S3 upload FAILED!"
    exit 1
fi
```

### 7.2 Синхронизация на удаленный сервер (rsync)

```bash
#!/bin/bash
# remote_sync.sh

LOCAL_BACKUP="/backup/mysql/"
REMOTE_HOST="backup-server.company.com"
REMOTE_USER="backup"
REMOTE_PATH="/backups/mysql-prod/"
SSH_KEY="/root/.ssh/backup_key"

echo "Syncing backups to remote server..."

rsync -avz --progress \
    --delete-after \
    -e "ssh -i $SSH_KEY" \
    "$LOCAL_BACKUP" \
    "$REMOTE_USER@$REMOTE_HOST:$REMOTE_PATH"

if [ $? -eq 0 ]; then
    echo "✅ Remote sync completed"
else
    echo "❌ Remote sync FAILED!"
    exit 1
fi
```

### 7.3 Автоматическая загрузка после бэкапа

```bash
#!/bin/bash
# backup_and_upload.sh

# 1. Создать бэкап
./full_mysqldump.sh
BACKUP_FILE="/backup/mysql/dumps/full_backup_$(date +%Y%m%d_*)*.sql.gz"

# 2. Проверить
./verify_dump.sh "$BACKUP_FILE"

# 3. Загрузить в S3
if [ $? -eq 0 ]; then
    ./s3_upload.sh "$BACKUP_FILE"
fi

# 4. Синхронизировать на удаленный сервер
./remote_sync.sh
```

---

## 8. Документирование бэкапов

### 8.1 Создание манифеста бэкапа

```bash
#!/bin/bash
# create_manifest.sh

BACKUP_FILE="$1"
MANIFEST="${BACKUP_FILE}.manifest.txt"

cat > "$MANIFEST" << EOF
==========================================
MySQL Backup Manifest
==========================================
Backup Date: $(date)
Server Hostname: $(hostname)
MySQL Version: $(mysql -V)
Backup File: $BACKUP_FILE
File Size: $(ls -lh "$BACKUP_FILE" | awk '{print $5}')

Checksum:
$(md5sum "$BACKUP_FILE")

Databases Included:
EOF

# Добавить список баз из дампа
if [[ "$BACKUP_FILE" == *.gz ]]; then
    gunzip -c "$BACKUP_FILE" | grep "^CREATE DATABASE" | sed 's/.*`\(.*\)`.*/\1/' >> "$MANIFEST"
else
    grep "^CREATE DATABASE" "$BACKUP_FILE" | sed 's/.*`\(.*\)`.*/\1/' >> "$MANIFEST"
fi

cat >> "$MANIFEST" << EOF

Binary Log Position:
EOF

mysql -u root -p -e "SHOW MASTER STATUS\G" >> "$MANIFEST" 2>/dev/null

echo "Manifest created: $MANIFEST"
```

### 8.2 Журнал бэкапов

```bash
#!/bin/bash
# log_backup.sh

LOG_FILE="/backup/mysql/backup_journal.log"
BACKUP_FILE="$1"

cat >> "$LOG_FILE" << EOF
---
Date: $(date -Iseconds)
File: $(basename "$BACKUP_FILE")
Size: $(ls -lh "$BACKUP_FILE" | awk '{print $5}')
MD5: $(md5sum "$BACKUP_FILE" | awk '{print $1}')
Status: SUCCESS
---
EOF
```

---

## Чек-лист выполнения главы

### ✅ Обязательные действия

- [ ] Создан полный логический дамп (mysqldump)
- [ ] Создан физический бэкап (XtraBackup)
- [ ] Сохранены конфигурационные файлы
- [ ] Экспортированы runtime переменные
- [ ] Все бэкапы сжаты (gzip)
- [ ] Созданы контрольные суммы (MD5)
- [ ] Выполнена проверка целостности
- [ ] Проведено тестовое восстановление
- [ ] Бэкапы скопированы на удаленное хранилище
- [ ] Создана документация (манифесты)

### 📊 Размеры бэкапов

Заполните после создания:

| Тип бэкапа | Размер | Время создания | Локация |
|------------|--------|----------------|---------|
| mysqldump (полный) | ___ GB | ___ мин | /backup/mysql/dumps/ |
| mysqldump (раздельные) | ___ GB | ___ мин | /backup/mysql/separate/ |
| XtraBackup | ___ GB | ___ мин | /backup/mysql/xtrabackup/ |
| Конфиги | ___ MB | ___ сек | /backup/mysql/configs/ |
| **ИТОГО** | ___ GB | ___ мин | |

### 🔍 Проверки

- [ ] Контрольная сумма совпадает
- [ ] SQL синтаксис валиден
- [ ] Размер файла адекватен размеру БД
- [ ] Тестовое восстановление успешно
- [ ] Файлы доступны на удаленном хранилище

---

## Полезные команды

```bash
# Проверить размер всех бэкапов
du -sh /backup/mysql/*

# Найти старые бэкапы
find /backup/mysql -type f -mtime +30

# Проверить место на диске
df -h /backup

# Список бэкапов с датами
ls -lht /backup/mysql/dumps/*.sql.gz | head -10

# Сравнить размеры БД и бэкапа
mysql -u root -p -e "SELECT SUM(data_length+index_length)/1024/1024 AS MB FROM information_schema.tables;"
ls -lh /backup/mysql/dumps/*.sql.gz
```

---

## Следующий шаг

После успешного создания всех резервных копий переходите к:

**[→ ГЛАВА 3: Подготовка инфраструктуры](./03-prepare-infrastructure.md)**

В следующей главе:
- Остановка MySQL сервисов
- Настройка репозиториев MariaDB
- Оптимизация системы
- Подготовка к установке
