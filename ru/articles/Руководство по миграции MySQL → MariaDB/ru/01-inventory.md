# ГЛАВА 1: Инвентаризация и аудит инфраструктуры

> **Цель главы:** Провести полный аудит существующей MySQL инфраструктуры для успешного планирования миграции

[← Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./02-backup.md)

---

## Содержание главы

1. [Введение и важность инвентаризации](#1-введение)
2. [Аудит баз данных](#2-аудит-баз-данных)
3. [Инвентаризация пользователей](#3-инвентаризация-пользователей)
4. [Анализ функций и объектов](#4-анализ-функций-и-объектов)
5. [Проверка репликации](#5-проверка-репликации)
6. [Инвентаризация конфигурации](#6-инвентаризация-конфигурации)
7. [Анализ производительности](#7-анализ-производительности)
8. [Проверка зависимостей](#8-проверка-зависимостей)
9. [Оценка совместимости](#9-оценка-совместимости)
10. [Создание отчета](#10-создание-отчета)

---

## 1. Введение и важность инвентаризации

### 1.1 Зачем нужна инвентаризация

Инвентаризация — это **фундамент успешной миграции**. Без детального понимания текущей инфраструктуры риск проблем возрастает в разы.

**Статистика:**
```plaintext
Проекты миграции БД:
- С полной инвентаризацией: 95% успешных миграций
- Без инвентаризации: 60% успешных миграций
- Средний downtime с инвентаризацией: 15 минут
- Средний downtime без инвентаризации: 4+ часа
```

### 1.2 Что мы будем собирать

Полная инвентаризация включает:

#### 📊 Данные
- Размер каждой базы данных
- Количество таблиц и записей
- Используемые storage engines
- Структура индексов
- Foreign keys и constraints

#### 👥 Пользователи и безопасность
- Список всех пользователей
- Привилегии и роли
- Authentication plugins
- SSL/TLS настройки

#### 🔧 Функциональность
- Stored procedures и functions
- Triggers
- Events (scheduled tasks)
- Views
- Partitioned tables

#### ⚙️ Конфигурация
- Параметры сервера
- Performance variables
- Репликация настройки
- Plugin'ы

#### 📈 Производительность
- Медленные запросы
- Индексы и их использование
- Buffer pool статистика
- Connection patterns

#### 🔗 Зависимости
- Подключенные приложения
- Используемые драйверы
- External tools и utilities

### 1.3 Необходимые инструменты

Перед началом убедитесь, что у вас есть:

```bash
# Основные утилиты MySQL
which mysql mysqldump mysqladmin

# Percona Toolkit (рекомендуется)
sudo apt install percona-toolkit -y

# Утилиты анализа
sudo apt install -y \
    sysstat \
    htop \
    iotop \
    nethogs \
    mytop
```

### 1.4 Права доступа

Создайте пользователя для аудита с правами только на чтение:

```sql
-- Создание аудит-пользователя
CREATE USER 'audit'@'localhost' IDENTIFIED BY 'AuditPassword123!';

-- Минимальные необходимые права
GRANT SELECT ON *.* TO 'audit'@'localhost';
GRANT PROCESS ON *.* TO 'audit'@'localhost';
GRANT REPLICATION CLIENT ON *.* TO 'audit'@'localhost';
GRANT SHOW DATABASES ON *.* TO 'audit'@'localhost';
GRANT SHOW VIEW ON *.* TO 'audit'@'localhost';

-- Для Performance Schema
GRANT SELECT ON performance_schema.* TO 'audit'@'localhost';
GRANT SELECT ON information_schema.* TO 'audit'@'localhost';

FLUSH PRIVILEGES;
```

**Проверка прав:**
```bash
mysql -u audit -p -e "SHOW GRANTS FOR 'audit'@'localhost';"
```

---

## 2. Аудит баз данных

### 2.1 Список всех баз данных с размерами

Это первый и самый важный шаг — понять, сколько данных вам предстоит мигрировать.

#### Базовый запрос

```sql
SELECT 
    table_schema AS 'Database',
    COUNT(*) AS 'Tables',
    ROUND(SUM(data_length) / 1024 / 1024, 2) AS 'Data Size (MB)',
    ROUND(SUM(index_length) / 1024 / 1024, 2) AS 'Index Size (MB)',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Total Size (MB)',
    ROUND(SUM(data_free) / 1024 / 1024, 2) AS 'Free Space (MB)'
FROM information_schema.tables
GROUP BY table_schema
ORDER BY SUM(data_length + index_length) DESC;
```

**Пример вывода:**
```plaintext
+--------------------+--------+----------------+-----------------+-----------------+------------------+
| Database           | Tables | Data Size (MB) | Index Size (MB) | Total Size (MB) | Free Space (MB)  |
+--------------------+--------+----------------+-----------------+-----------------+------------------+
| production_db      | 234    | 38234.56       | 7443.76         | 45678.32        | 1234.50          |
| analytics_db       | 89     | 10123.45       | 2222.22         | 12345.67        | 456.78           |
| staging_db         | 234    | 4567.89        | 1111.01         | 5678.90         | 123.45           |
| test_db            | 156    | 890.12         | 234.56          | 1124.68         | 45.67            |
| information_schema | 79     | 0.00           | 0.00            | 0.16            | 0.00             |
| mysql              | 31     | 1.89           | 0.59            | 2.48            | 0.00             |
| performance_schema | 87     | 0.00           | 0.00            | 0.00            | 0.00             |
+--------------------+--------+----------------+-----------------+-----------------+------------------+
```

#### Детальный анализ с фрагментацией

```sql
SELECT 
    table_schema AS 'Database',
    COUNT(*) AS 'Tables',
    ROUND(SUM(data_length) / 1024 / 1024, 2) AS 'Data (MB)',
    ROUND(SUM(index_length) / 1024 / 1024, 2) AS 'Index (MB)',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Total (MB)',
    ROUND(SUM(data_free) / 1024 / 1024, 2) AS 'Free (MB)',
    ROUND(SUM(data_free) / NULLIF(SUM(data_length + index_length), 0) * 100, 2) AS 'Fragmentation %'
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'performance_schema', 'mysql', 'sys')
GROUP BY table_schema
ORDER BY SUM(data_length + index_length) DESC;
```

**Интерпретация результатов:**

| Fragmentation % | Состояние | Действие |
|-----------------|-----------|----------|
| 0-5% | Отлично | Нет действий |
| 5-15% | Хорошо | Можно оптимизировать |
| 15-30% | Средне | Рекомендуется OPTIMIZE |
| >30% | Плохо | Обязательно OPTIMIZE перед миграцией |

### 2.2 Анализ storage engines

Важно понять, какие движки хранения используются, так как не все совместимы с MariaDB.

```sql
SELECT 
    engine AS 'Storage Engine',
    COUNT(*) AS 'Tables',
    ROUND(SUM(data_length) / 1024 / 1024, 2) AS 'Data (MB)',
    ROUND(SUM(index_length) / 1024 / 1024, 2) AS 'Index (MB)',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Total (MB)',
    ROUND(SUM(data_length + index_length) / SUM(SUM(data_length + index_length)) OVER () * 100, 2) AS 'Percentage %'
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')
GROUP BY engine
ORDER BY SUM(data_length + index_length) DESC;
```

**Пример вывода:**
```plaintext
+----------------+--------+-----------+------------+--------------+--------------+
| Storage Engine | Tables | Data (MB) | Index (MB) | Total (MB)   | Percentage % |
+----------------+--------+-----------+------------+--------------+--------------+
| InnoDB         | 687    | 52345.67  | 10234.56   | 62580.23     | 98.45        |
| MyISAM         | 23     | 890.12    | 123.45     | 1013.57      | 1.59         |
| MEMORY         | 5      | 0.23      | 0.00       | 0.23         | 0.00         |
| CSV            | 2      | 0.01      | 0.00       | 0.01         | 0.00         |
+----------------+--------+-----------+------------+--------------+--------------+
```

#### Совместимость storage engines

| Engine | MariaDB Совместимость | Рекомендация |
|--------|----------------------|--------------|
| **InnoDB** | ✅ Полностью совместим | Без изменений |
| **MyISAM** | ✅ Совместим | Рекомендуется конвертация в InnoDB |
| **MEMORY (HEAP)** | ✅ Совместим | Без изменений |
| **CSV** | ✅ Совместим | Без изменений |
| **Archive** | ✅ Совместим | Без изменений |
| **Blackhole** | ✅ Совместим | Без изменений |
| **NDB (Cluster)** | ❌ НЕ СОВМЕСТИМ | Миграция невозможна |
| **Federated** | ✅ Совместим | В MariaDB называется FederatedX |

**⚠️ Критически важно:** Если у вас есть таблицы на NDB engine, миграция на MariaDB невозможна. Вам нужно либо остаться на MySQL Cluster, либо мигрировать NDB таблицы на InnoDB.

### 2.3 Детальная информация по таблицам

#### Список крупнейших таблиц

```sql
SELECT 
    table_schema AS 'Database',
    table_name AS 'Table',
    engine AS 'Engine',
    table_rows AS 'Row Count',
    ROUND(data_length / 1024 / 1024, 2) AS 'Data (MB)',
    ROUND(index_length / 1024 / 1024, 2) AS 'Index (MB)',
    ROUND((data_length + index_length) / 1024 / 1024, 2) AS 'Total (MB)',
    ROUND(data_free / 1024 / 1024, 2) AS 'Free (MB)',
    ROUND(data_free / (data_length + index_length) * 100, 2) AS 'Frag %'
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')
  AND table_type = 'BASE TABLE'
ORDER BY (data_length + index_length) DESC
LIMIT 20;
```

#### Таблицы без primary key (потенциальная проблема)

```sql
SELECT 
    t.table_schema AS 'Database',
    t.table_name AS 'Table',
    t.engine AS 'Engine',
    t.table_rows AS 'Rows',
    ROUND((t.data_length + t.index_length) / 1024 / 1024, 2) AS 'Size (MB)'
FROM information_schema.tables t
LEFT JOIN information_schema.statistics s 
    ON t.table_schema = s.table_schema 
    AND t.table_name = s.table_name 
    AND s.index_name = 'PRIMARY'
WHERE t.table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')
  AND t.table_type = 'BASE TABLE'
  AND s.index_name IS NULL
ORDER BY t.table_rows DESC;
```

**Почему это важно:**
- Таблицы без PRIMARY KEY медленнее в репликации
- Могут вызвать проблемы в Galera Cluster
- Затрудняют point-in-time recovery

**Рекомендация:** Добавьте PRIMARY KEY перед миграцией:
```sql
ALTER TABLE your_table ADD PRIMARY KEY (id);
-- или если нет подходящей колонки:
ALTER TABLE your_table ADD COLUMN id BIGINT PRIMARY KEY AUTO_INCREMENT FIRST;
```

### 2.4 Анализ индексов

#### Неиспользуемые индексы

```sql
SELECT 
    object_schema AS 'Database',
    object_name AS 'Table',
    index_name AS 'Index',
    ROUND(stat_value * @@innodb_page_size / 1024 / 1024, 2) AS 'Index Size (MB)'
FROM mysql.innodb_index_stats
WHERE stat_name = 'size'
  AND object_schema NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
  AND index_name NOT IN ('PRIMARY', 'GEN_CLUST_INDEX')
  AND index_name NOT IN (
      SELECT DISTINCT index_name
      FROM performance_schema.table_io_waits_summary_by_index_usage
      WHERE object_schema = innodb_index_stats.object_schema
        AND object_name = innodb_index_stats.object_name
        AND index_name = innodb_index_stats.index_name
        AND count_star > 0
  )
ORDER BY stat_value DESC
LIMIT 20;
```

#### Дублирующиеся индексы

```sql
SELECT 
    s1.table_schema AS 'Database',
    s1.table_name AS 'Table',
    s1.index_name AS 'Index 1',
    s2.index_name AS 'Index 2',
    GROUP_CONCAT(s1.column_name ORDER BY s1.seq_in_index) AS 'Columns'
FROM information_schema.statistics s1
JOIN information_schema.statistics s2 
    ON s1.table_schema = s2.table_schema
    AND s1.table_name = s2.table_name
    AND s1.index_name < s2.index_name
    AND s1.column_name = s2.column_name
    AND s1.seq_in_index = s2.seq_in_index
WHERE s1.table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')
GROUP BY s1.table_schema, s1.table_name, s1.index_name, s2.index_name
HAVING COUNT(*) = (
    SELECT COUNT(*) 
    FROM information_schema.statistics 
    WHERE table_schema = s1.table_schema 
      AND table_name = s1.table_name 
      AND index_name = s1.index_name
);
```

**Рекомендация:** Удалите дублирующиеся и неиспользуемые индексы перед миграцией — это ускорит импорт данных.

### 2.5 Экспорт структуры БД

Сохраните структуру всех баз данных для документации:

```bash
#!/bin/bash
# export_database_structure.sh

OUTPUT_DIR="./db_structure_$(date +%Y%m%d)"
mkdir -p "$OUTPUT_DIR"

# Получить список баз данных
DATABASES=$(mysql -u audit -p -N -e "
    SELECT schema_name 
    FROM information_schema.schemata 
    WHERE schema_name NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys');
")

# Экспорт структуры каждой базы
for DB in $DATABASES; do
    echo "Exporting structure: $DB..."
    
    mysqldump \
        --user=audit \
        --password \
        --no-data \
        --routines \
        --triggers \
        --events \
        --single-transaction \
        "$DB" > "$OUTPUT_DIR/${DB}_structure.sql"
    
    echo "Exported: $DB"
done

echo "All database structures exported to: $OUTPUT_DIR"
```

### 2.6 Создание инвентаризационной таблицы

Создайте сводную таблицу для быстрого анализа:

```bash
#!/bin/bash
# create_database_inventory.sh

OUTPUT_FILE="database_inventory_$(date +%Y%m%d).csv"

mysql -u audit -p -e "
SELECT 
    table_schema AS 'Database',
    COUNT(*) AS 'Tables',
    SUM(table_rows) AS 'Total Rows',
    ROUND(SUM(data_length) / 1024 / 1024, 2) AS 'Data MB',
    ROUND(SUM(index_length) / 1024 / 1024, 2) AS 'Index MB',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Total MB',
    GROUP_CONCAT(DISTINCT engine) AS 'Engines'
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema', 'sys')
GROUP BY table_schema
ORDER BY SUM(data_length + index_length) DESC;
" | sed 's/\t/,/g' > "$OUTPUT_FILE"

echo "Inventory saved to: $OUTPUT_FILE"
```

---

## 3. Инвентаризация пользователей и привилегий

### 3.1 Список всех пользователей

```sql
SELECT 
    User AS 'Username',
    Host AS 'Host',
    plugin AS 'Auth Plugin',
    password_expired AS 'Password Expired',
    password_lifetime AS 'Password Lifetime',
    account_locked AS 'Account Locked',
    password_last_changed AS 'Password Changed',
    authentication_string != '' AS 'Has Password'
FROM mysql.user
ORDER BY User, Host;
```

**Пример вывода:**
```plaintext
+--------------+-------------+------------------------+------------------+-------------------+----------------+---------------------+--------------+
| Username     | Host        | Auth Plugin            | Password Expired | Password Lifetime | Account Locked | Password Changed    | Has Password |
+--------------+-------------+------------------------+------------------+-------------------+----------------+---------------------+--------------+
| admin        | localhost   | mysql_native_password  | N                | NULL              | N              | 2025-10-15 10:30:00 | 1            |
| app_user     | 192.168.1.% | mysql_native_password  | N                | NULL              | N              | 2025-10-20 14:22:00 | 1            |
| backup       | localhost   | mysql_native_password  | N                | NULL              | N              | 2025-09-01 08:15:00 | 1            |
| monitor      | localhost   | mysql_native_password  | N                | NULL              | N              | 2025-10-01 09:00:00 | 1            |
| repl         | 10.0.0.%    | mysql_native_password  | N                | NULL              | N              | 2025-08-15 12:45:00 | 1            |
| root         | localhost   | auth_socket            | N                | NULL              | N              | NULL                | 0            |
+--------------+-------------+------------------------+------------------+-------------------+----------------+---------------------+--------------+
```

### 3.2 Анализ authentication plugins

Проверьте, какие плагины аутентификации используются:

```sql
SELECT 
    plugin AS 'Auth Plugin',
    COUNT(*) AS 'User Count',
    GROUP_CONCAT(CONCAT(User, '@', Host) SEPARATOR ', ') AS 'Users'
FROM mysql.user
WHERE User != ''
GROUP BY plugin
ORDER BY COUNT(*) DESC;
```

**Совместимость плагинов:**

| Plugin MySQL | Plugin MariaDB | Совместимость | Действие |
|--------------|----------------|---------------|----------|
| `mysql_native_password` | `mysql_native_password` | ✅ Полная | Нет действий |
| `caching_sha2_password` | `mysql_native_password` | ⚠️ Частичная | Нужна конвертация |
| `auth_socket` / `unix_socket` | `unix_socket` | ✅ Полная | Нет действий |
| `sha256_password` | N/A | ❌ Нет | Нужна конвертация |

**Если используется `caching_sha2_password`:**
```sql
-- Найти таких пользователей
SELECT User, Host 
FROM mysql.user 
WHERE plugin = 'caching_sha2_password';

-- Конвертировать (потребует сброса пароля)
ALTER USER 'username'@'host' IDENTIFIED WITH mysql_native_password BY 'new_password';
```

### 3.3 Экспорт привилегий

#### Метод 1: Встроенный способ

```bash
#!/bin/bash
# export_user_grants.sh

OUTPUT_FILE="user_grants_$(date +%Y%m%d).sql"

# Получить список пользователей
mysql -u audit -p -N -e "
    SELECT DISTINCT CONCAT('SHOW GRANTS FOR ''', User, '''@''', Host, ''';') 
    FROM mysql.user 
    WHERE User NOT IN ('root', 'mysql.sys', 'mysql.session', 'mysql.infoschema')
      AND User != '';
" | while read query; do
    mysql -u root -p -N -e "$query" | sed 's/$/;/'
done > "$OUTPUT_FILE"

echo "Grants exported to: $OUTPUT_FILE"
```

#### Метод 2: Percona Toolkit (рекомендуется)

```bash
# Более надежный метод
pt-show-grants \
    --host=localhost \
    --user=root \
    --ask-pass \
    > user_grants_$(date +%Y%m%d).sql
```

### 3.4 Анализ привилегий

#### Пользователи с опасными привилегиями

```sql
-- Пользователи с SUPER привилегией
SELECT User, Host 
FROM mysql.user 
WHERE Super_priv = 'Y' 
  AND User NOT IN ('root');

-- Пользователи с доступом ко всем базам
SELECT 
    User, 
    Host,
    GROUP_CONCAT(DISTINCT Db) AS 'Databases'
FROM mysql.db
WHERE Db = '%' OR Db = '*'
GROUP BY User, Host;

-- Пользователи с доступом отовсюду
SELECT User, Host
FROM mysql.user
WHERE Host = '%'
  AND User != '';
```

**Рекомендации по безопасности:**
1. Ограничьте SUPER привилегию только админам
2. Избегайте `%` в Host - используйте конкретные IP/подсети
3. Применяйте принцип минимальных привилегий

### 3.5 Создание матрицы доступа

```sql
-- Матрица: пользователь → база → привилегии
SELECT 
    CONCAT(User, '@', Host) AS 'User@Host',
    Db AS 'Database',
    CONCAT(
        IF(Select_priv = 'Y', 'SELECT ', ''),
        IF(Insert_priv = 'Y', 'INSERT ', ''),
        IF(Update_priv = 'Y', 'UPDATE ', ''),
        IF(Delete_priv = 'Y', 'DELETE ', ''),
        IF(Create_priv = 'Y', 'CREATE ', ''),
        IF(Drop_priv = 'Y', 'DROP ', ''),
        IF(Grant_priv = 'Y', 'GRANT ', ''),
        IF(Index_priv = 'Y', 'INDEX ', ''),
        IF(Alter_priv = 'Y', 'ALTER ', '')
    ) AS 'Privileges'
FROM mysql.db
WHERE User != ''
ORDER BY User, Host, Db;
```

### 3.6 Документирование пользователей

Создайте таблицу для документации:

```bash
#!/bin/bash
# document_users.sh

cat > user_documentation_$(date +%Y%m%d).md << 'EOF'
# MySQL User Documentation

## User Inventory

| Username | Host | Purpose | Used By | Critical |
|----------|------|---------|---------|----------|
EOF

mysql -u audit -p -N -e "
SELECT CONCAT(
    '| ', User, 
    ' | ', Host, 
    ' | [PURPOSE] ',
    ' | [APPS] ',
    ' | [Y/N] |'
)
FROM mysql.user
WHERE User NOT IN ('root', 'mysql.sys', 'mysql.session', 'mysql.infoschema')
  AND User != ''
ORDER BY User, Host;
" >> user_documentation_$(date +%Y%m%d).md

echo "User documentation template created"
echo "Please fill in [PURPOSE], [APPS], and [Y/N] fields"
```

---

## 4. Анализ хранимых процедур, функций и триггеров

### 4.1 Инвентаризация stored routines

```sql
SELECT 
    ROUTINE_SCHEMA AS 'Database',
    ROUTINE_TYPE AS 'Type',
    ROUTINE_NAME AS 'Name',
    DTD_IDENTIFIER AS 'Returns',
    IS_DETERMINISTIC AS 'Deterministic',
    SQL_DATA_ACCESS AS 'Data Access',
    DEFINER AS 'Definer',
    CREATED AS 'Created',
    LAST_ALTERED AS 'Modified'
FROM information_schema.ROUTINES
WHERE ROUTINE_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
ORDER BY ROUTINE_SCHEMA, ROUTINE_TYPE, ROUTINE_NAME;
```

**Пример вывода:**
```plaintext
+---------------+-----------+----------------------+---------+---------------+-------------+-------------------+---------------------+---------------------+
| Database      | Type      | Name                 | Returns | Deterministic | Data Access | Definer           | Created             | Modified            |
+---------------+-----------+----------------------+---------+---------------+-------------+-------------------+---------------------+---------------------+
| production_db | FUNCTION  | calculate_discount   | decimal | YES           | READS SQL   | admin@localhost   | 2024-05-12 10:30:00 | 2025-08-15 14:20:00 |
| production_db | FUNCTION  | get_user_status      | varchar | NO            | READS SQL   | admin@localhost   | 2024-03-20 09:15:00 | 2024-03-20 09:15:00 |
| production_db | PROCEDURE | cleanup_old_orders   | NULL    | NO            | MODIFIES    | admin@localhost   | 2024-06-01 11:00:00 | 2025-09-10 16:45:00 |
| production_db | PROCEDURE | generate_report      | NULL    | NO            | READS SQL   | admin@localhost   | 2024-07-15 13:30:00 | 2025-10-01 10:00:00 |
+---------------+-----------+----------------------+---------+---------------+-------------+-------------------+---------------------+---------------------+
```

### 4.2 Экспорт определений routines

```bash
#!/bin/bash
# export_routines.sh

OUTPUT_DIR="./routines_$(date +%Y%m%d)"
mkdir -p "$OUTPUT_DIR"

# Получить список баз
DATABASES=$(mysql -u audit -p -N -e "
    SELECT DISTINCT ROUTINE_SCHEMA
    FROM information_schema.ROUTINES
    WHERE ROUTINE_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys');
")

for DB in $DATABASES; do
    echo "Exporting routines from: $DB..."
    
    # Экспорт процедур и функций
    mysqldump \
        --user=audit \
        --password \
        --no-create-info \
        --no-data \
        --routines \
        --skip-triggers \
        --databases "$DB" \
        > "$OUTPUT_DIR/${DB}_routines.sql"
done

echo "Routines exported to: $OUTPUT_DIR"
```

### 4.3 Проверка DEFINER

Проблема с DEFINER — частая причина ошибок при импорте:

```sql
-- Процедуры/функции с несуществующими DEFINER'ами
SELECT 
    r.ROUTINE_SCHEMA AS 'Database',
    r.ROUTINE_TYPE AS 'Type',
    r.ROUTINE_NAME AS 'Name',
    r.DEFINER AS 'Definer'
FROM information_schema.ROUTINES r
LEFT JOIN mysql.user u 
    ON r.DEFINER = CONCAT(u.User, '@', u.Host)
WHERE r.ROUTINE_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
  AND u.User IS NULL
ORDER BY r.ROUTINE_SCHEMA, r.ROUTINE_NAME;
```

**Решение:** Перед миграцией либо:
1. Создайте отсутствующих пользователей
2. Измените DEFINER на существующего пользователя
3. Удалите DEFINER из дампа (он будет установлен как текущий пользователь)

### 4.4 Инвентаризация триггеров

```sql
SELECT 
    TRIGGER_SCHEMA AS 'Database',
    TRIGGER_NAME AS 'Trigger',
    EVENT_MANIPULATION AS 'Event',
    EVENT_OBJECT_TABLE AS 'Table',
    ACTION_TIMING AS 'Timing',
    ACTION_STATEMENT AS 'Action',
    DEFINER AS 'Definer',
    CREATED AS 'Created'
FROM information_schema.TRIGGERS
WHERE TRIGGER_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
ORDER BY TRIGGER_SCHEMA, EVENT_OBJECT_TABLE, TRIGGER_NAME;
```

### 4.5 Экспорт триггеров

```bash
#!/bin/bash
# export_triggers.sh

OUTPUT_DIR="./triggers_$(date +%Y%m%d)"
mkdir -p "$OUTPUT_DIR"

DATABASES=$(mysql -u audit -p -N -e "
    SELECT DISTINCT TRIGGER_SCHEMA
    FROM information_schema.TRIGGERS
    WHERE TRIGGER_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys');
")

for DB in $DATABASES; do
    echo "Exporting triggers from: $DB..."
    
    mysqldump \
        --user=audit \
        --password \
        --no-create-info \
        --no-data \
        --triggers \
        --skip-routines \
        --databases "$DB" \
        > "$OUTPUT_DIR/${DB}_triggers.sql"
done

echo "Triggers exported to: $OUTPUT_DIR"
```

### 4.6 Инвентаризация events (scheduled tasks)

```sql
SELECT 
    EVENT_SCHEMA AS 'Database',
    EVENT_NAME AS 'Event',
    STATUS AS 'Status',
    EVENT_TYPE AS 'Type',
    EXECUTE_AT AS 'Execute At',
    INTERVAL_VALUE AS 'Interval Value',
    INTERVAL_FIELD AS 'Interval Unit',
    STARTS AS 'Starts',
    ENDS AS 'Ends',
    ON_COMPLETION AS 'On Completion',
    DEFINER AS 'Definer',
    CREATED AS 'Created',
    LAST_ALTERED AS 'Modified',
    LAST_EXECUTED AS 'Last Executed'
FROM information_schema.EVENTS
WHERE EVENT_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
ORDER BY EVENT_SCHEMA, EVENT_NAME;
```

### 4.7 Проверка views

```sql
SELECT 
    TABLE_SCHEMA AS 'Database',
    TABLE_NAME AS 'View Name',
    DEFINER AS 'Definer',
    SECURITY_TYPE AS 'Security',
    IS_UPDATABLE AS 'Updatable',
    CHECK_OPTION AS 'Check Option'
FROM information_schema.VIEWS
WHERE TABLE_SCHEMA NOT IN ('mysql', 'information_schema', 'performance_schema', 'sys')
ORDER BY TABLE_SCHEMA, TABLE_NAME;
```

---

## 5. Проверка репликации

### 5.1 Определение топологии репликации

Первый шаг — понять, используется ли репликация и какая топология.

```bash
# Проверка: является ли этот сервер Master
mysql -u audit -p -e "SHOW MASTER STATUS\G"

# Проверка: является ли этот сервер Slave
mysql -u audit -p -e "SHOW SLAVE STATUS\G"
```

**Возможные топологии:**

#### Standalone (нет репликации)
```
┌─────────────┐
│   MySQL     │
│  Standalone │
└─────────────┘
```

#### Master-Slave
```
┌─────────┐
│  Master │
└────┬────┘
     │
     ├──────┬──────┐
     ▼      ▼      ▼
┌────────┐┌────────┐┌────────┐
│ Slave1 ││ Slave2 ││ Slave3 │
└────────┘└────────┘└────────┘
```

#### Master-Master
```
┌─────────┐ ←→ ┌─────────┐
│ Master1 │    │ Master2 │
└─────────┘    └─────────┘
```

#### Multi-Source Replication
```
┌─────────┐    ┌─────────┐
│ Master1 │    │ Master2 │
└────┬────┘    └────┬────┘
     │              │
     └──────┬───────┘
            ▼
       ┌─────────┐
       │  Slave  │
       └─────────┘
```

### 5.2 Анализ Master статуса

Если это Master сервер:

```sql
-- Текущий статус master
SHOW MASTER STATUS;

-- Список подключенных slave серверов
SHOW SLAVE HOSTS;

-- Binary log файлы
SHOW BINARY LOGS;
```

**Пример вывода SHOW MASTER STATUS:**
```plaintext
+--------------------+----------+--------------+------------------+-------------------+
| File               | Position | Binlog_Do_DB | Binlog_Ignore_DB | Executed_Gtid_Set |
+--------------------+----------+--------------+------------------+-------------------+
| mysql-bin.000023   | 45678901 | production   |                  | uuid:1-1234567    |
+--------------------+----------+--------------+------------------+-------------------+
```

**Важные параметры для документирования:**
- **File**: Текущий binlog файл
- **Position**: Позиция в файле
- **Executed_Gtid_Set**: Если используется GTID

### 5.3 Анализ Slave статуса

Если это Slave сервер:

```sql
SHOW SLAVE STATUS\G
```

**Критически важные параметры:**

```plaintext
*************************** 1. row ***************************
               Slave_IO_State: Waiting for master to send event
                  Master_Host: 192.168.1.100
                  Master_User: repl
                  Master_Port: 3306
                Connect_Retry: 60
              Master_Log_File: mysql-bin.000023
          Read_Master_Log_Pos: 45678901
               Relay_Log_File: mysql-relay-bin.000015
                Relay_Log_Pos: 12345678
        Relay_Master_Log_File: mysql-bin.000023
             Slave_IO_Running: Yes                    ← Должно быть Yes
            Slave_SQL_Running: Yes                    ← Должно быть Yes
              Replicate_Do_DB: production,analytics
          Replicate_Ignore_DB: 
           Replicate_Do_Table: 
       Replicate_Ignore_Table: 
      Replicate_Wild_Do_Table: 
  Replicate_Wild_Ignore_Table: 
                   Last_Errno: 0                       ← Должно быть 0
                   Last_Error:                         ← Должно быть пусто
                 Skip_Counter: 0
          Exec_Master_Log_Pos: 45678901
              Relay_Log_Space: 23456789
        Seconds_Behind_Master: 0                       ← Должно быть 0 или малое число
                Last_IO_Errno: 0
                Last_IO_Error: 
               Last_SQL_Errno: 0
               Last_SQL_Error: 
         Executed_Gtid_Set: uuid:1-1234567
            Auto_Position: 1
     Replicate_Rewrite_DB: 
             Channel_Name: 
```

### 5.4 Проверка GTID

```sql
-- MySQL
SELECT @@gtid_mode;
SELECT @@gtid_executed;

-- Проверка пробелов в GTID
SELECT @@gtid_purged;
```

**⚠️ Важно:** MySQL и MariaDB используют **несовместимые** реализации GTID!

| Параметр | MySQL | MariaDB | Совместимость |
|----------|-------|---------|---------------|
| GTID Format | UUID:transaction_id | domain-server-sequence | ❌ Несовместимо |
| Переменная | `gtid_mode` | `gtid_strict_mode` | Разные |
| Executed | `@@gtid_executed` | `@@gtid_current_pos` | Разные |

**Следствие:** Нельзя сделать MariaDB slave'ом MySQL master'а через GTID. Нужно использовать position-based репликацию.

### 5.5 Анализ binlog формата

```sql
SELECT @@binlog_format;
```

**Типы binlog форматов:**

| Format | Описание | Рекомендация |
|--------|----------|--------------|
| **STATEMENT** | Логирует SQL команды | Устарело, не рекомендуется |
| **ROW** | Логирует изменения строк | ✅ Рекомендуется |
| **MIXED** | Комбинация STATEMENT и ROW | Возможны несогласованности |

**Для миграции:** Убедитесь, что используется **ROW** формат — он наиболее безопасен.

### 5.6 Документирование репликации

```bash
#!/bin/bash
# document_replication.sh

cat > replication_doc_$(date +%Y%m%d).md << 'EOF'
# MySQL Replication Documentation

## Topology
[Нарисуйте топологию]

## Master Configuration
EOF

# Master status
echo "### Master Status" >> replication_doc_$(date +%Y%m%d).md
mysql -u audit -p -e "SHOW MASTER STATUS\G" >> replication_doc_$(date +%Y%m%d).md

# Slave status (если это slave)
echo -e "\n### Slave Status" >> replication_doc_$(date +%Y%m%d).md
mysql -u audit -p -e "SHOW SLAVE STATUS\G" >> replication_doc_$(date +%Y%m%d).md

# Binary log files
echo -e "\n### Binary Logs" >> replication_doc_$(date +%Y%m%d).md
mysql -u audit -p -e "SHOW BINARY LOGS;" >> replication_doc_$(date +%Y%m%d).md

echo "Replication documentation created"
```

---

*Продолжение главы в следующем ответе из-за ограничения длины...*

**Следующие разделы:**
- 6. Инвентаризация конфигурации
- 7. Анализ производительности
- 8. Проверка зависимостей приложений
- 9. Оценка совместимости
- 10. Создание итогового отчета

Продолжить создание оставшейся части Главы 1?