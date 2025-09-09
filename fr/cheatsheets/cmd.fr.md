**1. Gestion des fichiers et des répertoires :**

*   **`attrib`** : Affiche ou modifie les attributs d'un fichier ou d'un répertoire (masqué, lecture seule, archive, etc.).
    *   **Syntaxe :** `attrib [+r|-r] [+a|-a] [+s|-s] [+h|-h] [lecteur:][chemin]nom_fichier`
    *   **Options :**
        *   `+r` : Définit l'attribut "lecture seule"
        *   `-r` : Supprime l'attribut "lecture seule"
        *   `+a` : Définit l'attribut "archive"
        *   `-a` : Supprime l'attribut "archive"
        *   `+s` : Définit l'attribut "système"
        *   `-s` : Supprime l'attribut "système"
        *   `+h` : Définit l'attribut "masqué"
        *   `-h` : Supprime l'attribut "masqué"
    *   **Exemples :**
        *   `attrib +h myfile.txt` : Rend le fichier `myfile.txt` masqué.
        *   `attrib -r myfile.txt` : Supprime l'attribut "lecture seule" du fichier `myfile.txt`.
        *   `attrib *.*` : Affiche les attributs de tous les fichiers du répertoire courant.

*   **`cd` ou `chdir`** : Change le répertoire courant.
    *   **Syntaxe :** `cd [chemin]` ou `chdir [chemin]`
    *   **Options :**
        *   `..` : Remonte au répertoire parent.
        *   `\` : Va à la racine du lecteur.
    *   **Exemples :**
        *   `cd Documents` : Va dans le dossier `Documents` du répertoire courant.
        *   `cd C:\Users\User\Downloads` : Va dans le dossier `Downloads` sur le lecteur C.
        *   `cd ..` : Remonte au répertoire parent.
        *   `cd \` : Va à la racine du lecteur courant.

*   **`copy`** : Copie un ou plusieurs fichiers.
    *   **Syntaxe :** `copy [fichier_source] [fichier_cible]`
    *   **Options :**
        *   `/a` : Copie un fichier ASCII
        *   `/b` : Copie un fichier binaire
        *   `/v` : Vérifie que les fichiers ont été copiés correctement
    *   **Exemples :**
        *   `copy myfile.txt mycopy.txt` : Copie le fichier `myfile.txt` vers `mycopy.txt`.
        *   `copy *.txt C:\Backup` : Copie tous les fichiers avec l'extension `.txt` dans le dossier `C:\Backup`.

*   **`del` ou `erase`** : Supprime un ou plusieurs fichiers.
    *   **Syntaxe :** `del [nom_fichier]` ou `erase [nom_fichier]`
    *   **Options :**
        *   `/p` : Demande confirmation avant de supprimer chaque fichier.
        *   `/f` : Supprime les fichiers "lecture seule".
        *   `/s` : Supprime les fichiers des sous-répertoires.
        *   `/q` : Supprime les fichiers sans confirmation.
    *   **Exemples :**
        *   `del myfile.txt` : Supprime le fichier `myfile.txt`.
        *   `del *.tmp` : Supprime tous les fichiers avec l'extension `.tmp`.
        *   `del /f /s *.log` : Supprime tous les fichiers avec l'extension `.log` dans le répertoire courant et tous les sous-répertoires, sans confirmation.

*   **`dir`** : Affiche la liste des fichiers et des répertoires dans le répertoire courant.
    *   **Syntaxe :** `dir [chemin] [options]`
    *   **Options :**
        *   `/a` : Affiche tous les fichiers (y compris les masqués).
        *   `/w` : Affiche la liste au format large.
        *   `/p` : Affiche la liste page par page.
        *   `/s` : Affiche les fichiers des sous-répertoires.
        *   `/b` : Affiche uniquement le nom du fichier.
    *   **Exemples :**
        *   `dir` : Affiche la liste des fichiers et des répertoires dans le répertoire courant.
        *   `dir C:\Users\User\Documents /a` : Affiche tous les fichiers du répertoire `Documents`.
        *   `dir /w` : Affiche la liste des fichiers et des répertoires dans le répertoire courant au format large.
        *   `dir /b /s *.txt` : Affiche tous les fichiers *.txt avec leur chemin complet.

*   **`mkdir` ou `md`** : Crée un nouveau répertoire.
    *   **Syntaxe :** `mkdir [chemin]` ou `md [chemin]`
    *   **Exemples :**
        *   `mkdir NewFolder` : Crée un nouveau dossier `NewFolder` dans le répertoire courant.
        *   `mkdir C:\Backup` : Crée un nouveau dossier `Backup` sur le lecteur `C`.

*   **`move`** : Déplace un ou plusieurs fichiers ou répertoires.
    *   **Syntaxe :** `move [fichier_source] [fichier_cible]`
    *   **Exemples :**
        *   `move myfile.txt C:\Documents` : Déplace le fichier `myfile.txt` vers le dossier `C:\Documents`.
        *   `move dir1 dir2` : Déplace le dossier `dir1` dans le dossier `dir2`.

*   **`rd` ou `rmdir`** : Supprime un répertoire.
    *   **Syntaxe :** `rd [chemin]` ou `rmdir [chemin]`
    *   **Options :**
        *   `/s` : Supprime le répertoire avec tous ses sous-répertoires.
        *   `/q` : Supprime le répertoire sans confirmation.
    *   **Exemples :**
        *   `rd myfolder` : Supprime le dossier vide `myfolder`.
        *   `rd /s /q myfolder` : Supprime le dossier `myfolder` avec tout son contenu sans confirmation.

*   **`ren` ou `rename`** : Renomme un fichier ou un répertoire.
    *   **Syntaxe :** `ren [ancien_nom] [nouveau_nom]`
    *   **Exemples :**
        *   `ren myfile.txt newfile.txt` : Renomme le fichier `myfile.txt` en `newfile.txt`.

*   **`type`** : Affiche le contenu d'un fichier texte.
    *   **Syntaxe :** `type [nom_fichier]`
    *   **Exemple :** `type myfile.txt` : Affiche le contenu du fichier `myfile.txt`.

*   **`xcopy`** : Copie des fichiers et des répertoires (y compris les sous-répertoires).
    *   **Syntaxe :** `xcopy [source] [destination] [options]`
    *   **Options :**
        *   `/s` : Copie les répertoires et les sous-répertoires (sauf les vides).
        *   `/e` : Copie les répertoires et les sous-répertoires (y compris les vides).
        *   `/i` : Si la destination n'existe pas, la crée.
        *   `/y` : Supprime la demande de confirmation de remplacement.
        *   `/d` : Copie uniquement les nouveaux fichiers.
    *   **Exemples :**
        *   `xcopy C:\Source D:\Destination /s` : Copie le répertoire `C:\Source` avec tous ses sous-répertoires dans le dossier `D:\Destination`.
        *   `xcopy C:\Source D:\Destination /e /y` : Copie le répertoire `C:\Source` avec tous ses sous-répertoires dans le dossier `D:\Destination`, y compris les vides et sans confirmation de remplacement.

**2. Travailler avec les disques :**

*   **`diskpart`** : Lance l'utilitaire de gestion des disques (partitions, volumes).
    *   **Syntaxe :** `diskpart`
    *   **Notes :**
        *   `diskpart` est un utilitaire interactif qui possède son propre ensemble de commandes.
        *   Des droits d'administrateur sont requis pour l'utiliser.
        *   Vous pouvez en savoir plus sur l'utilisation de `diskpart` avec la commande `help` à l'intérieur de cet utilitaire.
*   **`format`** : Formate un disque.
    *   **Syntaxe :** `format [lecteur:] [options]`
    *   **Options :**
        *   `/q` : Formatage rapide
        *   `/fs:file-system` : Choisir le type de système de fichiers (par exemple, NTFS, FAT32)
    *   **Exemples :**
        *   `format D: /q` : Formatage rapide du lecteur D:.
        *   `format E: /fs:NTFS` : Formatage du lecteur E: au système de fichiers NTFS.
    *   **Avertissement :** Le formatage d'un disque supprime toutes les données qu'il contient !
*   **`label`** : Définit ou modifie l'étiquette d'un disque.
    *   **Syntaxe :** `label [lecteur:][étiquette]`
    *   **Exemples :**
        *   `label D: NewLabel` : Définit l'étiquette du lecteur D comme NewLabel.
        *   `label D:` : Efface l'étiquette du lecteur D.

**3. Gestion du système :**

*   **`cls`** : Efface l'écran de la ligne de commande.
    *   **Syntaxe :** `cls`
*   **`date`** : Affiche ou modifie la date actuelle.
    *   **Syntaxe :** `date [nouvelle_date]`
    *   **Exemples :**
        *   `date` : Affiche la date actuelle.
        *   `date 12-25-2024` : Change la date au 25 décembre 2024.
*   **`exit`** : Quitte la ligne de commande.
    *   **Syntaxe :** `exit`
*   **`shutdown`** : Arrête ou redémarre l'ordinateur.
    *   **Syntaxe : `shutdown [options]`**
    *   **Options :**
        *   `/s` : Arrête l'ordinateur.
        *   `/r` : Redémarre l'ordinateur.
        *   `/a` : Annule l'arrêt ou le redémarrage.
        *   `/t xxx` : Délai en secondes avant l'arrêt ou le redémarrage.
    *   **Exemples :**
        *   `shutdown /s /t 60` : Arrête l'ordinateur dans 60 secondes.
        *   `shutdown /r` : Redémarre l'ordinateur.
        *   `shutdown /a` : Annule l'arrêt ou le redémarrage planifié.
*   **`tasklist`** : Affiche la liste des processus en cours d'exécution.
    *   **Syntaxe :** `tasklist [options]`
    *   `/v` : Informations supplémentaires
    *   `/fo csv` : Affiche au format CSV
    *   `/fi "nom_image eq notepad.exe"` : Trouve tous les processus du Bloc-notes
    *   **Exemples :**
        *   `tasklist` : Affiche la liste des processus en cours d'exécution.
        *   `tasklist /v` : Affiche la liste des processus en cours d'exécution avec des informations détaillées.

*   **`taskkill`** : Termine un processus.
    *   **Syntaxe :** `taskkill [options]`
    *   **Options :**
        *   `/im nom_image` : Termine le processus par son nom.
        *   `/pid pid` : Termine le processus par son identifiant.
        *   `/f` : Termine le processus de force.
    *   **Exemples :**
        *   `taskkill /im notepad.exe` : Termine tous les processus nommés `notepad.exe`.
        *   `taskkill /pid 1234` : Termine le processus avec l'identifiant 1234.
        *   `taskkill /im notepad.exe /f` : Termine de force tous les processus `notepad.exe`.
*   **`time`** : Affiche ou modifie l'heure actuelle.
    *   **Syntaxe :** `time [nouvelle_heure]`
    *   **Exemples :**
        *   `time` : Affiche l'heure actuelle.
        *   `time 15:30` : Définit l'heure à 15:30.
*   **`ver`** : Affiche la version du système d'exploitation.
    *   **Syntaxe :** `ver`
*   **`systeminfo`** : Affiche des informations détaillées sur le système.
    *   **Syntaxe :** `systeminfo`

*   **`taskmgr`** : Lance le gestionnaire des tâches.
    *   **Syntaxe :** `taskmgr`

**4. Réseau :**

*   **`ipconfig`** : Affiche la configuration réseau.
    *   **Syntaxe :** `ipconfig [options]`
    *   **Options :**
        *   `/all` : Affiche toutes les informations sur les adaptateurs réseau.
        *   `/release` : Libère l'adresse IP.
        *   `/renew` : Demande une nouvelle adresse IP.
    *   **Exemples :**
        *   `ipconfig` : Affiche la configuration réseau de base.
        *   `ipconfig /all` : Affiche toutes les informations sur tous les adaptateurs réseau.
        *   `ipconfig /release` : Libère l'adresse IP.
        *   `ipconfig /renew` : Demande une nouvelle adresse IP.
*   **`ping`** : Envoie une requête écho à un autre ordinateur sur le réseau.
    *   **Syntaxe :** `ping [nom_hôte_ou_adresse_ip] [options]`
    *   `-n xxx` : Nombre de requêtes
    *   `-t` : Demande un ping indéfiniment
    *   **Exemples :**
        *   `ping google.com` : Ping le serveur `google.com`.
        *   `ping 192.168.1.100` : Ping l'ordinateur avec l'adresse IP `192.168.1.100`.
        *   `ping google.com -n 10` : Exécute 10 pings.
*   **`tracert`** : Affiche le chemin des paquets vers un autre ordinateur sur le réseau.
    *   **Syntaxe :** `tracert [nom_hôte_ou_adresse_ip]`
    *   **Exemple :** `tracert google.com` : Affiche le chemin des paquets vers `google.com`.
*   **`netstat`** : Affiche les connexions réseau.
    *   **Syntaxe :** `netstat [options]`
    *   **Options :**
        *   `-a` : Affiche toutes les connexions.
        *   `-b` : Affiche les applications qui ont créé les connexions.
    *   **Exemples :**
        *   `netstat` : Affiche toutes les connexions actives.
        *   `netstat -a -b` : Affiche toutes les connexions et les applications en cours d'exécution qui les ont ouvertes.

*   **`nslookup`** : Interroge les informations DNS.
    *   **Syntaxe :** `nslookup [nom_hôte]`
    *   **Exemple :** `nslookup google.com` : Interroge les informations DNS pour `google.com`.

**5. Autres commandes :**

*   **`assoc`** : Affiche ou modifie les associations de fichiers.
    *   **Syntaxe :** `assoc [.extension]=[type_fichier]`
    *   **Exemples :**
        *   `assoc .txt` : Affiche le type de fichier pour l'extension `.txt`.
        *   `assoc .txt=txtfile` : Définit le type de fichier pour l'extension `.txt` comme `txtfile`.
*   **`call`** : Appelle un fichier de commandes à partir d'un autre.
    *   **Syntaxe :** `call [nom_fichier_de_commandes]`
    *   **Exemple :** `call mybatch.bat` : Appelle le fichier de commandes `mybatch.bat`.
*   **`chcp`** : Change la page de codes de la console.
    *   **Syntaxe :** `chcp [numéro_page_de_codes]`
    *   **Exemples :**
        *   `chcp 1251` : Définit la page de codes pour le cyrillique.
        *   `chcp` : Affiche la page de codes actuelle.
*   **`choice`** : Permet à l'utilisateur de choisir parmi une liste d'options.
    *   **Syntaxe :** `choice [/c [options]] [/n] [/t [secondes]] [/d [option]] [texte]`
    *   **Options :**
        *   `/c` : Spécifie les options disponibles.
        *   `/n` : Masque la liste des options disponibles.
        *   `/t` : Spécifie le temps d'attente (en secondes).
        *   `/d` : Spécifie l'option par défaut.
    *   **Exemple :** `choice /c yn /t 10 /d n "Voulez-vous vraiment quitter ?" `
*   **`find`** : Recherche une chaîne de texte dans un fichier.
    *   **Syntaxe :** `find "chaîne" [nom_fichier]`
    *   **Exemples :**
        *   `find "Hello" myfile.txt` : Recherche la chaîne "Hello" dans le fichier myfile.txt.

*   **`findstr`** : Recherche des chaînes de texte dans des fichiers (analogue plus puissant de `find`).
    *   **Syntaxe :** `findstr [options] "chaîne" [nom_fichier]`
    *   **Options :**
        *   `/i` : Recherche insensible à la casse.
        *   `/n` : Affiche les numéros de ligne.
        *   `/s` : Recherche dans tous les sous-répertoires.
    *   **Exemples :**
        *   `findstr /i "error" myfile.log` : Recherche la chaîne "error" (insensible à la casse) dans `myfile.log`.
        *   `findstr /n "error" *.log` : Recherche la chaîne "error" dans tous les fichiers .log et affiche les numéros de ligne.

*   **`gpupdate`** : Met à jour les stratégies de groupe.
    *   **Syntaxe :** `gpupdate [options]`
    *   **Options :**
        *   `/force` : Met à jour de force.
    *   **Exemple :** `gpupdate /force` : Met à jour de force les stratégies de groupe.
*   **`help` ou `/?`** : Affiche l'aide pour une commande.
    *   **Syntaxe :** `help [nom_commande]` ou `[nom_commande] /?`
    *   **Exemple :** `help dir` ou `dir /?` : Affiche l'aide pour la commande `dir`.
*   **`pause`** : Suspend l'exécution d'un fichier de commandes et attend une touche.
    *   **Syntaxe :** `pause`
*   **`path`** : Affiche ou modifie les variables d'environnement PATH.
    *   **Syntaxe :** `path [chemin]`
    *   **Exemples :**
        *   `path` : Affiche la valeur actuelle de la variable PATH.
        *   `path C:\bin` : Ajoute le dossier C:\bin à la variable PATH.
*   **`prompt`** : Configure la chaîne d'invite de la ligne de commande.
    *   **Syntaxe :** `prompt [texte]`
    *   **Exemples :**
        *   `prompt $p$g` : Définit la chaîne d'invite pour le chemin actuel.
        *   `prompt MyPrompt>` : Définit la chaîne d'invite `MyPrompt>`.
*   **`set`** : Affiche, définit ou supprime les variables d'environnement.
    *   **Syntaxe :** `set [nom=[valeur]]`
    *   **Exemples :**
        *   `set` : Affiche toutes les variables d'environnement.
        *   `set myvar=myvalue` : Définit la variable d'environnement `myvar` à `myvalue`.
        *   `set myvar=` : Supprime la variable d'environnement `myvar`.
*   **`start`** : Lance un programme ou ouvre un fichier.
    *   **Syntaxe :** `start [nom_programme_ou_fichier] [options]`
    *   **Exemples :**
        *   `start notepad.exe` : Lance le Bloc-notes.
        *   `start myfile.txt` : Ouvre le fichier `myfile.txt` avec le programme par défaut.
        *   `start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" "https://www.google.com"` : Ouvre un site web dans Chrome.
*   **`tree`** : Affiche la structure graphique des répertoires.
    *   **Syntaxe :** `tree [lecteur:][chemin] [options]`
    *   **Options :**
        *   `/f` : Affiche également les noms de fichiers.
        *   `/a` : Utilise des caractères ASCII.
    *   **Exemples :**
        *   `tree` : Affiche la structure du répertoire courant.
        *   `tree /f` : Affiche la structure du répertoire courant avec les fichiers.

*   **`where`** : Trouve l'emplacement d'un fichier.
    *   **Syntaxe :** `where [nom_fichier]`
    *   **Exemple :** `where notepad.exe`

**6. Commandes pour travailler avec les fichiers de commandes :**

*   **`echo`** : Affiche du texte à l'écran.
    *   **Syntaxe :** `echo [texte]`
    *   `echo on` : Active l'affichage des commandes lors de l'exécution du fichier batch.
    *   `echo off` : Désactive l'affichage des commandes lors de l'exécution du fichier batch.
    *   **Exemples :**
        *   `echo Hello, world!` : Affiche "Hello, world!" à l'écran.
        *   `echo off` : Désactive l'affichage des commandes.
        *   `echo on` : Active l'affichage des commandes.
*   **`rem`** : Ajoute un commentaire dans un fichier de commandes.
    *   **Syntaxe :** `rem [commentaire]`
    *   **Exemple :** `rem Ceci est un commentaire`
*   **`goto`** : Saute à une étiquette.
    *   **Syntaxe :** `goto [étiquette]`
    *   **Exemple :**
        ```batch
        :start
        echo Bonjour
        goto end
        echo Ceci ne sera pas affiché
        :end
        echo Au revoir
        ```
*   **`if`** : Exécute une logique conditionnelle.
    *   **Syntaxe :** `if [not] condition (commande1) else (commande2)`
    *   **Exemples :**
        *   `if exist file.txt echo le fichier existe` : Vérifie l'existence d'un fichier.
        *   `if %var%== "text" echo la variable a une valeur` : Vérifie la valeur d'une variable.
*   **`for`** : Exécute une action en boucle.
    *   **Syntaxe :** `for %%variable in (ensemble) do [commande]`
    *   **Exemple :**
        ```batch
        for %%a in (*.txt) do (
         echo %%a
         type %%a
         echo -------------
        )
        ```
        *   Affiche le nom de chaque fichier `.txt` et son contenu.

**Avertissement :**
*   Soyez prudent lorsque vous utilisez des commandes qui peuvent modifier le système, surtout avec des droits d'administrateur.
*   Avant d'exécuter la commande `format`, assurez-vous d'avoir sélectionné le bon disque.
