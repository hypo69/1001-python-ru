
# 🧑‍💻 Использование `array.array` в Python: когда и зачем применять

Модуль **`array`** предоставляет специализированный тип данных `array.array` для хранения последовательностей однотипных чисел. В отличие от универсального `list`, массивы `array.array` обеспечивают более эффективное использование памяти и повышенную производительность при работе с числовыми данными.

---

## 📦 Основные преимущества `array.array`

Ключевое отличие `array.array` от `list` — **компактное хранение данных**. Вместо списка указателей на объекты Python, `array.array` хранит значения как непрерывный блок байтов, что делает его идеальным для следующих задач.

---

### 1. Экономия памяти при работе с большими наборами чисел

При обработке миллионов числовых элементов экономия памяти становится критически важной. `array.array` значительно сокращает накладные расходы.

```python
import array
import sys

def compare_memory_usage(num_elements: int = 1_000_000) -> None:
    """
    Сравнивает использование памяти между list и array.array.

    Args:
        num_elements (int, optional): Количество элементов для теста. 
                                      По умолчанию 1,000,000.
    """
    # Создание списка с целочисленными объектами Python
    list_numbers = list(range(num_elements))
    
    # Создание массива, где числа хранятся как 4-байтовые C-типы int
    array_numbers = array.array('i', range(num_elements))

    list_size = sys.getsizeof(list_numbers)
    array_size = sys.getsizeof(array_numbers)

    print(f"Количество элементов: {num_elements}")
    print(f"Размер list:  {list_size / 1024 / 1024:.2f} MB")
    print(f"Размер array: {array_size / 1024 / 1024:.2f} MB")
    if array_size > 0:
        print(f"Экономия памяти: {list_size / array_size:.2f}x")

# Пример использования
if __name__ == "__main__":
    compare_memory_usage()
```
**Вывод:**
```
Количество элементов: 1000000
Размер list:  7.63 MB
Размер array: 3.82 MB
Экономия памяти: 2.00x
```

---

### 2. Повышение производительности числовых операций

Благодаря непрерывному расположению в памяти, математические операции над элементами `array.array` выполняются быстрее, так как процессор может эффективнее использовать кэш.

```python
import array
import timeit

def compare_performance(num_elements: int = 10_000_000) -> None:
    """
    Сравнивает производительность суммирования элементов в list и array.array.

    Args:
        num_elements (int, optional): Количество элементов для теста. 
                                      По умолчанию 10,000,000.
    """
    setup_code = f"""
import array
data = range({num_elements})
list_data = list(data)
array_data = array.array('i', data)
"""
    
    # Измерение времени для list
    list_time = timeit.timeit("sum(list_data)", setup=setup_code, number=10)
    
    # Измерение времени для array
    array_time = timeit.timeit("sum(array_data)", setup=setup_code, number=10)
    
    print(f"Время суммирования {num_elements} элементов (10 раз):")
    print(f"list:  {list_time:.4f} секунд")
    print(f"array: {array_time:.4f} секунд")

# Пример использования
if __name__ == "__main__":
    compare_performance()
```
**Вывод:**
```
Время суммирования 10000000 элементов (10 раз):
list:  2.1106 секунд
array: 1.1549 секунд
```

---

### 3. Прямая работа с C-библиотеками (`ctypes`, `struct`)

`array.array` идеально подходит для передачи данных в низкоуровневые библиотеки, написанные на C, так как его внутренняя структура совместима с C-массивами.

#### Пример с `ctypes`:

```python
import array
from ctypes import c_double, CDLL

def demonstrate_ctypes_usage() -> None:
    """
    Демонстрирует передачу array.array в C-функцию через ctypes.
    """
    # Массив с числами двойной точности (тип 'd')
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4])
    
    # Создание C-совместимого массива из py_array
    # Функция (c_double * len(py_array)) создает тип "массив из 4-х c_double"
    # (*py_array) распаковывает python-массив в аргументы этого конструктора
    c_array = (c_double * len(py_array))(*py_array)

    # Здесь мог бы быть вызов C-функции, например:
    # my_c_library = CDLL("./libmath.so")
    # my_c_library.sum_doubles(c_array, len(c_array))
    
    print(f"Python array: {py_array}")
    print(f"C-совместимый массив (ctypes): {[val for val in c_array]}")

# Пример использования
if __name__ == "__main__":
    demonstrate_ctypes_usage()
```

#### Пример со `struct` для упаковки данных:

```python
import array
import struct

def demonstrate_struct_packing(data: list[int]) -> bytes:
    """
    Упаковывает массив целых чисел в бинарную строку.

    Args:
        data (list[int]): Список целых чисел для упаковки.

    Returns:
        bytes: Бинарное представление данных.
    """
    arr = array.array('i', data)
    
    # Создание форматной строки вида '3i' для 3-х целых чисел
    format_string = f'{len(arr)}i'
    
    # Упаковка данных в бинарный формат
    binary_data = struct.pack(format_string, *arr)
    
    print(f"Исходный массив: {arr}")
    print(f"Бинарные данные: {binary_data}")
    
    # Проверка: распаковка обратно
    unpacked_data = struct.unpack(format_string, binary_data)
    print(f"Распакованные данные: {unpacked_data}")
    
    return binary_data

# Пример использования
if __name__ == "__main__":
    demonstrate_struct_packing([10, 20, 30])
```

---

### 4. Эффективная сериализация и десериализация

Методы `.tobytes()` и `.frombytes()` позволяют быстро преобразовывать массив в байты и обратно, что идеально для сохранения в файлы или передачи по сети.

```python
import array

def handle_binary_data() -> None:
    """
    Демонстрирует сериализацию и десериализацию array.array в байты.
    """
    # Создание исходного массива
    source_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"Исходный массив: {source_array}")

    # Сериализация массива в байты
    binary_data = source_array.tobytes()
    print(f"Данные в байтах: {binary_data}")

    # Десериализация из байтов в новый массив
    new_array = array.array('i')
    new_array.frombytes(binary_data)
    print(f"Восстановленный массив: {new_array}")

    # Проверка целостности
    assert source_array == new_array, "Данные не совпадают!"
    print("Целостность данных подтверждена.")

# Пример использования
if __name__ == "__main__":
    handle_binary_data()
```

---

### 5. Гарантия типовой однородности

`array.array` принудительно сохраняет только один тип данных, указанный при создании. Это защищает от случайного добавления элементов другого типа.

```python
import array

def demonstrate_type_safety() -> None:
    """
    Показывает, что array.array не позволяет добавлять элементы другого типа.
    """
    arr = array.array('i', [100, 200, 300])
    print(f"Массив целых чисел: {arr}")
    
    try:
        # Попытка добавить строковый элемент
        arr.append('hello')
    except TypeError as e:
        # Ожидаемое исключение
        print(f"\nПопытка добавить 'hello' вызвала ошибку: {e}")
        print("Это подтверждает строгую типизацию массива.")

# Пример использования
if __name__ == "__main__":
    demonstrate_type_safety()
```

---

### 6. Прямая запись и чтение из бинарных файлов

Методы `.tofile()` и `.fromfile()` упрощают работу с бинарными файлами, позволяя избежать промежуточной сериализации.

```python
import array
from pathlib import Path

def work_with_binary_files(file_path_str: str = "data.bin") -> None:
    """
    Записывает массив в бинарный файл и читает его обратно.

    Args:
        file_path_str (str, optional): Имя файла для сохранения.
                                       По умолчанию "data.bin".
    """
    file_path = Path(file_path_str)
    source_array = array.array('f', [1.5, 2.7, 3.14])

    try:
        # Запись в файл
        with file_path.open('wb') as f:
            source_array.tofile(f)
        print(f"Массив {source_array} записан в файл '{file_path}'.")

        # Чтение из файла
        new_array = array.array('f')
        with file_path.open('rb') as f:
            # Чтение 3-х элементов типа 'f' (float)
            new_array.fromfile(f, len(source_array))
        print(f"Массив {new_array} прочитан из файла.")
        
        assert source_array == new_array

    finally:
        # Гарантированное удаление файла после выполнения
        if file_path.exists():
            file_path.unlink()
            print(f"Временный файл '{file_path}' удален.")

# Пример использования
if __name__ == "__main__":
    work_with_binary_files()
```

---

## 🔹 Сравнительная таблица: `array.array` vs `list`

| Характеристика | `array.array` | `list` |
| :--- | :--- | :--- |
| **Тип данных** | Однотипные примитивы (числа, символы) | Любые объекты Python |
| **Память** | Низкое потребление | Высокое потребление |
| **Производительность** | Высокая для числовых операций | Ниже для числовых операций |
| **API** | Ограниченный набор методов | Богатый и гибкий API |
| **Совместимость с C**| Высокая, прямая передача данных | Требуются преобразования |
| **Бинарная сериализация** | Встроенные методы (`.tobytes`, `.tofile`)| Требуется `struct`, `pickle` и т.д. |

---

**Вывод:**

🚀 Используйте `array.array`, когда работаете с большими объемами **однотипных числовых данных**, и для вас критичны **производительность** и **эффективное использование памяти**.

Для большинства повседневных задач, где требуется гибкость и хранение разнородных данных, `list` остается лучшим выбором.