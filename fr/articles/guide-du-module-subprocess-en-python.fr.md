## Travailler avec la bibliothèque `subprocess` en Python


### 1. **Qu'est-ce que `subprocess` et pourquoi en a-t-on besoin ?**

Le module `subprocess` en Python fournit une interface pour créer de nouveaux processus,
se connecter à leurs flux d'entrée/sortie/erreur et obtenir leurs codes de retour.
Il permet aux scripts Python d'exécuter et de gérer d'autres programmes,
écrits dans n'importe quel langage, qu'il s'agisse d'utilitaires système, de scripts shell ou d'autres exécutables.

**Contexte historique :**

Avant l'avènement de `subprocess`, les fonctions du module `os`, telles que `os.system()`, `os.spawn*()`, ainsi que le module `commands` (en Python 2) étaient utilisées pour exécuter des processus externes. Ces approches présentaient un certain nombre d'inconvénients :
*   `os.system()` : Exécute une commande via le shell système, ce qui est peu sûr lorsque l'on travaille avec des entrées utilisateur et moins flexible dans la gestion des flux.
*   `os.spawn*()` : Plus flexibles, mais difficiles à utiliser et dépendantes de la plate-forme.
*   Le module `popen2` (et ses variantes) : Fournissait un accès aux flux, mais était complexe et présentait des problèmes de blocage.

Le module `subprocess` a été introduit dans Python 2.4 (PEP 324) comme un moyen unifié et plus sûr d'interagir avec les processus enfants. Il encapsule les meilleures fonctionnalités des modules précédents et fournit une API plus propre.

**Principales tâches résolues avec `subprocess` :**

*   Exécution de commandes du système d'exploitation (par exemple, `ls`, `dir`, `ping`).
*   Exécution d'utilitaires externes pour le traitement des données (par exemple, `grep`, `awk`, `ffmpeg`, `ImageMagick`).
*   Intégration avec les systèmes de contrôle de version (`git`, `svn`).
*   Exécution de compilateurs ou d'interpréteurs d'autres langages.
*   Automatisation de l'administration système.
*   Organisation de l'interaction entre différents programmes.

---

### 2. Fonctions et classes principales

Le module `subprocess` offre plusieurs façons d'exécuter des processus :

*   **`subprocess.run(args, ..., capture_output=False, text=False, check=False, timeout=None)`**
    *   Il s'agit de l'API de haut niveau **recommandée**, apparue dans Python 3.5.
    *   Exécute une commande, attend sa fin et renvoie un objet `CompletedProcess`.
    *   Convient à la plupart des cas où il suffit d'exécuter une commande et d'obtenir le résultat.

    ```python
    import subprocess

    # Exécution simple
    result = subprocess.run(["ls", "-l"], capture_output=True, text=True, check=True)
    print("Stdout:", result.stdout)
    # Si check=True et que la commande a renvoyé une valeur non nulle, CalledProcessError sera levée
    ```

*   **`subprocess.Popen(args, ..., stdin=None, stdout=None, stderr=None, shell=False, cwd=None, env=None)`**
    *   Il s'agit de la classe principale pour la création et la gestion des processus enfants.
    *   Offre une flexibilité maximale : exécution non bloquante, contrôle détaillé des flux d'E/S, possibilité d'envoyer des signaux au processus.
    *   La fonction `run()` utilise `Popen` en interne.

    ```python
    import subprocess

    process = subprocess.Popen(["sleep", "5"])
    print(f"Processus démarré avec le PID : {process.pid}")
    # ... on peut faire autre chose ...
    process.wait() # Attendre la fin
    print(f"Le processus s'est terminé avec le code : {process.returncode}")
    ```

*   **Fonctions obsolètes, mais que l'on rencontre encore (étaient l'API principale avant Python 3.5) :**
    *   `subprocess.call(args, ...)` : Exécute une commande et attend sa fin. Renvoie le code de retour. Similaire à `os.system()`, mais plus sûr si `shell=False`.
    *   `subprocess.check_call(args, ...)` : Comme `call()`, mais lève `CalledProcessError` si le code de retour n'est pas 0.
    *   `subprocess.check_output(args, ...)` : Exécute une commande, attend la fin et renvoie sa sortie standard (stdout) sous forme de chaîne d'octets. Lève `CalledProcessError` si le code de retour n'est pas 0.

    Bien que ces fonctions fonctionnent toujours, `subprocess.run()` fournit une interface plus pratique et unifiée pour les mêmes tâches.

---

### 3. Arguments clés des fonctions `run()` et `Popen()`

Ces arguments permettent de configurer finement le lancement et l'interaction avec le processus enfant :

*   **`args`** :
    *   Le premier argument et obligatoire.
    *   Peut être une liste de chaînes (recommandé) ou une seule chaîne (si `shell=True`).
    *   Le premier élément de la liste est le nom du fichier exécutable, les autres sont ses arguments.
    *   Exemple : `["python", "myscript.py", "--arg1", "value1"]`

*   **`stdin`, `stdout`, `stderr`** :
    *   Définissent comment l'entrée standard, la sortie et le flux d'erreurs du processus enfant seront gérés.
    *   Valeurs possibles :
        *   `None` (par défaut) : Hérités du processus parent.
        *   `subprocess.PIPE` : Un canal (pipe) est créé à travers lequel les données peuvent être échangées. `process.stdin`, `process.stdout`, `process.stderr` deviennent des objets de type fichier.
        *   `subprocess.DEVNULL` : Redirige le flux vers "nulle part" (analogue à `/dev/null`).
        *   Un descripteur de fichier ouvert (un entier).
        *   Un objet fichier existant (par exemple, un fichier ouvert `open('output.txt', 'w')`).

*   **`capture_output=True` (pour `run()`) :**
    *   Une option pratique, équivalente à la définition de `stdout=subprocess.PIPE` et `stderr=subprocess.PIPE`.
    *   Le résultat sera disponible dans `result.stdout` et `result.stderr`.

*   **`text=True` (ou `universal_newlines=True` pour la compatibilité) :**
    *   Si `True`, les flux `stdout` et `stderr` (ainsi que `stdin`, si une chaîne est passée) seront ouverts en mode texte en utilisant l'encodage par défaut (généralement UTF-8). Le décodage/encodage se fait automatiquement.
    *   Si `False` (par défaut), les flux sont traités comme des octets.
    *   Depuis Python 3.7, `text` est l'alias préféré pour `universal_newlines`. Vous pouvez également spécifier un encodage spécifique via `encoding` et un gestionnaire d'erreurs via `errors`.

*   **`shell=False` (par défaut) :**
    *   Si `False` (recommandé pour des raisons de sécurité et de prévisibilité), `args` doit être une liste. La commande est exécutée directement.
    *   Si `True`, `args` est passé comme une chaîne au shell système (par exemple, `/bin/sh` sous Unix, `cmd.exe` sous Windows) pour interprétation. Cela permet d'utiliser les fonctionnalités du shell (variables, substitutions, pipelines), mais est **DANGEREUX** si `args` contient une entrée utilisateur non vérifiée (risque d'injection de commande).

*   **`cwd=None` :**
    *   Définit le répertoire de travail courant pour le processus enfant. Par défaut, il est hérité du parent.

*   **`env=None` :**
    *   Un dictionnaire qui définit les variables d'environnement pour le nouveau processus. Par défaut, l'environnement du processus parent est hérité. S'il est spécifié, il remplace complètement l'environnement hérité. Pour ajouter/modifier des variables tout en conservant le reste, vous devez d'abord copier `os.environ` puis le modifier.

*   **`timeout=None` :**
    *   Le temps maximum en secondes alloué à l'exécution de la commande. Si le processus ne se termine pas dans ce délai, une exception `subprocess.TimeoutExpired` sera levée. `Popen.communicate()` accepte également un `timeout`.

*   **`check=False` (pour `run()`) :**
    *   Si `True` et que le processus se termine avec un code de retour non nul, une exception `subprocess.CalledProcessError` sera levée.

---

### 4. Travailler avec les résultats et les erreurs

**L'objet `CompletedProcess` (le résultat de `run()`) :**

```python
import subprocess

try:
    # Essayer d'exécuter une commande qui peut échouer
    result = subprocess.run(
        ["git", "stotus"], # 'stotus' - une faute de frappe pour démontrer une erreur
        capture_output=True,
        text=True,
        check=True, # Lèvera une exception si le code de retour != 0
        timeout=10
    )
    print("Commande exécutée avec succès.")
    print("Code de retour :", result.returncode)
    print("Stdout :", result.stdout)
    print("Stderr :", result.stderr) # Généralement vide en cas de succès

except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de la commande (CalledProcessError) :")
    print(f"  Commande : {e.cmd}")
    print(f"  Code de retour : {e.returncode}")
    print(f"  Stdout : {e.stdout}") # Peut contenir une sortie avant l'erreur
    print(f"  Stderr : {e.stderr}") # Contient généralement des informations sur l'erreur
except subprocess.TimeoutExpired as e:
    print(f"La commande ne s'est pas terminée en {e.timeout} secondes.")
    print(f"  Commande : {e.cmd}")
    if e.stdout: print(f"  Stdout (partiel) : {e.stdout.decode(errors='ignore')}") # stdout est en octets
    if e.stderr: print(f"  Stderr (partiel) : {e.stderr.decode(errors='ignore')}") # stderr est en octets
except FileNotFoundError:
    print("Erreur : commande ou programme introuvable.")
except Exception as e:
    print(f"Une autre erreur s'est produite : {e}")
```

**Attributs de `CompletedProcess` :**
*   `args` : Les arguments utilisés pour lancer le processus.
*   `returncode` : Le code de retour du processus. 0 signifie généralement un succès.
*   `stdout` : La sortie standard du processus (octets ou une chaîne si `text=True` et `capture_output=True`).
*   `stderr` : Le flux d'erreurs standard du processus (octets ou une chaîne si `text=True` et `capture_output=True`).

**Exceptions :**
*   `subprocess.CalledProcessError` : Levée si `check=True` (pour `run()`) ou si `check_call()`, `check_output()` sont utilisés et que la commande se termine avec un code non nul. Contient `returncode`, `cmd`, `output` (ou `stdout`), `stderr`.
*   `subprocess.TimeoutExpired` : Si le délai d'attente a expiré. Contient `cmd`, `timeout`, `stdout`, `stderr` (sortie partielle, le cas échéant).
*   `FileNotFoundError` : Si le fichier exécutable n'est pas trouvé.

**Interaction avec un objet `Popen` :**

La classe `Popen` donne plus de contrôle :

```python
import subprocess
import time

# Exécuter un processus en arrière-plan
process = subprocess.Popen(["ping", "-c", "5", "google.com"], stdout=subprocess.PIPE, text=True)

print(f"Processus PID : {process.pid} démarré.")

# Vérification de l'état non bloquante
while process.poll() is None: # poll() renvoie None si le processus est toujours en cours d'exécution
    print("Le processus est toujours en cours d'exécution...")
    # Vous pouvez lire la sortie au fur et à mesure (attention, cela peut bloquer !)
    # line = process.stdout.readline()
    # if line: print(f"Sortie : {line.strip()}")
    time.sleep(1)

# Attendre la fin et obtenir toute la sortie/les erreurs
# stdout_data, stderr_data = process.communicate(timeout=10) # Méthode sûre

# Si communicate() n'a pas été utilisé, après poll() != None, vous pouvez lire le reste
if process.stdout:
    for line in process.stdout:
        print(f"Sortie finale : {line.strip()}")

print(f"Le processus s'est terminé avec le code : {process.returncode}")

# Si vous devez forcer la fin
# process.terminate() # Envoie SIGTERM
# time.sleep(0.5)
# if process.poll() is None: # S'il ne s'est pas terminé
#     process.kill()      # Envoie SIGKILL
```

*   `process.poll()` : Vérifie si le processus enfant s'est terminé. Renvoie le code de retour ou `None`. Non bloquant.
*   `process.wait(timeout=None)` : Attend la fin du processus enfant. Renvoie le code de retour. Bloquant.
*   `process.communicate(input=None, timeout=None)` :
    *   Le moyen le plus sûr d'interagir avec un processus lors de l'utilisation de `PIPE`.
    *   Envoie des données à `stdin` (si `input` est spécifié), lit toutes les données de `stdout` et `stderr` jusqu'à la fin et attend la fin du processus.
    *   Renvoie un tuple `(stdout_data, stderr_data)`.
    *   Aide à éviter les interblocages qui peuvent survenir lors de la lecture/écriture directe dans `process.stdout`/`process.stdin` si les tampons débordent.
*   `process.terminate()` : Envoie le signal `SIGTERM` au processus (terminaison douce).
*   `process.kill()` : Envoie le signal `SIGKILL` au processus (terminaison brutale).
*   `process.send_signal(signal)` : Envoie le signal spécifié au processus.
*   `process.stdin`, `process.stdout`, `process.stderr` : Objets de type fichier pour les canaux, s'ils ont été créés avec `PIPE`.

---

### 5. Scénarios d'utilisation avancés

**Redirection de la sortie d'une commande vers l'entrée d'une autre (pipelines) :**

Émulation de `ps aux | grep python` :

```python
import subprocess

# Exécuter la première commande, sa sortie standard sera un PIPE
ps_process = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE)

# Exécuter la deuxième commande, son entrée standard sera la sortie standard de la première commande
# La sortie standard de la deuxième commande est également un PIPE pour lire le résultat
grep_process = subprocess.Popen(
    ["grep", "python"],
    stdin=ps_process.stdout, # Lier stdout de ps à stdin pour grep
    stdout=subprocess.PIPE,
    text=True
)

# Important ! Fermer stdout de la première commande dans le processus parent,
# pour que grep reçoive EOF lorsque ps se termine.
if ps_process.stdout:
    ps_process.stdout.close()  

# Obtenir la sortie de grep
stdout_data, stderr_data = grep_process.communicate()

print("Résultat du pipeline : ")
print(stdout_data)

if stderr_data:
    print("Erreurs de grep :", stderr_data)

# S'assurer que les deux processus sont terminés
ps_process.wait() 
# grep_process.wait() # communicate() a déjà attendu
print(f"code de retour de ps : {ps_process.returncode}")
print(f"code de retour de grep : {grep_process.returncode}")
```
*Remarque :* Pour les pipelines simples, `subprocess.run("ps aux | grep python", shell=True, ...)` peut être plus simple, mais moins sûr et flexible.

**Exécution asynchrone de processus :**

`Popen` est non bloquant par nature. Vous pouvez exécuter plusieurs processus et les gérer en parallèle.

```python
import subprocess
import time

commands = [
    ["ping", "-c", "3", "google.com"],
    ["sleep", "2"],
    ["ls", "-l", "/nonexistentpath"] # Commande avec une erreur
]

processes = []
for cmd_args in commands:
    print(f"Exécution : {' '.join(cmd_args)}")
    # Pour l'asynchronisme, il est préférable de rediriger stdout/stderr,
    # pour ne pas interférer les uns avec les autres ou avec la console du parent.
    # DEVNULL si la sortie n'est pas nécessaire, PIPE si elle est nécessaire plus tard.
    proc = subprocess.Popen(cmd_args, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    processes.append(proc)

# Faire autre chose ou attendre la fin
while any(p.poll() is None for p in processes):
    print("En attente de la fin de tous les processus...")
    time.sleep(0.5)

print("\nRésultats : ")
for i, p in enumerate(processes):
    print(f"La commande '{' '.join(commands[i])}' s'est terminée avec le code : {p.returncode}")
```

**Interaction interactive avec un processus :**

C'est une tâche complexe qui nécessite une gestion minutieuse des flux pour éviter les interblocages. `communicate()` est bon pour un échange unique. Pour une longue session interactive, vous devrez peut-être lire/écrire directement dans `p.stdin`, `p.stdout`, `p.stderr` en utilisant des E/S non bloquantes ou des threads séparés.

```python
import subprocess

# Exemple : démarrage d'une session python interactive
process = subprocess.Popen(
    ['python', '-i'], # -i pour le mode interactif
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True,
    bufsize=1 # Mise en mémoire tampon de ligne pour stdout/stderr (pour l'interactivité)
)

def send_command(cmd_str):
    print(f">>> {cmd_str}")
    process.stdin.write(cmd_str + '\n')
    process.stdin.flush() # Important !

def read_output():
    # La lecture de la sortie peut être délicate, car il faut savoir quand s'arrêter.
    # C'est un exemple très simplifié. Pour les tâches réelles, des solutions plus robustes sont nécessaires.
    # Par exemple, lire jusqu'à un certain modèle (l'invite de la ligne de commande).
    output = ""
    # Lire stdout. Dans une application réelle, cela doit être fait de manière non bloquante ou dans un thread séparé.
    # Ici, nous supposons qu'après la commande, il y aura une sortie immédiatement.
    # C'est une hypothèse très fragile pour le cas général !
    try:
        # Popen n'a pas de readline avec un délai d'attente, c'est l'une des difficultés
        # Vous pouvez utiliser select sur process.stdout.fileno()
        # ou lire caractère par caractère/ligne par ligne dans un thread séparé
        # Pour des raisons de simplicité, ce n'est pas ici
        while True: # Attention, cela peut bloquer !
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
# Lecture du message de bienvenue de Python
# C'est très simplifié, car nous ne savons pas exactement combien de lignes lire
for _ in range(5): # Essayons de lire quelques lignes
    try:
        # Popen stdout n'a pas de délai d'attente, il faut lire attentivement
        # stdout.readline() peut bloquer.
        # Dans les applications réelles, select ou des threads sont nécessaires ici.
        line = process.stdout.readline()
        if not line: break
        initial_output += line
        if ">>>" in line: break # Invite trouvée
    except BlockingIOError:
        break # S'il y avait une lecture non bloquante
print(f"Sortie initiale :\n{initial_output.strip()}")


send_command("a = 10")
# Pour l'interaction interactive, la lecture de la sortie est la partie la plus difficile.
# communicate() n'est pas adapté, car il ferme les flux.
# Vous devez lire attentivement depuis process.stdout et process.stderr,
# éventuellement dans des threads séparés, pour ne pas bloquer le principal.
# Cet exemple n'est PAS prêt pour la production pour une interactivité complexe.
# print(read_output()) # Ce read_output est très primitif

send_command("print(a * 2)")
# print(read_output())

# Terminer le processus
process.stdin.write("exit()\n")
process.stdin.flush()
stdout_data, stderr_data = process.communicate(timeout=5) # Attendre la fin et récupérer le reste

print("\nSortie standard finale : ")
print(stdout_data)
if stderr_data:
    print("\nErreur standard finale : ")
    print(stderr_data)

print(f"Le processus Python s'est terminé avec le code : {process.returncode}")

# Pour une véritable interaction interactive, on utilise souvent des pty (pseudo-terminaux)
# via le module `pty` sur les systèmes de type Unix, ou des bibliothèques comme `pexpect`.
```
*Avertissement* : L'interaction interactive directe avec `Popen` via `stdin`/`stdout`/`stderr` est difficile en raison des blocages et de la mise en mémoire tampon. Pour une interactivité fiable, on utilise souvent des bibliothèques comme `pexpect` (pour Unix) ou des analogues, qui fonctionnent avec des pseudo-terminaux (pty).

**Travailler avec les encodages :**
*   Utilisez `text=True` (ou `universal_newlines=True`) pour le décodage/encodage automatique.
*   Si nécessaire, vous pouvez spécifier `encoding="votre-encodage"` et `errors="gestionnaire-d'erreurs"` (par exemple, `replace`, `ignore`).
*   Si `text=False` (par défaut), `stdout` et `stderr` seront des chaînes d'octets. Vous devrez les décoder manuellement : `result.stdout.decode('utf-8', errors='replace')`.

---

### 6. Sécurité et meilleures pratiques

*   **Risques de `shell=True` et d'injection de commande :**
    *   N'utilisez **jamais** `shell=True` avec des commandes construites à partir d'une entrée utilisateur non vérifiée. Cela ouvre la voie à l'injection de commande.
    *   Exemple de vulnérabilité :
        ```python
        # DANGEREUX !
        filename = input("Entrez un nom de fichier à supprimer : ") # L'utilisateur entre "myinnocentfile.txt; rm -rf /"
        subprocess.run(f"rm {filename}", shell=True, check=True)
        ```
    *   Si `shell=True` est absolument nécessaire (par exemple, pour utiliser des pipes `|` ou des caractères génériques `*` directement dans la ligne de commande), échappez soigneusement toutes les parties de la commande formées de l'extérieur à l'aide de `shlex.quote()` (depuis Python 3.3).

*   **Validation et échappement de l'entrée utilisateur :**
    *   Même si `shell=False`, si les arguments de la commande sont formés à partir de l'entrée utilisateur, ils doivent être validés. Par exemple, si un nom de fichier est attendu, assurez-vous qu'il s'agit bien d'un nom de fichier valide et non de quelque chose comme `../../../etc/passwd`.

*   **Passage d'arguments sous forme de liste (lorsque `shell=False`) :**
    *   C'est le moyen le plus sûr. Chaque argument est passé comme un élément distinct de la liste, et le système d'exploitation les traite correctement, sans essayer de les interpréter comme faisant partie d'une commande shell.
    *   Exemple : `subprocess.run(["rm", filename_from_user])` — ici, `filename_from_user` sera toujours traité comme un seul argument (nom de fichier), même s'il contient des espaces ou des caractères spéciaux.

*   **Gestion des erreurs et des codes de retour :**
    *   Vérifiez toujours le `returncode` ou utilisez `check=True` (pour `run()`) / `check_call()` / `check_output()` pour vous assurer que la commande s'est exécutée avec succès.
    *   Gérez les exceptions possibles (`CalledProcessError`, `TimeoutExpired`, `FileNotFoundError`).

*   **Gestion des ressources :**
    *   Si vous ouvrez des canaux (`PIPE`), assurez-vous qu'ils sont finalement fermés. `Popen.communicate()` le fait automatiquement. Si vous travaillez directement avec `p.stdin`, `p.stdout`, `p.stderr`, vous devrez peut-être les fermer explicitement.
    *   Dans les applications à longue durée de vie, assurez-vous que les processus enfants se terminent correctement et ne deviennent pas des "zombies". Utilisez `p.wait()` ou `p.communicate()`. Si nécessaire, utilisez `p.terminate()` ou `p.kill()`.

*   **Encodages :** Soyez attentif aux encodages lorsque vous utilisez `text=True` ou lors du décodage manuel de chaînes d'octets. Les problèmes d'encodage sont une source fréquente d'erreurs.

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
    # Cette ligne ne sera pas exécutée si check=True, car une exception sera levée
except subprocess.CalledProcessError as e:
    print(f"Erreur lors de l'exécution de la commande : {e.cmd}")
    print(f"Code de retour : {e.returncode}")
    if e.stderr:
        print(f"Stderr : {e.stderr.strip()}")
```

**2. Capture de la sortie d'une commande :**
```python
import subprocess

try:
    result = subprocess.run(
        ["git", "status", "--short"],
        capture_output=True,
        text=True,
        check=True,
        cwd="."  # Spécifier le répertoire courant comme répertoire de travail pour git
    )
    print("État de Git : ")
    print(result.stdout)
except FileNotFoundError:
    print("Erreur : commande 'git' introuvable. Git est-il installé et dans le PATH ?")
except subprocess.CalledProcessError as e:
    print(f"Erreur git : {e.stderr}")
```

**3. Envoi de données à l'entrée d'un processus (en utilisant `communicate`) :**
```python
import subprocess

# Envoyer du texte à 'grep' pour la recherche
input_text = "hello world\npython is fun\nhello python"
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
        print("Aucune correspondance pour 'python' trouvée.")
    else: # autre erreur de grep
        print(f"Erreur de grep (code {process.returncode}) : ")
        if stderr_data: print(stderr_data)

except subprocess.TimeoutExpired:
    print("Grep n'a pas répondu à temps.")
    process.kill() # Tuer le processus s'il est bloqué
    process.communicate() # Récupérer la sortie/les erreurs restantes
```

**4. Création d'un pipeline (`ls -l | wc -l`) sans `shell=True` :**
(Un exemple plus détaillé se trouvait dans la section 5)
```python
import subprocess

ls_proc = subprocess.Popen(["ls", "-l"], stdout=subprocess.PIPE)
wc_proc = subprocess.Popen(["wc", "-l"], stdin=ls_proc.stdout, stdout=subprocess.PIPE, text=True)

if ls_proc.stdout: # S'assurer que stdout existe
    ls_proc.stdout.close()  # Permet à wc_proc de recevoir EOF lorsque ls_proc se termine

output, _ = wc_proc.communicate()
print(f"Nombre de fichiers/répertoires : {output.strip()}")
```

**5. Utilisation de `timeout` :**
```python
import subprocess

try:
    # Une commande qui s'exécutera pendant 5 secondes
    result = subprocess.run(["sleep", "5"], timeout=2)
    print("La commande 'sleep 5' s'est terminée (n'aurait pas dû avec timeout=2).")
except subprocess.TimeoutExpired as e:
    print(f"La commande '{e.cmd}' ne s'est pas terminée en {e.timeout} secondes.")
```

---

### 8. Conclusion et ressources utiles

Le module `subprocess` est un outil indispensable pour tout développeur Python qui a besoin d'interagir avec des programmes externes ou l'environnement système. Il offre un équilibre entre la facilité d'utilisation (via `subprocess.run()`) et une flexibilité puissante (via `subprocess.Popen()`).

**Points clés :**
*   Préférez `subprocess.run()` pour la plupart des tâches.
*   Utilisez `subprocess.Popen()` pour l'exécution asynchrone ou la gestion complexe des flux.
*   **Évitez `shell=True`**, en particulier avec les entrées utilisateur, en raison des risques de sécurité. Passez les commandes sous forme de liste d'arguments.
*   Gérez toujours les codes de retour et les exceptions possibles.
*   Soyez attentif aux encodages lorsque vous travaillez avec une sortie texte (`text=True` ou décodage manuel).
*   `communicate()` est votre ami pour un échange de données sûr via `PIPE`.

**Ressources utiles :**
*   Documentation officielle de Python pour le module `subprocess` : [https://docs.python.org/3/library/subprocess.html](https://docs.python.org/3/library/subprocess.html)
*   PEP 324 – `subprocess` - A New Process Module : [https://peps.python.org/pep-0324/](https://peps.python.org/pep-0324/)
