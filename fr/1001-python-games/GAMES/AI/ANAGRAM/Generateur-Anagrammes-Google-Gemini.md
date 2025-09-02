# Générateur d'anagrammes utilisant Google Gemini

Ceci est un code simple pour générer des anagrammes à l'aide du grand modèle linguistique Google Gemini.

## Description

Le programme prend en entrée un ensemble de lettres russes et tente de trouver un mot russe existant composé de ces lettres (en utilisant tout ou partie d'entre elles).

## Règles des anagrammes

*   Seuls les mots russes existants sont utilisés.
*   Lors de la recherche d'anagrammes, seules les lettres russes sont prises en compte. Les chiffres et autres symboles sont ignorés.
*   S'il est possible de former plusieurs mots, l'un d'entre eux est renvoyé.
*   Si aucun mot ne peut être formé à partir des lettres données, le message "Pas d'anagrammes" est renvoyé.

## Utilisation

1.  **Clé API Google Gemini.**

    CLÉ API POUR LE MODÈLE ICI : [https://aistudio.google.com/](https://aistudio.google.com/)

    Ou vous pouvez utiliser la mienne :

    AIzaSyCprZ9Tr-rB_xFau5zgWsKPM_6W-FmUntk

    J'ai créé la clé pour l'apprentissage et la compréhension du code. Ne surchargez pas le modèle !

2.  **Installez les bibliothèques nécessaires :**

    ```bash
    pip install google-generativeai
    ```

3.  **Exécutez le script :**

    ```bash
    python anagram_generator.py
    ```

4.  Le script demandera la clé API. Entrez-la.
5.  Après cela, entrez les lettres pour lesquelles vous souhaitez trouver une anagramme.

## Explication du code

*   `import google.generativeai as genai` : Importe la bibliothèque pour interagir avec Gemini.
*   `import re` : Importe la bibliothèque pour travailler avec les expressions régulières (pour nettoyer l'entrée).
*   La classe `GoogleGenerativeAI` encapsule la logique d'interaction avec le modèle Gemini.
*   `system_instruction` : Il s'agit de l'invite système (instruction) pour Gemini, qui explique ce qui est attendu d'elle.
*   `re.sub(r"[^а-яА-ЯёЁ]", "", q)` : Cette ligne supprime de la chaîne d'entrée `q` tous les caractères qui ne sont pas des lettres russes. `[^а-яА-ЯёЁ]` est une expression régulière qui signifie "tout caractère *n'étant pas* dans la plage a-я, А-Я et ёЁ".
*   La vérification `if not q:` vérifie si la chaîne est devenue vide après la suppression de tous les caractères non cyrilliques.
*   `model.generate_content(q)` : Envoie la requête `q` au modèle Gemini.
*   La gestion des exceptions `try...except` permet d'éviter le plantage du programme en cas d'erreurs lors de l'interaction avec l'API.

## Exemple d'utilisation

```
Entrez les lettres pour lesquelles Gemini trouvera une anagramme : сон
нос
Entrez les lettres pour lesquelles Gemini trouvera une anagramme : апельсин
спаниель
Entrez les lettres pour lesquelles Gemini trouvera une anagramme : 12345абвг
абвг
Entrez les lettres pour lesquelles Gemini trouvera une anagramme : 
```

