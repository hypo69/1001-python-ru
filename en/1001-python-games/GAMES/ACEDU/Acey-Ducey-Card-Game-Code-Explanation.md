# **Acey-Ducey Card Game**

## Description
This is a simulation of the Acey-Ducey card game. The player places bets based on the probability that the next card will fall between two already open cards.

- **Starting Capital:** The player starts with $100.
- **Game Rules:**
  1. The computer deals two cards.
  2. The player can decide whether to place a bet or not.
  3. If a bet is placed, a third card is drawn.
  4. If the value of the third card falls between the first two cards, the player wins the bet. Otherwise, the bet is lost.
- The game ends when the player loses all capital or manually ends it.

## How the code works
---

### **1. Import library**
```python
import random
```
- **random** – a library for generating random numbers. It is used to shuffle the deck of cards and select random cards.

---

### **2. Create a deck of cards**
```python
def create_deck():
    ranks = list(range(2, 15))  # Cards from 2 to 14 (Ace = 14)
    deck = ranks * 4  # 4 suits
    random.shuffle(deck)
    return deck
```
- **ranks** – a list of card values from 2 to 14 (Ace = 14).
- **deck** – created by multiplying the `ranks` list by 4 to get 4 suits (spades, hearts, diamonds, clubs).
- **random.shuffle(deck)** – shuffles the deck of cards.
- The function returns the shuffled deck.

---

### **3. Display card in readable format**
```python
def card_name(value):
    if value == 11:
        return "Jack"
    elif value == 12:
        return "Queen"
    elif value == 13:
        return "King"
    elif value == 14:
        return "Ace"
    else:
        return str(value)
```
- The function takes the numeric value of the card (from 2 to 14) and returns its text representation.
- For example, 11 → "Jack", 14 → "Ace".

---

### **4. Main game loop**
```python
def play_acey_ducey():
    print("Welcome to Acey Ducey!")
    print("Rules: You place a bet, guessing if the next card will be between the two dealt cards.")
    print("If the card is equal to one of the dealt cards or an Ace, you lose.")
    print("Enter '0' to skip turn.\n")

    money = 100  # Player's starting balance
    deck = create_deck()
```
- **money** – player's starting balance ($100).
- **deck** – a deck of cards is created using the `create_deck()` function.

---

### **5. Dealing two cards**
```python
while money > 0 and len(deck) >= 3:
    print(f"Your current balance: ${money}")

    # Deal two cards
    card1 = deck.pop()
    card2 = deck.pop()
    while card1 == card2:  # If cards are the same, draw new ones
        deck.insert(0, card1)
        deck.insert(0, card2)
        card1 = deck.pop()
        card2 = deck.pop()

    print(f"First card: {card_name(card1)}")
    print(f"Second card: {card_name(card2)}")
```
- **deck.pop()** – extracts the last card from the deck.
- **while card1 == card2** – checks if the dealt cards are the same. If they are, it returns them to the top of the deck and draws new ones.
- **card_name(card1)** – converts the numeric value of the card to text.

---

### **6. Determining the range**
```python
low_card = min(card1, card2)
high_card = max(card1, card2)
```
- **low_card** – minimum value of the two cards.
- **high_card** – maximum value of the two cards.

---

### **7. Place a bet or skip turn**
```python
try:
    bet = int(input(f"Place your bet (from 0 to {money}) or enter '0' to skip turn: "))
    if bet < 0 or bet > money:
        print("Invalid bet. Please try again.")
        continue
    if bet == 0:
        print("You skipped your turn.\n")
        continue  # Skip turn
except ValueError:
    print("Please enter a number.")
    continue
```
- **input()** – prompts the player for a bet.
- **try-except** – handles errors if the player entered non-numeric input.
- **if bet < 0 or bet > money** – checks if the bet is valid.
- **if bet == 0** – if the bet is 0, the player skips the turn.

---

### **8. Draw next card**
```python
next_card = deck.pop()
print(f"Next card: {card_name(next_card)}")
```
- **next_card** – extracts the next card from the deck.
- **card_name(next_card)** – converts the card value to text representation.

---

### **9. Check result**
```python
if next_card == card1 or next_card == card2 or next_card == 14:
    print("You lose!")
    money -= bet
elif low_card < next_card < high_card:
    print("You win!")
    money += bet
else:
    print("You lose!")
    money -= bet
```
- **if next_card == card1 or next_card == card2 or next_card == 14** – if the next card is equal to one of the dealt cards or it's an Ace, the player loses.
- **elif low_card < next_card < high_card** – if the next card is between the two dealt cards, the player wins.
- **else** – in all other cases, the player loses.

---

### **10. Game termination**
```python
if money <= 0:
    print("You ran out of money. Game over.")
else:
    print(f"Game over. Your final balance: ${money}")
```
- If the player runs out of money, the game ends.
- If the deck runs out of cards, the game also ends.

---

### **11. Start game**
```python
if __name__ == "__main__":
    play_acey_ducey()
```
- This block starts the game if the file is executed directly (not imported as a module).

---

### **Key concepts used in the code:**
1. **Functions** – code is divided into functions for readability and reusability.
2. **Lists** – the deck of cards is represented as a list.
3. **Loops** – used to process game turns.
4. **Conditions** – check game rules.
5. **Exception handling** – used to handle input errors.
6. **Random number generation** – for shuffling the deck and selecting cards.

```