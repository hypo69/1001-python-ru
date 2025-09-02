## Gemini CLI : Techniques avancées et automatisation de scénarios (Partie 2)

Dans la première partie, nous avons couvert les bases : installation, authentification et exécution de commandes uniques. Passons maintenant au niveau supérieur. Dans cette partie, nous apprendrons à Gemini CLI à exécuter des scénarios complexes en plusieurs étapes qui peuvent être enregistrés, réutilisés et partagés avec l'équipe. Cela transformera l'outil d'un simple assistant en un puissant moteur d'automatisation.

### Mécanisme d'exécution de scénarios

L'idée clé est d'utiliser les fichiers `.md` comme des "recettes" ou des "scénarios" pour Gemini. À l'intérieur d'un tel fichier, nous décrivons en langage naturel la séquence d'actions que l'IA doit effectuer.

Pour exécuter un scénario, nous utiliserons l'outil intégré `ReadFile`. Nous demanderons simplement à Gemini de lire le fichier d'instructions et de les exécuter.

**La commande de base pour exécuter n'importe quel scénario :**
```
> Lis et exécute les instructions du fichier 'nom_du_scénario.md'
```

Examinons maintenant quelques scénarios utiles.

Créez un répertoire `scenarios`.
```bash
/path/to/gemini-cli > mkdir scenarios
```

dans lequel nous stockerons nos scénarios.


### Scénario : "Audit du dépôt Git"

Cette tâche est familière à tous les développeurs : avant de commencer à travailler, vous devez vérifier l'état actuel du projet. Créons un scénario qui le fera pour nous.

1.  **Dans le répertoire `scenarios`, créez un fichier `git-health-check.md`** avec le contenu suivant :

    ```markdown
    Vous êtes un ingénieur Git expérimenté. Votre tâche consiste à effectuer un audit complet du dépôt actuel. 
    
    Suivez ces étapes strictement dans l'ordre et attendez ma confirmation pour chaque commande : 
    
    1.  **Vérifier l'état :** Montrez-moi l'état actuel du dépôt pour voir les fichiers non suivis ou modifiés. Suggérez la commande `!git status`.
    2.  **Récupérer les mises à jour :** Obtenez les dernières modifications du serveur distant, mais ne les appliquez pas. Suggérez la commande `!git fetch origin`.
    3.  **Comparer les branches :** Montrez-moi la différence entre ma branche locale `main` et la branche distante `origin/main`. Suggérez la commande `!git log main..origin/main --oneline`.
    4.  **Trouver les gros fichiers :** Trouvez les 5 plus gros fichiers du projet qui ne se trouvent pas dans `.git`. Suggérez la commande `!find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5`.
    5.  **Résumer :** À la fin, décrivez brièvement l'état du dépôt en fonction des données obtenues.
    ```

2.  **Exécutez le scénario dans Gemini CLI :**

    ```
    > Lis et exécute le script 'git-health-check.md'
    ```

![1](assets/1.png)


En fait, il n'y a pas de dépôt dans ce répertoire, Gemini proposera de créer un nouveau dépôt.
Gemini CLI corrigera indépendamment les erreurs lors de la création du dépôt, par exemple, si vous avez oublié de l'initialiser, il proposera de le faire,
ainsi que les erreurs actuelles lors de l'exécution du script

## Étape 1 : Vérification de l'état

![2](assets/2.png)

Réponse de Gemini :
```text
>✦ Je suis un ingénieur Git expérimenté. Je commence l'audit de votre dépôt.
> Étape 1 : Vérification de l'état
>Pour vérifier l'état actuel du dépôt et voir les fichiers non suivis ou modifiés, j'exécuterai la commande `git status`.
```
Exécution de la commande `git status`...
![3](assets/3.png)

Réponse de Gemini :
```text
✦ Erreur : C:\Users\user\Documents\repos n'est pas un dépôt Git.

  Veuillez spécifier dans lequel des sous-répertoires je dois exécuter l'audit. Par exemple, public_repositories.
```
Nous demandons de créer un nouveau dépôt.
![4](assets/4.png)
Réponse de Gemini :
```text
✦ Excellent, le dépôt Git a été créé. Je peux maintenant continuer l'audit.


  Exécution de git status pour vérifier les fichiers non suivis.
```
![5](assets/5.png)

...

![6](assets/6.png)

Réponse de Gemini :
```text
✦ Il y a de nombreux fichiers et dossiers non suivis dans le dépôt. Pour continuer, je dois les ajouter à l'index. J'ajouterai tous les fichiers.
```

![7](assets/7.png)
...
![8](assets/8.png)

Une erreur s'est produite lors de l'exécution de la commande
```text 
error: pathspec 'commit"' did not match any file(s) known to git
```
Réponse de Gemini :
```text
✦ Il semble qu'il y ait eu une erreur avec les guillemets dans la commande. Je vais réessayer en utilisant des guillemets simples pour le message de commit.
```

![9](assets/9.png)
![10](assets/10.png)
Cette fois, ça a marché !

Réponse de Gemini :
```text
✦ Excellent, le premier commit a été créé avec succès. Je vais maintenant supprimer le fichier temporaire avec le message de commit.
```
Maintenant, gemini supprimera le fichier temporaire avec le message de commit.

gemini cli applique la commande appropriée à son tour ('rm','del')

![11](assets/11.png)




### Étape 2 : Récupération des mises à jour
Comme le dépôt distant n'existe pas, gemini cli obtiendra une erreur.
Notez qu'il s'attend lui-même à une erreur

![12](assets/12.png)


### Étape 3 : Comparaison des branches

Il y aura également une erreur ici, car la branche `main` n'existe pas.
![13](assets/13.png)


###   Étape 4 : Recherche de gros fichiers

![14](assets/14.png)
Réponse de Gemini :
```text
La commande `find` n'a pas fonctionné car sous Windows, vous devez utiliser `dir`. Gemini corrigera l'erreur lui-même et suggérera la commande correcte.

Ensuite, gemini cli discute des étapes suivantes :
✦ THINK: The user wants me to find the 5 largest files in the project.
  The previous command find . -type f -not -path "./.git/*" -printf "%s %p\n" | sort -rn | head -n 5 failed because find, sort, and head
  are not native Windows commands. I need to use a PowerShell equivalent.

   1. Get all files: Get-ChildItem -Recurse -File
   2. Exclude .git directory: Where-Object { $_.FullName -notlike "*.git\*" }
   3. Sort by size (descending): Sort-Object -Property Length -Descending
   4. Select the top 5: Select-Object -First 5
   5. Format the output: ForEach-Object { "{0} {1}" -f $_.Length, $_.FullName }

  Let's combine these into a single PowerShell command.Il semble que find et head ne soient pas disponibles dans votre environnement Windows. Je vais utiliser PowerShell,
  pour effectuer la même tâche.
```
![15](assets/15.png)

Échec à nouveau

gemini cli continue de raisonner sur la suite des opérations :
Réponse de Gemini :
```text
 ╰──────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────╯
✦ THINK: The user wants to find the 5 largest files.
  The PowerShell command is still not executing correctly. It seems that the pipe | and special characters are being misinterpreted by the
  shell when passed as a single command string.

  I will try to execute the command by first saving the script to a file and then executing the file with PowerShell.

   1. Create a PowerShell script file (find_large_files.ps1).
   2. The content of the script will be: Get-ChildItem -Recurse -File | Where-Object { $_.FullName -notlike "*.git\*" } | Sort-Object
      -Property Length -Descending | Select-Object -First 5 | Format-Table Length, FullName -AutoSize
   3. Execute the script using powershell -File find_large_files.ps1.
   4. Delete the script file.Il semble que la transmission de commandes complexes à PowerShell directement pose des problèmes. Je vais créer un fichier de script PowerShell temporaire,
      l'exécuter, puis le supprimer.

```
![16](assets/16.png)

Cette fois, tout a fonctionné !

### Étape 5 : Résumé
gemini cli résume :
```text
 État du dépôt : 

   * Dépôt local : Initialisé, et tous les fichiers du dossier racine C:\Users\user\Documents\repos ont été ajoutés au premier commit.
   * Dépôt distant : Non configuré. Il n'y a pas d'origine distante, il n'est donc pas possible d'obtenir des mises à jour ou de comparer des branches.
   * Gros fichiers : Plusieurs fichiers très volumineux ont été trouvés, principalement dans les sous-répertoires venv et public_repositories. Les plus gros d'entre eux sont
     des bibliothèques .lib et des archives .zip. Il est recommandé d'ajouter les chemins contenant de gros fichiers binaires (par exemple, venv, *.zip) au fichier .gitignore,
     pour éviter qu'ils ne se retrouvent dans le dépôt.

  L'audit est terminé.
```
![17](assets/17.png)


### Scénario : "Nettoyage de l'environnement Docker"

Au fil du temps, Docker accumule de nombreuses images, conteneurs et réseaux inutiles. Ce scénario vous aidera à tout nettoyer en toute sécurité.

1.  **Créez un fichier `docker-cleanup.md`** :

    ```markdown
    Vous êtes un ingénieur DevOps responsable de la propreté du système. Votre tâche consiste à nettoyer en toute sécurité l'environnement Docker.
    
    Suivez ces étapes :
    
    1.  **Afficher les conteneurs en cours d'exécution :** Tout d'abord, listez tous les conteneurs actifs afin que je puisse m'assurer que je n'arrête rien d'important. Suggérez `!docker ps`.
    2.  **Arrêter tous les conteneurs :** Après mon approbation, suggérez une commande pour arrêter TOUS les conteneurs en cours d'exécution. La commande est : `!docker stop $(docker ps -q)`.
    3.  **Nettoyage global :** Effectuez maintenant un nettoyage complet du système des images en suspens (dangling), des conteneurs arrêtés, des réseaux inutilisés et du cache de construction. Suggérez la commande la plus sûre et la plus efficace `!docker system prune -af`.
    4.  **Rapport :** Après l'exécution, signalez l'espace qui a été libéré, en fonction de la sortie de la dernière commande.
    ```

2.  **Exécutez le scénario dans Gemini CLI :**

    ```
    > Lis et exécute le script de nettoyage Docker du fichier 'docker-cleanup.md'
    ```
**Résultat :** Gemini vous guidera à travers un processus de nettoyage sûr, en demandant une confirmation à chaque étape critique.

---


### Scénario : "Lancement d'applications système"

Comme le montre l'exemple, Gemini est excellent pour lancer des applications. Formalisons cela sous la forme d'un scénario simple pour Windows.

1.  **Créez un fichier `open-windows-tools.md`** :

    ```markdown
    Vous êtes un administrateur système Windows. Votre tâche consiste à ouvrir des utilitaires système sur demande.
    
    - Si je demande "planificateur de tâches", suggérez d'exécuter `!taskschd.msc`.
    - Si je demande "éditeur du registre", prévenez du danger et suggérez d'exécuter `!regedit`.
    - Si je demande "moniteur de ressources", suggérez d'exécuter `!resmon`.
    - Si je demande "gestionnaire des tâches", suggérez d'exécuter `!taskmgr`.
    - Si je demande "invite de commandes", suggérez d'exécuter `!cmd`.
    - Si je demande "explorateur", suggérez d'exécuter `!explorer`.
    De même pour les autres utilitaires.
    ```

2.  **Exécutez le scénario et donnez une commande :**

    ```
    > Utilise les instructions de 'open-windows-tools.md'. Ouvre le planificateur de tâches.
    ```
**Résultat :** Gemini comprendra le contexte du fichier et votre demande, puis suggérera d'exécuter la commande nécessaire.

> **Réponse de Gemini :**
> ```text
> D'accord, j'ouvre le Planificateur de tâches.
> 
> Exécuter `!taskschd.msc` ? (y/n)
> ```
Après confirmation, l'utilitaire Windows standard s'ouvrira sur votre écran.
```