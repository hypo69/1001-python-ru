# 🧑‍💻 Utilizzo di `array.array` in Python: quando e perché usarlo

Il modulo **`array`** fornisce un tipo di dato specializzato `array.array` per memorizzare sequenze di numeri dello stesso tipo. A differenza del `list` universale, gli array `array.array` offrono un uso più efficiente della memoria e prestazioni migliorate quando si lavora con dati numerici.

---

## 📦 Vantaggi principali di `array.array`

La differenza fondamentale tra `array.array` e `list` è la **memorizzazione compatta dei dati**. Invece di un elenco di puntatori a oggetti Python, `array.array` memorizza i valori come un blocco continuo di byte, rendendolo ideale per i seguenti compiti.

---

### 1. Risparmio di memoria quando si lavora con grandi set di numeri

Quando si elaborano milioni di elementi numerici, il risparmio di memoria diventa di importanza critica. `array.array` riduce significativamente l'overhead.

```python
import array
import sys

def compare_memory_usage(num_elements: int = 1_000_000) -> None:
    """
    Confronta l'utilizzo della memoria tra list e array.array.

    Args:
        num_elements (int, optional): Numero di elementi per il test. 
                                      Predefinito 1,000,000.
    """
    # Creazione di una lista con oggetti interi Python
    list_numbers = list(range(num_elements))
    
    # Creazione di un array in cui i numeri sono memorizzati come int di tipo C a 4 byte
    array_numbers = array.array('i', range(num_elements))

    list_size = sys.getsizeof(list_numbers)
    array_size = sys.getsizeof(array_numbers)

    print(f"Numero di elementi: {num_elements}")
    print(f"Dimensione list:  {list_size / 1024 / 1024:.2f} MB")
    print(f"Dimensione array: {array_size / 1024 / 1024:.2f} MB")
    if array_size > 0:
        print(f"Risparmio di memoria: {list_size / array_size:.2f}x")

# Esempio di utilizzo
if __name__ == "__main__":
    compare_memory_usage()
```
**Output:**
```
Numero di elementi: 1000000
Dimensione list:  7.63 MB
Dimensione array: 3.82 MB
Risparmio di memoria: 2.00x
```

---

### 2. Aumento delle prestazioni delle operazioni numeriche

Grazie alla disposizione continua in memoria, le operazioni matematiche sugli elementi di `array.array` vengono eseguite più velocemente, poiché il processore può utilizzare la cache in modo più efficiente.

```python
import array
import timeit

def compare_performance(num_elements: int = 10_000_000) -> None:
    """
    Confronta le prestazioni della somma di elementi in list e array.array.

    Args:
        num_elements (int, optional): Numero di elementi per il test. 
                                      Predefinito 10,000,000.
    """
    setup_code = f"""
import array
data = range({num_elements})
list_data = list(data)
array_data = array.array('i', data)
"""
    
    # Misurazione del tempo per list
    list_time = timeit.timeit("sum(list_data)", setup=setup_code, number=10)
    
    # Misurazione del tempo per array
    array_time = timeit.timeit("sum(array_data)", setup=setup_code, number=10)
    
    print(f"Tempo di somma di {num_elements} elementi (10 volte):")
    print(f"list:  {list_time:.4f} secondi")
    print(f"array: {array_time:.4f} secondi")

# Esempio di utilizzo
if __name__ == "__main__":
    compare_performance()
```
**Output:**
```
Tempo di somma di 10000000 elementi (10 volte):
list:  2.1106 secondi
array: 1.1549 secondi
```

---

### 3. Lavoro diretto con librerie C (`ctypes`, `struct`)

`array.array` è ideale per passare dati a librerie di basso livello scritte in C, poiché la sua struttura interna è compatibile con gli array C.

#### Esempio con `ctypes`:

```python
import array
from ctypes import c_double, CDLL

def demonstrate_ctypes_usage() -> None:
    """
    Dimostra il passaggio di array.array a una funzione C tramite ctypes.
    """
    # Array con numeri a doppia precisione (tipo 'd')
    py_array = array.array('d', [1.1, 2.2, 3.3, 4.4])
    
    # Creazione di un array compatibile con C da py_array
    # La funzione (c_double * len(py_array)) crea un tipo "array di 4 c_double"
    # (*py_array) scompone l'array python negli argomenti di questo costruttore
    c_array = (c_double * len(py_array))(*py_array)

    # Qui potrebbe esserci una chiamata a una funzione C, ad esempio:
    # my_c_library = CDLL("./libmath.so")
    # my_c_library.sum_doubles(c_array, len(c_array))
    
    print(f"Array Python: {py_array}")
    print(f"Array compatibile con C (ctypes): {[val for val in c_array]}")

# Esempio di utilizzo
if __name__ == "__main__":
    demonstrate_ctypes_usage()
```

#### Esempio con `struct` per l'impacchettamento dei dati:

```python
import array
import struct

def demonstrate_struct_packing(data: list[int]) -> bytes:
    """
    Impacchetta un array di interi in una stringa binaria.

    Args:
        data (list[int]): Elenco di interi da impacchettare.

    Returns:
        bytes: Rappresentazione binaria dei dati.
    """
    arr = array.array('i', data)
    
    # Creazione di una stringa di formato come '3i' per 3 interi
    format_string = f'{len(arr)}i'
    
    # Impacchettamento dei dati in formato binario
    binary_data = struct.pack(format_string, *arr)
    
    print(f"Array originale: {arr}")
    print(f"Dati binari: {binary_data}")
    
    # Verifica: spacchettamento inverso
    unpacked_data = struct.unpack(format_string, binary_data)
    print(f"Dati spacchettati: {unpacked_data}")
    
    return binary_data

# Esempio di utilizzo
if __name__ == "__main__":
    demonstrate_struct_packing([10, 20, 30])
```

---

### 4. Serializzazione e deserializzazione efficienti

I metodi `.tobytes()` e `.frombytes()` consentono di convertire rapidamente un array in byte e viceversa, il che è ideale per il salvataggio in file o la trasmissione in rete.

```python
import array

def handle_binary_data() -> None:
    """
    Dimostra la serializzazione e deserializzazione di array.array in byte.
    """
    # Creazione dell'array sorgente
    source_array = array.array('i', [1, 2, 3, 4, 5])
    print(f"Array sorgente: {source_array}")

    # Serializzazione dell'array in byte
    binary_data = source_array.tobytes()
    print(f"Dati in byte: {binary_data}")

    # Deserializzazione da byte a un nuovo array
    new_array = array.array('i')
    new_array.frombytes(binary_data)
    print(f"Array ripristinato: {new_array}")

    # Verifica dell'integrità
    assert source_array == new_array, "I dati non corrispondono!"
    print("Integrità dei dati confermata.")

# Esempio di utilizzo
if __name__ == "__main__":
    handle_binary_data()
```

---

### 5. Garanzia di omogeneità del tipo

`array.array` impone la memorizzazione di un solo tipo di dato, specificato al momento della creazione. Ciò protegge dall'aggiunta accidentale di elementi di un tipo diverso.

```python
import array

def demonstrate_type_safety() -> None:
    """
    Mostra che array.array non consente l'aggiunta di elementi di un tipo diverso.
    """
    arr = array.array('i', [100, 200, 300])
    print(f"Array di interi: {arr}")
    
    try:
        # Tentativo di aggiungere un elemento stringa
        arr.append('hello')
    except TypeError as e:
        # Eccezione attesa
        print(f"\nTentativo di aggiungere 'hello' ha causato un errore: {e}")
        print("Questo conferma la tipizzazione rigorosa dell'array.")

# Esempio di utilizzo
if __name__ == "__main__":
    demonstrate_type_safety()
```

---

### 6. Scrittura e lettura diretta da file binari

I metodi `.tofile()` e `.fromfile()` semplificano il lavoro con i file binari, evitando la serializzazione intermedia.

```python
import array
from pathlib import Path

def work_with_binary_files(file_path_str: str = "data.bin") -> None:
    """
    Scrive un array in un file binario e lo legge di nuovo.

    Args:
        file_path_str (str, optional): Nome del file da salvare.
                                       Predefinito "data.bin".
    """
    file_path = Path(file_path_str)
    source_array = array.array('f', [1.5, 2.7, 3.14])

    try:
        # Scrittura su file
        with file_path.open('wb') as f:
            source_array.tofile(f)
        print(f"Array {source_array} scritto nel file '{file_path}'.")

        # Lettura da file
        new_array = array.array('f')
        with file_path.open('rb') as f:
            # Lettura di 3 elementi di tipo 'f' (float)
            new_array.fromfile(f, len(source_array))
        print(f"Array {new_array} letto dal file.")
        
        assert source_array == new_array
        print("Integrità dei dati confermata.")

    finally:
        # Eliminazione garantita del file dopo l'esecuzione
        if file_path.exists():
            file_path.unlink()
            print(f"File temporaneo '{file_path}' eliminato.")

# Esempio di utilizzo
if __name__ == "__main__":
    work_with_binary_files()
```

---

## 🔹 Tabella comparativa: `array.array` vs `list`

| Caratteristica | `array.array` | `list` |
| :--- | :--- | :--- |
| **Tipo di dati** | Primitivi omogenei (numeri, caratteri) | Qualsiasi oggetto Python |
| **Memoria** | Basso consumo | Alto consumo |
| **Prestazioni** | Elevate per operazioni numeriche | Inferiori per operazioni numeriche |
| **API** | Set di metodi limitato | API ricca e flessibile |
| **Compatibilità con C**| Elevata, trasferimento dati diretto | Richiede conversioni |
| **Serializzazione binaria** | Metodi integrati (`.tobytes`, `.tofile`) | Richiede `struct`, `pickle`, ecc. |

---

**Conclusione:**

🚀 Usa `array.array` quando lavori con grandi volumi di **dati numerici omogenei**, e per te sono critici **prestazioni** ed **efficienza nell'uso della memoria**.

Per la maggior parte dei compiti quotidiani, dove è richiesta flessibilità e memorizzazione di dati eterogenei, `list` rimane la scelta migliore.
