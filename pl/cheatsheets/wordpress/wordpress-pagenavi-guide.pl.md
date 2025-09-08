# Pełny przewodnik po zmiennych w WP-PageNavi dla WordPressa

Nawigacja po stronach to ważna część każdego bloga lub serwisu informacyjnego na WordPressie. Jednym z najpopularniejszych narzędzi do wygodnej nawigacji po stronach jest wtyczka **WP-PageNavi**. Pozwala ona zastąpić standardowe linki „Poprzednia / Następna” bardziej elastyczną i estetyczną paginacją.

Jedną z kluczowych możliwości jest konfiguracja tekstu linków za pomocą **zmiennych**, które automatycznie podstawiają bieżący numer strony, całkowitą liczbę stron i inne informacje.

W tym artykule omówimy **wszystkie dostępne zmienne**, przykłady ich użycia i pokażemy na zrzutach ekranu, gdzie należy je wstawić.

---

## Gdzie znajdują się ustawienia WP-PageNavi

Po zainstalowaniu wtyczki przejdź w panelu administracyjnym WordPressa do:

**Ustawienia → PageNavi**

Tam zobaczysz menu do konfiguracji tekstu linków (przykład na zrzucie ekranu poniżej):

![Ustawienia PageNavi w WordPressie](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 W każdym polu można używać zmiennych, aby dynamicznie wyświetlać bieżącą stronę, całkowitą liczbę stron i inne elementy nawigacji.

---

## Dostępne zmienne WP-PageNavi

Wtyczka udostępnia zestaw placeholderów (zmiennych szablonowych), które można wykorzystać w ustawieniach:

### 🔹 %CURRENT_PAGE%
Wyświetla **numer bieżącej strony**.

Przykład:
```

Jesteś na stronie %CURRENT\_PAGE%

```
👉 Jeśli jesteś na stronie 3, wynik będzie następujący:
```

Jesteś na stronie 3

```

---

### 🔹 %TOTAL_PAGES%
Pokazuje **całkowitą liczbę stron**.

Przykład:
```

Łącznie stron: %TOTAL\_PAGES%

```
👉 Jeśli jest łącznie 10 stron, wynik będzie następujący:
```

Łącznie stron: 10

```

---

### 🔹 %PAGE_NUMBER%
Służy do wyświetlania **numeru każdej strony** na liście.

Przykład:
```

Strona %PAGE\_NUMBER%

```
👉 W nawigacji pojawią się linki:
```

Strona 1 | Strona 2 | Strona 3 | ...

```

---

## Tabela zmiennych WP-PageNavi

| Zmienna           | Opis                                  | Przykład konfiguracji                   | Wynik (jeśli 3. strona z 10) |
|-------------------|---------------------------------------|-----------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Numer bieżącej strony                 | `Teraz jesteś na stronie %CURRENT_PAGE%` | `Teraz jesteś na stronie 3` |
| **%TOTAL_PAGES%**  | Całkowita liczba stron                | `Łącznie stron: %TOTAL_PAGES%`          | `Łącznie stron: 10` |
| **%PAGE_NUMBER%**  | Numer każdej strony na liście         | `Strona %PAGE_NUMBER%`                  | `Strona 1 | Strona 2 | Strona 3 …` |
| **1 (statycznie)** | Pierwsza strona (brak zmiennej)      | `Pierwsza` lub `Strona 1`               | `Pierwsza` |
| **%TOTAL_PAGES%**  | Ostatnia strona                       | `Strona %TOTAL_PAGES%`                  | `Strona 10` |
| **← / → / …**      | Symbole strzałek i skrótów            | `← Poprzednia`, `Następna →`, `…`       | `← Poprzednia | 1 | 2 | 3 | … | 10 | Następna →` |

---

## Przykład pełnej konfiguracji

Na powyższym zrzucie ekranu można wypełnić pola w następujący sposób:

- **Text For Number Of Pages**:  
  `Strona %CURRENT_PAGE% z %TOTAL_PAGES%`

- **Text For Current Page**:  
  `%PAGE_NUMBER%`

- **Text For Page**:  
  `%PAGE_NUMBER%`

- **Text For First Page**:  
  `Pierwsza`

- **Text For Last Page**:  
  `Strona %TOTAL_PAGES%`

- **Text For Previous Page**:  
  `← Wstecz`

- **Text For Next Page**:  
  `Dalej →`

- **Text For Previous …**:  
  `…`

- **Text For Next …**:  
  `…`

👉 W rezultacie odwiedzający zobaczą nawigację podobną do tej:
```

← Wstecz | Pierwsza | 1 | 2 | 3 | … | Strona 10 | Dalej →

```

---

## Podsumowanie

Zmienne w WP-PageNavi są proste, ale dają elastyczność w konfiguracji nawigacji:

- `%CURRENT_PAGE%` — bieżąca strona  
- `%TOTAL_PAGES%` — łączna liczba stron  
- `%PAGE_NUMBER%` — numer konkretnej strony  

Dla pierwszej strony użyj `1`, a dla ostatniej — `%TOTAL_PAGES%`.

Dzięki tym ustawieniom nawigacja na stronie może stać się bardziej zrozumiała i wygodna dla odwiedzających.
