**1. Gestion des fichiers et des répertoires :**

*   **`attrib`**: Affiche ou modifie les attributs d'un fichier ou d'un répertoire (masqué, lecture seule, archive, etc.).
    *   **Syntaxe :** `attrib [+r|-r] [+a|-a] [+s|-s] [+h|-h] [lecteur:][chemin]nom_fichier`
    *   **Options :**
        *   `+r`: Définir l'attribut "lecture seule"
        *   `-r`: Supprimer l'attribut "lecture seule"
        *   `+a`: Définir l'attribut "archive"
        *   `-a`: Supprimer l'attribut "archive"
        *   `+s`: Définir l'attribut "système"
        *   `-s`: Supprimer l'attribut "système"
        *   `+h`: Définir l'attribut "masqué"
        *   `-h`: Supprimer l'attribut "masqué"
    *   **Exemples :**
        *   `attrib +h myfile.txt`: Rendre le fichier `myfile.txt` masqué.
        *   `attrib -r myfile.txt`: Supprimer l'attribut "lecture seule" du fichier `myfile.txt`.
        *   `attrib *.*`: Afficher les attributs de tous les fichiers du répertoire courant.

*   **`cd` ou `chdir`**: Change le répertoire courant.
    *   **Syntaxe :** `cd [chemin]` ou `chdir [chemin]`
    *   **Options :**
        *   `..`: Remonter au répertoire parent.
        *   `\`: Aller à la racine du lecteur.
    *   **Exemples :**
        *   `cd Documents`: Aller dans le dossier `Documents` du répertoire courant.
        *   `cd C:\Users\User\Downloads`: Aller dans le dossier `Downloads` sur le lecteur C.
        *   `cd ..`: Remonter au répertoire parent.
        *   `cd \`: Aller à la racine du lecteur courant.

*   **`copy`**: Copie un ou plusieurs fichiers.
    *   **Syntaxe :** `copy [fichier_source] [fichier_cible]`
    *   **Options :**
        *  `/a` - Copier un fichier ASCII
        *  `/b` - Copier un fichier binaire
        *  `/v` - Vérifier que les fichiers ont été copiés correctement
    *   **Exemples :**
        *   `copy myfile.txt mycopy.txt`: Copier le fichier `myfile.txt` vers `mycopy.txt`.
        *   `copy *.txt C:\Backup`: Copier tous les fichiers avec l'extension `.txt` dans le dossier `C:\Backup`.

*   **`del` ou `erase`**: Supprime un ou plusieurs fichiers.
    *   **Syntaxe :** `del [nom_fichier]` ou `erase [nom_fichier]`
    *   **Options :**
        *   `/p`: Demander confirmation avant de supprimer chaque fichier.
        *   `/f`: Supprimer les fichiers "lecture seule".
        *   `/s`: Supprimer les fichiers des sous-répertoires.
        *   `/q` - Supprimer les fichiers sans confirmation.
    *   **Exemples :**
        *   `del myfile.txt`: Supprimer le fichier `myfile.txt`.
        *   `del *.tmp`: Supprimer tous les fichiers avec l'extension `.tmp`.
        *   `del /f /s *.log` - Supprimer tous les fichiers avec l'extension .log dans le répertoire courant et tous les sous-répertoires, sans confirmation.

*   **`dir`**: Affiche une liste de fichiers et de répertoires dans le répertoire courant.
    *   **Syntaxe :** `dir [chemin] [options]`
    *   **Options :**
        *   `/a`: Afficher tous les fichiers (y compris les masqués).
        *   `/w`: Afficher la liste au format large.
        *   `/p`: Afficher la liste page par page.
        *   `/s`: Afficher également les fichiers des sous-répertoires.
        *   `/b` - Afficher uniquement le nom du fichier.
    *   **Exemples :**
        *   `dir`: Afficher une liste de fichiers et de répertoires dans le répertoire courant.
        *   `dir C:\Users\User\Documents /a`: Afficher tous les fichiers dans le répertoire `Documents`.
        *   `dir /w`: Afficher une liste de fichiers et de répertoires dans le répertoire courant au format large.
         *   `dir /b /s *.txt`: Afficher tous les fichiers *.txt avec le chemin complet.

*   **`mkdir` ou `md`**: Crée un nouveau répertoire.
    *   **Syntaxe :** `mkdir [chemin]` ou `md [chemin]`
    *   **Exemples :**
        *   `mkdir NewFolder`: Créer un nouveau dossier `NewFolder` dans le répertoire courant.
        *   `mkdir C:\Backup`: Créer un nouveau dossier `Backup` sur le lecteur `C`.

*   **`move`**: Déplace un ou plusieurs fichiers ou répertoires.
    *   **Syntaxe :** `move [fichier_source] [fichier_cible]`
    *   **Exemples :**
        *   `move myfile.txt C:\Documents`: Déplacer le fichier `myfile.txt` vers le dossier `C:\Documents`.
        *  `move dir1 dir2` - Déplacer le dossier `dir1` vers le dossier `dir2`.

*  **`rd` ou `rmdir`**: Supprime un répertoire.
    *   **Syntaxe :** `rd [chemin]` ou `rmdir [chemin]`
    *   **Options :**
         *   `/s`: Supprimer le répertoire avec tous ses sous-répertoires.
        *   `/q` - Supprimer le répertoire sans confirmation.
    *   **Exemples :**
        *   `rd myfolder`: Supprimer le dossier vide `myfolder`.
        *  `rd /s /q myfolder` - Supprimer le dossier `myfolder` avec tout son contenu sans confirmation.

*   **`ren` ou `rename`**: Renomme un fichier ou un répertoire.
    *   **Syntaxe :** `ren [ancien_nom] [nouveau_nom]`
    *   **Exemples :**
        *   `ren myfile.txt newfile.txt`: Renommer le fichier `myfile.txt` en `newfile.txt`.

*   **`type`**: Affiche le contenu d'un fichier texte.
    *   **Syntaxe :** `type [nom_fichier]`
    *   **Exemple :** `type myfile.txt`: Afficher le contenu du fichier `myfile.txt`.

*   **`xcopy`**: Copie des fichiers et des répertoires (y compris les sous-répertoires).
    *   **Syntaxe :** `xcopy [source] [destination] [options]`
    *   **Options :**
        *   `/s`: Copier les répertoires et les sous-répertoires (sauf les vides).
        *   `/e`: Copier les répertoires et les sous-répertoires (y compris les vides).
        *   `/i`: Si la destination n'existe pas, la créer.
        *   `/y`: Supprimer la demande de confirmation d'écrasement.
        *  `/d` - Copier uniquement les nouveaux fichiers.
    *   **Exemples :**
        *   `xcopy C:\Source D:\Destination /s`: Copier le répertoire `C:\Source` vers tous les sous-répertoires du dossier `D:\Destination`.
        *   `xcopy C:\Source D:\Destination /e /y`: Copier le répertoire `C:\Source` vers tous les sous-répertoires du dossier `D:\Destination`, y compris les vides et sans confirmation d'écrasement.

**2. Opérations sur les disques :**

*   **`diskpart`**: Lance l'utilitaire de gestion des disques (partitions, volumes).
    *   **Syntaxe :** `diskpart`
    *   **Remarques :**
        *   `diskpart` est un utilitaire interactif qui possède son propre ensemble de commandes.
        *   Des privilèges d'administrateur sont requis pour l'utiliser.
        *   Vous pouvez en savoir plus sur l'utilisation de `diskpart` avec la commande `help` à l'intérieur de cet utilitaire.
*   **`format`**: Formate un disque.
    *   **Syntaxe :** `format [lecteur:] [options]`
    *   **Options :**
        *  `/q` - Formatage rapide
        *  `/fs:file-system` - Choisir le type de système de fichiers (par exemple, NTFS, FAT32)
    *   **Exemples :**
        *   `format D: /q`: Formatage rapide du lecteur D:.
        *   `format E: /fs:NTFS`: Formatage du lecteur E: au système de fichiers NTFS.
    *   **Avertissement :** Le formatage d'un lecteur supprime toutes les données qu'il contient !
*   **`label`**: Définit ou modifie l'étiquette du disque.
    *   **Syntaxe :** `label [lecteur:][étiquette]`
    *   **Exemples :**
        * `label D: NewLabel` - Définir l'étiquette du lecteur D sur NewLabel.
        * `label D:` - Supprimer l'étiquette du lecteur D.

**3. Gestion du système :**

*   **`cls`**: Efface l'écran de l'invite de commandes.
    *   **Syntaxe :** `cls`
*   **`date`**: Affiche ou modifie la date actuelle.
    *   **Syntaxe :** `date [nouvelle_date]`
    *   **Exemples :**
        *   `date`: Afficher la date actuelle.
        *   `date 12-25-2024`: Changer la date au 25 décembre 2024.
*   **`exit`**: Quitte l'invite de commandes.
    *   **Syntaxe :** `exit`
*   **`shutdown`**: Arrête ou redémarre l'ordinateur.
    *   **Syntaxe :** `shutdown [options]`
    *   **Options :**
        *   `/s`: Arrêter l'ordinateur.
        *   `/r`: Redémarrer l'ordinateur.
        *   `/a`: Annuler l'arrêt ou le redémarrage.
        *  `/t xxx` - Délai en secondes avant l'arrêt ou le redémarrage.
    *   **Exemples :**
        *   `shutdown /s /t 60`: Arrêter l'ordinateur dans 60 secondes.
        *   `shutdown /r`: Redémarrer l'ordinateur.
        *   `shutdown /a`: Annuler l'arrêt ou le redémarrage planifié.
*   **`tasklist`**: Affiche une liste des processus en cours d'exécution.
    *   **Syntaxe :** `tasklist [options]`
    *  `/v` - Informations supplémentaires.
    *  `/fo csv` - Sortie au format CSV.
    *  `/fi "nom_image eq notepad.exe"` - Trouver tous les processus du bloc-notes.
    *   **Exemples :**
        *   `tasklist`: Afficher une liste des processus en cours d'exécution.
        *   `tasklist /v`: Afficher une liste des processus en cours d'exécution avec des informations détaillées.

*   **`taskkill`**: Termine un processus.
    *   **Syntaxe :** `taskkill [options]`
    *   **Options :**
         * `/im nom_image` - Terminer le processus par nom.
        *   `/pid pid` - Terminer le processus par ID.
        *   `/f` - Forcer la terminaison du processus.
     *   **Exemples :**
        *   `taskkill /im notepad.exe`: Terminer tous les processus nommés `notepad.exe`.
        *   `taskkill /pid 1234`: Terminer le processus avec l'ID 1234.
        *  `taskkill /im notepad.exe /f` - Forcer la terminaison de tous les processus `notepad.exe`.
*   **`time`**: Affiche ou modifie l'heure actuelle.
    *   **Syntaxe :** `time [nouvelle_heure]`
    *   **Exemples :**
        *   `time`: Afficher l'heure actuelle.
        *   `time 15:30`: Définir l'heure à 15:30.
*   **`ver`**: Affiche la version du système d'exploitation.
    *   **Syntaxe :** `ver`
*   **`systeminfo`**: Affiche des informations détaillées sur le système.
    *   **Syntaxe :** `systeminfo`

*   **`taskmgr`**: Lance le Gestionnaire des tâches.
    *  **Syntaxe :** `taskmgr`

**4. Réseau :**

*   **`ipconfig`**: Affiche la configuration réseau.
    *   **Syntaxe :** `ipconfig [options]`
    *   **Options :**
        *   `/all`: Afficher toutes les informations sur les adaptateurs réseau.
        *   `/release`: Libérer l'adresse IP.
        *   `/renew`: Demander une nouvelle adresse IP.
    *   **Exemples :**
        *   `ipconfig`: Afficher la configuration réseau de base.
        *   `ipconfig /all`: Afficher toutes les informations sur tous les adaptateurs réseau.
        * `ipconfig /release` - Libérer l'adresse IP.
        * `ipconfig /renew` - Demander une nouvelle adresse IP.
*   **`ping`**: Envoie une requête écho à un autre ordinateur du réseau.
    *   **Syntaxe :** `ping [nom_hôte_ou_adresse_ip] [options]`
     *  `-n xxx` - Nombre de requêtes.
     *  `-t` - Pinger indéfiniment.
    *   **Exemples :**
        *   `ping google.com`: Pinger le serveur `google.com`.
        *   `ping 192.168.1.100`: Pinger l'ordinateur avec l'adresse IP `192.168.1.100`.
        *  `ping google.com -n 10` - Effectuer 10 pings.
*   **`tracert`**: Affiche le chemin des paquets vers un autre ordinateur du réseau.
    *   **Syntaxe :** `tracert [nom_hôte_ou_adresse_ip]`
    *   **Exemple :** `tracert google.com`: Afficher le chemin des paquets vers `google.com`.
*   **`netstat`**: Affiche les connexions réseau.
    *   **Syntaxe :** `netstat [options]`
    *   **Options :**
         *   `-a`: Affiche toutes les connexions.
        *   `-b`: Affiche les applications qui ont créé des connexions.
    *   **Exemples :**
        * `netstat` - Afficher toutes les connexions actives.
        * `netstat -a -b` - Afficher toutes les connexions et les applications qui les ont ouvertes.

*   **`nslookup`**: Interroge les informations DNS.
    *   **Syntaxe :** `nslookup [nom_hôte]`
    *   **Exemple :** `nslookup google.com`: Interroger les informations DNS pour `google.com`.

**5. Autres commandes :**

*   **`assoc`**: Affiche ou modifie les associations de fichiers.
    *   **Syntaxe :** `assoc [.extension]=[type_fichier]`
    *   **Exemples :**
        *   `assoc .txt`: Afficher le type de fichier pour l'extension `.txt`.
        *   `assoc .txt=txtfile`: Définir le type de fichier pour l'extension `.txt` comme `txtfile`.
*   **`call`**: Appelle un fichier de commandes à partir d'un autre.
    *   **Syntaxe :** `call [nom_fichier_de_commandes]`
    *   **Exemple :** `call mybatch.bat`: Appeler le fichier de commandes `mybatch.bat`.
*   **`chcp`**: Change la page de code de la console.
    *   **Syntaxe :** `chcp [numéro_page_de_code]`
    *   **Exemples :**
        *   `chcp 1251`: Définir la page de code pour le cyrillique.
        *   `chcp`: Afficher la page de code actuelle.
*   **`choice`**: Permet à l'utilisateur de choisir parmi une liste d'options.
    *   **Syntaxe :** `choice [/c [options]] [/n] [/t [secondes]] [/d [option]] [texte]`
    *   **Options :**
        *   `/c`: Spécifie les options disponibles.
        *   `/n`: Masque la liste des options disponibles.
        *   `/t`: Spécifie le délai d'attente (en secondes).
        *   `/d`: Spécifie l'option par défaut.
    *   **Exemple :** `choice /c yn /t 10 /d n "Voulez-vous vraiment quitter ?"`
*   **`find`**: Recherche une chaîne de texte dans un fichier.
    *   **Syntaxe :** `find "chaîne" [nom_fichier]`
    *   **Exemples :**
        *  `find "Hello" myfile.txt` - Recherche la chaîne "Hello" dans le fichier myfile.txt.

*   **`findstr`**: Recherche des chaînes de texte dans les fichiers (plus puissant que `find`).
    *   **Syntaxe :** `findstr [options] "chaîne" [nom_fichier]`
    *   **Options :**
         *  `/i` - Recherche insensible à la casse.
        *   `/n` - Afficher les numéros de ligne.
        *   `/s` - Rechercher dans tous les sous-répertoires.
    *   **Exemples :**
        *   `findstr /i "error" myfile.log`: Recherche la chaîne "error" (insensible à la casse) dans `myfile.log`.
        * `findstr /n "error" *.log` - Recherche la chaîne "error" dans tous les fichiers .log, et affiche les numéros de ligne.

*   **`gpupdate`**: Met à jour les stratégies de groupe.
    *   **Syntaxe :** `gpupdate [options]`
    *   **Options :**
         *  `/force` - Forcer la mise à jour.
    *   **Exemple :** `gpupdate /force` - Forcer la mise à jour des stratégies de groupe.
*   **`help` ou `/?`**: Affiche l'aide pour une commande.
    *   **Syntaxe :** `help [nom_commande]` ou `[nom_commande] /?`
    *   **Exemple :** `help dir` ou `dir /?`: Afficher l'aide pour la commande `dir`.
*   **`pause`**: Suspend l'exécution d'un fichier de commandes et attend une touche.
    *   **Syntaxe :** `pause`
*  **`path`**: Affiche ou modifie les variables d'environnement PATH.
   *   **Syntaxe** : `path [chemin]`
   *   **Exemples** :
         *  `path`: Afficher la valeur actuelle de la variable PATH.
        *  `path C:\bin` - Ajouter le dossier C:\bin à la variable PATH.
*   **`prompt`**: Configure la chaîne d'invite de commandes.
    *   **Syntaxe :** `prompt [texte]`
    *   **Exemples :**
        *   `prompt $p$g`: Définir la chaîne d'invite pour le chemin actuel.
        *   `prompt MyPrompt>`: Définir la chaîne d'invite `MyPrompt>`.
*   **`set`**: Affiche, définit ou supprime des variables d'environnement.
    *   **Syntaxe :** `set [nom=[valeur]]`
    *   **Exemples :**
        *   `set`: Afficher toutes les variables d'environnement.
        *   `set myvar=myvalue`: Définir la variable d'environnement `myvar` sur `myvalue`.
        *   `set myvar=`: Supprimer la variable d'environnement `myvar`.
*   **`start`**: Lance un programme ou ouvre un fichier.
    *   **Syntaxe :** `start [nom_programme_ou_fichier] [options]`
    *   **Exemples :**
        *   `start notepad.exe`: Lancer le Bloc-notes.
        *   `start myfile.txt`: Ouvrir le fichier `myfile.txt` avec le programme par défaut.
        *   `start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"` - Ouvrir un site web dans Chrome.
*   **`tree`**: Affiche la structure graphique des répertoires.
    *   **Syntaxe :** `tree [lecteur:][chemin] [options]`
    *   **Options :**
        * `/f`: Afficher également les noms de fichiers.
        * `/a` - Utiliser des caractères ASCII.
    *   **Exemples :**
         *   `tree` - Afficher la structure du répertoire courant.
         *   `tree /f` - Afficher la structure du répertoire courant avec les fichiers.

*   **`where`**: Trouve l'emplacement d'un fichier.
    *   **Syntaxe :** `where [nom_fichier]`
    *   **Exemple :** `where notepad.exe`

**6. Commandes de fichiers de commandes :**

*   **`echo`**: Affiche du texte à l'écran.
    *   **Syntaxe :** `echo [texte]`
    *  `echo on` - Activer l'affichage des commandes lors de l'exécution du fichier batch.
    *  `echo off` - Désactiver l'affichage des commandes lors de l'exécution du fichier batch.
    *   **Exemples :**
        *   `echo Hello, world!`: Afficher "Hello, world!".
        *   `echo off` - Désactiver la sortie des commandes.
        *  `echo on` - Activer la sortie des commandes.
*   **`rem`**: Ajoute un commentaire à un fichier de commandes.
    *   **Syntaxe :** `rem [commentaire]`
    *   **Exemple :** `rem This is a comment`
*   **`goto`**: Saute à une étiquette.
    *   **Syntaxe :** `goto [étiquette]`
    *   **Exemple :
```batch
:start
echo Hello
goto end
echo This will not be displayed
:end
echo Goodbye
```
*   **`if`**: Exécute une logique conditionnelle.
    *   **Syntaxe :** `if [not] condition (commande1) else (commande2)`
    *   **Exemples :**
         * `if exist file.txt echo file exists` - Vérifier l'existence d'un fichier.
         * `if %var%== "text" echo variable has value` - Vérifier la valeur d'une variable.
*  **`for`**: Exécute une action cyclique.
  * **Syntaxe :** `for %%variable in (ensemble) do [commande]`
  * **Exemple :
```batch
for %%a in (*.txt) do (
 echo %%a
 type %%a
 echo -------------
)
```
       * Afficher le nom de chaque fichier `.txt` et son contenu.

**Avertissement :**
*   Soyez prudent lorsque vous utilisez des commandes qui peuvent modifier le système, surtout lorsque vous les utilisez avec des privilèges d'administrateur.
*   Avant d'exécuter la commande `format`, assurez-vous d'avoir sélectionné le bon lecteur.
