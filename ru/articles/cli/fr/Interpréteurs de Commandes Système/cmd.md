# cmd

## Catégorie : Interpréteurs de commandes système

### Objectif : Invite de commandes Windows classique.

### Introduction
L'invite de commandes Windows (`cmd.exe`) est un interpréteur de ligne de commande pour les systèmes d'exploitation Windows. Il permet aux utilisateurs d'exécuter des commandes pour effectuer diverses tâches, gérer des fichiers et des répertoires, configurer les paramètres système, et bien plus encore. Il fournit une interface textuelle pour interagir avec le système d'exploitation.

### Commandes importantes et exemples

Voici quelques commandes `cmd` essentielles et leur utilisation :

#### 1. `dir` - Afficher une liste de fichiers et de sous-répertoires

La commande `dir` affiche une liste de fichiers et de sous-répertoires dans un répertoire spécifié.

```cmd
dir [lecteur:][chemin][nom_fichier] [/A[[:]attributs]] [/B] [/C] [/D] [/L] [/N] [/O[[:]ordre_tri]] [/P] [/Q] [/R] [/S] [/T[[:]champ_heure]] [/W] [/X] [/4]
```

**Drapeaux/Paramètres** :
*   `/A[[:]attributs]` : Affiche les fichiers avec les attributs spécifiés.
    *   `D` : Répertoires
    *   `R` : Fichiers en lecture seule
    *   `H` : Fichiers cachés
    *   `A` : Fichiers prêts pour l'archivage
    *   `S` : Fichiers système
    *   `I` : Fichiers non indexés par le contenu
    *   `L` : Points de réanalyse (Reparse Points)
    *   `O` : Fichiers hors ligne
    *   `-` : Préfixe signifiant "non" (par exemple, `/A:-H` pour exclure les fichiers cachés).
*   `/B` : Utilise le format nu (sans en-tête ni résumé), listant uniquement le nom du répertoire ou le nom et l'extension du fichier.
*   `/S` : Affiche les fichiers dans le répertoire spécifié et tous les sous-répertoires.
*   `/P` : Met en pause après chaque écran d'informations.
*   `/O[[:]ordre_tri]` : Trie la sortie.
    *   `N` : Par nom, alphabétique.
    *   `E` : Par extension, alphabétique.
    *   `S` : Par taille, du plus petit au plus grand.
    *   `D` : Par date/heure, du plus ancien au plus récent.
    *   `G` : Regroupe les répertoires en premier.
    *   `-` : Préfixe pour inverser l'ordre de tri.
*   `/W` : Utilise le format de liste large.
*   `/?` : Affiche l'aide pour la commande.

**Exemples** :
*   `dir` : Liste les fichiers et répertoires dans le répertoire actuel.
*   `dir /S` : Liste tous les fichiers et sous-répertoires dans le répertoire actuel et ses sous-répertoires.
*   `dir *.txt` : Liste tous les fichiers avec l'extension `.txt` dans le répertoire actuel.
*   `dir /A:H` : Liste les fichiers cachés.
*   `dir /S /B *.log > logs.txt` : Trouve tous les fichiers `.log` dans le répertoire actuel et les sous-répertoires, les liste au format nu, et redirige la sortie vers `logs.txt`.

**Conditions de succès** :
*   La commande s'exécute et affiche la liste de répertoires demandée.
*   Aucun message d'erreur n'est affiché.
*   La commande renvoie généralement un code de sortie de `0`.

**Conditions d'échec** :
*   "Fichier introuvable" : Si le chemin ou le modèle de nom de fichier spécifié n'existe pas.
*   "Accès refusé." : Si vous n'avez pas les permissions nécessaires pour accéder au répertoire.
*   Si la sortie est redirigée vers un fichier et que le répertoire du fichier de sortie n'existe pas, cela peut entraîner une "Erreur de création de fichier".

#### 2. `copy` - Copier un ou plusieurs fichiers

La commande `copy` duplique un ou plusieurs fichiers d'un emplacement à un autre.

```cmd
copy [/D] [/V] [/N] [/Y | /-Y] [/Z] [/L] [/A | /B] source [/A | /B] [+ source [/A | /B] [+ ...]] [destination [/A | /B]] [/?]
```

**Drapeaux/Paramètres** :
*   `source` : Spécifie le(s) fichier(s) à copier. Les caractères génériques (`*`, `?`) peuvent être utilisés.
*   `destination` : Spécifie le répertoire et/ou le nom de fichier pour le(s) nouveau(x) fichier(s).
*   `/V` : Vérifie que les nouveaux fichiers sont écrits correctement.
*   `/Y` : Supprime les invites de confirmation pour écraser un fichier de destination existant.
*   `/-Y` : Force l'affichage d'une invite pour confirmer l'écrasement d'un fichier de destination existant.
*   `/A` : Indique un fichier texte ASCII.
*   `/B` : Indique un fichier binaire.
*   `/Z` : Copie les fichiers en mode redémarrable, utile pour les fichiers volumineux sur un réseau.
*   `/?` : Affiche l'aide pour la commande.

**Exemples** :
*   `copy fichier.txt C:\backup` : Copie `fichier.txt` du répertoire actuel vers `C:\backup`.
*   `copy *.doc C:\reports /V` : Copie tous les fichiers `.doc` du répertoire actuel vers `C:\reports` et vérifie la copie.
*   `copy C:\source\fichier1.txt + C:\source\fichier2.txt C:\destination\combine.txt` : Combine `fichier1.txt` et `fichier2.txt` en `combine.txt`.
*   `copy D:\lisezmoi.htm` : Copie `lisezmoi.htm` du lecteur D: vers le répertoire actuel.

**Conditions de succès** :
*   Le(s) fichier(s) sont copiés vers la destination sans messages d'erreur.
*   Un message comme "1 fichier(s) copié(s)." est affiché.
*   Le `ERRORLEVEL` est `0`.

**Conditions d'échec** :
*   "Le système ne peut pas trouver le fichier spécifié." : Si le fichier source n'existe pas.
*   "Accès refusé." : Si vous n'avez pas les permissions d'écriture dans le répertoire de destination ou les permissions de lecture pour le fichier source.
*   "Il n'y a pas assez d'espace sur le disque." : Si le lecteur de destination est plein.
*   Si `/V` est utilisé et que la vérification échoue, un message d'erreur apparaîtra.
*   `ERRORLEVEL` sera non nul (par exemple, `1` pour une défaillance générale).

#### 3. `ping` - Vérifier la connectivité au niveau IP

La commande `ping` envoie des messages de requête d'écho ICMP (Internet Control Message Protocol) à un hôte cible pour vérifier la connectivité au niveau IP.

```cmd
ping [/t] [/a] [/n nombre] [/l taille] [/f] [/i TTL] [/v TOS] [/r nombre] [/s nombre] [{/j liste_hôtes | /k liste_hôtes}] [/w délai] [/R] [/S adresse_source] [/4] [/6] nom_cible
```

**Drapeaux/Paramètres** :
*   `nom_cible` : Spécifie le nom d'hôte ou l'adresse IP de la destination.
*   `/t` : Ping l'hôte spécifié jusqu'à interruption (Ctrl+C pour arrêter, Ctrl+Pause pour afficher les statistiques).
*   `/a` : Résout les adresses en noms d'hôtes.
*   `/n nombre` : Spécifie le nombre de requêtes d'écho à envoyer (par défaut : 4).
*   `/l taille` : Spécifie la taille du tampon d'envoi en octets (par défaut : 32).
*   `/w délai` : Spécifie le délai d'attente en millisecondes pour chaque réponse (par défaut : 4000ms).
*   `/?` : Affiche l'aide pour la commande.

**Exemples** :
*   `ping google.com` : Ping `google.com` quatre fois.
*   `ping 192.168.1.1 -n 10` : Ping l'adresse IP `192.168.1.1` dix fois.
*   `ping localhost` : Ping la machine locale.
*   `ping -t 8.8.8.8` : Ping en continu le serveur DNS de Google jusqu'à arrêt manuel.

**Conditions de succès** :
*   "Réponse de <adresse IP>" : Indique une réponse réussie de la cible.
*   "TTL=" dans la sortie.
*   Un résumé affichant "Paquets : Envoyés = X, Reçus = X, Perdus = 0 (0% de perte)".
*   La commande renvoie un code de sortie de `0`.

**Conditions d'échec** :
*   "Délai d'attente de la demande dépassé." : La cible n'a pas répondu dans le délai spécifié.
*   "Hôte de destination inaccessible." : Aucune route vers l'hôte de destination n'a pu être trouvée.
*   "La requête Ping n'a pas pu trouver l'hôte <nom_hôte>. Vérifiez le nom et réessayez." : Le nom d'hôte n'a pas pu être résolu en adresse IP (problème DNS).
*   "Échec général." : Indique un problème avec l'interface réseau locale.
*   Un résumé affichant "Paquets : Envoyés = X, Reçus = Y, Perdus = Z (Z% de perte)" où Z > 0.
*   La commande renvoie un code de sortie non nul (par exemple, `1` si l'hôte est inaccessible).

#### 4. `mkdir` (ou `md`) - Créer un répertoire

La commande `mkdir` crée un nouveau répertoire ou sous-répertoire.

```cmd
mkdir [lecteur:]chemin
```

**Drapeaux/Paramètres** :
*   `[lecteur:]chemin` : Spécifie le lecteur et le chemin du répertoire à créer.
*   `/?` : Affiche l'aide pour la commande.
*   (Remarque : Le drapeau `-p` pour créer des répertoires parents, courant dans les systèmes de type Unix, n'est pas un drapeau `cmd` standard. Les extensions de commande dans Windows permettent de créer des répertoires intermédiaires dans un chemin spécifié avec une seule commande `mkdir`, ce qui est effectivement similaire à `-p` dans certains cas).

**Exemples** :
*   `mkdir nouveau_dossier` : Crée un répertoire nommé `nouveau_dossier` dans le répertoire actuel.
*   `mkdir C:\projets\mon_projet` : Crée `mon_projet` à l'intérieur de `C:\projets`. Si `C:\projets` n'existe pas, `cmd` avec les extensions de commande activées le créera.
*   `md "Mes Documents"` : Crée un répertoire nommé "Mes Documents" (les guillemets sont nécessaires en raison de l'espace).

**Conditions de succès** :
*   Le répertoire est créé sans aucun message d'erreur.
*   Aucune sortie n'est généralement affichée en cas de succès.
*   Le `ERRORLEVEL` est `0`.

**Conditions d'échec** :
*   "Un sous-répertoire ou un fichier <nom_répertoire> existe déjà." : Si un répertoire portant le même nom existe déjà à l'emplacement spécifié.
*   "Le système ne peut pas trouver le chemin spécifié." : Si un répertoire intermédiaire dans le chemin n'existe pas et que les extensions de commande sont désactivées (ou si le chemin est invalide).
*   "Accès refusé." : Si vous n'avez pas les permissions d'écriture dans le répertoire parent.
*   Le `ERRORLEVEL` est non nul (par exemple, `1`).

#### 5. `del` (ou `erase`) - Supprimer un ou plusieurs fichiers

La commande `del` supprime un ou plusieurs fichiers.

```cmd
del [/p] [/f] [/s] [/q] [/a[:attributs]] noms
```

**Drapeaux/Paramètres** :
*   `noms` : Spécifie une liste d'un ou plusieurs fichiers à supprimer. Les caractères génériques (`*`, `?`) peuvent être utilisés.
*   `/P` : Demande une confirmation avant de supprimer chaque fichier.
*   `/F` : Force la suppression des fichiers en lecture seule.
*   `/S` : Supprime les fichiers spécifiés de tous les sous-répertoires. Affiche les noms des fichiers au fur et à mesure de leur suppression.
*   `/Q` : Mode silencieux ; supprime les invites de confirmation de suppression.
*   `/A[:attributs]` : Supprime les fichiers en fonction des attributs.
    *   `R` : Fichiers en lecture seule
    *   `H` : Fichiers cachés
    *   `S` : Fichiers système
    *   `A` : Fichiers prêts pour l'archivage
    *   `-` : Préfixe signifiant "non"
*   `/?` : Affiche l'aide pour la commande.

**Exemples** :
*   `del ancien_fichier.txt` : Supprime `ancien_fichier.txt` du répertoire actuel.
*   `del *.bak /Q` : Supprime tous les fichiers avec l'extension `.bak` dans le répertoire actuel sans invite.
*   `del /S /Q C:\temp\*.*` : Supprime tous les fichiers dans `C:\temp` et ses sous-répertoires sans invite.
*   `del /F lecture_seule.txt` : Force la suppression d'un fichier en lecture seule nommé `lecture_seule.txt`.

**Conditions de succès** :
*   Le(s) fichier(s) sont supprimés sans messages d'erreur.
*   Si `/P` n'est pas utilisé, il peut n'y avoir aucune sortie en cas de succès, ou un message comme "Fichier supprimé - <nom_fichier>" si `/S` est utilisé.
*   Le `ERRORLEVEL` est `0`.

**Conditions d'échec** :
*   "Impossible de trouver <nom_fichier>" : Si le fichier spécifié n'existe pas.
*   "Accès refusé." : Si vous n'avez pas les permissions nécessaires pour supprimer le fichier, ou si le fichier est utilisé par un autre processus et que `/F` n'est pas suffisant.
*   "Le processus ne peut pas accéder au fichier car il est utilisé par un autre processus." : Si le fichier est verrouillé par une autre application.
*   `del` supprimera les fichiers à l'intérieur d'un répertoire si un nom de répertoire est donné, mais il ne supprimera pas le répertoire lui-même. Pour supprimer des répertoires, utilisez `rmdir`.
*   Le `ERRORLEVEL` est non nul.

### Pour en savoir plus
Pour des informations plus détaillées, consultez la documentation officielle de `cmd`.

