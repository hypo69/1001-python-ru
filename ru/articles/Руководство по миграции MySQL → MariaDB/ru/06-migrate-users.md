# ГЛАВА 6: Миграция пользователей и привилегий

> **Цель главы:** Восстановить пользователей и их привилегии

[← Предыдущая глава](./05-import-data.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./07-testing.md)

---

## Содержание

1. [Экспорт пользователей](#1-экспорт-пользователей)
2. [Импорт в MariaDB](#2-импорт-в-mariadb)
3. [Обработка плагинов](#3-обработка-плагинов)
4. [Настройка ролей](#4-настройка-ролей)
5. [Проверка доступа](#5-проверка-доступа)

---

## 1. Экспорт пользователей

### 1.1 Экспорт с MySQL сервера

```bash
#!/bin/bash
# export_users.sh

# Percona Toolkit (рекомендуется)
pt-show-grants --host=localhost --user=root --password > users.sql
```

---

## 2. Импорт в MariaDB

### 2.1 Базовый импорт

```bash
# Импорт пользователей
mariadb -u root -p < users.sql

# Проверка
mariadb -u root -p -e "SELECT User, Host, plugin FROM mysql.user;"
```

---

## 3. Обработка плагинов

### 3.1 Конвертация caching_sha2_password

```sql
-- Найти пользователей с sha2
SELECT User, Host, plugin 
FROM mysql.user 
WHERE plugin = 'caching_sha2_password';

-- Конвертировать
ALTER USER 'username'@'host' 
IDENTIFIED WITH mysql_native_password BY 'newpassword';
```

---

## 4. Настройка ролей

### 4.1 Создание ролей (MariaDB 10.1+)

```sql
-- Создать роли
CREATE ROLE developer;
GRANT SELECT, INSERT, UPDATE, DELETE ON app_db.* TO developer;

CREATE ROLE analyst;
GRANT SELECT ON app_db.* TO analyst;

-- Назначить роли
GRANT developer TO 'john'@'%';
SET DEFAULT ROLE developer FOR 'john'@'%';

FLUSH PRIVILEGES;
```

---

## 5. Проверка доступа

### 5.1 Тест подключений

```bash
#!/bin/bash
# test_user_connections.sh

# Файл: username:password:host
while IFS=: read user pass host; do
    echo "Testing: $user@$host"
    mariadb -h "$host" -u "$user" -p"$pass" -e "SELECT 'OK';" 2>&1
done < users_test.txt
```

---

## Чек-лист

- [ ] Пользователи экспортированы
- [ ] Импорт в MariaDB выполнен
- [ ] Плагины совместимы
- [ ] Роли настроены
- [ ] Доступ протестирован

---

**[→ ГЛАВА 7: Тестирование миграции](./07-testing.md)**
