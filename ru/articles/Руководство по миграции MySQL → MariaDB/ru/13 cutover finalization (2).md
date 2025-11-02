
# ГЛАВА 13: Переключение на production и финализация

> **Цель главы:** Безопасно переключиться на MariaDB и завершить миграцию

[← Предыдущая глава](./12-monitoring-maintenance.md) | [Назад к оглавлению](./00-INDEX.md)

---

## Содержание

1. [Чек-лист перед переключением](#1-чек-лист-перед-переключением)
2. [Обновление конфигураций](#2-обновление-конфигураций)
3. [Production cutover](#3-production-cutover)
4. [Мониторинг после миграции](#4-мониторинг-после-миграции)
5. [План отката](#5-план-отката)
6. [Отключение MySQL](#6-отключение-mysql)
7. [Финальная документация](#7-финальная-документация)

---

## 1. Чек-лист перед переключением

### 1.1 Pre-Cutover Checklist (за 1 неделю)

```markdown
# Production Cutover Checklist

## Техническая готовность
- [ ] Все тесты пройдены успешно
- [ ] Полный бэкап создан и проверен
- [ ] Тестовая миграция выполнена
- [ ] Мониторинг настроен и работает
- [ ] План отката готов и протестирован
- [ ] Disaster recovery план документирован

## Организационная готовность
- [ ] Команда уведомлена о дате/времени
- [ ] Окно техобслуживания согласовано
- [ ] Stakeholders информированы
- [ ] Документация обновлена
- [ ] Контакты дежурной команды актуальны

## Инфраструктура
- [ ] DNS записи подготовлены
- [ ] Load balancer сконфигурирован
- [ ] Firewall правила обновлены
- [ ] SSL сертификаты валидны
- [ ] Мониторинг alertы настроены

## Приложения
- [ ] Все приложения протестированы с MariaDB
- [ ] Драйверы обновлены
- [ ] Connection strings подготовлены
- [ ] Graceful shutdown реализован
- [ ] Rollback процедура задокументирована
```

### 1.2 Go/No-Go критерии

```plaintext
КРИТЕРИИ ДЛЯ GO (продолжения миграции):

✅ Все системы зеленые
✅ Бэкап успешно восстановлен на тесте
✅ Все критичные баги исправлены
✅ Команда полностью готова
✅ Погода (нет других критичных изменений)

КРИТЕРИИ ДЛЯ NO-GO (отмены миграции):

❌ Проблемы с бэкапами
❌ Критичные баги не исправлены
❌ Недостаточно персонала
❌ Другие критичные изменения в тот же день
❌ Проблемы с тестовой миграцией
```

---

## 2. Обновление конфигураций

### 2.1 Скрипт обновления DSN

```bash
#!/bin/bash
# update_app_configs.sh

OLD_HOST="mysql.company.local"
NEW_HOST="mariadb.company.local"

CONFIG_FILES=(
    "/etc/webapp/database.yml"
    "/etc/api/config.json"
    "/etc/worker/settings.ini"
)

for file in "${CONFIG_FILES[@]}"; do
    if [ -f "$file" ]; then
        echo "Updating: $file"
        
        # Бэкап
        cp "$file" "${file}.backup_$(date +%Y%m%d)"
        
        # Замена
        sed -i "s/$OLD_HOST/$NEW_HOST/g" "$file"
        
        echo "✅ Updated: $file"
    else
        echo "⚠️  Not found: $file"
    fi
done

echo "All configs updated. Review and restart applications."
```

### 2.2 Обновление DNS

```bash
#!/bin/bash
# update_dns.sh

# 1. За день до миграции: уменьшить TTL
# mysql.company.local TTL 3600 → 60

# 2. В день миграции: обновить A-record
# mysql.company.local → 192.168.1.200 (новый MariaDB IP)

# 3. Проверить обновление
dig mysql.company.local +short

# 4. После миграции: вернуть TTL
# mysql.company.local TTL 60 → 3600
```

---

## 3. Production cutover

### 3.1 Пошаговая процедура

```bash
#!/bin/bash
# production_cutover.sh

LOG_FILE="/var/log/mariadb_cutover.log"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== PRODUCTION CUTOVER STARTED ==="
log "Timestamp: $TIMESTAMP"

# === ФАЗА 1: ПОДГОТОВКА (15 минут) ===
log "PHASE 1: Preparation"

# 1.1 Установить read-only на MySQL
log "Setting MySQL to read-only..."
mysql -u root -p << EOF
SET GLOBAL read_only = ON;
SET GLOBAL super_read_only = ON;
FLUSH TABLES WITH READ LOCK;
EOF

if [ $? -ne 0 ]; then
    log "❌ FAILED to set read-only"
    exit 1
fi

# 1.2 Подождать завершения транзакций
log "Waiting for active transactions..."
sleep 30

ACTIVE_TRX=$(mysql -u root -p -N -e "SELECT COUNT(*) FROM information_schema.innodb_trx;")
log "Active transactions: $ACTIVE_TRX"

# 1.3 Финальный snapshot
log "Creating final snapshot..."
mysqldump --all-databases --single-transaction > "/backup/final_snapshot_$TIMESTAMP.sql"

# === ФАЗА 2: ОСТАНОВКА ПРИЛОЖЕНИЙ (5 минут) ===
log "PHASE 2: Stopping applications"

systemctl stop webapp
systemctl stop api-server
systemctl stop worker

log "Applications stopped"

# === ФАЗА 3: ПЕРЕКЛЮЧЕНИЕ (5 минут) ===
log "PHASE 3: Cutover"

# 3.1 Обновить конфигурации
log "Updating configurations..."
./update_app_configs.sh

# 3.2 Обновить DNS (если используется)
log "Updating DNS..."
# ./update_dns.sh

# 3.3 Обновить load balancer
log "Updating load balancer..."
# Переключить backend с MySQL на MariaDB

# === ФАЗА 4: ЗАПУСК НА MARIADB (10 минут) ===
log "PHASE 4: Starting on MariaDB"

# 4.1 Финальная проверка MariaDB
if ! mariadb -u root -p -e "SELECT 1;" > /dev/null 2>&1; then
    log "❌ MariaDB not responding!"
    log "ABORTING CUTOVER"
    exit 1
fi

# 4.2 Запустить приложения
log "Starting applications on MariaDB..."
systemctl start webapp
sleep 5
systemctl start api-server
sleep 5
systemctl start worker

# === ФАЗА 5: ПРОВЕРКА (15 минут) ===
log "PHASE 5: Verification"

# 5.1 Smoke tests
log "Running smoke tests..."
curl -f http://localhost:8000/health || log "⚠️  Health check warning"

# 5.2 Проверка подключений
CONNECTIONS=$(mariadb -u root -p -N -e "SHOW STATUS LIKE 'Threads_connected';" | awk '{print $2}')
log "MariaDB connections: $CONNECTIONS"

# 5.3 Проверка репликации (если есть)
if mariadb -u root -p -e "SHOW SLAVE STATUS\G" 2>/dev/null | grep -q "Slave_IO_Running"; then
    log "Checking replication..."
    mariadb -u root -p -e "SHOW SLAVE STATUS\G" | grep -E "Slave_.*_Running|Seconds_Behind_Master" | tee -a "$LOG_FILE"
fi

log "=== CUTOVER COMPLETED SUCCESSFULLY ==="
log "Monitor logs: tail -f /var/log/mysql/error.log"
log "Application logs: tail -f /var/log/webapp/app.log"
```

### 3.2 Timeline примера миграции

```plaintext
18:00 - Начало maintenance window
18:00 - MySQL → read-only
18:05 - Финальный snapshot
18:10 - Остановка приложений
18:15 - Переключение конфигов
18:20 - Запуск на MariaDB
18:25 - Smoke tests
18:30 - Мониторинг начат
19:00 - Конец maintenance window

Итого: 1 час
Фактический downtime: 10 минут
```

---

## 4. Мониторинг после миграции

### 4.1 24-часовой интенсивный мониторинг

```bash
#!/bin/bash
# post_migration_monitor.sh

LOG_FILE="/var/log/mariadb_post_migration.log"
DURATION_HOURS=24
CHECK_INTERVAL=300  # 5 минут

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "=== POST-MIGRATION MONITORING STARTED (${DURATION_HOURS}h) ==="

END_TIME=$(($(date +%s) + DURATION_HOURS * 3600))

while [ $(date +%s) -lt $END_TIME ]; do
    log "--- Checkpoint ---"
    
    # Подключения
    CONNECTIONS=$(mariadb -u root -p -N -e "SHOW STATUS LIKE 'Threads_connected';" | awk '{print $2}')
    log "Connections: $CONNECTIONS"
    
    # QPS
    QPS=$(mariadb -u root -p -N -e "SHOW GLOBAL STATUS LIKE 'Questions';" | awk '{print $2}')
    log "Total Questions: $QPS"
    
    # Медленные запросы
    SLOW=$(mariadb -u root -p -N -e "SHOW GLOBAL STATUS LIKE 'Slow_queries';" | awk '{print $2}')
    log "Slow Queries: $SLOW"
    
    # Ошибки в логе
    ERRORS=$(sudo tail -100 /var/log/mysql/error.log | grep -c ERROR)
    log "Recent Errors: $ERRORS"
    
    if [ "$ERRORS" -gt 10 ]; then
        log "⚠️  WARNING: High error count!"
        sudo tail -20 /var/log/mysql/error.log | tee -a "$LOG_FILE"
    fi
    
    # Проверка приложений
    if ! curl -f http://localhost:8000/health > /dev/null 2>&1; then
        log "❌ Application health check FAILED!"
        # Отправить alert
    else
        log "✅ Application healthy"
    fi
    
    # Подождать до следующей проверки
    sleep $CHECK_INTERVAL
done

log "=== POST-MIGRATION MONITORING COMPLETED ==="
```

### 4.2 Метрики для отслеживания

```plaintext
Первые 24 часа отслеживать:

✅ Uptime: 100%
✅ Connections: стабильные, нет всплесков
✅ QPS: сравнимые с MySQL
✅ Slow queries: < 1% от общего числа
✅ Errors: минимальные или отсутствуют
✅ Replication lag: 0-2 секунды
✅ Buffer pool hit ratio: > 95%
✅ Response time: сравнимый или лучше
```

---

## 5. План отката

### 5.1 Критерии для отката

```plaintext
ОТКАТ НЕОБХОДИМ ЕСЛИ:

❌ Критичные ошибки в production
❌ Приложения не работают > 30 минут
❌ Потеря данных обнаружена
❌ Производительность < 50% от нормы
❌ Невозможно устранить проблему быстро
```

### 5.2 Скрипт экстренного отката

```bash
#!/bin/bash
# emergency_rollback.sh

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log "=== EMERGENCY ROLLBACK TO MYSQL ==="

# 1. Остановить приложения
log "PHASE 1: Stopping applications"
systemctl stop webapp api-server worker

# 2. Остановить MariaDB
log "PHASE 2: Stopping MariaDB"
systemctl stop mariadb

# 3. Запустить MySQL
log "PHASE 3: Starting MySQL"
systemctl start mysql

# Подождать готовности
sleep 10

if ! mysql -u root -p -e "SELECT 1;" > /dev/null 2>&1; then
    log "❌ MySQL failed to start!"
    exit 1
fi

# 4. Снять read-only
log "PHASE 4: Removing read-only"
mysql -u root -p << EOF
UNLOCK TABLES;
SET GLOBAL read_only = OFF;
SET GLOBAL super_read_only = OFF;
EOF

# 5. Откатить конфигурации
log "PHASE 5: Restoring configs"
for file in /etc/*/database.yml /etc/*/config.json; do
    if [ -f "${file}.backup_"* ]; then
        BACKUP=$(ls -t "${file}.backup_"* | head -1)
        cp "$BACKUP" "$file"
        log "Restored: $file"
    fi
done

# 6. Запустить приложения на MySQL
log "PHASE 6: Starting applications on MySQL"
systemctl start webapp
systemctl start api-server
systemctl start worker

# 7. Проверка
log "PHASE 7: Verification"
sleep 10
curl -f http://localhost:8000/health

if [ $? -eq 0 ]; then
    log "✅ ROLLBACK SUCCESSFUL"
else
    log "❌ ROLLBACK MAY HAVE ISSUES"
fi

log "=== ROLLBACK COMPLETED ==="
```

---

## 6. Отключение MySQL

### 6.1 Через 1 неделю после успешной миграции

```bash
#!/bin/bash
# decommission_mysql.sh

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log "=== MySQL DECOMMISSIONING ==="

# 1. Финальная проверка - MariaDB работает
if ! systemctl is-active --quiet mariadb; then
    log "❌ MariaDB is NOT running! Aborting."
    exit 1
fi

# 2. Финальный архив MySQL
log "Creating final MySQL archive..."
tar -czf "/backup/mysql_final_$(date +%Y%m%d).tar.gz" \
    /var/lib/mysql/ \
    /etc/mysql/ \
    /var/log/mysql/

# 3. Остановить MySQL
log "Stopping MySQL..."
systemctl stop mysql
systemctl disable mysql

# 4. Удалить пакеты (опционально)
read -p "Remove MySQL packages? (yes/no): " REMOVE
if [ "$REMOVE" = "yes" ]; then
    apt remove --purge mysql-server mysql-client -y
    log "MySQL packages removed"
fi

# 5. Архивировать данные
log "Archiving MySQL data..."
mkdir -p /archive/mysql_old
mv /var/lib/mysql "/archive/mysql_old/data_$(date +%Y%m%d)"
mv /etc/mysql "/archive/mysql_old/config_$(date +%Y%m%d)"

log "✅ MySQL DECOMMISSIONED"
log "Archive: /archive/mysql_old/"
log "Backup: /backup/mysql_final_*.tar.gz"
```

---

## 7. Финальная документация

### 7.1 Отчет о миграции

```markdown
# MariaDB Migration Report

## Executive Summary
**Date:** 2025-11-01  
**Duration:** 4 часа (planned 6 hours)  
**Status:** ✅ SUCCESS  
**Downtime:** 15 минут (planned 30 minutes)

## Migration Details

### Pre-Migration State
- MySQL Version: 8.0.35
- Total Databases: 5
- Total Data Size: 63.7 GB
- Applications: 3 (Web API, Worker, Admin Panel)

### Post-Migration State
- MariaDB Version: 10.11.6
- All databases migrated: ✅
- All applications operational: ✅
- Performance improvement: +12%

## Timeline
| Time  | Event |
|-------|-------|
| 18:00 | Backup completed |
| 18:05 | MySQL → read-only |
| 18:10 | Final data sync |
| 18:15 | Applications stopped |
| 18:20 | Config updates |
| 18:25 | Applications started on MariaDB |
| 18:30 | Smoke tests passed |
| 18:45 | Monitoring confirmed stable |
| 19:00 | Maintenance window closed |

## Issues Encountered
1. **Minor:** Character set warning in stored procedure
   - Resolution: Updated collation to utf8mb4_unicode_ci
2. **Minor:** Connection pool timeout in worker
   - Resolution: Increased pool size 10 → 20

## Post-Migration Metrics (24h)
- Uptime: 100%
- Average QPS: 850 (vs 780 on MySQL, +9%)
- Slow Queries: 0.02% (vs 0.05% on MySQL)
- Connection Errors: 0
- Replication Lag: 0s

## Performance Comparison
| Metric | MySQL | MariaDB | Change |
|--------|-------|---------|--------|
| Avg Query Time | 45ms | 40ms | -11% |
| QPS | 780 | 850 | +9% |
| Buffer Pool Hit | 94.2% | 97.1% | +3% |
| Slow Queries/hr | 12 | 5 | -58% |

## Recommendations
1. ✅ Continue monitoring for 1 week
2. ✅ Decommission MySQL after 1 week
3. ✅ Update documentation
4. ⏳ Plan Galera Cluster (Q4 2025)

## Team
- DBA Lead: [Name]
- DevOps: [Name]
- Developer: [Name]

## Sign-off
- [x] DBA Team
- [x] DevOps Team
- [x] Development Team
- [x] Management

---
Report generated: 2025-11-02 14:00:00
```

### 7.2 Обновление документации

```markdown
# Documentation Updates Checklist

## Technical Documentation
- [ ] Runbooks updated
- [ ] Connection strings documented
- [ ] Backup procedures updated
- [ ] Disaster recovery plan revised
- [ ] Monitoring dashboards documented
- [ ] Alert contacts updated

## Operational Documentation
- [ ] On-call procedures updated
- [ ] Escalation paths documented
- [ ] Known issues documented
- [ ] FAQ updated

## Training Materials
- [ ] MariaDB specific features
- [ ] New backup procedures
- [ ] Monitoring tools
- [ ] Troubleshooting guides
```

---

## Чек-лист финализации

### ✅ Немедленно после миграции (0-24 часа)

- [ ] Интенсивный мониторинг запущен
- [ ] Все приложения работают
- [ ] Нет критичных ошибок
- [ ] Производительность в норме
- [ ] Клиенты не сообщают о проблемах

### ✅ Через 1 неделю

- [ ] Стабильность подтверждена
- [ ] MySQL можно отключить
- [ ] Финальный архив MySQL создан
- [ ] Документация обновлена
- [ ] Команда обучена

### ✅ Через 1 месяц

- [ ] Долгосрочная стабильность подтверждена
- [ ] Все метрики в норме
- [ ] Оптимизации применены
- [ ] Lessons learned документированы
- [ ] Празднование успеха! 🎉

---

## Заключение

**Поздравляем! Миграция на MariaDB завершена успешно!** 🚀

Вы получили:
- ✅ Улучшенную производительность
- ✅ Открытую и независимую платформу
- ✅ Расширенные возможности
- ✅ Экономию на лицензиях
- ✅ Прозрачное развитие

**Следующие шаги:**
1. Продолжайте мониторинг
2. Оптимизируйте производительность
3. Планируйте Galera Cluster
4. Изучайте новые функции MariaDB

---

## Полезные ссылки

- [MariaDB Documentation](https://mariadb.com/kb/)
- [MariaDB vs MySQL](https://mariadb.com/kb/en/mariadb-vs-mysql-compatibility/)
- [Community Forum](https://mariadb.com/kb/en/community/)

---

**Удачи в работе с MariaDB!** 💪

[← Назад к оглавлению](./00-INDEX.md)