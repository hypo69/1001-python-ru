**Guide des commandes PowerShell**

**1. Bases de la navigation et du travail avec les fichiers et les répertoires**

*   **`Get-ChildItem` (ou `gci`, `ls`, `dir`)** : Obtient une liste de fichiers et de sous-répertoires à l'emplacement spécifié.
    *   **Syntaxe** : `Get-ChildItem [chemin] [paramètres]`
    *   **Paramètres principaux :**
        *   `-Path` : Spécifie le chemin du répertoire.
        *   `-Include` : Filtre par nom de fichier (avec les caractères génériques `*` et `?`).
        *   `-Exclude` : Exclut les fichiers par nom.
        *   `-Recurse` : Affiche les fichiers et les dossiers dans tous les sous-répertoires.
        *   `-Force` : Afficher les fichiers cachés.
        *   `-File` : Afficher uniquement les fichiers.
        *   `-Directory` : Afficher uniquement les dossiers.
    *   **Exemples :**
        *   `Get-ChildItem` : Liste des fichiers et des dossiers dans le répertoire courant.
        *   `Get-ChildItem -Path C:\Users\User\Documents` : Liste des fichiers et des dossiers dans `C:\Users\User\Documents`.
        *   `Get-ChildItem -Include *.txt` : Liste uniquement les fichiers texte dans le répertoire courant.
        *   `Get-ChildItem -Path C:\ -Recurse -Directory` : Afficher tous les répertoires sur le lecteur C.
        *  `Get-ChildItem -Force` : Afficher tous les fichiers, y compris les cachés.

*   **`Set-Location` (ou `sl`, `cd`)** : Change le répertoire courant.
    *   **Syntaxe** : `Set-Location [chemin]`
    *   **Exemples :**
        *   `Set-Location C:\Windows` : Aller dans le répertoire `C:\Windows`.
        *   `Set-Location ..` : Aller dans le répertoire parent.
        * `Set-Location /` - Aller à la racine du lecteur.
*   **`New-Item`** : Crée un nouveau fichier ou répertoire.
    *   **Syntaxe** : `New-Item -Path [chemin] -ItemType [type] -Name [nom]`
    *   **Paramètres principaux :**
        *   `-ItemType` : `file` ou `directory`.
        *   `-Name` : Nom du nouvel élément.
        *   `-Value` : Contenu du fichier.
    *   **Exemples :**
        *   `New-Item -ItemType directory -Name NewFolder` : Créer un dossier `NewFolder`.
        *   `New-Item -ItemType file -Name myfile.txt` : Créer un fichier vide `myfile.txt`.
        *   `New-Item -ItemType file -Name myfile.txt -Value "Hello, world!"` : Créer le fichier `myfile.txt` avec du contenu.

*  **`Remove-Item` (ou `rm`, `del`, `erase`)** : Supprime des fichiers et des répertoires.
    *   **Syntaxe :** `Remove-Item [chemin] [paramètres]`
    *   **Paramètres principaux :**
         *   `-Recurse` :  Supprimer tous les sous-répertoires.
        *   `-Force` : Suppression forcée (y compris les fichiers "lecture seule" et les répertoires).
       *  `-Confirm` - Demander confirmation pour chaque suppression.
    *   **Exemples :**
        *   `Remove-Item myfile.txt` : Supprimer le fichier `myfile.txt`.
        *   `Remove-Item -Path C:\Temp -Recurse -Force` : Supprimer le dossier `C:\Temp` avec tous les sous-dossiers et fichiers.

*   **`Copy-Item`** : Copie des fichiers et des répertoires.
    *   **Syntaxe** : `Copy-Item [chemin_source] [chemin_destination] [paramètres]`
    *   **Paramètres principaux :**
        *   `-Recurse` : Copier tous les sous-répertoires.
        *   `-Force` : Écraser les fichiers existants sans confirmation.
    *   **Exemples :**
        *   `Copy-Item -Path myfile.txt -Destination mycopy.txt` : Copier le fichier `myfile.txt` vers `mycopy.txt`.
        *   `Copy-Item -Path C:\Source -Destination D:\Backup -Recurse` : Copier le dossier `C:\Source` vers tous les sous-répertoires du dossier `D:\Backup`.

*   **`Move-Item`** : Déplace des fichiers et des répertoires.
    *   **Syntaxe** : `Move-Item [chemin_source] [chemin_destination] [paramètres]`
      *  `-Force` - Forcer le déplacement et l'écrasement.

    *   **Exemples :**
        *   `Move-Item -Path myfile.txt -Destination D:\Documents` : Déplacer le fichier `myfile.txt` vers le dossier `D:\Documents`.
         *   `Move-Item -Path "C:\MyFolder" -Destination "D:\" -Force` : Déplacer le dossier C:\MyFolder vers D:\ de force, même si un dossier portant ce nom existe déjà.

*   **`Rename-Item`** : Renomme un fichier ou un répertoire.
    *   **Syntaxe** : `Rename-Item -Path [chemin] -NewName [nouveau_nom]`
    *   **Exemple :**
        *   `Rename-Item -Path myfile.txt -NewName newfile.txt` : Renommer le fichier `myfile.txt` en `newfile.txt`.

*   **`Get-Content` (ou `gc`)** : Affiche ou obtient le contenu d'un fichier.
    *   **Syntaxe** : `Get-Content [chemin]`
    *   **Exemple :**
        *   `Get-Content myfile.txt` : Afficher le contenu du fichier `myfile.txt`.
*   **`Set-Content`** : Remplace ou crée le contenu d'un fichier.
    *  **Syntaxe :** `Set-Content [chemin] [paramètres]`
        *  `-value` - texte à écrire.
   *   **Exemple :** `Set-Content myfile.txt "Nouveau texte"` - Remplacer le texte du fichier `myfile.txt`.

*   **`Add-Content`** : Ajoute du contenu à la fin d'un fichier.
   * **Syntaxe :** `Add-Content [chemin] [paramètres]`
       *  `-value` - texte à ajouter.

   *   **Exemple :** `Add-Content myfile.txt "Plus de texte"` - Ajouter du texte à la fin de `myfile.txt`.

**2. Gestion des processus :**

*   **`Get-Process` (ou `gps`)** : Obtient une liste des processus en cours d'exécution.
    *   **Syntaxe** : `Get-Process [paramètres]`
    *   **Paramètres principaux :**
        *   `-Name` : Filtrer par nom de processus.
        *   `-Id` : Filtrer par identifiant de processus.
        *    `-IncludeUserName` : Afficher l'utilisateur qui a démarré le processus.
    *   **Exemples :**
        *   `Get-Process` : Liste de tous les processus en cours d'exécution.
        *   `Get-Process -Name notepad` : Liste des processus nommés `notepad`.
        *    `Get-Process -IncludeUserName` : Liste de tous les processus en cours d'exécution avec les utilisateurs.

*   **`Stop-Process`** : Termine un processus.
    *   **Syntaxe** : `Stop-Process [paramètres]`
     *  `-Id` - Spécifier l'ID du processus.
    *   `-Name` - Spécifier le nom du processus.
    *  `-Force` - Forcer la terminaison du processus.
    *   **Exemples :**
        *   `Stop-Process -Name notepad` : Terminer tous les processus `notepad`.
         *    `Stop-Process -Id 1234` : Terminer le processus avec l'ID 1234.
        *    `Stop-Process -Name chrome -Force` : Forcer la terminaison de tous les processus `chrome`.

**3. Gestion des services :**

*   **`Get-Service`** : Obtient une liste de services.
    *   **Syntaxe** : `Get-Service [paramètres]`
    *   **Paramètres principaux :**
         * `-Name` : Afficher uniquement les services avec le nom spécifié.
         * `-DisplayName` : Afficher uniquement les services avec le nom d'affichage spécifié.
        *   `-Status` : Filtrer par statut (Running, Stopped).
    *   **Exemples :**
        *   `Get-Service` : Liste de tous les services.
        *   `Get-Service -Name Spooler` : Afficher le service Spooler.
       *   `Get-Service -Status Running` : Afficher les services en cours d'exécution.
*  **`Start-Service`** : Démarre un service.
   *   **Syntaxe** : `Start-Service [nom_service]`
   *   **Exemple :** `Start-Service Spooler` - Démarrer le service Spooler.

*   **`Stop-Service`** : Arrête un service.
    *   **Syntaxe** : `Stop-Service [nom_service]`
        *  `-Force` - Forcer l'arrêt du service.
    *   **Exemple :** `Stop-Service Spooler` : Arrêter le service Spooler.
        *   `Stop-Service Spooler -Force` : Forcer l'arrêt du service Spooler.

*  **`Restart-Service`** : Redémarre un service.
   *   **Syntaxe :** `Restart-Service [nom_service]`
   *   **Exemple :** `Restart-Service Spooler` - Redémarrer le service Spooler.

**4. Travail en réseau**

*   **`Test-NetConnection`** : Teste la connexion réseau.
    *   **Syntaxe** : `Test-NetConnection [nom_hôte_ou_adresse_ip] [paramètres]`
    *  `-Port` - Numéro de port.
    *   **Exemples :**
        *   `Test-NetConnection google.com` : Tester la connexion à `google.com`.
        * `Test-NetConnection google.com -Port 80` : Tester la connexion à google.com sur le port 80.
*   **`Get-NetIPConfiguration`** : Obtient la configuration réseau.
    *   **Syntaxe** : `Get-NetIPConfiguration`
    *   **Exemple :**
        *   `Get-NetIPConfiguration` : Afficher la configuration réseau.
*   **`Resolve-DnsName`** : Interroge les informations DNS.
    *   **Syntaxe** : `Resolve-DnsName [nom_hôte]`
    *   **Exemple :** `Resolve-DnsName google.com` : Interroger les informations DNS pour `google.com`.

**5. Opérations de registre**

*   **`Get-ItemProperty`** : Obtient la valeur d'une propriété du registre.
    *   **Syntaxe** : `Get-ItemProperty -Path [chemin_registre]`
    *   **Exemple :** `Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion"`
*   **`Set-ItemProperty`** : Définit la valeur d'une propriété dans le registre.
    *   **Syntaxe** : `Set-ItemProperty -Path [chemin_registre] -Name [nom_propriété] -Value [valeur]`
    *   **Exemple :** `Set-ItemProperty -Path "HKCU:\Control Panel\Desktop" -Name Wallpaper -Value "C:\image.jpg"`

**6. Autre**

*   **`Clear-Host`** : Efface l'écran de la console.
    *   **Syntaxe :** `Clear-Host`
*   **`Get-Date`** : Obtient la date et l'heure actuelles.
    *   **Syntaxe :** `Get-Date`
*    **`Start-Process`** : Lance un programme ou ouvre un fichier.
    *   **Syntaxe :** `Start-Process [nom_programme_ou_fichier] [options]`
   *   **Exemples :**
        *   `Start-Process notepad.exe` : Lancer le Bloc-notes.
        *   `Start-Process myfile.txt` : Ouvrir le fichier `myfile.txt` avec le programme par défaut.
        *   `Start-Process -FilePath "C:\Program Files\Google\Chrome\Application\chrome.exe" -ArgumentList "https://www.google.com"` - Ouvrir un site web dans Chrome.

*   **`Get-Help`** : Affiche l'aide pour une commande.
    *   **Syntaxe** : `Get-Help [nom_commande]`
    *   **Exemple :** `Get-Help Get-Process` : Afficher l'aide pour la commande `Get-Process`.
*   **`Exit`** : Termine la session PowerShell.
    *   **Syntaxe :** `Exit`
*  **`Get-Variable`** : Affiche les variables actuelles.
    *  **Syntaxe** : `Get-Variable`
*   **`Get-Alias`** : Affiche les alias de commandes.
    *   **Syntaxe** : `Get-Alias`
*   **`Set-Alias`** : Crée un alias pour une commande.
    *  **Syntaxe** : `Set-Alias [nom_alias] [nom_commande]`
    *  **Exemple** : `Set-Alias gci Get-ChildItem`

**Remarques :**

*   Les commandes `PowerShell` (cmdlets) ont généralement la forme `Verbe-Nom` (par exemple, `Get-Process`, `Set-Location`).
*   `PowerShell` est insensible à la casse, vous pouvez donc écrire les commandes comme `Get-ChildItem` ou `get-childitem`.
*   `PowerShell` fonctionne avec des objets, vous pouvez donc utiliser l'opérateur `|` pour transmettre la sortie d'une commande à l'entrée d'une autre (par exemple, `Get-Process | Sort-Object -Property CPU`).
*  De nombreuses commandes prennent en charge l'utilisation de caractères génériques (*) pour travailler avec plusieurs fichiers (par exemple `Get-ChildItem *.txt`).
*   Certaines commandes nécessitent des privilèges d'administrateur.
