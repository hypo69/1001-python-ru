# ГЛАВА 9: Настройка безопасности

> **Цель главы:** Защитить MariaDB от несанкционированного доступа

[← Предыдущая глава](./08-performance-tuning.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./10-replication-clustering.md)

---

## Содержание

1. [Базовая защита](#1-базовая-защита)
2. [Управление пользователями](#2-управление-пользователями)
3. [SSL/TLS шифрование](#3-ssltls-шифрование)
4. [Audit logging](#4-audit-logging)
5. [Firewall и сеть](#5-firewall-и-сеть)
6. [Best practices](#6-best-practices)

---

## 1. Базовая защита

### 1.1 mariadb-secure-installation

```bash
# Запуск интерактивной настройки
sudo mariadb-secure-installation
```

**Выполняемые действия:**
```plaintext
1. Установка пароля root
2. Удаление anonymous пользователей
3. Запрет удаленного root доступа
4. Удаление тестовой базы
5. Перезагрузка таблиц привилегий
```

### 1.2 Автоматическая настройка

```bash
#!/bin/bash
# secure_mariadb.sh

mysql -u root << EOF
# Удалить anonymous пользователей
DELETE FROM mysql.user WHERE User='';

# Удалить remote root
DELETE FROM mysql.user WHERE User='root' AND Host NOT IN ('localhost', '127.0.0.1', '::1');

# Удалить test базу
DROP DATABASE IF EXISTS test;
DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%';

# Применить изменения
FLUSH PRIVILEGES;
EOF

echo "✅ MariaDB secured"
```

---

## 2. Управление пользователями

### 2.1 Принцип минимальных привилегий

```sql
-- ❌ Плохо
GRANT ALL PRIVILEGES ON *.* TO 'user'@'%';

-- ✅ Хорошо
GRANT SELECT, INSERT, UPDATE, DELETE ON app_db.* TO 'app_user'@'192.168.1.%';
```

### 2.2 Создание пользователей для разных целей

```sql
-- Приложение
CREATE USER 'app_user'@'192.168.1.%' IDENTIFIED BY 'AppPass123!';
GRANT SELECT, INSERT, UPDATE, DELETE ON app_db.* TO 'app_user'@'192.168.1.%';

-- Read-only для отчетов
CREATE USER 'reports'@'10.0.0.%' IDENTIFIED BY 'ReportsPass123!';
GRANT SELECT ON app_db.* TO 'reports'@'10.0.0.%';

-- Backup
CREATE USER 'backup'@'localhost' IDENTIFIED BY 'BackupPass123!';
GRANT SELECT, RELOAD, LOCK TABLES, REPLICATION CLIENT ON *.* TO 'backup'@'localhost';

FLUSH PRIVILEGES;
```

### 2.3 Ограничение ресурсов

```sql
-- Ограничить подключения и запросы
ALTER USER 'app_user'@'192.168.1.%' 
    WITH MAX_USER_CONNECTIONS 50
         MAX_QUERIES_PER_HOUR 10000
         MAX_UPDATES_PER_HOUR 5000;
```

---

## 3. SSL/TLS шифрование

### 3.1 Генерация сертификатов

```bash
#!/bin/bash
# generate_ssl_certs.sh

CERT_DIR="/etc/mysql/certs"
sudo mkdir -p "$CERT_DIR"

# CA сертификат
sudo openssl genrsa 2048 > "$CERT_DIR/ca-key.pem"
sudo openssl req -new -x509 -nodes -days 3650 \
    -key "$CERT_DIR/ca-key.pem" \
    -out "$CERT_DIR/ca.pem" \
    -subj "/C=US/ST=State/L=City/O=Company/CN=MariaDB-CA"

# Серверный сертификат
sudo openssl req -newkey rsa:2048 -days 3650 -nodes \
    -keyout "$CERT_DIR/server-key.pem" \
    -out "$CERT_DIR/server-req.pem" \
    -subj "/C=US/ST=State/L=City/O=Company/CN=mariadb-server"

sudo openssl rsa -in "$CERT_DIR/server-key.pem" \
    -out "$CERT_DIR/server-key.pem"

sudo openssl x509 -req -in "$CERT_DIR/server-req.pem" \
    -days 3650 -CA "$CERT_DIR/ca.pem" \
    -CAkey "$CERT_DIR/ca-key.pem" -set_serial 01 \
    -out "$CERT_DIR/server-cert.pem"

# Клиентский сертификат
sudo openssl req -newkey rsa:2048 -days 3650 -nodes \
    -keyout "$CERT_DIR/client-key.pem" \
    -out "$CERT_DIR/client-req.pem" \
    -subj "/C=US/ST=State/L=City/O=Company/CN=mariadb-client"

sudo openssl rsa -in "$CERT_DIR/client-key.pem" \
    -out "$CERT_DIR/client-key.pem"

sudo openssl x509 -req -in "$CERT_DIR/client-req.pem" \
    -days 3650 -CA "$CERT_DIR/ca.pem" \
    -CAkey "$CERT_DIR/ca-key.pem" -set_serial 02 \
    -out "$CERT_DIR/client-cert.pem"

# Права
sudo chown -R mysql:mysql "$CERT_DIR"
sudo chmod 600 "$CERT_DIR"/*.pem

echo "✅ SSL certificates generated"
```

### 3.2 Настройка SSL в конфиге

```ini
[mysqld]
# SSL Configuration
ssl-ca   = /etc/mysql/certs/ca.pem
ssl-cert = /etc/mysql/certs/server-cert.pem
ssl-key  = /etc/mysql/certs/server-key.pem

# Требовать SSL для всех (опционально)
require_secure_transport = ON
```

### 3.3 Проверка SSL

```bash
# Перезапустить MariaDB
sudo systemctl restart mariadb

# Проверить SSL
mariadb -u root -p -e "SHOW VARIABLES LIKE '%ssl%';"

# Тест подключения с SSL
mariadb -u root -p \
    --ssl-ca=/etc/mysql/certs/ca.pem \
    --ssl-cert=/etc/mysql/certs/client-cert.pem \
    --ssl-key=/etc/mysql/certs/client-key.pem \
    -e "STATUS" | grep SSL
```

### 3.4 Требовать SSL для пользователей

```sql
-- Требовать SSL
ALTER USER 'app_user'@'%' REQUIRE SSL;

-- Требовать конкретный сертификат
ALTER USER 'admin'@'%' REQUIRE 
    SUBJECT '/C=US/ST=State/O=Company/CN=admin'
    AND ISSUER '/C=US/ST=State/O=Company/CN=MariaDB-CA';

FLUSH PRIVILEGES;
```

---

## 4. Audit logging

### 4.1 Установка Audit Plugin

```bash
# Установить плагин
sudo apt install mariadb-plugin-audit -y

# Включить
mariadb -u root -p -e "INSTALL SONAME 'server_audit';"
```

### 4.2 Конфигурация Audit

```ini
# /etc/mysql/mariadb.conf.d/50-server.cnf

[mysqld]
# Server Audit Plugin
plugin-load-add = server_audit
server_audit_logging = ON
server_audit_events = CONNECT,QUERY_DDL,QUERY_DML
server_audit_output_type = FILE
server_audit_file_path = /var/log/mysql/audit.log
server_audit_file_rotate_size = 1000000
server_audit_file_rotations = 9
```

### 4.3 Анализ audit логов

```bash
# Просмотр
sudo tail -f /var/log/mysql/audit.log

# Поиск failed logins
sudo grep "ACCESS DENIED" /var/log/mysql/audit.log

# Поиск DROP команд
sudo grep "DROP" /var/log/mysql/audit.log
```

---

## 5. Firewall и сеть

### 5.1 UFW правила

```bash
#!/bin/bash
# configure_firewall.sh

# Разрешить только с определенных сетей
sudo ufw allow from 192.168.1.0/24 to any port 3306 proto tcp

# Или конкретные хосты
sudo ufw allow from 192.168.1.100 to any port 3306 proto tcp
sudo ufw allow from 192.168.1.101 to any port 3306 proto tcp

# Проверить
sudo ufw status numbered
```

### 5.2 Ограничение bind-address

```ini
[mysqld]
# Слушать только на внутреннем интерфейсе
bind-address = 10.0.0.5

# Или только localhost
bind-address = 127.0.0.1
```

---

## 6. Best practices

### 6.1 Скрипт проверки безопасности

```bash
#!/bin/bash
# security_audit.sh

echo "=== MariaDB Security Audit ==="

# Пользователи без пароля
echo -e "\n1. Users without password:"
mariadb -u root -p -e "
SELECT User, Host FROM mysql.user 
WHERE authentication_string = '';"

# Пользователи с '%' host
echo -e "\n2. Users with '%' host:"
mariadb -u root -p -e "
SELECT User, Host FROM mysql.user 
WHERE Host = '%';"

# Старые плагины
echo -e "\n3. Users with old password plugins:"
mariadb -u root -p -e "
SELECT User, Host, plugin FROM mysql.user 
WHERE plugin = 'mysql_old_password';"

# SSL статус
echo -e "\n4. SSL Status:"
mariadb -u root -p -e "SHOW VARIABLES LIKE '%ssl%';"

echo -e "\n=== Audit Complete ==="
```

### 6.2 Регулярные проверки

```bash
# Добавить в cron для ежедневной проверки
0 2 * * * /usr/local/bin/security_audit.sh > /var/log/mariadb_security_audit.log
```

---

## Чек-лист

### ✅ Обязательные действия

- [ ] mariadb-secure-installation выполнен
- [ ] Root пароль установлен
- [ ] Anonymous пользователи удалены
- [ ] Test база удалена
- [ ] SSL/TLS настроен
- [ ] Audit logging включен
- [ ] Firewall настроен
- [ ] Пользователи следуют принципу минимальных привилегий
- [ ] Регулярный security audit настроен

### 🔒 Проверки безопасности

- [ ] Нет пользователей без пароля
- [ ] Нет пользователей с Host='%'
- [ ] SSL работает
- [ ] Audit логи пишутся
- [ ] Firewall блокирует нежелательный доступ

---

## Следующий шаг

**[→ ГЛАВА 10: Репликация и кластеризация](./10-replication-clustering.md)**

В следующей главе:
- Master-Slave репликация
- Master-Master репликация
- Galera Cluster
- Мониторинг репликации