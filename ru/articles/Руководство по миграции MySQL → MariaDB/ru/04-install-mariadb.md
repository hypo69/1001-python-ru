# ГЛАВА 4: Установка MariaDB Server

> **Цель главы:** Установить и выполнить первичную настройку MariaDB

[← Предыдущая глава](./03-prepare-infrastructure.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./05-import-data.md)

---

## Содержание

1. [Установка пакетов](#1-установка-пакетов)
2. [Первый запуск](#2-первый-запуск)
3. [Настройка root доступа](#3-настройка-root-доступа)
4. [Базовая конфигурация](#4-базовая-конфигурация)
5. [Проверка установки](#5-проверка-установки)

---

## 1. Установка пакетов

### 1.1 Основная установка

```bash
#!/bin/bash
# install_mariadb.sh

echo "[$(date)] Installing MariaDB..."

# Обновить индекс пакетов
sudo apt update

# Установить MariaDB Server и Client
sudo apt install -y \
    mariadb-server \
    mariadb-client \
    mariadb-backup

# Опциональные компоненты
sudo apt install -y \
    mariadb-plugin-rocksdb \
    mariadb-plugin-connect

echo "✅ MariaDB installed"
mariadb --version
```

### 1.2 Для Galera Cluster

```bash
# Если планируется кластер
sudo apt install -y galera-4 mariadb-plugin-galera
```

---

## 2. Первый запуск

### 2.1 Запуск сервиса

```bash
# Включить автозапуск
sudo systemctl enable mariadb

# Запустить
sudo systemctl start mariadb

# Проверить статус
sudo systemctl status mariadb
```

### 2.2 Проверка подключения

```bash
# Подключиться как root
sudo mariadb

# Внутри MariaDB
MariaDB> SELECT VERSION();
MariaDB> SHOW DATABASES;
MariaDB> EXIT;
```

---

## 3. Настройка root доступа

### 3.1 Установка пароля для root

```bash
# Изменить плагин аутентификации
sudo mariadb << EOF
ALTER USER 'root'@'localhost' IDENTIFIED BY 'StrongRootPassword123!';
FLUSH PRIVILEGES;
EOF

# Теперь подключение с паролем
mariadb -u root -p
```

### 3.2 Создание admin пользователя

```sql
CREATE USER 'admin'@'localhost' IDENTIFIED BY 'AdminPass123!';
GRANT ALL PRIVILEGES ON *.* TO 'admin'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
```

---

## 4. Базовая конфигурация

### 4.1 Основной конфиг

```bash
sudo tee /etc/mysql/mariadb.conf.d/50-server.cnf << 'EOF'
[mysqld]

# Basic Settings
user                    = mysql
pid-file                = /run/mysqld/mysqld.pid
socket                  = /run/mysqld/mysqld.sock
port                    = 3306
basedir                 = /usr
datadir                 = /var/lib/mysql
tmpdir                  = /tmp

# Network
bind-address            = 0.0.0.0
max_connections         = 200
connect_timeout         = 10
wait_timeout            = 600
max_allowed_packet      = 64M

# InnoDB
default_storage_engine  = InnoDB
innodb_buffer_pool_size = 1G
innodb_log_file_size    = 256M
innodb_flush_log_at_trx_commit = 2
innodb_flush_method     = O_DIRECT
innodb_file_per_table   = 1

# Logging
log_error               = /var/log/mysql/error.log
slow_query_log          = 1
slow_query_log_file     = /var/log/mysql/slow.log
long_query_time         = 2

# Character Set
character-set-server    = utf8mb4
collation-server        = utf8mb4_unicode_ci

[client]
port                    = 3306
socket                  = /run/mysqld/mysqld.sock
default-character-set   = utf8mb4
EOF
```

### 4.2 Перезапуск с новым конфигом

```bash
# Проверить синтаксис
sudo mariadbd --validate-config

# Перезапустить
sudo systemctl restart mariadb
sudo systemctl status mariadb
```

---

## 5. Проверка установки

### 5.1 Базовые проверки

```bash
# Версия
mariadb --version

# Статус
sudo systemctl status mariadb

# Порт
sudo netstat -tlnp | grep 3306

# Переменные
mariadb -u root -p -e "SHOW VARIABLES LIKE 'version%';"
```

### 5.2 Чек-лист

- [ ] MariaDB установлен
- [ ] Сервис запущен
- [ ] Root пароль установлен
- [ ] Конфигурация применена
- [ ] Порт 3306 слушает
- [ ] Подключение работает

---

## Следующий шаг

**[→ ГЛАВА 5: Импорт данных из MySQL](./05-import-data.md)**
