# ГЛАВА 7: Проверка и тестирование миграции

> **Цель главы:** Убедиться в успешности миграции

[← Предыдущая глава](./06-migrate-users.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./08-performance-tuning.md)

---

## Содержание

1. [Проверка данных](#1-проверка-данных)
2. [Функциональное тестирование](#2-функциональное-тестирование)
3. [Нагрузочное тестирование](#3-нагрузочное-тестирование)
4. [Тестирование приложений](#4-тестирование-приложений)
5. [Анализ логов](#5-анализ-логов)

---

## 1. Проверка данных

### 1.1 Сравнение количества записей

```sql
-- Подсчет записей в таблицах
SELECT 
    table_schema,
    table_name,
    table_rows
FROM information_schema.tables
WHERE table_schema NOT IN ('information_schema', 'mysql', 'performance_schema')
ORDER BY table_schema, table_name;
```

### 1.2 Проверка контрольных сумм

```bash
# CHECKSUM таблиц
mariadb -u root -p production_db -e "CHECKSUM TABLE users, orders, products;"
```

---

## 2. Функциональное тестирование

### 2.1 Проверка stored procedures

```sql
-- Список процедур
SELECT ROUTINE_SCHEMA, ROUTINE_NAME, ROUTINE_TYPE
FROM information_schema.ROUTINES
WHERE ROUTINE_SCHEMA NOT IN ('mysql', 'information_schema');

-- Тест выполнения
CALL test_procedure(1);
```

### 2.2 Проверка triggers

```sql
-- Список триггеров
SHOW TRIGGERS FROM production_db;

-- Тест триггера
INSERT INTO test_table (name) VALUES ('test');
SELECT * FROM log_table ORDER BY created_at DESC LIMIT 1;
```

---

## 3. Нагрузочное тестирование

### 3.1 Sysbench тест

```bash
# Подготовка
sysbench /usr/share/sysbench/oltp_read_write.lua \
    --mysql-host=localhost \
    --mysql-user=root \
    --mysql-password=password \
    --mysql-db=sbtest \
    --tables=10 \
    --table-size=100000 \
    prepare

# Запуск теста
sysbench /usr/share/sysbench/oltp_read_write.lua \
    --mysql-host=localhost \
    --mysql-user=root \
    --mysql-password=password \
    --mysql-db=sbtest \
    --tables=10 \
    --threads=10 \
    --time=60 \
    run
```

---

## 4. Тестирование приложений

### 4.1 Smoke tests

```bash
#!/bin/bash
# app_smoke_tests.sh

echo "=== Application Smoke Tests ==="

# Web API
curl -f http://localhost:8000/health || echo "❌ API failed"

# Worker
systemctl status app-worker | grep "active (running)"

echo "=== Tests Complete ==="
```

---

## 5. Анализ логов

### 5.1 Проверка error log

```bash
# Ошибки за последний час
sudo grep -i error /var/log/mysql/error.log | tail -50

# Критичные ошибки
sudo grep -iE 'fatal|crash|corruption' /var/log/mysql/error.log
```

### 5.2 Slow queries

```bash
# Топ медленных запросов
sudo mysqldumpslow -s t -t 10 /var/log/mysql/slow.log
```

---

## Чек-лист

- [ ] Данные целостны
- [ ] Stored routines работают
- [ ] Triggers функционируют
- [ ] Нагрузочные тесты пройдены
- [ ] Приложения работают
- [ ] Логи чисты

---

**[→ ГЛАВА 8: Оптимизация производительности](./08-performance-tuning.md)**
