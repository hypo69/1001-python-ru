# Sets in Python

**1. Introduction: What are sets?**

In computer science and mathematics, sets are a way to represent collections of unique elements. It is important to understand that:

*   **Uniqueness:** Each element in a set must be unique. Repetitions are not allowed.
*   **Unordered:** The order of elements in a set does not matter.


**2. Sets and fruits**

Let's imagine that we only have the fruits themselves:

*   🍎 (apple)
*   🍐 (pear)
*   🍉 (melon)
*   🧺 (basket)

It is important that:

1.  **There are *no* identical fruits in the set:** If there is an apple in the set, there will not be another identical apple. Each fruit is unique in its set.
2.  **The order of fruits does not matter:** If there is an apple and a pear in the set, it is the same as if there were a pear and an apple. The order does not matter.

For example, `{🍎, 🍐, 🍉}` is a set containing an apple, a pear, and a melon.

**3. Why do sets require unique elements?**

*   Sets are designed to track the *presence* of elements, not their *quantity*.
*   The uniqueness of elements simplifies the execution of set operations.
*   Sets are used to eliminate data redundancy.

**4. Set operations (fruit sets):**

1.  **Union: "Gather all fruits into one set"**
    *   Combine two sets of fruits, gathering all fruits into a new set. If there are identical fruits in two sets, the new set will only contain one such fruit.
    *   If set A contains {🍎, 🍐}, and set B contains {🍐, 🍉}, then set A ∪ B will contain {🍎, 🍐, 🍉}.

2.  **Intersection: "Find common fruits"**
    *   Find *only* those fruits that are present in both set A and set B.
    *   If set A contains {🍎, 🍐}, and set B contains {🍐, 🍉}, then set A ∩ B will only contain {🍐}.

3.  **Difference: "Fruits that are in one set but not in another"**
    *   Find *only* those fruits that are present in set A but not in set B.
    *   If set A contains {🍎, 🍐}, and set B contains {🍐, 🍉}, then set A - B will contain {🍎}, and set B - A will contain {🍉}.

4.  **Symmetric Difference: "Fruits that are only in one of the sets"**
    *   Find *all* fruits that are present in either set A or set B, but not in both simultaneously.
    *   If set A contains {🍎, 🍐}, and set B contains {🍐, 🍉}, then set A ^ B will contain {🍎, 🍉}.

5.  **Subset: "Are all fruits from one set present in another?"**
    *   Check if set A is a subset of set B. This means that all fruits from set A are also present in set B.
    *   **Example:** If set A contains {🍎, 🍐}, and set B contains {🍎, 🍐, 🍉}, then A <= B.

6.  **Superset: "Does one set contain all fruits from another?"**
    *   Check if set A is a superset of set B. This means that all fruits from set B are also present in set A.
    *   If set A contains {🍎, 🍐, 🍉}, and set B contains {🍎, 🍐}, then A >= B.



```python
from typing import Set

def create_fruit_set(fruit_string: str) -> Set[str]:
    """
    Creates a set of fruits from a string.

    Args:
        fruit_string: String of fruits (🍎, 🍐, 🍉, 🧺).

    Returns:
        Set of unique fruits.
    """
    if not all(fruit in ["🍎", "🍐", "🍉", "🧺"] for fruit in fruit_string):
        raise ValueError("String can only contain 🍎, 🍐, 🍉, 🧺 symbols")
    return set(fruit_string)  # Use set() to create a set

def display_set(fruit_set: Set[str]) -> str:
  """
  Converts a set of fruits to a string for display.

    Args:
        fruit_set: Set of fruits.

    Returns:
        String for display.
  """
  return "{" + ", ".join(fruit_set) + "}"


# Create fruit sets
fruits_set_A = create_fruit_set("🍎🍐")  # Set A: {🍎, 🍐}
fruits_set_B = create_fruit_set("🍐🍉")  # Set B: {🍐, 🍉}
fruits_set_C = create_fruit_set("🍎🍐🍉")  # Set C: {🍎, 🍐, 🍉}
fruits_set_D = create_fruit_set("🧺")  # Set D: {🧺}

# Print sets
print(f"Set A: {display_set(fruits_set_A)}")
print(f"Set B: {display_set(fruits_set_B)}")
print(f"Set C: {display_set(fruits_set_C)}")
print(f"Set D: {display_set(fruits_set_D)}")

# Union of sets
union_result = fruits_set_A | fruits_set_B
print(f"A ∪ B: {display_set(union_result)}")  # Result: {🍎, 🍐, 🍉}

# Intersection of sets
intersection_result = fruits_set_A & fruits_set_B
print(f"A ∩ B: {display_set(intersection_result)}")  # Result: {🍐}

# Difference of sets
difference_result_AB = fruits_set_A - fruits_set_B
print(f"A - B: {display_set(difference_result_AB)}")  # Result: {🍎}
difference_result_BA = fruits_set_B - fruits_set_A
print(f"B - A: {display_set(difference_result_BA)}")  # Result: {🍉}

# Symmetric difference of sets
symmetric_difference_result = fruits_set_A ^ fruits_set_B
print(f"A ^ B: {display_set(symmetric_difference_result)}")  # Result: {🍎, 🍉}

# Subset
subset_result1 = fruits_set_A <= fruits_set_C
print(f"A <= C: {subset_result1}")  # Result: True (A is a subset of C)
subset_result2 = fruits_set_A <= fruits_set_B
print(f"A <= B: {subset_result2}") # Result: False (A is not a subset of B)

# Superset
superset_result1 = fruits_set_C >= fruits_set_A
print(f"C >= A: {superset_result1}")  # Result: True (C is a superset of A)
superset_result2 = fruits_set_B >= fruits_set_A
print(f"B >= A: {superset_result2}")  # Result: False (B is not a superset of A)

# Check for element presence
print(f"🍎 in A: {'🍎' in fruits_set_A}")  # Result: True
print(f"🍉 in A: {'🍉' in fruits_set_A}")  # Result: False
```

*   **`create_fruit_set(fruit_string)`:** This function creates a set from a string of fruits.
    *   `set(fruit_string)` converts the string into a set, removing duplicates and making the order of elements irrelevant.
    *   We check that the string consists only of allowed Unicode characters.
*   **`display_set(fruit_set)`:** This function is used to convert a set into a readable string for output.
*   **Examples:** We create several sets and apply various operations to them. The results of each operation are printed to the screen.



**5. Practice tasks:**

1.  Create your own fruit sets and try all operations on them.
2.  Implement the `is_disjoint(set1, set2)` function, which will check if two sets are disjoint (intersection = empty set).
3.  Implement the `power_set(fruit_set)` function, which will return the set of all subsets of a given set.
4.  Try to apply sets to solve a real problem. For example, you have two lists of guests for a party, find guests who are in both lists, guests who are only in the first list, etc.
