### **Czas wielomianowy**

**Czas wielomianowy** to termin używany w teorii złożoności obliczeniowej do opisania czasu wykonania algorytmu, który rośnie jako wielomian rozmiaru danych wejściowych. Jeśli czas wykonania algorytmu można wyrazić jako \(O(n^k)\), gdzie \(n\) to rozmiar danych wejściowych, a \(k\) to stała, to taki algorytm działa w czasie wielomianowym.

#### **Przykłady:**
1. **Sortowanie listy**: Algorytmy takie jak sortowanie przez scalanie lub sortowanie szybkie działają w \(O(n \log n)\), co jest czasem wielomianowym.
2. **Znajdowanie najkrótszej ścieżki w grafie**: Algorytm Dijkstry działa w \(O(n^2)\) lub \(O(n \log n)\) w zależności od implementacji, co również jest wielomianowe.

#### **Cechy:**
- Algorytmy działające w czasie wielomianowym są uważane za **wydajne** i **praktycznie stosowalne**.
- Problemy, które można rozwiązać w czasie wielomianowym, należą do klasy **P**.

---

### **Czas wykładniczy**

**Czas wykładniczy** to czas wykonania algorytmu, który rośnie wykładniczo w zależności od rozmiaru danych wejściowych. Jeśli czas wykonania można wyrazić jako \(O(k^n)\), gdzie \(n\) to rozmiar danych wejściowych, a \(k\) to stała, to taki algorytm działa w czasie wykładniczym.

#### **Przykłady:**
1. **Problem komiwojażera**: Rozwiązanie siłowe wszystkich możliwych tras wymaga \(O(n!)\) czasu, co jest gorsze niż wykładnicze.
2. **Iteracja po wszystkich podzbiorach**: Algorytm, który sprawdza wszystkie możliwe podzbiory zbioru \(n\) elementów, działa w \(O(2^n)\).

#### **Cechy:**
- Algorytmy działające w czasie wykładniczym są uważane za **nieefektywne** dla dużych danych wejściowych, ponieważ czas wykonania staje się niepraktycznie duży nawet dla stosunkowo małych \(n\).
- Problemy, które można rozwiązać tylko w czasie wykładniczym, często należą do klas **NP-trudnych** lub **NP-zupełnych**.

---

### **Porównanie czasu wielomianowego i wykładniczego**

| **Charakterystyka** | **Czas wielomianowy** | **Czas wykładniczy** |
| ----------------------------- | -------------------------------------- | ---------------------------------------- |
| **Wzrost czasu wykonania** | Powolny (np. \(n^2\), \(n^3\)) | Szybki (np. \(2^n\), \(3^n\)) |
| **Przykłady problemów** | Sortowanie, wyszukiwanie najkrótszej ścieżki | Problem komiwojażera, wyliczanie podzbiorów |
| **Praktyczna stosowalność** | Wydajny dla dużych danych | Niepraktyczny dla dużych danych |
| **Klasa złożoności** | P | NP-trudne, NP-zupełne |

---

### **Dlaczego to jest ważne?**

1. **Czas wielomianowy**:
   - Algorytmy działające w czasie wielomianowym są uważane za **praktycznie stosowalne**, ponieważ mogą przetwarzać duże ilości danych w rozsądnym czasie.
   - Problemy klasy **P** (rozwiązywalne w czasie wielomianowym) są podstawą wielu zastosowań w informatyce, takich jak przetwarzanie danych, sieci, kryptografia i sztuczna inteligencja.

2. **Czas wykładniczy**:
   - Algorytmy działające w czasie wykładniczym stają się **niepraktyczne** nawet dla stosunkowo małych danych wejściowych. Na przykład dla \(n = 100\), \(2^n\) już przekracza liczbę atomów w obserwowalnym wszechświecie.
   - Problemy, które można rozwiązać tylko w czasie wykładniczym, często wymagają użycia **metod aproksymacyjnych**, **heurystyk** lub **obliczeń równoległych**.

---

### **Przykład dla zrozumienia**

Wyobraź sobie, że masz problem i chcesz go rozwiązać dla \(n = 10\) i \(n = 100\):

- **Czas wielomianowy \(n^2\)**:
  - Dla \(n = 10\): \(10^2 = 100\) operacji.
  - Dla \(n = 100\): \(100^2 = 10\,000\) operacji.

- **Czas wykładniczy \(2^n\)**:
  - Dla \(n = 10\): \(2^{10} = 1\,024\) operacji.
  - Dla \(n = 100\): \(2^{100} \approx 1.26 \times 10^{30}\) operacji.

Jak widać, dla \(n = 100\) algorytm wielomianowy wykona 10 000 operacji, co jest całkiem realistyczne, podczas gdy algorytm wykładniczy będzie wymagał \(1.26 \times 10^{30}\) operacji, co jest praktycznie niemożliwe.

Aby utworzyć wykresy ilustrujące różnicę między czasem wielomianowym a wykładniczym, możesz użyć różnych funkcji matematycznych. Oto przykłady funkcji, które można wykorzystać do wizualizacji:

---

### **Funkcje wielomianowe**
1. **Funkcja liniowa**:  
   \( f(n) = n \)  
   Przykład: czas wykonania algorytmu, który przetwarza każdy element raz.

2. **Funkcja kwadratowa**:  
   \( f(n) = n^2 \)  
   Przykład: czas wykonania algorytmu z zagnieżdżonymi pętlami, np. sortowanie bąbelkowe.

3. **Funkcja sześcienna**:  
   \( f(n) = n^3 \)  
   Przykład: czas wykonania algorytmu, który przetwarza dane trójwymiarowe.

4. **Funkcja logarytmiczna**:  
   \( f(n) = \log n \)    
   Przykład: czas wykonania wyszukiwania binarnego.

5. **Funkcja liniowo-logarytmiczna**:  
   \( f(n) = n \log n \)  
   Przykład: czas wykonania sortowania szybkiego lub sortowania przez scalanie.

---

### **Funkcje wykładnicze**
1. **Funkcja wykładnicza**:  
   \( f(n) = 2^n \)  
   Przykład: czas wykonania algorytmu, który iteruje po wszystkich podzbiorach zbioru.

2. **Funkcja silni**:  
   \( f(n) = n! \)  
   Przykład: czas wykonania algorytmu, który iteruje po wszystkich permutacjach (np. Problem komiwojażera).

3. **Funkcja wykładnicza o innej podstawie**:  
   \( f(n) = 3^n \)  
   Przykład: czas wykonania algorytmu, który eksploruje wszystkie możliwe kombinacje.

---

### **Przykładowy kod do rysowania wykresów (Python, Matplotlib)**

```python
import matplotlib.pyplot as plt
import numpy as np
import math # Import the standard math module

# Zakres wartości n
n = np.linspace(1, 20, 100)

# Funkcje wielomianowe
linear = n
quadratic = n**2
cubic = n**3
logarithmic = np.log(n)
nlogn = n * np.log(n)

# Funkcje wykładnicze
exponential = 2**n
# Użyj math.factorial z zaimportowanego modułu math
factorial = [math.factorial(int(i)) for i in n]  # Silnia jest zdefiniowana tylko dla liczb całkowitych

# Rysowanie wykresów
plt.figure(figsize=(10, 6))

# Funkcje wielomianowe
plt.plot(n, linear, label='Liniowa: $f(n) = n$')
plt.plot(n, quadratic, label='Kwadratowa: $f(n) = n^2$')
plt.plot(n, cubic, label='Sześcienna: $f(n) = n^3$')
plt.plot(n, logarithmic, label='Logarytmiczna: $f(n) = \log n$')
plt.plot(n, nlogn, label='Liniowo-logarytmiczna: $f(n) = n \log n$')

# Funkcje wykładnicze
plt.plot(n, exponential, label='Wykładnicza: $f(n) = 2^n$')
plt.plot(n, factorial, label='Silnia: $f(n) = n!$')

# Ustawienia wykresu
plt.yscale('log')  # Skala logarytmiczna dla wygody
plt.xlabel('Rozmiar wejścia (n)')
plt.ylabel('Złożoność czasowa')
plt.title('Porównanie złożoności czasowej wielomianowej i wykładniczej')
plt.legend()
plt.grid(True)
plt.show()
```

---
![Exponetialy](../assets/exponetialy.png)

### **Co pokaże wykres?**
- **Funkcje wielomianowe** rosną powoli i pozostają na dole wykresu.
- **Funkcje wykładnicze** rosną bardzo szybko i wznoszą się nawet dla małych wartości \(n\).
- Użycie **skali logarytmicznej** (na osi Y) pomaga wizualizować różnicę między funkcjami wielomianowymi a wykładniczymi, ponieważ ich wartości różnią się o rzędy wielkości.

---