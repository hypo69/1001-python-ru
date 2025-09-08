<!-- Translated to en -->
# 🧑‍💻 Using `array.array` in Python: when and why to apply

Модуль **`array`** provides a specialized data type `array.array` for storing sequences of homogeneous numbers. Unlike the universal `list`, `array.array` arrays provide more efficient memory usage and increased performance when working with numerical data.

---

## 📦 Key advantages of `array.array`

The key difference between `array.array` and `list` is **compact data storage**. Instead of a list of pointers to Python objects, `array.array` stores values as a contiguous block of bytes, which makes it ideal for the following tasks.

---

### 1. Memory savings when working with large sets of numbers

When processing millions of numerical elements, memory savings become critically important. `array.array` significantly reduces overhead.

```python
import array
import sys

def compare_memory_usage(num_elements: int = 1_000_000) -> None:
    """
    Compares memory usage between list and array.array.

    Args:
        num_elements (int, optional): Number of elements for the test. 
                                      Defaults to 1,000,000.
    """
    # Create a list with integer Python objects
    list_numbers = list(range(num_elements))
    
    # Create an array where numbers are stored as 4-byte C-type ints
    array_numbers = array.array('i', range(num_elements))

    list_size = sys.getsizeof(list_numbers)
    array_size = sys.getsizeof(array_numbers)

    print(f"Number of elements: {num_elements}")
    print(f"List size:  {list_size / 1024 / 1024:.2f} MB")
    print(f"Array size: {array_size / 1024 / 1024:.2f} MB")
    if array_size > 0:
        print(f"Memory savings: {list_size / array_size:.2f}x")

# Example usage
if __name__ == "__main__":
    compare_memory_usage()
```
**Output:**
```
Количество элементов: 1000000
Размер list:  7.63 MB
Размер array: 3.82 MB
Экономия памяти: 2.00x
```

---

### 2. Increased performance of numerical operations

Due to contiguous memory allocation, mathematical operations on `array.array` elements are performed faster, as the processor can make more efficient use of the cache.

```python
import array
import timeit

def compare_performance(num_elements: int = 10_000_000) -> None:
    """
    Compares the performance of summing elements in list and array.array.

    Args:
        num_elements (int, optional): Number of elements for the test. 
                                      Defaults to 10,000,000.
    """
    setup_code = f"""
import array
data = range({num_elements})
list_data = list(data)
array_data = array.array('i', data)
"""
    
    # Measure time for list
    list_time = timeit.timeit("sum(list_data)", setup=setup_code, number=10)
    
    # Measure time for array
    array_time = timeit.timeit("sum(array_data)", setup=setup_code, number=10)
    
    print(f"Time to sum {num_elements} elements (10 times):")
    print(f"list:  {list_time:.4f} seconds")
    print(f"array: {array_time:.4f} seconds")

# Example usage
if __name__ == "__main__":
    compare_performance()
```
**Output:**
```
Количество элементов: 10000000
Размер list:  2.1106 секунд
Размер array: 1.1549 секунд
```

---

### 3. Direct work with C libraries (`ctypes`, `struct`)

`array.array` is ideal for passing data to low-level libraries written in C, as its internal structure is compatible with C arrays.

#### Example with `ctypes`:

```python
import array
from ctypes import c_double, CDLL

def demonstrate_ctypes_usage() -> None:
    """
    Demonstrates passing array.array to a C function via ctypes.
    """
    # Array with double-precision numbers (type 'd')
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4])
    
    # Create a C-compatible array from py_array
    # The function (c_double * len(py_array)) creates a type "array of 4 c_double"
    # (*py_array) unpacks the python array into the arguments of this constructor
    c_array = (c_double * len(py_array))(*py_array)

    # Here could be a call to a C function, for example:
    # my_c_library = CDLL("./libmath.so")
    # my_c_library.sum_doubles(c_array, len(c_array))
    
    print(f"Python array: {py_array}")
    print(f"C-compatible array (ctypes): {[val for val in c_array]}")

# Example usage
if __name__ == "__main__":
    demonstrate_ctypes_usage()
```

#### Example with `struct` for data packing:

```python
import array
import struct

def demonstrate_struct_packing(data: list[int]) -> bytes:
    """
    Packs an array of integers into a binary string.

    Args:
        data (list[int]): List of integers to pack.

    Returns:
        bytes: Binary representation of the data.
    """
    arr = array.array('i', data)
    
    # Create a format string like '3i' for 3 integers
    format_string = f'{len(arr)}i'
    
    # Pack data into binary format
    binary_data = struct.pack(format_string, *arr)
    
    print(f"Original array: {arr}")
    print(f"Binary data: {binary_data}")
    
    # Check: unpack back
    unpacked_data = struct.unpack(format_string, binary_data)
    print(f"Unpacked data: {unpacked_data}")
    
    return binary_data

# Example usage
if __name__ == "__main__":
    demonstrate_struct_packing([10, 20, 30])
```

---

### 4. Efficient serialization and deserialization

The `.tobytes()` and `.frombytes()` methods allow quickly converting an array to bytes and back, which is ideal for saving to files or transmitting over a network.

```python
import array

def handle_binary_data() -> None:
    """
    Demonstrates serialization and deserialization of array.array to bytes.
    """
    # Create original array
    source_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"Original array: {source_array}")

    # Serialize array to bytes
    binary_data = source_array.tobytes()
    print(f"Data in bytes: {binary_data}")

    # Deserialize from bytes to new array
    new_array = array.array('i')
    new_array.frombytes(binary_data)
    print(f"Restored array: {new_array}")

    # Check integrity
    assert source_array == new_array, "Data mismatch!"
    print("Data integrity confirmed.")

# Example usage
if __name__ == "__main__":
    handle_binary_data()
```

---

### 5. Guarantee of type homogeneity

`array.array` strictly enforces only one data type, specified at creation. This prevents accidental addition of elements of a different type.

```python
import array

def demonstrate_type_safety() -> None:
    """
    Shows that array.array does not allow adding elements of a different type.
    """
    arr = array.array('i', [100, 200, 300])
    print(f"Integer array: {arr}")
    
    try:
        # Attempt to add a string element
        arr.append('hello')
    except TypeError as e:
        # Expected exception
        print(f"\nAttempt to add 'hello' raised an error: {e}")
        print("This confirms strict array typing.")

# Example usage
if __name__ == "__main__":
    demonstrate_type_safety()
```

---

### 6. Direct writing and reading from binary files

The `.tofile()` and `.fromfile()` methods simplify working with binary files, avoiding intermediate serialization.

```python
import array
from pathlib import Path

def work_with_binary_files(file_path_str: str = "data.bin") -> None:
    """
    Writes an array to a binary file and reads it back.

    Args:
        file_path_str (str, optional): File name for saving.
                                       Defaults to "data.bin".
    """
    file_path = Path(file_path_str)
    source_array = array.array('f', [1.5, 2.7, 3.14])

    try:
        # Write to file
        with file_path.open('wb') as f:
            source_array.tofile(f)
        print(f"Array {source_array} written to file '{file_path}'.")

        # Read from file
        new_array = array.array('f')
        with file_path.open('rb') as f:
            # Read 3 elements of type 'f' (float)
            new_array.fromfile(f, len(source_array))
        print(f"Array {new_array} read from file.")
        
        assert source_array == new_array

    finally:
        # Guaranteed file deletion after execution
        if file_path.exists():
            file_path.unlink()
            print(f"Temporary file '{file_path}' deleted.")

# Example usage
if __name__ == "__main__":
    work_with_binary_files()
```

---

## 🔹 Comparative table: `array.array` vs `list`

| Characteristic | `array.array` | `list` |
| :--- | :--- | :--- |
| **Data type** | Homogeneous primitives (numbers, characters) | Any Python objects |
| **Memory** | Low consumption | High consumption |
| **Performance** | High for numerical operations | Lower for numerical operations |
| **API** | Limited set of methods | Rich and flexible API |
| **C compatibility**| High, direct data transfer | Conversions required |
| **Binary serialization** | Built-in methods (`.tobytes`, `.tofile`) | Requires `struct`, `pickle` etc. |

---

**Conclusion:**

🚀 Use `array.array` when working with large volumes of **homogeneous numerical data**, and when **performance** and **efficient memory usage** are critical for you.

For most everyday tasks where flexibility and storage of heterogeneous data are required, `list` remains the best choice.
