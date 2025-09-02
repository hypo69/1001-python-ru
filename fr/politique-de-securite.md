<table>
<tr>
<TD>
<A HREF = 'https://github.com/hypo69/hypotez/blob/master/README.MD'>[Racine ↑]</A>
</TD>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/src/README.MD'>Code</a>
</td>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/docs/gemini/out/README.MD'>Documentation</a> 
</td>
<td>
<a href='https://github.com/hypo69/hypotez/blob/master/README.RU.MD'>Русский</a>
</td>
</tr>
</table>

Stockage des paramètres de l'application
=======================================

### 1. Stockage des mots de passe et des informations d'identification dans KeePass

Pour stocker en toute sécurité les informations d'identification telles que les mots de passe et les clés API, utilisez KeePass. Suivez ces étapes:

1.  **Créer une base de données KeePass**:
    -   Ouvrez KeePass et créez une nouvelle base de données en sélectionnant **Fichier > Nouvelle base de données**.
    -   Définissez un mot de passe principal fort pour protéger la base de données.
    -   **Emplacement**: Enregistrez le fichier de la base de données KeePass (`credentials.kdbx`) dans le dossier `secrets` de votre projet:
        ```
        racine
        ├── données
        ├── secrets
        │   └── credentials.kdbx  # <-- Fichier de la base de données KeePass
        │   └── passowrd.txt
        │   └── <googke api josn kes>.json
        ├── src
        └── ...

        - Ne partagez jamais le fichier `credentials.kdbx` avec d'autres. ❗
        - Assurez-vous que le fichier est stocké dans un emplacement sécurisé accessible uniquement à vous. (Le dossier `secrets` à la racine du projet est exclu de `git`).
        - Mettez régulièrement à jour vos clés API et vos mots de passe de base de données.     ```

2.  **Créer des groupes et des entrées**:
    -   Votre base de données doit contenir plusieurs groupes pour organiser les informations d'identification. Par exemple:
        -   **fournisseurs**
            -   **aliexpress**
                -   Entrée pour l'API contenant:
                    -   `api_key`: Votre clé API Aliexpress.
                    -   `secret`: Votre clé secrète Aliexpress.
                    -   `tracking_id`: ID de suivi.
                    -   `email`: Votre adresse e-mail.
                    -   `password`: Votre mot de passe Aliexpress.
            -   **openai**
                -   Entrée pour l'API OpenAI contenant:
                    -   `api_key`: Votre clé API OpenAI.
            -   **discord**
                -   Entrée pour l'API Discord contenant:
                    -   `application_id`: ID de l'application Discord.
                    -   `public_key`: Clé publique.
                    -   `bot_token`: Jeton du bot.
            -   **prestashop** et d'autres services avec les entrées correspondantes.

3.  **Ajouter des propriétés personnalisées**:
    -   Lors de la création d'entrées, ajoutez des propriétés personnalisées pour stocker des données supplémentaires. Par exemple, dans l'entrée Aliexpress, ajoutez des champs pour:
        -   `tracking_id`
        -   `username`
        -   `email`

### 2. Configuration du fichier `settings.json`

Le fichier `settings.json` stocke les principaux paramètres de votre projet. Voici comment le configurer:

1.  **Créer le fichier `settings.json`**:
    -   Créez un fichier nommé `settings.json` dans le répertoire `/src` de votre projet.

2.  **Exemple de contenu du fichier `settings.json`**:
    ```json
    {
      "google_drive": "H:\\Mon Drive\\hypo69",  // Chemin vers le dossier Google Drive utilisé pour stocker les données.
      "mode": "debug",                          // Mode de l'application: 'debug' pour le développement ou 'production' pour le mode live.
      "git_user": "hypo69",                    // Nom d'utilisateur pour accéder au référentiel Git.
      "git": "hypo"                             // Nom du référentiel Git.
    }
    ```

3.  **Description des champs**:
    -   **google_drive**: Le chemin d'accès au répertoire de votre Google Drive où les données du projet seront stockées. Assurez-vous que ce chemin est correct pour votre système.
    -   **mode**: Spécifiez le mode de votre application. Utilisez `debug` pour les tests et `production` pour le déploiement.
    -   **git_user**: Votre nom d'utilisateur sur GitHub ou une autre plateforme où votre référentiel est hébergé.
    -   **git**: Le nom de votre référentiel qui est utilisé pour suivre les modifications du code.

### 3. Protection des informations sensibles

-   **Données sensibles**: Le fichier contenant vos clés API et vos mots de passe est stocké dans le dossier `secrets`, qui n'est **pas inclus dans le référentiel Git** pour empêcher tout accès non autorisé. Tous les mots de passe et clés API doivent être chargés depuis KeePass au démarrage du programme, comme décrit dans le code.
-   **Sauvegarde**: Sauvegardez régulièrement votre base de données KeePass et votre fichier `settings.json` pour éviter la perte de données.

## Signaler une vulnérabilité

Si vous trouvez une vulnérabilité de sécurité dans notre projet, veuillez la signaler en suivant ces étapes:

1.  **E-mail**: Envoyez un e-mail à [security@example.com] avec une description de la vulnérabilité.
2.  **Informations à inclure**:
    -   Une description détaillée du problème
    -   Étapes pour reproduire la vulnérabilité
    -   Version(s) affectée(s)
    -   Toute autre information pertinente

3.  **Délai de réponse**: Vous pouvez vous attendre à recevoir un accusé de réception dans les 48 heures. Nous nous efforçons de fournir des mises à jour sur l'état de la vulnérabilité signalée chaque semaine jusqu'à sa résolution.

4.  **Résultat**: Si la vulnérabilité est confirmée, nous travaillerons sur un correctif et vous informerons lorsqu'il sera disponible. Si nous déterminons que le rapport n'est pas une vulnérabilité, nous vous informerons de notre décision.

## Versions prises en charge

| Version | Prise en charge    |
| ------- | ------------------ |
| 5.1.x   | :white_check_mark: |
| 5.0.x   | :x:                |
| 4.0.x   | :white_check_mark: |
| < 4.0   | :x:                |

Merci de nous aider à maintenir notre projet en sécurité!

---