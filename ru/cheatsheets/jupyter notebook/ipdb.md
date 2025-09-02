# **Краткое руководство по отладке в Jupyter Notebook с ipdb**  

В этом руководстве:  
✅ **Установку и настройку `ipdb`**  
✅ **3 способа запуска отладчика**  
✅ **Все ключевые команды `ipdb` с примерами**  
✅ **Тактики отладки реального кода**  
✅ **Альтернативные инструменты**  

---

## **1. Установка и подготовка**  

### Установка через pip:  
```bash
pip install ipdb
```

### Импорт в Jupyter:  
```python
import ipdb
```

---

## **2. Три способа запуска отладки**  

### **Способ 1: Явная точка останова (`ipdb.set_trace()`)**  
```python
def calculate_discount(price, discount):
    final_price = price * (1 - discount)
    ipdb.set_trace()  # Остановка здесь
    return final_price * 1.1  # Добавляем налог

calculate_discount(1000, 0.2)
```
**Что происходит:**  
- Выполнение останавливается на `ipdb.set_trace()`  
- Можно проверить значения переменных (`price`, `discount`)  
- Пошагово выполнить код  

### **Способ 2: Постфактум-отладка (`%debug`)**  
Если код упал с ошибкой:  
```python
def load_data(filename):
    with open(filename) as f:
        return f.read()

try:
    load_data("missing_file.txt")
except Exception as e:
    %debug  # Запуск отладчика на месте ошибки
```
**Преимущество:** Не нужно заранее расставлять точки останова.  

### **Способ 3: Магическая команда `%%debug`**  
Для отладки всей ячейки:  
```python
%%debug
def risky_operation(x):
    return 100 / x

risky_operation(0)
```
Отладчик запустится сразу при выполнении ячейки.  

---

## **3. Полный справочник команд ipdb**  

### **Основные команды:**  
| Команда | Описание | Пример |
|---------|----------|--------|
| `n` (next) | Шаг вперед (не заходя в функции) | `n` |
| `s` (step) | Шаг с заходом в функцию | `s` |
| `c` (continue) | Продолжить выполнение | `c` |
| `q` (quit) | Выйти из отладчика | `q` |

### **Анализ кода:**  
| Команда | Описание | Пример |
|---------|----------|--------|
| `l` (list) | Показать код вокруг | `l 5,10` (строки 5-10) |
| `w` (where) | Вывести стек вызовов | `w` |
| `u`/`d` | Перемещение по стеку | `u 2` (вверх на 2 уровня) |

### **Работа с переменными:**  
| Команда | Описание | Пример |
|---------|----------|--------|
| `p` (print) | Напечатать переменную | `p price` |
| `pp` | Pretty-print | `pp large_dict` |
| `!` | Выполнить Python-код | `!x = 10` |

---

## **4. Реальные примеры отладки**  

### **Пример 1: Отладка цикла**  
```python
def find_negative(numbers):
    ipdb.set_trace()
    for i, num in enumerate(numbers):
        if num < 0:
            return i
    return -1

find_negative([1, 3, -5, 10])
```
**Тактика:**  
1. Проверить входные данные (`p numbers`)  
2. Шагать через цикл (`n`), наблюдая за `i` и `num`  
3. В момент `num == -5` проверить состояние  

### **Пример 2: Рекурсивная функция**  
```python
def factorial(n):
    ipdb.set_trace()
    if n == 1:
        return 1
    return n * factorial(n-1)

factorial(4)
```
**Особенности:**  
- Используем `w` для просмотра стека вызовов  
- `u 2` переходит на 2 уровня выше в стеке  
- `p n` покажет текущее значение на каждом уровне  

---

## **5. Продвинутые техники**  

### **Условные точки останова**  
```python
for i in range(100):
    if i == 50:
        ipdb.set_trace()  # Сработает только на 50-й итерации
    process_data(i)
```

### **Отладка асинхронного кода**  
```python
import asyncio

async def fetch_data():
    await asyncio.sleep(1)
    ipdb.set_trace()  # Работает в Jupyter с ядром IPython ≥7.0
    return "data"

await fetch_data()
```

---

## **6. Альтернативные инструменты**  

### **Встроенный дебаггер Jupyter (новые версии)**  
```python
# В Jupyter Lab ≥3.0
from IPython.core.debugger import set_trace
set_trace()  # Аналог ipdb
```

### **VS Code + Jupyter**  
Использование `debugpy` для визуальной отладки:  
```python
import debugpy
debugpy.listen(5678)
debugpy.breakpoint()  # Точка останова для VS Code
```

---


🕵️‍   Удачного кодинга!