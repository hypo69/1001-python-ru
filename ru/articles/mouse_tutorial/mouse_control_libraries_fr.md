# Contrôle de la Souris en Python : Aperçu et Comparaison des Bibliothèques

L'automatisation des actions de la souris est un outil puissant pour les tests, la recherche scientifique, les processus métier et la création de technologies d'assistance. Au sein de l'écosystème Python, plusieurs bibliothèques existent à ces fins, chacune avec ses propres forces et cas d'utilisation. Dans cet article, nous examinerons en détail trois bibliothèques multiplateformes principales : `PyAutoGUI`, `pynput` et `mouse`, et mentionnerons également brièvement d'autres solutions spécialisées.

## 1. Bibliothèque PyAutoGUI : Automatisation GUI de Haut Niveau

`PyAutoGUI` est une bibliothèque multiplateforme puissante et facile à utiliser qui permet aux scripts Python de contrôler la souris et le clavier, de prendre des captures d'écran et d'effectuer d'autres tâches d'automatisation de l'interface utilisateur graphique (GUI). Elle est idéale pour automatiser les tâches routinières, tester des logiciels et créer des bots. **Prend en charge Windows, macOS et Linux.**

### Installation

```bash
pip install pyautogui
```

### Fonctionnalités Clés

*   **Mouvement du Curseur** : `pyautogui.moveTo(x, y, duration=seconds)` pour un mouvement absolu et `pyautogui.move(xOffset, yOffset, duration=seconds)` pour un mouvement relatif.
*   **Clics de Souris** : `pyautogui.click()`, `pyautogui.rightClick()`, `pyautogui.doubleClick()`, `pyautogui.tripleClick()`. Vous pouvez spécifier les coordonnées et le bouton.
*   **Glisser-déposer (Drag and Drop)** : `pyautogui.dragTo(x, y, duration=seconds)` ou `pyautogui.drag(xOffset, yOffset, duration=seconds)`.
*   **Défilement de la Molette de la Souris** : `pyautogui.scroll(amount)` (valeur positive fait défiler vers le haut, négative vers le bas).
*   **Interaction Clavier** : `pyautogui.write()`, `pyautogui.press()`, `pyautogui.hotkey()`.
*   **Obtenir la Position du Curseur** : `pyautogui.position()`.
*   **Failsafe** : Une fonction de sécurité intégrée qui arrête le script lorsque le curseur de la souris est déplacé vers l'un des quatre coins de l'écran.

### Exemples d'Utilisation

```python
import pyautogui
import time

# Déplacer le curseur
pyautogui.moveTo(100, 150, duration=1)
print(f"Curseur déplacé vers {pyautogui.position()}")

# Clic gauche
pyautogui.click(200, 250)
print("Clic effectué.")

# Glisser-déposer
pyautogui.moveTo(500, 500, duration=0.5)
pyautogui.dragTo(600, 600, duration=1)
print("Glisser-déposer effectué.")

# Défilement de la molette
pyautogui.scroll(-100)
print("Défilement vers le bas effectué.")

# Taper du texte
pyautogui.write('Bonjour, PyAutoGUI!', interval=0.1)
print("Texte tapé.")
```

### Quand utiliser PyAutoGUI ?

✅ Idéal si vous avez besoin d'un moyen rapide et facile d'automatiser les actions de l'utilisateur, de simuler des entrées et de prendre des captures d'écran. Il est excellent pour les scripts d'automatisation de haut niveau où un contrôle détaillé des événements d'entrée n'est pas requis.

❌ Pas le meilleur choix pour la surveillance d'événements de bas niveau ou le blocage d'entrées.

## 2. Bibliothèque pynput : Contrôle et Surveillance Flexibles

`pynput` est un outil moderne et activement maintenu pour la surveillance et le contrôle complets des périphériques d'entrée. Il fournit un accès détaillé aux événements de la souris et du clavier, y compris la possibilité de les bloquer ou de les modifier en temps réel. **Prend en charge Windows, macOS et Linux.**

### Installation

```bash
pip install pynput
```

### Fonctionnalités Clés

*   **Écouteurs d'Événements Complets** : `pynput.mouse.Listener` permet de suivre les mouvements, les clics et le défilement avec accès aux coordonnées, au type de bouton et à l'état (enfoncé/relâché).
*   **Blocage d'Événements** : Si un gestionnaire d'événements renvoie `False`, l'événement n'est pas transmis au système. C'est une fonctionnalité unique et puissante.
*   **Contrôle de la Souris via un Contrôleur** : `pynput.mouse.Controller` pour émuler des actions (positionnement, mouvement relatif, clics, défilement).
*   **Architecture Clavier Unifiée** : Combine facilement les actions de la souris et du clavier.
*   **Sécurité des Threads** : Les écouteurs fonctionnent dans des threads séparés, offrant une gestion flexible.

### Exemples d'Utilisation

```python
from pynput import mouse
from pynput.mouse import Controller, Button
import time

# Contrôle de la souris
mouse_ctrl = Controller()
print(f"Position actuelle : {mouse_ctrl.position}")
mouse_ctrl.position = (100, 200)
mouse_ctrl.move(50, -50)
mouse_ctrl.click(Button.left, 1)
mouse_ctrl.scroll(0, 2)
print("Actions de la souris effectuées.")

# Écouteur d'événements
def on_click(x, y, button, pressed):
    print(f"Clic à ({x}, {y}) avec le bouton {button}. Enfoncé : {pressed}")
    if not pressed:
        # Arrêter l'écouteur après le relâchement du bouton
        return False

listener = mouse.Listener(on_click=on_click)
listener.start()
print("Écouteur actif. Cliquez avec la souris.")
listener.join() # Attendre la fin de l'écouteur
print("Écouteur terminé.")
```

### Quand utiliser pynput ?

✅ Idéal si vous :
- Avez besoin d'**analyser le comportement de l'utilisateur** (coordonnées, trajectoires, fréquence des clics).
- Créez des **systèmes de raccourcis clavier**, des **filtres d'entrée** ou des **technologies d'assistance**.
- Voulez **bloquer ou modifier l'entrée** en temps réel.
- Menez une **expérience scientifique**, des **tests d'utilisabilité** ou un **système de sécurité**.
- Nécessitez une **intégration souris et clavier** dans un seul script.

❌ Pas le choix le plus rapide si vous avez seulement besoin d'enregistrer et de rejouer des actions sans analyse.

## 3. Bibliothèque mouse : Simplicité et Enregistrement d'Actions

La bibliothèque `mouse` est un outil minimaliste mais efficace pour émuler et enregistrer des séquences d'actions de la souris. Sa principale caractéristique est le support intégré pour l'enregistrement et la lecture, ce qui la rend idéale pour le prototypage rapide de macros. **Prend en charge Windows, macOS et Linux.**

### Installation

```bash
pip install mouse
```

### Fonctionnalités Clés

*   **Mouvement du Curseur** : `mouse.move(x, y, absolute=True/False)`.
*   **Clics de Souris** : `mouse.click('left'/'right'/'middle')`.
*   **Glisser-déposer** : `mouse.drag(x1, y1, x2, y2, absolute=True)`.
*   **Molette de Défilement** : `mouse.wheel(delta)`.
*   **Obtenir la Position du Curseur** : `mouse.get_position()`.
*   **Vérifier l'État du Bouton** : `mouse.is_pressed(button)`.
*   **Enregistrer et Rejouer des Événements** : `mouse.record()` et `mouse.play()`. C'est une fonction intégrée unique.
*   **Gestionnaire de Clic Simple** : `mouse.on_click(handler)`.

### Exemples d'Utilisation

```python
import mouse
import time

# Déplacer et cliquer
mouse.move(200, 300, absolute=True, duration=0.2)
mouse.click('left')
print("Déplacement et clic effectués.")

# Enregistrer et rejouer (nécessite une entrée interactive)
print("Commencez l'enregistrement. Appuyez sur le bouton droit pour arrêter.")
# events = mouse.record()
# print("Enregistrement terminé. Lecture...")
# mouse.play(events[:-1]) # Rejouer tous les événements sauf le dernier (relâchement du bouton droit)
# print("Lecture terminée.")

# Défilement
mouse.wheel(-2)
print("Défilement vers le bas effectué.")
```

### Quand utiliser mouse ?

✅ Idéal pour :
- L'enregistrement et la relecture d'actions routinières.
- Les scripts d'automatisation simples sans retour d'information.
- Les exemples éducatifs et les démonstrations où la simplicité maximale est essentielle.

❌ Ne convient pas pour :
- L'analyse du comportement de l'utilisateur (les gestionnaires ne reçoivent pas les coordonnées).
- La création de filtres ou de bloqueurs d'entrée.
- L'intégration du clavier.
- Le projet n'a pas été mis à jour depuis 2021, ce qui peut être un risque pour les projets à long terme.

## 4. Autres Bibliothèques Notables

Bien que `PyAutoGUI`, `pynput` et `mouse` soient les plus polyvalentes, d'autres bibliothèques existent pour des tâches plus spécifiques :

*   **PyDirectInput** : Une bibliothèque spécialisée conçue comme une alternative à `PyAutoGUI` pour l'automatisation des jeux. Elle peut contourner les problèmes où certains jeux peuvent ne pas enregistrer les entrées de `PyAutoGUI` en raison de leurs mécanismes spécifiques de gestion des entrées.
*   **pywinauto** : Axée sur l'automatisation de l'interface utilisateur de Windows. Elle interagit avec les contrôles Windows en utilisant les frameworks d'accessibilité et d'automatisation de l'interface utilisateur, ce qui en fait un choix fiable pour l'automatisation des applications Windows natives en ciblant des éléments plutôt que des coordonnées d'écran.

## 5. Tableau Comparatif

| Fonctionnalité / Bibliothèque | PyAutoGUI | pynput | mouse |
|-------------------------------|:---------:|:------:|:-----:|
| **Systèmes d'exploitation pris en charge** | Windows, macOS, Linux | Windows, macOS, Linux | Windows, macOS, Linux |
|-------------------------------|:---------:|:------:|:-----:|
| **Installation**              | `pip install pyautogui` | `pip install pynput` | `pip install mouse` |
| **Mouvement du Curseur**      | ✅ Abs./Rel. | ✅ Abs./Rel. | ✅ Abs./Rel. |
| **Clics de Souris**           | ✅ Tous types | ✅ Tous types | ✅ Tous types |
| **Glisser-déposer**           | ✅ `dragTo()` | ⚠️ Manuel | ✅ `drag()` |
| **Molette de Défilement**     | ✅ Oui      | ✅ Oui   | ✅ Oui  |
| **Obtenir la Position**       | ✅ Oui      | ✅ Oui   | ✅ Oui  |
| **Vérifier l'État du Bouton** | ❌ Non      | ⚠️ Via Écouteur | ✅ Oui  |
| **Enregistrement/Lecture**    | ❌ Non      | ❌ Non (manuel seulement) | ✅ Intégré |
| **Coordonnées dans le Gestionnaire** | ❌ Non      | ✅ Oui   | ❌ Non  |
| **Blocage d'Événements**      | ❌ Non      | ✅ Oui (`return False`) | ❌ Non  |
| **Intégration Clavier**       | ✅ Oui      | ✅ Oui   | ❌ Non  |
| **Support Actif**             | ✅ Oui      | ✅ Oui   | ❌ Non (depuis 2021) |
| **Failsafe**                  | ✅ Oui      | ❌ Non   | ❌ Non  |
| **Complexité de l'API**       | Moyenne     | Moyenne/Élevée | Basse   |

## Conclusion

Le choix d'une bibliothèque de contrôle de la souris en Python dépend de vos besoins spécifiques :

*   **PyAutoGUI** : Votre choix par défaut pour l'automatisation GUI de haut niveau lorsque vous devez simuler des actions utilisateur, y compris le clavier et les captures d'écran, sans analyse approfondie des événements.
*   **pynput** : Idéal pour les projets nécessitant un contrôle précis des événements de la souris (et du clavier), une surveillance, une analyse, ainsi que la possibilité de bloquer ou de modifier les entrées en temps réel. C'est un outil professionnel pour les systèmes complexes.
*   **mouse** : Mieux adapté aux tâches simples d'enregistrement et de lecture de macros, où la simplicité maximale et un code minimal sont importants. Cependant, le manque de support actif doit être pris en compte.

Pour les nouveaux projets nécessitant flexibilité et support à long terme, `pynput` est recommandé. Si votre tâche est l'automatisation rapide d'actions routinières, `PyAutoGUI` sera un excellent choix.
