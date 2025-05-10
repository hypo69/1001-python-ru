### `question_084.md`

**Вопрос 84.** Какой результат будет получен при выполнении следующего кода Python?

```python
def anagram(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    return sorted(word1) == sorted(word2)

print(anagram("cinema", "iceman"))
print(anagram("cool", "loco"))
print(anagram("men", "women"))
print(anagram("python", "pythno"))
```

-   A.  `True True True True`
-   B.  `True False True False`
-   C.  `False True False True`
-   D.  `True True False True`

**Правильный ответ: D**

**Объяснение:**

Код проверяет, являются ли два слова анаграммами (состоят из одних и тех же букв, но в разном порядке).

1. **Функция `anagram(word1, word2)`:**
   - Преобразует оба слова в нижний регистр (`lower()`).
   - Сортирует буквы каждого слова (`sorted()`).
   - Если отсортированные буквы одинаковы, возвращает `True` (слова - анаграммы), иначе `False`.

2. **Результаты вызовов:**
   - `"cinema"` и `"iceman"`: Анаграммы. `sorted("cinema") == sorted("iceman")` -> `True`
   - `"cool"` и `"loco"`: Анаграммы. `sorted("cool") == sorted("loco")` -> `True`
   - `"men"` и `"women"`: Не анаграммы. `sorted("men") != sorted("women")` -> `False`
   - `"python"` и `"pythno"`: Анаграммы. `sorted("python") == sorted("pythno")` -> `True`

Таким образом, вывод программы: `True True False True`.
