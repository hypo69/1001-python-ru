# Jeu de bannière : Création de bannière textuelle

    
Le programme crée une bannière textuelle à partir du texte saisi par l'utilisateur. Il salue l'utilisateur, demande le texte et l'affiche sous forme de bannière formatée.
Le code démontre les principes de base du travail avec les fonctions, les entrées/sorties et les opérateurs conditionnels en Python.

---

## **Comment fonctionne le programme**

Le programme se compose de deux parties principales :
1. **Fonction `create_banner(text)`** – responsable de la création et de l'affichage de la bannière textuelle.
2. **Partie principale du programme** – interaction avec l'utilisateur : salutation, demande de texte et validation de la saisie.

---

## **Code du programme**

```python
# Jeu de bannière : Création de bannière textuelle

# Fonction pour créer une bannière
def create_banner(text):
    """
    Crée une bannière textuelle à partir du texte saisi.
    :param text: La chaîne à convertir en bannière.
    :return: None
    """
    # Déterminer la largeur de la bannière (longueur du texte + 4 caractères pour le cadre)
    banner_width = len(text) + 4

    # Afficher la bordure supérieure de la bannière
    print("*" * banner_width)

    # Afficher le texte avec un cadre
    print(f"* {text} *")

    # Afficher la bordure inférieure de la bannière
    print("*" * banner_width)

# Partie principale du programme
if __name__ == "__main__":
    # Saluer l'utilisateur
    print("Bienvenue dans le jeu Banner !")
    print("Entrez du texte, et je créerai une bannière textuelle pour vous.")

    # Demander le texte à l'utilisateur
    user_text = input("Entrez du texte : ")

    # Vérifier que le texte n'est pas vide
    if user_text.strip() == "":
        print("Vous n'avez pas entré de texte. Veuillez réessayer.")
    else:
        # Créer et afficher la bannière
        print("\nVotre bannière est prête :")
        create_banner(user_text)
```

---

## **Description du fonctionnement du code**

### **1. Fonction `create_banner(text)`**
- **Accepte :** la chaîne `text` – le texte à convertir en bannière.
- **Exécute :**
  - Calcule la largeur de la bannière, en ajoutant 4 caractères pour le cadre (`*` et espaces).
  - Affiche les bordures supérieure et inférieure de la bannière à l'aide du caractère `*`.
  - Affiche le texte entouré d'un cadre.

### **2. Partie principale du programme**
- **Salue** l'utilisateur et explique ce que fait le programme.
- **Demande** à l'utilisateur le texte pour créer une bannière.
- **Vérifie** que le texte n'est pas vide :
  - Si l'utilisateur a saisi une chaîne vide, le programme signale une erreur et demande de réessayer.
  - Si du texte est saisi, le programme affiche la bannière créée.

---

## **Exemple de programme**

Si l'utilisateur a saisi le texte `"Bonjour"`, le programme affichera :
```
*********
* Bonjour *
*********
```

---


## **Comment l'interpréteur analyse le code**

### **Ordre d'exécution des opérateurs en Python**
- Python lit le code ligne par ligne, en commençant par le haut et en descendant.
- Chaque ligne est exécutée séquentiellement, sauf si elle fait partie d'une fonction, d'une condition ou d'une boucle.

### **Définition des fonctions**
- Les fonctions sont définies à l'aide du mot-clé `def`.
- La définition d'une fonction n'exécute pas son code, mais crée seulement un "modèle" pour un appel futur.

### **Appels de fonctions**
- Lorsqu'une fonction est appelée, Python passe à sa définition et exécute le code qu'elle contient.
- Une fois l'exécution de la fonction terminée, le contrôle revient à l'endroit d'où elle a été appelée.

### **Instructions conditionnelles (if, else)**
- Les instructions conditionnelles vérifient une condition et exécutent le code à l'intérieur du bloc si la condition est vraie.
- Si la condition est fausse, Python ignore le bloc et passe à la ligne suivante.

### **Boucles (for, while)**
- Les boucles permettent de répéter l'exécution d'un bloc de code plusieurs fois.
- Python vérifie la condition de la boucle avant chaque itération.

### **Opérateurs d'affectation (=)**
- Les opérateurs d'affectation stockent une valeur dans une variable.
- Cela se produit avant que d'autres opérations, telles que les appels de fonctions ou les instructions conditionnelles, ne soient exécutées.

### **Expressions et calculs**
- Les expressions (par exemple, `len(text) + 4`) sont évaluées avant que leur résultat ne soit utilisé dans d'autres parties du code.

---

## **Résumé**

Ce programme démontre les principes de base du travail avec les fonctions, les entrées/sorties et les instructions conditionnelles en Python. Il peut être utile aux débutants pour apprendre le langage et comprendre comment fonctionne l'interpréteur Python.
