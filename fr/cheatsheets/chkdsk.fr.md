### Comment vérifier et corriger les erreurs de disque dur sous Windows : aide-mémoire CHKDSK et PowerShell

Avec le temps, des erreurs logiques peuvent s'accumuler sur un disque dur ou un SSD, et des secteurs endommagés peuvent apparaître, entraînant un ralentissement du système, des plantages de programmes et même une perte de données. Heureusement, Windows dispose d'outils intégrés pour diagnostiquer et corriger ces problèmes.

Dans cet aide-mémoire, je vais vous montrer deux façons de contrôler l'état des disques : l'utilitaire `chkdsk` et les commandes PowerShell.

### Partie 1 : Utilitaire CHKDSK

**CHKDSK** (Check Disk) — est un utilitaire de ligne de commande standard qui vérifie le système de fichiers d'un volume à la recherche d'erreurs logiques et physiques.

#### Comment exécuter CHKDSK

Pour exécuter des commandes qui modifient le système, vous aurez besoin des droits d'administrateur.

1.  Appuyez sur `Win + S` ou sur le bouton « Démarrer ».
2.  Tapez `cmd` ou « Invite de commandes ».
3.  Dans les résultats de la recherche, cliquez avec le bouton droit sur « Invite de commandes » et sélectionnez **« Exécuter en tant qu'administrateur »**.

#### Paramètres principaux (commutateurs) de CHKDSK

La commande a la syntaxe suivante : `chkdsk [lecteur :] [paramètres]`

Paramètres fréquemment utilisés :

*   `chkdsk C:`
    Lance la vérification du lecteur C: en mode « lecture seule ». L'utilitaire signalera les erreurs trouvées mais ne les corrigera pas.

*   **/f**
    Corrige les erreurs sur le disque. S'il y a des fichiers ouverts sur le disque (ce qui est presque toujours le cas pour le disque système), l'utilitaire proposera d'effectuer la vérification au prochain redémarrage du système.
    *Exemple :* `chkdsk D: /f`

*   **/r**
    Recherche les secteurs défectueux (bad sectors) et tente de récupérer les informations lisibles. Ce commutateur **inclut la fonctionnalité du commutateur `/f`**, il n'est donc pas strictement nécessaire de les utiliser ensemble, bien que ce ne soit pas une erreur. Une vérification avec `/r` prend beaucoup plus de temps.
    *Exemple :* `chkdsk D: /r`

*   **/x**
    Démonte de force le volume avant la vérification, si nécessaire. Tous les descripteurs ouverts pour ce disque deviendront invalides. Ce commutateur **inclut également la fonctionnalité de `/f`**.
    *Exemple :* `chkdsk D: /x`

*   **/b** (pour le système de fichiers NTFS uniquement)
    Effectue une réévaluation des clusters défectueux sur le disque. Ce commutateur est le plus complet, car il **inclut la fonctionnalité de `/r`**.
    *Exemple :* `chkdsk C: /b`

*   **/scan** (pour NTFS uniquement)
    Lance une analyse en ligne du volume. Cela signifie que le disque n'a pas besoin d'être démonté et que vous pouvez continuer à travailler sur le système pendant l'analyse. Cependant, la correction des problèmes trouvés nécessitera le commutateur suivant ou un redémarrage.
    *Exemple :* `chkdsk C: /scan`

*   **/spotfix** (pour NTFS uniquement)
    Effectue une correction ponctuelle et très rapide des erreurs sur le volume. Nécessite le démontage du disque, tout comme le commutateur `/f`.
    *Exemple :* `chkdsk D: /spotfix`

#### Exemples d'exécution de CHKDSK

*   **Vérification rapide du lecteur D: sans correction :**
    ```
    chkdsk D:
    ```

*   **Vérification et correction des erreurs sur le lecteur D :**
    ```
    chkdsk D: /f
    ```

*   **Vérification la plus complète du disque système C: avec détection et récupération des secteurs défectueux :**
    ```
    chkdsk C: /f /r
    ```
    *ou simplement :*
    ```
    chkdsk C: /r
    ```

#### Que faire si le disque est utilisé ?

Lorsque vous tentez d'exécuter une vérification avec correction (`/f` ou `/r`) pour le disque système (généralement `C:`), vous verrez un message :

`Impossible d'exécuter la commande CHKDSK car le volume spécifié est utilisé par un autre processus. Voulez-vous planifier la vérification de ce volume au prochain redémarrage du système ? (O/N)`

Appuyez sur la touche `O`, puis sur `Entrée`. La vérification sera planifiée et démarrera automatiquement au prochain redémarrage de l'ordinateur.

---

### Partie 2 : Commandes PowerShell

PowerShell — est un shell d'automatisation qui offre des commandes modernes et flexibles pour la gestion du système.

#### Comment exécuter PowerShell

Comme pour l'invite de commandes, vous aurez besoin des droits d'administrateur.

1.  Appuyez sur `Win + S` ou sur le bouton « Démarrer ».
2.  Tapez `powershell`.
3.  Dans les résultats de la recherche, cliquez avec le bouton droit sur « Windows PowerShell » et sélectionnez **« Exécuter en tant qu'administrateur »**.

#### Commande principale : `Repair-Volume`

Dans PowerShell, l'applet de commande `Repair-Volume` est utilisée pour vérifier et corriger les disques.

Il peut être utile de commencer par afficher la liste de tous les volumes du système à l'aide de la commande :
```powershell
Get-Volume
```

#### Paramètres principaux de `Repair-Volume`

*   `-DriveLetter`
    Spécifie la lettre du lecteur à vérifier.

*   `-Scan`
    Analyse le volume à la recherche d'erreurs et les signale. C'est l'analogue de `chkdsk` sans commutateurs.
    *Exemple :* `Repair-Volume -DriveLetter D -Scan`

*   `-SpotFix`
    Effectue une correction rapide en ligne sans qu'il soit nécessaire de démonter le volume pendant une longue période. Analogue à `chkdsk /spotfix`.
    *Exemple :* `Repair-Volume -DriveLetter D -SpotFix`

*   `-OfflineScanAndFix`
    Effectue une vérification et une correction complètes du disque hors ligne. C'est l'analogue le plus complet de la commande `chkdsk /f /r`. Le système demandera un redémarrage si le volume est utilisé.
    *Exemple :* `Repair-Volume -DriveLetter C -OfflineScanAndFix`

#### Exemples PowerShell

*   **Analyser le lecteur C: à la recherche d'erreurs (sans correction) :**
    ```powershell
    Repair-Volume -DriveLetter C -Scan
    ```
    Vous verrez le résultat dans le champ `HealthStatus` (par exemple, `Healthy` ou `Needs-Repair`).

*   **Effectuer une correction rapide pour le lecteur D :**
    ```powershell
    Repair-Volume -DriveLetter D -SpotFix
    ```

*   **Planifier une vérification et une correction complètes du disque système C: au prochain redémarrage :**
    ```powershell
    Repair-Volume -DriveLetter C -OfflineScanAndFix
    ```
    PowerShell, comme `chkdsk`, vous informera de la nécessité d'un redémarrage et planifiera la tâche.


Pour la plupart des utilisateurs, le résultat de `chkdsk C: /r` et `Repair-Volume -DriveLetter C -OfflineScanAndFix` sera le même. Le choix dépend de vos préférences et de vos tâches.

**Remarque importante :** Avant d'effectuer toute opération sérieuse sur le disque, surtout si vous soupçonnez des problèmes physiques, **sauvegardez toujours les données importantes !** Les outils peuvent corriger les erreurs, mais ils ne peuvent pas garantir à 100 % l'intégrité des informations sur un support endommagé.