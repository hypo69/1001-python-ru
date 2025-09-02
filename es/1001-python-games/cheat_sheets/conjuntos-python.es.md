# Conjuntos en Python

**1. Introducción: ¿Qué son los conjuntos?**

En informática y matemáticas, los conjuntos son una forma de representar colecciones de elementos únicos. Es importante entender que:

*   **Unicidad:** Cada elemento de un conjunto debe ser único. No se permiten duplicados.
*   **Desordenado:** El orden de los elementos en un conjunto no importa.


**2. Conjuntos y frutas**

Imaginaremos que solo tenemos las frutas mismas:

*   🍎 (manzana)
*   🍐 (pera)
*   🍉 (melón)
*   🧺 (cesta)

Es importante que:

1.  **No hay *frutas idénticas* en el conjunto:** Si hay una manzana en el conjunto, no habrá otra manzana idéntica. Cada fruta es única en su conjunto.
2.  **El orden de las frutas no importa:** Si hay una manzana y una pera en el conjunto, es lo mismo que si hubiera una pera y una manzana. El orden no importa.

Por ejemplo, `{🍎, 🍐, 🍉}` es un conjunto que contiene una manzana, una pera y un melón.

**3. ¿Por qué los conjuntos requieren elementos únicos?**

*   Los conjuntos están diseñados para rastrear la *presencia* de elementos, no su *cantidad*.
*   La unicidad de los elementos simplifica la realización de operaciones en conjuntos.
*   Los conjuntos se utilizan para eliminar la redundancia de datos.

**4. Operaciones en conjuntos (conjuntos de frutas):**

1.  **Unión: "Reunir todas las frutas en un solo conjunto"**
    *   Combinar dos conjuntos de frutas, reuniendo todas las frutas en un nuevo conjunto. Si hay frutas idénticas en ambos conjuntos, el nuevo conjunto solo tendrá una de esas frutas.
    *   Si el conjunto A tiene {🍎, 🍐}, y el conjunto B tiene {🍐, 🍉}, entonces el conjunto A ∪ B será {🍎, 🍐, 🍉}.

2.  **Intersección: "Encontrar frutas comunes"**
    *   Encontrar *solo* aquellas frutas que están tanto en el conjunto A como en el conjunto B.
    *   Si el conjunto A tiene {🍎, 🍐}, y el conjunto B tiene {🍐, 🍉}, entonces el conjunto A ∩ B solo será {🍐}.

3.  **Diferencia: "Frutas que están en un conjunto pero no en otro"**
    *   Encontrar *solo* aquellas frutas que están en el conjunto A, pero no en el conjunto B.
    *   Si el conjunto A tiene {🍎, 🍐}, y el conjunto B tiene {🍐, 🍉}, entonces el conjunto A - B será {🍎}, y el conjunto B - A será {🍉}.

4.  **Diferencia simétrica: "Frutas que solo están en uno de los conjuntos"**
    *   Encontrar *todas* las frutas que están en el conjunto A o en el conjunto B, pero no en ambos simultáneamente.
    *   Si el conjunto A tiene {🍎, 🍐}, y el conjunto B tiene {🍐, 🍉}, entonces el conjunto A ^ B será {🍎, 🍉}.

5.  **Subconjunto: "¿Están todas las frutas de un conjunto en otro?"**
    *   Comprobar si el conjunto A es un subconjunto del conjunto B. Esto significa que todas las frutas del conjunto A también están en el conjunto B.
    *   **Ejemplo:** Si el conjunto A tiene {🍎, 🍐}, y el conjunto B tiene {🍎, 🍐, 🍉}, entonces A <= B.

6.  **Superconjunto: "¿Un conjunto contiene todas las frutas de otro?"**
    *   Comprobar si el conjunto A es un superconjunto del conjunto B. Esto significa que todas las frutas del conjunto B también están en el conjunto A.
    *   Si el conjunto A tiene {🍎, 🍐, 🍉}, y el conjunto B tiene {🍎, 🍐}, entonces A >= B.



```python
from typing import Set

def create_fruit_set(fruit_string: str) -> Set[str]:
    """
    Crea un conjunto de frutas a partir de una cadena.

    Args:
        fruit_string: Cadena de frutas (🍎, 🍐, 🍉, 🧺).

    Returns:
        Un conjunto de frutas únicas.
    """
    if not all(fruit in ["🍎", "🍐", "🍉", "🧺"] for fruit in fruit_string):
        raise ValueError("La cadena solo puede contener los símbolos 🍎, 🍐, 🍉, 🧺")
    return set(fruit_string)  # Usar set() para crear un conjunto

def display_set(fruit_set: Set[str]) -> str:
  """
  Convierte un conjunto de frutas en una cadena para mostrar.

    Args:
        fruit_set: Conjunto de frutas.

    Returns:
        Cadena para mostrar.
  """
  return "{" + ", ".join(fruit_set) + "}"


# Crear conjuntos de frutas
fruits_set_A = create_fruit_set("🍎🍐")  # Conjunto A: {🍎, 🍐}
fruits_set_B = create_fruit_set("🍐🍉")  # Conjunto B: {🍐, 🍉}
fruits_set_C = create_fruit_set("🍎🍐🍉")  # Conjunto C: {🍎, 🍐, 🍉}
fruits_set_D = create_fruit_set("🧺")  # Conjunto D: {🧺}

# Mostrar conjuntos
print(f"Conjunto A: {display_set(fruits_set_A)}")
print(f"Conjunto B: {display_set(fruits_set_B)}")
print(f"Conjunto C: {display_set(fruits_set_C)}")
print(f"Conjunto D: {display_set(fruits_set_D)}")

# Unión de conjuntos
union_result = fruits_set_A | fruits_set_B
print(f"A ∪ B: {display_set(union_result)}")  # Resultado: {🍎, 🍐, 🍉}

# Intersección de conjuntos
intersection_result = fruits_set_A & fruits_set_B
print(f"A ∩ B: {display_set(intersection_result)}")  # Resultado: {🍐}

# Diferencia de conjuntos
difference_result_AB = fruits_set_A - fruits_set_B
print(f"A - B: {display_set(difference_result_AB)}")  # Resultado: {🍎}
difference_result_BA = fruits_set_B - fruits_set_A
print(f"B - A: {display_set(difference_result_BA)}")  # Resultado: {🍉}

# Diferencia simétrica de conjuntos
symmetric_difference_result = fruits_set_A ^ fruits_set_B
print(f"A ^ B: {display_set(symmetric_difference_result)}")  # Resultado: {🍎, 🍉}

# Subconjunto
subset_result1 = fruits_set_A <= fruits_set_C
print(f"A <= C: {subset_result1}")  # Resultado: True (A es un subconjunto de C)
subset_result2 = fruits_set_A <= fruits_set_B
print(f"A <= B: {subset_result2}") # Resultado: False (A no es un subconjunto de B)

# Superconjunto
superset_result1 = fruits_set_C >= fruits_set_A
print(f"C >= A: {superset_result1}")  # Resultado: True (C es un superconjunto de A)
superset_result2 = fruits_set_B >= fruits_set_A
print(f"B >= A: {superset_result2}")  # Resultado: False (B no es un superconjunto de A)

# Comprobar la presencia de un elemento
print(f"🍎 en A: {'🍎' in fruits_set_A}")  # Resultado: True
print(f"🍉 en A: {'🍉' in fruits_set_A}")  # Resultado: False
```

*   **`create_fruit_set(fruit_string)`:** Esta función crea un conjunto a partir de una cadena de frutas.
    *   `set(fruit_string)` convierte la cadena en un conjunto, eliminando duplicados y haciendo que el orden de los elementos sea irrelevante.
    *   Comprobamos que la cadena solo contenga caracteres Unicode permitidos.
*   **`display_set(fruit_set)`:** Esta función se utiliza para convertir un conjunto en una cadena legible para la salida.
*   **Ejemplos:** Creamos varios conjuntos y les aplicamos varias operaciones. Los resultados de cada operación se imprimen en la pantalla.



**5. Tareas de práctica:**

1.  Cree sus propios conjuntos de frutas y pruebe todas las operaciones en ellos.
2.  Implemente una función `is_disjoint(set1, set2)` que verifique si dos conjuntos son disjuntos (intersección = conjunto vacío).
3.  Implemente una función `power_set(fruit_set)` que devuelva el conjunto de todos los subconjuntos de un conjunto dado.
4.  Intente aplicar conjuntos para resolver un problema real. Por ejemplo, tiene dos listas de invitados para una fiesta, encuentre los invitados que están en ambas listas, los invitados que están solo en la primera lista, etc.

