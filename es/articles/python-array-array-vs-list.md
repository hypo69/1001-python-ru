# 🧑‍💻 Uso de `array.array` en Python: Cuándo y por qué usarlo

El módulo **`array`** proporciona un tipo de datos especializado `array.array` para almacenar secuencias de números del mismo tipo. A diferencia de la `list` de propósito general, los arrays `array.array` proporcionan un uso más eficiente de la memoria y un mayor rendimiento al trabajar con datos numéricos.

---

## 📦 Ventajas clave de `array.array`

La diferencia clave entre `array.array` y `list` es el **almacenamiento compacto de datos**. En lugar de una lista de punteros a objetos de Python, `array.array` almacena los valores como un bloque contiguo de bytes, lo que lo hace ideal para las siguientes tareas.

---

### 1. Ahorro de memoria al trabajar con grandes conjuntos de números

Al procesar millones de elementos numéricos, el ahorro de memoria se vuelve crítico. `array.array` reduce significativamente la sobrecarga.

```python
import array
import sys

def compare_memory_usage(num_elements: int = 1_000_000) -> None:
    """
    Compara el uso de memoria entre list y array.array.

    Args:
        num_elements (int, optional): El número de elementos a probar.
                                      El valor predeterminado es 1.000.000.
    """
    # Crear una lista con objetos enteros de Python
    list_numbers = list(range(num_elements))
    
    # Crear un array donde los números se almacenan como enteros de tipo C de 4 bytes
    array_numbers = array.array('i', range(num_elements))

    list_size = sys.getsizeof(list_numbers)
    array_size = sys.getsizeof(array_numbers)

    print(f"Número de elementos: {num_elements}")
    print(f"Tamaño de la lista:  {list_size / 1024 / 1024:.2f} MB")
    print(f"Tamaño del array: {array_size / 1024 / 1024:.2f} MB")
    if array_size > 0:
        print(f"Ahorro de memoria: {list_size / array_size:.2f}x")

# Ejemplo de uso
if __name__ == "__main__":
    compare_memory_usage()
```
**Salida:**
```
Número de elementos: 1000000
Tamaño de la lista:  7.63 MB
Tamaño del array: 3.82 MB
Ahorro de memoria: 2.00x
```

---

### 2. Mayor rendimiento de las operaciones numéricas

Gracias a su diseño de memoria contigua, las operaciones matemáticas en los elementos de `array.array` son más rápidas porque el procesador puede usar la caché de manera más eficiente.

```python
import array
import timeit

def compare_performance(num_elements: int = 10_000_000) -> None:
    """
    Compara el rendimiento de sumar elementos en una lista y un array.array.

    Args:
        num_elements (int, optional): El número de elementos a probar.
                                      El valor predeterminado es 10.000.000.
    """
    setup_code = f"""
import array
data = range({num_elements})
list_data = list(data)
array_data = array.array('i', data)
"""
    
    # Medir el tiempo para la lista
    list_time = timeit.timeit("sum(list_data)", setup=setup_code, number=10)
    
    # Medir el tiempo para el array
    array_time = timeit.timeit("sum(array_data)", setup=setup_code, number=10)
    
    print(f"Tiempo para sumar {num_elements} elementos (10 veces):")
    print(f"lista:  {list_time:.4f} segundos")
    print(f"array: {array_time:.4f} segundos")

# Ejemplo de uso
if __name__ == "__main__":
    compare_performance()
```
**Salida:**
```
Tiempo para sumar 10000000 elementos (10 veces):
lista:  2.1106 segundos
array: 1.1549 segundos
```

---

### 3. Trabajo directo con bibliotecas de C (`ctypes`, `struct`)

`array.array` es ideal para pasar datos a bibliotecas de nivel bajo escritas en C, ya que su estructura interna es compatible con los arrays de C.

#### Ejemplo con `ctypes`:

```python
import array
from ctypes import c_double, CDLL

def demonstrate_ctypes_usage() -> None:
    """
    Muestra cómo pasar un array.array a una función de C a través de ctypes.
    """
    # Array con números de doble precisión (tipo 'd')
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4])
    
    # Crear un array compatible con C a partir de py_array
    # La función (c_double * len(py_array)) crea un tipo "array de 4 c_double"
    # (*py_array) desempaqueta el array de python en los argumentos de este constructor
    c_array = (c_double * len(py_array))(*py_array)

    # Aquí podría haber una llamada a una función de C, por ejemplo:
    # my_c_library = CDLL("./libmath.so")
    # my_c_library.sum_doubles(c_array, len(c_array))
    
    print(f"Array de Python: {py_array}")
    print(f"Array compatible con C (ctypes): {[val for val in c_array]}")

# Ejemplo de uso
if __name__ == "__main__":
    demonstrate_ctypes_usage()
```

#### Ejemplo con `struct` para empaquetar datos:

```python
import array
import struct

def demonstrate_struct_packing(data: list[int]) -> bytes:
    """
    Empaqueta un array de enteros en una cadena binaria.

    Args:
        data (list[int]): Una lista de enteros para empaquetar.

    Returns:
        bytes: La representación binaria de los datos.
    """
    arr = array.array('i', data)
    
    # Crear una cadena de formato como '3i' para 3 enteros
    format_string = f'{len(arr)}i'
    
    # Empaquetar los datos en un formato binario
    binary_data = struct.pack(format_string, *arr)
    
    print(f"Array original: {arr}")
    print(f"Datos binarios: {binary_data}")
    
    # Comprobación: desempaquetar de nuevo
    unpacked_data = struct.unpack(format_string, binary_data)
    print(f"Datos desempaquetados: {unpacked_data}")
    
    return binary_data

# Ejemplo de uso
if __name__ == "__main__":
    demonstrate_struct_packing([10, 20, 30])
```

---

### 4. Serialización y deserialización eficientes

Los métodos `.tobytes()` y `.frombytes()` le permiten convertir rápidamente un array a bytes y viceversa, lo que es ideal para guardar en archivos o enviar a través de una red.

```python
import array

def handle_binary_data() -> None:
    """
    Muestra la serialización y deserialización de un array.array a bytes.
    """
    # Crear el array de origen
    source_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"Array de origen: {source_array}")

    # Serializar el array a bytes
    binary_data = source_array.tobytes()
    print(f"Datos en bytes: {binary_data}")

    # Deserializar de bytes a un nuevo array
    new_array = array.array('i')
    new_array.frombytes(binary_data)
    print(f"Array restaurado: {new_array}")

    # Comprobar la integridad
    assert source_array == new_array, "¡Los datos no coinciden!"
    print("Integridad de los datos confirmada.")

# Ejemplo de uso
if __name__ == "__main__":
    handle_binary_data()
```

---

### 5. Garantía de homogeneidad de tipos

`array.array` obliga a que solo se almacene un tipo de datos, especificado en la creación. Esto protege contra la adición accidental de elementos de un tipo diferente.

```python
import array

def demonstrate_type_safety() -> None:
    """
    Muestra que array.array no permite añadir elementos de un tipo diferente.
    """
    arr = array.array('i', [100, 200, 300])
    print(f"Array de enteros: {arr}")
    
    try:
        # Intentar añadir un elemento de tipo cadena
        arr.append('hello')
    except TypeError as e:
        # Excepción esperada
        print(f"\nEl intento de añadir 'hello' ha provocado un error: {e}")
        print("Esto confirma el tipado estricto del array.")

# Ejemplo de uso
if __name__ == "__main__":
    demonstrate_type_safety()
```

---

### 6. Escritura y lectura directas en archivos binarios

Los métodos `.tofile()` y `.fromfile()` simplifican el trabajo con archivos binarios, permitiéndole evitar la serialización intermedia.

```python
import array
from pathlib import Path

def work_with_binary_files(file_path_str: str = "data.bin") -> None:
    """
    Escribe un array en un archivo binario y lo lee de nuevo.

    Args:
        file_path_str (str, optional): El nombre del archivo a guardar.
                                       El valor predeterminado es "data.bin".
    """
    file_path = Path(file_path_str)
    source_array = array.array('f', [1.5, 2.7, 3.14])

    try:
        # Escribir en el archivo
        with file_path.open('wb') as f:
            source_array.tofile(f)
        print(f"Array {source_array} escrito en el archivo '{file_path}'.")

        # Leer del archivo
        new_array = array.array('f')
        with file_path.open('rb') as f:
            # Leer 3 elementos de tipo 'f' (float)
            new_array.fromfile(f, len(source_array))
        print(f"Array {new_array} leído del archivo.")
        
        assert source_array == new_array

    finally:
        # Eliminación garantizada del archivo después de la ejecución
        if file_path.exists():
            file_path.unlink()
            print(f"Archivo temporal '{file_path}' eliminado.")

# Ejemplo de uso
if __name__ == "__main__":
    work_with_binary_files()
```

---

## 🔹 Tabla comparativa: `array.array` vs `list`

| Característica | `array.array` | `list` |
| :--- | :--- | :--- |
| **Tipo de datos** | Primitivos homogéneos (números, caracteres) | Cualquier objeto de Python |
| **Memoria** | Bajo consumo | Alto consumo |
| **Rendimiento** | Alto para operaciones numéricas | Menor para operaciones numéricas |
| **API** | Conjunto limitado de métodos | API rica y flexible |
| **Compatibilidad con C**| Alta, paso directo de datos | Requiere conversiones |
| **Serialización binaria** | Métodos incorporados (`.tobytes`, `.tofile`)| Requiere `struct`, `pickle`, etc. |

---

**Conclusión:**

🚀 Usa `array.array` cuando trabajes con grandes volúmenes de **datos numéricos homogéneos**, y cuando el **rendimiento** y el **uso eficiente de la memoria** sean críticos para ti.

Para la mayoría de las tareas cotidianas en las que se requiere flexibilidad y almacenamiento de datos heterogéneos, `list` sigue siendo la mejor opción.
