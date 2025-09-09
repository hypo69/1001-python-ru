## Travailler avec la bibliothèque `subprocess` en Python


### 1. **Qu'est-ce que `subprocess` et pourquoi est-il nécessaire ?**

Le module `subprocess` en Python fournit une interface pour créer de nouveaux processus,
se connecter à leurs flux d'entrée/sortie/erreur et obtenir leurs codes de retour.
Il permet aux scripts Python de lancer et de gérer d'autres programmes,
écrits dans n'importe quel langage, qu'il s'agisse d'utilitaires système, de scripts shell ou d'autres exécutables.

**Contexte historique :**

Avant `subprocess`, les fonctions du module `os`, telles que `os.system()`, `os.spawn*()`, ainsi que le module `commands` (dans Python 2), étaient utilisées pour lancer des processus externes. Ces approches présentaient un certain nombre d'inconvénients :
*   `os.system()` : Exécute une commande via le shell système, ce qui est dangereux lors de l'utilisation d'entrées utilisateur non fiables et moins flexible dans la gestion des flux.
*   `os.spawn*()` : Plus flexibles, mais complexes à utiliser et dépendants de la plateforme.
*   Le module `popen2` (et ses variantes) : Fournissait un accès aux flux, mais était complexe et présentait des problèmes de blocage.

Le module `subprocess` a été introduit dans Python 2.4 (PEP 324) comme un moyen unifié et plus sûr d'interagir avec les processus enfants. Il encapsule les meilleures fonctionnalités des modules précédents et fournit une API plus propre.

**Principales tâches résolues avec `subprocess` :**

*   Exécution de commandes du système d'exploitation (par exemple, `ls`, `dir`, `ping`).
*   Lancement d'utilitaires externes pour le traitement des données (par exemple, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Intégration avec les systèmes de contrôle de version (`git`, `svn`).
*   Lancement de compilateurs ou d'interprètes d'autres langages.
*   Automatisation de l'administration système.
*   Organisation de l'interaction entre différents programmes.

---

### 2. Fonctions et classes principales

Le module `subprocess` offre plusieurs façons de lancer des processus :

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   C'est l'API de haut niveau **recommandée**, apparue dans Python 3.5.
    *   Exécute une commande, attend sa fin et renvoie un objet `CompletedProcess`.
    *   Convient à la plupart des cas où il suffit d'exécuter une commande et d'obtenir un résultat.

    ```python
    import subprocess

    # Exécution simple
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout :", result.stdout)
    # Si check=True et la commande a renvoyé une valeur non nulle, une CalledProcessError sera levée
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   C'est la classe principale pour créer et gérer les processus enfants.
    *   Offre une flexibilité maximale : lancement non bloquant, contrôle détaillé des flux d'E/S, possibilité d'envoyer des signaux au processus.
    *   La fonction `run()` utilise `Popen` en interne.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Processus lancé avec PID : {process.pid}")
    # ... peut faire d'autres travaux ...
    process.wait() # Attendre la fin
    print(f"Processus terminé avec le code : {process.returncode}")
    ```

*   **Fonctions obsolètes, mais toujours présentes (avant Python 3.5, elles étaient l'API principale) :**
    *   `subprocess.call(args, ...)` : Exécute une commande et attend sa fin. Renvoie le code de retour. Similaire à `os.system()`, mais plus sûr si `shell=False`.
    *   `subprocess.check_call(args, ...)` : Comme `call()`, mais lève `CalledProcessError` si le code de retour n'est pas 0.
    *   `subprocess.check_output(args, ...)` : Exécute une commande, attend sa fin et renvoie sa sortie standard (stdout) sous forme de chaîne d'octets. Lève `CalledProcessError` si le code de retour n'est pas 0.

    Bien que ces fonctions fonctionnent toujours, `subprocess.run()` fournit une interface plus pratique et unifiée pour les mêmes tâches.

---

### 3. Arguments clés des fonctions `run()` et `Popen()`

Ces arguments permettent de configurer finement le lancement et l'interaction avec le processus enfant :

*   **`args`** :
    *   Premier argument et obligatoire.
    *   Peut être une liste de chaînes (recommandé) ou une seule chaîne (si `shell=True`).
    *   Le premier élément de la liste est le nom de l'exécutable, les autres sont ses arguments.
    *   Exemple : `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`** :
    *   Déterminent la manière dont les flux d'entrée, de sortie et d'erreur standard du processus enfant seront gérés.
    *   Valeurs possibles :
        *   `None` (par défaut) : Hérités du processus parent.
        *   `subprocess.PIPE` : Un tube (pipe) est créé, à travers lequel les données peuvent être échangées. `process.stdin`, `process.stdout`, `process.stderr` deviennent des objets de type fichier.
        *   `subprocess.DEVNULL` : Redirige le flux vers le "néant" (analogue à `/dev/null`).
        *   Un descripteur de fichier ouvert (un entier).
        *   Un objet fichier existant (par exemple, un fichier ouvert `open('output.txt', 'w')`).

*   **`capture_output=True` (pour `run()`) :**
    *   Une option pratique, équivalente à la définition de `stdout=subprocess.PIPE` et `stderr=subprocess.PIPE`.
    *   Le résultat sera disponible dans `result.stdout` et `result.stderr`.

*   **`text=True` (ou `universal_newlines=True` pour la compatibilité) :**
    *   Si `True`, les flux `stdout` et `stderr` (ainsi que `stdin`, si une chaîne est passée) seront ouverts en mode texte en utilisant l'encodage par défaut (généralement UTF-8). Le décodage/encodage se fait automatiquement.
    *   Si `False` (par défaut), les flux sont traités comme des octets.
    *   À partir de Python 3.7, `text` est l'alias préféré pour `universal_newlines`. Vous pouvez également spécifier un encodage spécifique via `encoding` et un gestionnaire d'erreurs via `errors`.

*   **`shell=False` (par défaut) :**
    *   Si `False` (recommandé pour des raisons de sécurité et de prévisibilité), `args` doit être une liste. La commande est lancée directement.
    *   Si `True`, `args` est passé sous forme de chaîne au shell système (par exemple, `/bin/sh` sous Unix, `cmd.exe` sous Windows) pour interprétation. Cela permet d'utiliser les fonctionnalités du shell (variables, substitutions, pipelines), mais est **DANGEREUX** si `args` contient des entrées utilisateur non fiables (risque d'injection de commandes).

*   **`cwd=None` :**
    *   Définit le répertoire de travail actuel pour le processus enfant. Par défaut, il hérite du processus parent.

*   **`env=None` :**
    *   Un dictionnaire définissant les variables d'environnement pour le nouveau processus. Par défaut, l'environnement du processus parent est hérité. S'il est spécifié, il remplace complètement l'environnement hérité. Pour ajouter/modifier des variables tout en conservant les autres, vous devez d'abord copier `os.environ`, puis le modifier.

*   **`timeout=None` :**
    *   Temps maximal en secondes alloué à l'exécution de la commande. Si le processus ne se termine pas dans ce délai, une exception `subprocess.TimeoutExpired` sera levée. `Popen.communicate()` accepte également `timeout`.

*   **`check=False` (pour `run()`) :**
    *   Si `True` et que le processus se termine avec un code de retour non nul, une exception `subprocess.CalledProcessError` sera levée.

---

### 4. Travailler avec les résultats et les erreurs

**Objet `CompletedProcess` (résultat de `run()`) :**

```python
import subprocess

try:
    # Tenter d'exécuter une commande qui peut échouer
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - faute de frappe pour la démonstration
        capture_output=True,
        text=True,
        check=True, # Lèvera une exception si returncode != 0
        timeout=10
    )
    print("Commande exécutée avec succès.")
    print("Code de retour :", result.returncode)
    print("Stdout :", result.stdout)
    print("Stderr :", result.stderr) # Généralement vide en cas de succès

except subprocess.CalledProcessError as e:
    print(f"Erreur d'exécution de la commande (CalledProcessError) :")
    print(f"  Commande : {e.cmd}")
    print(f"  Code de retour : {e.returncode}")
    print(f"  Stdout : {e.stdout}") # Peut contenir la sortie avant l'erreur
    print(f"  Stderr : {e.stderr}") # Généralement ici les informations d'erreur
except subprocess.TimeoutExpired as e:
    print(f"La commande ne s'est pas terminée dans les {e.timeout} secondes.")
    print(f"  Commande : {e.cmd}")
    if e.stdout: print(f"  Stdout (partiel) : {e.stdout.decode(errors='ignore')}") # stdout est en octets
    if e.stderr: print(f"  Stderr (partiel) : {e.stderr.decode(errors='ignore')}") # stderr est en octets
except FileNotFoundError:
    print("Erreur : commande ou programme introuvable.")
except Exception as e:
    print(f"Une autre erreur est survenue : {e}")
```

**Attributs de `CompletedProcess` :**
*   `args` : Arguments utilisés pour lancer le processus.
*   `returncode` : Code de retour du processus. 0 signifie généralement le succès.
*   `stdout` : Sortie standard du processus (octets ou chaîne, si `text=True` et `capture_output=True`).
*   `stderr` : Flux d'erreur standard du processus (octets ou chaîne, si `text=True` et `capture_output=True`).

**Exceptions :**
*   `subprocess.CalledProcessError` : Levée si `check=True` (pour `run()`) ou si `check_call()`, `check_output()` sont utilisés et que la commande s'est terminée avec un code non nul. Contient `returncode`, `cmd`, `output` (ou `stdout`), `stderr`.
*   `subprocess.TimeoutExpired` : Si le délai d'attente est dépassé. Contient `cmd`, `timeout`, `stdout`, `stderr` (sortie partielle, le cas échéant).
*   `FileNotFoundError` : Si l'exécutable est introuvable.

**Interaction avec l'objet `Popen` :**

La classe `Popen` offre plus de contrôle :

```python
import subprocess
import time

# Lancer le processus en arrière-plan
process = subprocess.Popen(["ping", "-c", "5", "google.com"], stdout=subprocess.PIPE, text=True)

print(f"Processus PID : {process.pid} lancé.")

# Vérification de l'état non bloquante
while process.poll() is None: # poll() renvoie None si le processus est toujours en cours d'exécution
    print("Processus toujours en cours d'exécution...")
    # Peut lire la sortie au fur et à mesure (attention, peut bloquer !)
    # line = process.stdout.readline()
    # if line: print(f"Sortie : {line.strip()}")
    time.sleep(1)

# Attendre la fin et obtenir toutes les sorties/erreurs
# stdout_data, stderr_data = process.communicate(timeout=10) # Méthode sûre

# Si communicate() n'a pas été utilisé, après poll() != None, on peut lire le reste
if process.stdout:
    for line in process.stdout:
        print(f"Sortie finale : {line.strip()}")

print(f"Processus terminé avec le code : {process.returncode}")

# Si une terminaison forcée est nécessaire
# process.terminate() # Envoie SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # Si non terminé
#     process.kill()      # Envoie SIGKILL
```

*   `process.poll()` : Vérifie si le processus enfant s'est terminé. Renvoie le code de retour ou `None`. Non bloquant.
*   `process.wait(timeout=None)` : Attend la fin du processus enfant. Renvoie le code de retour. Bloquant.
*   `process.communicate(input=None, timeout=None)` :
    *   La méthode la plus sûre pour interagir avec un processus lorsque des `PIPE` sont utilisés.
    *   Envoie des données à `stdin` (si `input` est spécifié), lit toutes les données de `stdout` et `stderr` jusqu'à la fin et attend la fin du processus.
    *   Renvoie un tuple `(stdout_data, stderr_data)`.
    *   Aide à éviter les interblocages qui peuvent survenir lors de la lecture/écriture directe dans `process.stdout`/`process.stdin` si les tampons débordent.
*   `process.terminate()` : Envoie un signal `SIGTERM` au processus (terminaison gracieuse).
*   `process.kill()` : Envoie un signal `SIGKILL` au processus (terminaison forcée).
*   `process.send_signal(signal)` : Envoie le signal spécifié au processus.
*   `process.stdin`, `process.stdout`, `process.stderr` : Objets de type fichier pour les tubes, s'ils ont été créés avec `PIPE`.

---

### 5. Scénarios d'utilisation avancés

**Redirection de la sortie d'une commande vers l'entrée d'une autre (pipelines) :**

Émulation de `ps aux | grep python` :

```python
import subprocess

# Lancer la première commande, son stdout sera PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Lancer la deuxième commande, son stdin sera stdout de la première commande
# stdout de la deuxième commande également PIPE, pour lire le résultat
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Lier stdout de ps à stdin pour grep
    stdout=subprocess.PIPE,
    text=True
)

# Important ! Fermer stdout de la première commande dans le processus parent,
# afin que grep reçoive EOF lorsque ps aura terminé.
if ps_process.stdout:
    ps_process.stdout.close() 

# Obtenir la sortie de grep
stdout_data, stderr_data = grep_process.communicate()

print("Résultat du pipeline : ")
print(stdout_data)

if stderr_data:
    print("Erreurs grep :", stderr_data)

# S'assurer que les deux processus sont terminés
ps_process.wait()
# grep_process.wait() # communicate() a déjà attendu
print(f"Code de retour ps : {ps_process.returncode}")
print(f"Code de retour grep : {grep_process.returncode}")
```
*Note :* Pour les pipelines simples, `subprocess.run("ps aux | grep python", shell=True, ...)` peut être plus simple, mais moins sûr et flexible.

**Lancement asynchrone de processus :**

`Popen` est intrinsèquement non bloquant. Vous pouvez lancer plusieurs processus et les gérer en parallèle.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Commande avec erreur
]

processes = []
for cmd_args in commands:
    print(f"Lancement : {' '.join(cmd_args)}")
    # Pour l'asynchronisme, stdout/stderr sont mieux redirigés,
    # pour éviter d'interférer les uns avec les autres ou avec la console du parent.
    # DEVNULL si la sortie n'est pas nécessaire, PIPE si nécessaire plus tard.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Faire d'autres travaux ou attendre la fin
while any(p.poll() is None for p in processes):
    print("Attente de la fin de tous les processus...")
    time.sleep(0.5)

print("\nRésultats : ")
for i, p in enumerate(processes):
    print(f"Commande '{' '.join(commands[i])}' terminée avec le code : {p.returncode}")
```

**Interaction interactive avec le processus :**

C'est une tâche complexe, nécessitant une gestion prudente des flux pour éviter les interblocages. `communicate()` est bon pour un échange unique. Pour une session interactive prolongée, la lecture/écriture directe dans `p.stdin`, `p.stdout`, `p.stderr` à l'aide d'E/S non bloquantes ou de threads séparés peut être nécessaire.

```python
import subprocess

# Exemple : lancement d'une session python interactive
process = subprocess.Popen(
    ['python', '-i'], # -i pour le mode interactif
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Tampon de ligne pour stdout/stderr (pour l'interactivité)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Important !

def read_output():
    # La lecture de la sortie peut être complexe, car il faut savoir quand s'arrêter.
    # C'est un exemple très simplifié. Pour les tâches réelles, des solutions plus robustes sont nécessaires.
    # Par exemple, lire jusqu'à un certain motif (invite de commande).
    output = ""
    # Lire stdout. Dans une application réelle, cela doit être fait de manière non bloquante ou dans un thread séparé.
    # Ici, nous supposons qu'après une commande, il y aura une sortie immédiate.
    # C'est une hypothèse très fragile pour le cas général !
    try:
        # Popen n'a pas de readline avec timeout, c'est l'une des difficultés
        # Peut utiliser select sur process.stdout.fileno()
        # ou lire caractère par caractère/ligne par ligne dans un thread séparé
        # Pour la simplicité, ce n'est pas inclus ici
        while True: # Attention, peut bloquer !
            line = process.stdout.readline()
            if not line: break # EOF
            if ">>> " in line or "... " in line: # Détecteur d'invite primitif
                output += line
                break
            output += line
    except Exception as e:
        print(f"Erreur de lecture : {e}")
    return output.strip()

# Initialisation : lire l'invite initiale
initial_output = ""
# Lire le message d'accueil de Python
# C'est très simplifié, car nous ne savons pas exactement combien de lignes lire
for _ in range(5): # Essayer de lire quelques lignes
    try:
        # Popen stdout n'a pas de timeout, il faut lire attentivement
        # stdout.readline() peut bloquer.
        # Dans les applications réelles, select ou des threads sont nécessaires ici.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Invite trouvée
    except BlockingIOError:
        break # Si la lecture non bloquante était utilisée
print(f"Sortie initiale :\n{initial_output.strip()}")


send_command("a = 10")
# Pour l'interaction interactive, la lecture de la sortie est la partie la plus complexe.
# communicate() ne convient pas, car il ferme les flux.
# Il faut lire attentivement depuis process.stdout et process.stderr, 
# éventuellement dans des threads séparés, pour éviter de bloquer le thread principal.
# Cet exemple n'est PAS prêt pour la production pour une interactivité complexe.
# print(read_output()) # Ce read_output est très primitif

send_command("print(a * 2)")
# print(read_output())

# Terminer le processus
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Attendre la fin et collecter le reste

print("\nStdout final : ")
print(stdout_data)
if stderr_data:
    print("\nStderr final : ")
    print(stderr_data)

print(f"Processus Python terminé avec le code : {process.returncode}")

# Pour une véritable interaction interactive, on utilise souvent des pty (pseudo-terminaux)
# via le module `pty` dans les systèmes de type Unix, ou des bibliothèques comme `pexpect`.
```
*Avertissement* : L'interaction interactive directe avec `Popen` via `stdin`/`stdout`/`stderr` est complexe en raison des blocages et de la mise en mémoire tampon. Pour une interactivité fiable, des bibliothèques comme `pexpect` (pour Unix) ou des équivalents qui fonctionnent avec des pseudo-terminaux (pty) sont souvent utilisées.

---

### 6. Sécurité et meilleures pratiques

*   **Risques de `shell=True` et d'injection de commandes :**
    *   **N'utilisez jamais** `shell=True` avec des commandes construites à partir d'entrées utilisateur non fiables. Cela ouvre la porte à l'injection de commandes.
    *   Exemple de vulnérabilité :
        ```python
        # DANGEREUX !
        filename = input("Entrez le nom du fichier à supprimer : ") # L'utilisateur entre "monfichierinnocent.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Si `shell=True` est absolument nécessaire (par exemple, pour utiliser des pipes `|` ou des substitutions `*` directement dans la chaîne de commande), échappez soigneusement toutes les parties de la commande formées à partir d'une entrée externe à l'aide de `shlex.quote()` (à partir de Python 3.3).

*   **Validation et échappement des entrées utilisateur :**
    *   Même si `shell=False`, si les arguments de commande sont formés à partir d'une entrée utilisateur, ils doivent être validés. Par exemple, si un nom de fichier est attendu, assurez-vous qu'il s'agit bien d'un nom de fichier valide et non de quelque chose comme `../../../etc/passwd`.

*   **Passer les arguments sous forme de liste (lorsque `shell=False`) :**
    *   C'est la méthode la plus sûre. Chaque argument est passé comme un élément de liste distinct, et le système d'exploitation les gère correctement, sans essayer de les interpréter comme faisant partie de la commande shell.
    *   Exemple : `subprocess.run(["rm", filename_from_user])` — ici `filename_from_user` sera toujours traité comme un seul argument (nom de fichier), même s'il contient des espaces ou des caractères spéciaux.

*   **Gestion des erreurs et des codes de retour :**
    *   Vérifiez toujours le `returncode` ou utilisez `check=True` (pour `run()`) / `check_call()` / `check_output()` pour vous assurer que la commande s'est exécutée avec succès.
    *   Gérez les exceptions possibles (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Gestion des ressources :**
    *   Si vous ouvrez des pipes (`PIPE`), assurez-vous qu'ils sont finalement fermés. `Popen.communicate()` le fait automatiquement. Si vous travaillez directement avec `p.stdin/stdout/stderr`, leur fermeture explicite peut être nécessaire.
    *   Dans les applications à longue durée de vie, assurez-vous que les processus enfants se terminent correctement et ne deviennent pas des «zombies». Utilisez `p.wait()` ou `p.communicate()`. Si nécessaire, utilisez `p.terminate()` ou `p.kill()`.

*   **Encodages :** Soyez attentif aux encodages lorsque vous utilisez `text=True` ou lorsque vous décodez manuellement des chaînes d'octets. Les problèmes d'encodage sont une source fréquente d'erreurs.

---

### 7. Exemples pratiques

**1. Exécution d'une commande simple et vérification du code de retour :**
```python
import subprocess

try:
    # Exécuter 'ls' pour un répertoire existant
    result = subprocess.run(["ls", "-l", "/tmp"], check=True)
    print(f"Commande 'ls /tmp' exécutée, code de retour : {result.returncode}")

    # Exécuter 'ls' pour un répertoire inexistant
    result_fail = subprocess.run(["ls", "/nonexistent"], check=True, stderr=subprocess.PIPE, text=True)
    # Cette ligne ne s'exécutera pas si check=True, car une exception sera levée
except subprocess.CalledProcessError as e:
    print(f"Erreur d'exécution de la commande : {e.cmd}")
    print(f"Code de retour : {e.returncode}")
    if e.stderr:
        print(f"Stderr : {e.stderr.strip()}")
```

**2. Capture de la sortie de commande :**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Spécifier le répertoire actuel comme répertoire de travail pour git
    )
    print("Statut Git : ")
    print(result.stdout)
except FileNotFoundError:
    print("Erreur : commande 'git' introuvable. Git est-il installé et dans le PATH ?")
except subprocess.CalledProcessError as e:
    print(f"Erreur Git : {e.stderr}")
```

**3. Envoi de données à l'entrée du processus (à l'aide de `communicate`) :**
```python
import subprocess

# Envoyer du texte à 'grep' pour la recherche
input_text = "bonjour le monde\npython est amusant\nbonjour python"
try:
    process = subprocess.Popen(
        ["grep", "python"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )
    stdout_data, stderr_data = process.communicate(input=input_text, timeout=5)

    if process.returncode == 0: # grep a trouvé des correspondances
        print("Lignes trouvées : ")
        print(stdout_data)
    elif process.returncode == 1: # grep n'a trouvé aucune correspondance
        print("Aucune correspondance 'python' trouvée.")
    else: # autre erreur grep
        print(f"Erreur grep (code {process.returncode}) : ")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep n'a pas répondu à temps.")
    process.kill() # Tuer le processus s'il est bloqué
    process.communicate() # Collecter la sortie/les erreurs restantes
```

**4. Création d'un pipeline (`ls -l | wc -l`) sans `shell=True` :**
(Un exemple plus détaillé se trouvait dans la section 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # S'assurer que stdout existe
    ls_proc.stdout.close()  # Permet à wc_proc de recevoir EOF lorsque ls_proc est terminé

output, _ = wc_proc.communicate()
print(f"Nombre de fichiers/répertoires : {output.strip()}")
```

**5. Utilisation de `timeout` :**
```python
import subprocess

try:
    # Commande qui s'exécutera pendant 5 secondes
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("Commande 'sleep 5' terminée (n'aurait pas dû avec timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"Commande '{e.cmd}' ne s'est pas terminée dans les {e.timeout} secondes.")
```

---

### 8. Conclusion et ressources utiles

Le module `subprocess` est un outil indispensable pour tout développeur Python qui a besoin d'interagir avec des programmes externes ou l'environnement système. Il offre un équilibre entre la simplicité d'utilisation (via `subprocess.run()`) et une flexibilité puissante (via `subprocess.Popen()`).

**Points clés :**
*   Préférez `subprocess.run()` pour la plupart des tâches.
*   Utilisez `subprocess.Popen()` pour l'exécution asynchrone ou la gestion complexe des flux.
*   **Évitez `shell=True`**, surtout avec les entrées utilisateur, en raison des risques de sécurité. Passez les commandes sous forme de liste d'arguments.
*   Gérez toujours les codes de retour et les exceptions possibles.
*   Soyez attentif aux encodages lorsque vous travaillez avec la sortie texte (`text=True` ou décodage manuel).
*   `communicate()` est votre ami pour un échange de données sécurisé via `PIPE`.

**Ressources utiles :**
*   Documentation officielle de Python sur le module `subprocess` : [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - Un nouveau module de processus : [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)

```