# ГЛАВА 8: Оптимизация производительности

> **Цель главы:** Настроить MariaDB для оптимальной производительности

[← Предыдущая глава](./07-testing.md) | [Назад к оглавлению](./00-INDEX.md) | [Следующая глава →](./09-security.md)

---

## Содержание

1. [Расчет параметров](#1-расчет-параметров)
2. [Оптимизация InnoDB](#2-оптимизация-innodb)
3. [Настройка кэширования](#3-настройка-кэширования)
4. [Оптимизация памяти](#4-оптимизация-памяти)
5. [Настройки сети](#5-настройки-сети)

---

## 1. Расчет параметров

### 1.1 Автоматический расчет

```bash
#!/bin/bash
# calculate_settings.sh

TOTAL_RAM_MB=$(free -m | grep Mem | awk '{print $2}')
CPU_CORES=$(nproc)

# 70% RAM для InnoDB buffer pool
INNODB_BUFFER=$((TOTAL_RAM_MB * 70 / 100))

# 50 соединений на ядро
MAX_CONNECTIONS=$((CPU_CORES * 50))

cat << EOF
=== Recommended Settings ===
Total RAM: ${TOTAL_RAM_MB}MB
CPU Cores: ${CPU_CORES}

innodb_buffer_pool_size = ${INNODB_BUFFER}M
max_connections = ${MAX_CONNECTIONS}
thread_cache_size = $((MAX_CONNECTIONS / 4))
table_open_cache = $((MAX_CONNECTIONS * 2))
