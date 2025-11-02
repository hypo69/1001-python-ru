# ГЛАВА 5: Импорт данных из MySQL

> **Цель главы:** Восстановить данные из MySQL бэкапа в MariaDB

[← Предыдущая глава](./04-install-mariadb.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./06-migrate-users.md)

---

## Содержание

1. [Подготовка дампа](#1-подготовка-дампа)
2. [Импорт данных](#2-импорт-данных)
3. [Оптимизация импорта](#3-оптимизация-импорта)
4. [Обработка ошибок](#4-обработка-ошибок)
5. [Проверка целостности](#5-проверка-целостности)
6. [Обновление системных таблиц](#6-обновление-системных-таблиц)

---

## 1. Подготовка дампа

### 1.1 Распаковка и проверка

```bash
#!/bin/bash
# prepare_dump.sh

DUMP_FILE="/backup/mysql/full_backup_20251101.sql.gz"
WORK_FILE="/tmp/import.sql"

# Распаковать
gunzip -c "$DUMP_FILE" > "$WORK_FILE"

# Проверить размер
ls -lh "$WORK_FILE"

# Проверить содержимое
head -n 50 "$WORK_FILE"
```

### 1.2 Очистка DEFINER

```bash
# Удалить все DEFINER из дампа
sed -i 's/DEFINER=[^ ]*//g' /tmp/import.sql

# Или заменить на current user
sed -i 's/DEFINER=[^ ]*/DEFINER=CURRENT_USER/g' /tmp/import.sql
```

---

## 2. Импорт данных

### 2.1 Базовый импорт

```bash
# Простой импорт
mariadb -u root -p < /tmp/import.sql

# С логированием
mariadb -u root -p < /tmp/import.sql 2>&1 | tee import.log
```

### 2.2 Импорт с прогрессом

```bash
# Установить pv
sudo apt install pv -y

# Импорт с прогресс-баром
pv /tmp/import.sql | mariadb -u root -p
```

---

## 3. Оптимизация импорта

### 3.1 Временные настройки

```sql
-- Перед импортом
SET GLOBAL innodb_flush_log_at_trx_commit = 0;
SET GLOBAL foreign_key_checks = 0;
SET GLOBAL unique_checks = 0;
SET GLOBAL sql_log_bin = 0;

-- Импортировать
SOURCE /tmp/import.sql;

-- Вернуть настройки
SET GLOBAL innodb_flush_log_at_trx_commit = 1;
SET GLOBAL foreign_key_checks = 1;
SET GLOBAL unique_checks = 1;
SET GLOBAL sql_log_bin = 1;
```

---

## 4. Обработка ошибок

### 4.1 Частые ошибки

**ERROR 1227: Access denied**
```bash
# Решение: удалить DEFINER
sed -i 's/DEFINER=[^ ]*//g' /tmp/import.sql
```

**ERROR 1215: Cannot add foreign key**
```sql
SET FOREIGN_KEY_CHECKS=0;
SOURCE /tmp/import.sql;
SET FOREIGN_KEY_CHECKS=1;
```

---

## 5. Проверка целостности

### 5.1 Проверка баз данных

```sql
SELECT 
    table_schema AS 'Database',
    ROUND(SUM(data_length + index_length) / 1024 / 1024, 2) AS 'Size (MB)',
    COUNT(*) AS 'Tables'
FROM information_schema.tables
GROUP BY table_schema
ORDER BY SUM(data_length + index_length) DESC;
```

### 5.2 Сравнение с оригиналом

```sql
-- Количество записей в ключевых таблицах
SELECT COUNT(*) FROM production_db.users;
SELECT COUNT(*) FROM production_db.orders;

-- Проверка дат
SELECT 
    MIN(created_at) AS oldest,
    MAX(created_at) AS newest
FROM production_db.users;
```

---

## 6. Обновление системных таблиц

### 6.1 Запуск mariadb-upgrade

```bash
# Обновить системные таблицы
sudo mariadb-upgrade -u root -p

# С подробным выводом
sudo mariadb-upgrade -u root -p --verbose

# Принудительно
sudo mariadb-upgrade -u root -p --force
```

---

## Чек-лист

- [ ] Дамп подготовлен
- [ ] DEFINER очищен
- [ ] Данные импортированы
- [ ] Ошибок нет
- [ ] Целостность проверена
- [ ] mariadb-upgrade выполнен

---

**[→ ГЛАВА 6: Миграция пользователей](./06-migrate-users.md)**
