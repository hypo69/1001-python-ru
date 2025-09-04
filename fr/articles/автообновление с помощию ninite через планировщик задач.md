Vous avez tout à fait raison. Merci pour la clarification. L'utilisation des guillemets «ёлочки» est standard pour la typographie russe.

Voici la version corrigée de l'article avec les guillemets corrects :

***

### Comment mettre à jour automatiquement les programmes à l'aide de Ninite et du Planificateur de tâches Windows

Maintenir les logiciels à jour est essentiel pour la sécurité et la stabilité de votre système. Cependant, la vérification et l'installation manuelles des mises à jour pour chaque application peuvent prendre beaucoup de temps. Dans cet article, nous verrons comment automatiser ce processus à l'aide du service Ninite.com et du Planificateur de tâches Windows intégré.

### Partie 1 : Familiarisation avec Ninite et création d'un installateur

Ninite est un service conçu pour l'installation et la mise à jour simultanées de plusieurs applications populaires. Il vise à vous faire gagner du temps en éliminant le besoin d'installer manuellement chaque programme, de parcourir les assistants d'installation et de refuser les offres d'installation de barres d'outils ou d'autres logiciels indésirables.

**Principales caractéristiques et avantages de Ninite :**

*   **Installation sans actions inutiles :** Vous n'avez pas besoin de cliquer sur «suivant» ou de refuser les barres d'outils et les éléments indésirables supplémentaires. Il suffit de sélectionner les applications souhaitées et d'exécuter l'installateur.
*   **Versions toujours à jour :** Ninite utilise des robots pour suivre les mises à jour, vous obtenez donc toujours les dernières versions stables des applications.
*   **Automatisation du processus :** Ninite fonctionne en arrière-plan, installant les applications dans des emplacements standard et dans la langue de votre système. Il ignore les applications déjà mises à jour et les demandes de redémarrage des installateurs.
*   **Sécurité :** Les applications sont téléchargées directement depuis les sites officiels des éditeurs, et leurs signatures numériques ou leurs hachages sont vérifiés avant le lancement pour garantir l'authenticité.
*   **Prise en charge du système :** Ninite fonctionne sur Windows 11, 10, 8.x, 7 et les versions de serveur équivalentes.
*   **Gratuit pour un usage domestique :** Le site est gratuit pour l'usage personnel (sans publicité ni logiciels indésirables). La version payante de Ninite Pro offre des fonctionnalités étendues pour la gestion des logiciels dans les organisations.

**Sections d'applications (catégories) parmi lesquelles vous pouvez choisir :**

Ninite propose un large éventail de programmes, regroupés par catégories :

*   **Navigateurs Web (Web Browsers) :** Chrome, Opera, Firefox, Edge, Brave.
*   **Messagerie (Messaging) :** Zoom, Discord, Teams, Pidgin, Thunderbird.
*   **Multimédia (Media) :** iTunes, VLC, AIMP, foobar2000, Audacity, K-Lite Codecs, Spotify, HandBrake.
*   **Imagerie (Imaging) :** Krita, Blender, Paint.NET, GIMP, IrfanView, Inkscape, Greenshot, ShareX.
*   **Documents :** Foxit Reader, LibreOffice, SumatraPDF, OpenOffice.
*   **Sécurité (Security) :** Malwarebytes, Avast, AVG, Avira.
*   **Stockage en ligne (Online Storage) :** Dropbox, Google Drive, OneDrive.
*   **Utilitaires (Utilities) :** TeamViewer, ImgBurn, TeraCopy, Revo, WinDirStat, CCleaner.
*   **Compression :** 7-Zip, PeaZip, WinRAR.
*   **Outils de développement (Developer Tools) :** Python, Git, FileZilla, Notepad++, WinSCP, PuTTY, Visual Studio Code.
*   **Et bien plus encore :** y compris .NET, Java, utilitaires et autres outils utiles.

**Comment sélectionner et télécharger le fichier d'installation :**

1.  **Sélectionnez les applications :** Sur la page principale de ninite.com, vous verrez une liste de catégories avec des applications. Cochez les cases des programmes que vous souhaitez installer ou maintenir à jour.
2.  **Téléchargez l'installateur :** Après avoir sélectionné les applications, cliquez sur le bouton **«Get Your Ninite»**. Le site générera et vous proposera de télécharger un fichier exécutable personnel. Ce petit fichier est votre installateur/metteur à jour universel.

### Partie 2 : Configuration des mises à jour automatiques

Maintenant que vous avez un installateur Ninite configuré, voyons où il est préférable de le placer et comment configurer le lancement automatique.

**Où placer le fichier Ninite**

Pour que le système puisse trouver et exécuter votre fichier Ninite sans problème, il est recommandé de créer un dossier séparé pour celui-ci. Cela évitera la suppression ou le déplacement accidentel du fichier.

**Recommandations de placement :**

*   **Évitez les dossiers système :** Ne sauvegardez pas le fichier à la racine du lecteur `C:` ou dans le dossier `C:\Windows`.
*   **Créez un dossier dédié :** Une bonne pratique serait de créer un dossier, par exemple, `C:\NiniteUpdater`. Cela simplifiera la gestion du fichier et sa recherche future.

Déplacez le fichier Ninite téléchargé depuis le site (par exemple, `Ninite-bundle-logiciels.exe`) vers le dossier que vous avez créé précédemment (`C:\NiniteUpdater`).

**Configuration du lancement automatique via le Planificateur de tâches Windows**

Pour que la vérification et la mise à jour des programmes se produisent automatiquement chaque dimanche, nous utiliserons l'outil intégré de Windows — le **Planificateur de tâches**.

**1. Ouverture du Planificateur de tâches :**

*   Appuyez sur les touches `Win + R`, tapez `taskschd.msc` et appuyez sur Entrée.

**2. Création d'une nouvelle tâche :**

Dans la fenêtre du Planificateur de tâches, dans le volet droit «Actions», sélectionnez **«Créer une tâche de base...»**.

*   **Nom et description :** Entrez un nom clair pour votre tâche, par exemple, «Mise à jour hebdomadaire de Ninite». Cliquez sur «Suivant».
*   **Déclencheur (heure de lancement) :** À cette étape, vous devez spécifier la fréquence d'exécution de la tâche.
    *   Sélectionnez «Hebdomadaire» et cliquez sur «Suivant».
    *   Spécifiez le jour de la semaine — «dimanche». Vous pouvez également choisir une heure de lancement qui vous convient, par exemple, lorsque l'ordinateur est généralement allumé mais n'est pas utilisé activement. Cliquez sur «Suivant».
*   **Action :** Ici, nous spécifierons le programme à exécuter.
    *   Sélectionnez «Démarrer un programme» et cliquez sur «Suivant».
    *   Dans le champ «Programme ou script», cliquez sur le bouton «Parcourir...» et trouvez votre fichier Ninite dans le dossier que vous avez créé précédemment (`C:\NiniteUpdater\Ninite-bundle-logiciels.exe`).
    *   Cliquez sur «Suivant».
*   **Achèvement :** À la dernière étape, vérifiez tous les paramètres spécifiés. Si tout est correct, cliquez sur «Terminer».

Maintenant, le Planificateur de tâches exécutera automatiquement votre fichier Ninite chaque dimanche à l'heure que vous avez spécifiée. Lorsque Ninite s'exécutera en arrière-plan, il vérifiera les versions des programmes que vous avez sélectionnés et, s'il trouve des mises à jour, il les téléchargera et les installera sans votre intervention. Ainsi, vous obtenez un système simple et fiable pour maintenir votre logiciel à jour.
