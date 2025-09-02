# **Jeu de cartes Acey-Ducey**

## Description
Il s'agit d'une simulation du jeu de cartes Acey-Ducey. Le joueur place des paris en fonction de la probabilité que la carte suivante tombe entre les deux cartes déjà ouvertes.

- **Capital de départ :** Le joueur commence avec 100 dollars.
- **Règles du jeu :**
  1. L'ordinateur distribue deux cartes.
  2. Le joueur peut décider de placer un pari ou non.
  3. Si un pari est placé, une troisième carte est tirée.
  4. Si la valeur de la troisième carte tombe entre les deux premières cartes, le joueur gagne le pari. Sinon, le pari est perdu.
- Le jeu se termine lorsque le joueur perd tout son capital ou le termine manuellement.

## Comment fonctionne le code
---

### **1. Importation de la bibliothèque**
```python
import random
```
- **random** – bibliothèque pour la génération de nombres aléatoires. Elle est utilisée pour mélanger le paquet de cartes et sélectionner des cartes aléatoires.

---

### **2. Création d'un paquet de cartes**
```python
def create_deck():
    ranks = list(range(2, 15))  # Cartes de 2 à 14 (As = 14)
    deck = ranks * 4  # 4 couleurs
    random.shuffle(deck)
    return deck
```
- **ranks** – liste des valeurs de cartes de 2 à 14 (As = 14).
- **deck** – créé en multipliant la liste `ranks` par 4 pour obtenir 4 couleurs (piques, cœurs, carreaux, trèfles).
- **random.shuffle(deck)** – mélange le paquet de cartes.
- La fonction renvoie le paquet mélangé.

---

### **3. Affichage de la carte dans un format lisible**
```python
def card_name(value):
    if value == 11:
        return "Valet"
    elif value == 12:
        return "Dame"
    elif value == 13:
        return "Roi"
    elif value == 14:
        return "As"
    else:
        return str(value)
```
- La fonction prend la valeur numérique de la carte (de 2 à 14) et renvoie sa représentation textuelle.
- Par exemple, 11 → "Valet", 14 → "As".

---

### **4. Boucle de jeu principale**
```python
def play_acey_ducey():
    print("Bienvenue au jeu Acey Ducey !")
    print("Règles : Vous placez un pari, en devinant si la prochaine carte sera entre les deux cartes déjà distribuées.")
    print("Si la carte est égale à l'une des cartes distribuées ou à un As, vous perdez.")
    print("Entrez '0' pour passer le tour.\n")

    money = 100  # Solde de départ du joueur
    deck = create_deck()
```
- **money** – solde de départ du joueur (100 dollars).
- **deck** – un paquet de cartes est créé à l'aide de la fonction `create_deck()`.

---

### **5. Distribution de deux cartes**
```python
while money > 0 and len(deck) >= 3:
    print(f"Votre solde actuel : ${money}")

    # Distribuer deux cartes
    card1 = deck.pop()
    card2 = deck.pop()
    while card1 == card2:  # Si les cartes sont identiques, en tirer de nouvelles
        deck.insert(0, card1)
        deck.insert(0, card2)
        card1 = deck.pop()
        card2 = deck.pop()

    print(f"Première carte : {card_name(card1)}")
    print(f"Deuxième carte : {card_name(card2)}")
```
- **deck.pop()** – extrait la dernière carte du paquet.
- **while card1 == card2** – vérifie si les cartes distribuées sont identiques. Si oui, les replace en haut du paquet et en tire de nouvelles.
- **card_name(card1)** – convertit la valeur numérique de la carte en texte.

---

### **6. Détermination de la plage**
```python
low_card = min(card1, card2)
high_card = max(card1, card2)
```
- **low_card** – valeur minimale des deux cartes.
- **high_card** – valeur maximale des deux cartes.

---

### **7. Placer un pari ou passer le tour**
```python
try:
    bet = int(input(f"Placez votre pari (de 0 à {money}) ou entrez '0' pour passer le tour : "))
    if bet < 0 or bet > money:
        print("Pari invalide. Veuillez réessayer.")
        continue
    if bet == 0:
        print("Vous avez passé votre tour.\n")
        continue  # Passer le tour
except ValueError:
    print("Veuillez entrer un nombre.")
    continue
```
- **input()** – demande au joueur de placer un pari.
- **try-except** – gère les erreurs si le joueur a entré une valeur non numérique.
- **if bet < 0 or bet > money** – vérifie si le pari est valide.
- **if bet == 0** – si le pari est 0, le joueur passe le tour.

---

### **8. Tirer la carte suivante**
```python
next_card = deck.pop()
print(f"Carte suivante : {card_name(next_card)}")
```
- **next_card** – extrait la carte suivante du paquet.
- **card_name(next_card)** – convertit la valeur de la carte en représentation textuelle.

---

### **9. Vérifier le résultat**
```python
if next_card == card1 or next_card == card2 or next_card == 14:
    print("Vous perdez !")
    money -= bet
elif low_card < next_card < high_card:
    print("Vous gagnez !")
    money += bet
else:
    print("Vous perdez !")
    money -= bet
```
- **if next_card == card1 or next_card == card2 or next_card == 14** – si la carte suivante est égale à l'une des cartes distribuées ou si c'est un As, le joueur perd.
- **elif low_card < next_card < high_card** – si la carte suivante est entre les deux cartes distribuées, le joueur gagne.
- **else** – dans tous les autres cas, le joueur perd.

---

### **10. Fin du jeu**
```python
if money <= 0:
    print("Vous n'avez plus d'argent. Fin de la partie.")
else:
    print(f"Partie terminée. Votre solde final : ${money}")
```
- Si le joueur n'a plus d'argent, la partie se termine.
- Si le paquet de cartes est épuisé, la partie se termine également.

---

### **11. Lancement du jeu**
```python
if __name__ == "__main__":
    play_acey_ducey()
```
- Ce bloc lance le jeu si le fichier est exécuté directement (et non importé comme un module).

---

### **Concepts clés utilisés dans le code :**
1. **Fonctions** – le code est divisé en fonctions pour la lisibilité et la réutilisabilité.
2. **Listes** – le paquet de cartes est représenté comme une liste.
3. **Boucles** – utilisées pour traiter les tours de jeu.
4. **Conditions** – vérifient les règles du jeu.
5. **Gestion des exceptions** – utilisée pour gérer les erreurs de saisie.
6. **Génération de nombres aléatoires** – pour mélanger le paquet et sélectionner les cartes.

```