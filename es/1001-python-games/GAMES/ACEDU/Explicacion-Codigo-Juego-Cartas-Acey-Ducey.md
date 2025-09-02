# **Juego de cartas Acey-Ducey**

## Descripción
Esta es una simulación del juego de cartas Acey-Ducey. El jugador realiza apuestas basándose en la probabilidad de que la siguiente carta caiga entre dos cartas ya abiertas.

- **Capital inicial:** El jugador comienza con 100 dólares.
- **Reglas del juego:**
  1. La computadora reparte dos cartas.
  2. El jugador puede decidir si apostar o no.
  3. Si se realiza una apuesta, se saca una tercera carta.
  4. Si el valor de la tercera carta cae entre las dos primeras cartas, el jugador gana la apuesta. De lo contrario, la apuesta se pierde.
- El juego termina cuando el jugador pierde todo su capital o lo finaliza manualmente.

## Cómo funciona el código
---

### **1. Importar biblioteca**
```python
import random
```
- **random** – una biblioteca para generar números aleatorios. Se utiliza para barajar la baraja de cartas y seleccionar cartas aleatorias.

---

### **2. Crear una baraja de cartas**
```python
def create_deck():
    ranks = list(range(2, 15))  # Cartas del 2 al 14 (As = 14)
    deck = ranks * 4  # 4 palos
    random.shuffle(deck)
    return deck
```
- **ranks** – una lista de valores de cartas del 2 al 14 (As = 14).
- **deck** – se crea multiplicando la lista `ranks` por 4 para obtener 4 palos (picas, corazones, diamantes, tréboles).
- **random.shuffle(deck)** – baraja la baraja de cartas.
- La función devuelve la baraja barajada.

---

### **3. Mostrar carta en formato legible**
```python
def card_name(value):
    if value == 11:
        return "Jota"
    elif value == 12:
        return "Reina"
    elif value == 13:
        return "Rey"
    elif value == 14:
        return "As"
    else:
        return str(value)
```
- La función toma el valor numérico de la carta (del 2 al 14) y devuelve su representación textual.
- Por ejemplo, 11 → "Jota", 14 → "As".

---

### **4. Bucle principal del juego**
```python
def play_acey_ducey():
    print("\u00a1Bienvenido a Acey Ducey!")
    print("Reglas: Usted hace una apuesta, adivinando si la siguiente carta estará entre las dos cartas repartidas.")
    print("Si la carta es igual a una de las cartas repartidas o un As, pierde.")
    print("Ingrese '0' para pasar el turno.\n")

    money = 100  # Saldo inicial del jugador
    deck = create_deck()
```
- **money** – saldo inicial del jugador (100 dólares).
- **deck** – se crea una baraja de cartas usando la función `create_deck()`.

---

### **5. Repartir dos cartas**
```python
while money > 0 and len(deck) >= 3:
    print(f"Su saldo actual: ${money}")

    # Repartir dos cartas
    card1 = deck.pop()
    card2 = deck.pop()
    while card1 == card2:  # Si las cartas son iguales, sacar nuevas
        deck.insert(0, card1)
        deck.insert(0, card2)
        card1 = deck.pop()
        card2 = deck.pop()

    print(f"Primera carta: {card_name(card1)}")
    print(f"Segunda carta: {card_name(card2)}")
```
- **deck.pop()** – extrae la óltima carta de la baraja.
- **while card1 == card2** – comprueba si las cartas repartidas son iguales. Si lo son, las devuelve a la parte superior de la baraja y saca nuevas.
- **card_name(card1)** – convierte el valor numérico de la carta a texto.

---

### **6. Determinar el rango**
```python
low_card = min(card1, card2)
high_card = max(card1, card2)
```
- **low_card** – valor mínimo de las dos cartas.
- **high_card** – valor máximo de las dos cartas.

---

### **7. Hacer una apuesta o pasar el turno**
```python
try:
    bet = int(input(f"Haga su apuesta (de 0 a {money}) o ingrese '0' para pasar el turno: "))
    if bet < 0 or bet > money:
        print("Apuesta inválida. Intente de nuevo.")
        continue
    if bet == 0:
        print("Ha pasado su turno.\n")
        continue  # Pasar turno
except ValueError:
    print("Por favor, ingrese un número.")
    continue
```
- **input()** – solicita al jugador una apuesta.
- **try-except** – maneja errores si el jugador ingresó una entrada no numérica.
- **if bet < 0 or bet > money** – comprueba si la apuesta es válida.
- **if bet == 0** – si la apuesta es 0, el jugador pasa el turno.

---

### **8. Sacar la siguiente carta**
```python
next_card = deck.pop()
print(f"Siguiente carta: {card_name(next_card)}")
```
- **next_card** – extrae la siguiente carta de la baraja.
- **card_name(next_card)** – convierte el valor de la carta a representación textual.

---

### **9. Comprobar el resultado**
```python
if next_card == card1 or next_card == card2 or next_card == 14:
    print("\u00a1Pierdes!")
    money -= bet
elif low_card < next_card < high_card:
    print("\u00a1Ganas!")
    money += bet
else:
    print("\u00a1Pierdes!")
    money -= bet
```
- **if next_card == card1 or next_card == card2 or next_card == 14** – si la siguiente carta es igual a una de las cartas repartidas o es un As, el jugador pierde.
- **elif low_card < next_card < high_card** – si la siguiente carta está entre las dos cartas repartidas, el jugador gana.
- **else** – en todos los demás casos, el jugador pierde.

---

### **10. Finalización del juego**
```python
if money <= 0:
    print("Te quedaste sin dinero. Fin del juego.")
else:
    print(f"Juego terminado. Su saldo final: ${money}")
```
- Si el jugador se queda sin dinero, el juego termina.
- Si la baraja se queda sin cartas, el juego también termina.

---

### **11. Iniciar juego**
```python
if __name__ == "__main__":
    play_acey_ducey()
```
- Este bloque inicia el juego si el archivo se ejecuta directamente (no se importa como un módulo).

---

### **Conceptos clave utilizados en el código:**
1. **Funciones** – el código se divide en funciones para facilitar la lectura y la reutilización.
2. **Listas** – la baraja de cartas se representa como una lista.
3. **Bucles** – se utilizan para procesar los turnos del juego.
4. **Condiciones** – comprueban las reglas del juego.
5. **Manejo de excepciones** – se utiliza para manejar errores de entrada.
6. **Generación de números aleatorios** – para barajar la baraja y seleccionar cartas.

```