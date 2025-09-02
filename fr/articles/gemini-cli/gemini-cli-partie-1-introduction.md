## Gemini CLI : Introduction et premiers pas.

**Gemini CLI** est un outil qui fonctionne directement dans votre terminal, comprend votre base de code et vous aide à corriger les erreurs avec des requêtes en langage naturel. C'est la réponse de Google au Claude Code d'Anthropic.
Vous pouvez utiliser Gemini 1.5 Pro (lorsque vous atteignez la limite, l'outil passera à Gemini 1.5 Flash) et sa fenêtre de contexte de 1 million de jetons pour effectuer jusqu'à 60 requêtes par minute et 1000 requêtes par jour, le tout gratuitement.

### Contenu
*   Comprendre et naviguer dans de grandes bases de code
*   Détecter et corriger les erreurs
*   Écrire et tester du code
*   Outils Gemini CLI
*   Intégration de Google CLI avec MCP

### Principales fonctionnalités de Gemini CLI :
*   **Édition et refactoring :** Améliore et simplifie automatiquement votre code sous la direction de l'IA.
*   **Détection et correction d'erreurs :** Trouve les bogues et suggère des correctifs.
*   **Compréhension du code :** Gemini CLI peut résumer l'architecture, expliquer les rôles des modules ou créer des organigrammes d'exécution.
*   **Génération de tests :** Crée automatiquement des cas de test pour `pytest`
*   **Prise en charge de la documentation :** Vous pouvez créer des documents markdown structurés, des journaux de modifications et des réponses aux problèmes GitHub directement dans le terminal.
*   **Exécution de commandes :** Gemini CLI peut exécuter des commandes shell telles que `git`, `npm`, `pip` et autres, vous permettant de gérer des projets sans quitter le CLI.

---

### Étape 1 : Prérequis

Pour commencer, installez Node.js (version 18 ou supérieure). Vous pouvez télécharger le programme d'installation de votre choix ou exécuter les commandes bash suivantes dans votre terminal :

```bash
# Télécharger et installer nvm (Node Version Manager) :
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# Initialiser nvm dans la session de terminal actuelle
. "$HOME/.nvm/nvm.sh"

# Télécharger et installer Node.js (par exemple, la version 22) :
nvm install 22

# Vérifier la version de Node.js :
node -v # Devrait afficher "v22.17.0" ou similaire

# Vérifier la version de npm :
npm -v # Devrait afficher "10.9.2" ou similaire
```

> ⚠️ **Important pour les utilisateurs de Windows :**
> La commande `nvm` ci-dessus est pour **Linux/macOS** et **ne fonctionnera pas dans PowerShell ou cmd.exe**.
> Pour Windows, utilisez [nvm-windows](https://github.com/coreybutler/nvm-windows) en téléchargeant `nvm-setup.exe` depuis la section [Releases](https://github.com/coreybutler/nvm-windows/releases).
> Alternativement, vous pouvez installer WSL (Windows Subsystem for Linux) et exécuter les commandes dans Ubuntu ou une autre distribution Linux.

---
### Étape 2 : Configuration de Gemini CLI

#### Étape 2.1 : Installation de Gemini CLI
Une fois Node.js et npm installés et vérifiés, installez Gemini CLI en exécutant la commande suivante dans votre terminal :
```bash
npx https://github.com/google-gemini/gemini-cli
```
Ou utilisez `npm` pour l'installer globalement :
```bash
npm install -g @google/gemini-cli
gemini
```
Après l'installation, tapez `gemini` dans le terminal pour accéder à l'outil.

#### Étape 2.2 : Authentification
Vous pouvez utiliser votre compte Google personnel pour vous authentifier. Cela vous donnera jusqu'à 60 requêtes par minute et 1000 requêtes par jour lors de l'utilisation de Gemini.
![First Run](assets/gemini_cli_1/auth.png)

Dans ce guide, j'ai utilisé **Se connecter avec Google**, mais vous pouvez également utiliser une **clé API** (définie comme variable d'environnement ou dans un fichier `.env`) ou vous authentifier via **Vertex AI**.

Pour générer une nouvelle clé API, connectez-vous à **AI Studio** avec votre compte Google et cliquez sur "Créer une clé API".
```bash
# Définir la clé comme variable d'environnement
export GEMINI_API_KEY="Your_API_Key"

# Ou créer un fichier .env
GEMINI_API_KEY="Your_API_Key"
```
Vous pouvez utiliser la commande `/auth` dans la zone de texte pour changer de méthode d'authentification si nécessaire.

---

### Étape 3 : Configuration d'un projet dans Gemini CLI
![Start](assets/gemini_cli_1/start.png)
Une fois le CLI en cours d'exécution, nous pouvons commencer à interagir avec Gemini depuis le terminal. Il y a deux façons de travailler avec un projet.

#### 1. Démarrer un nouveau projet
Pour démarrer un projet à partir de zéro, exécutez les commandes suivantes :
```bash
cd new-project/
gemini
```
À l'intérieur du CLI, utilisez une invite pour résoudre le problème qui vous intéresse, par exemple :
> Écrivez le code de l'encodeur pour un transformateur à partir de zéro.
![Example 1](assets/gemini_cli_1/example_1.png)
Donnez la permission d'écrire des fichiers :
![File](assets/gemini_cli/file.png)

#### 2. Travailler avec un projet existant
Si vous avez déjà une base de code, vous pouvez travailler avec elle en exécutant les commandes suivantes :
```bash
git clone https://github.com/AashiDutt/Google-Agent-Development-Kit-Demo
cd Google-Agent-Development-Kit-Demo
gemini
```
À l'intérieur du CLI, utilisez une invite, par exemple :
> Fournissez-moi un résumé de toutes les modifications apportées à la base de code au cours du dernier mois.

---

### Étape 4 : Expérimentation avec Gemini CLI
À titre d'exemple, j'utiliserai le projet **[Planificateur de voyage 🌍🛫 basé sur ADK](https://github.com/AashiDutt/Google-Agent-Development-Kit-Demo)**.
Avec Gemini CLI, je vais vous montrer comment :
1.  explorer la base de code
2.  détecter un bogue ou un problème sur GitHub ou dans un fichier
3.  refactoriser le code et générer des tests unitaires
4.  créer un rapport markdown des modifications apportées
5.  visualiser la base de code en générant un organigramme

#### Exploration et compréhension de la base de code
Commençons par demander à Gemini d'explorer et d'expliquer la base de code.

**Invite :** `Explorez le répertoire actuel et décrivez l'architecture du projet.`

Gemini CLI renverra un résumé structuré expliquant l'architecture :
*   **Interface utilisateur :** Une application Streamlit (`travel_ui.py`) fournit une interface pour l'interaction.
*   **Orchestration :** `host_agent` agit comme un coordinateur central.
*   **Agents spécialisés :** `flight_agent`, `stay_agent`, `activities_agent` pour la recherche de vols, d'hôtels et de divertissements.
*   **Communication :** Les agents communiquent entre eux via une API RESTful sur FastAPI.
*   **Composants partagés :** `shared/schemas.py` définit des structures de données communes.

Cela vous aidera à vous repérer sans lire chaque fichier manuellement.

#### Analyse et résolution d'un problème GitHub
Explorons quelques problèmes ouverts du référentiel GitHub.

**Invite :** `Voici un problème GitHub : [@search https://github.com/AashiDutt/Google-Agent-Development-Kit-Demo/issues/1]. Analysez la base de code et proposez un plan de correction en 3 étapes. Quels fichiers/fonctions doivent être modifiés ?`

Gemini CLI a enquêté sur le problème :
*   En utilisant la fonction `@search`, il a récupéré des données de GitHub.
*   A identifié la cause première comme une erreur de sérialisation JSON (dans ce cas, la fonction asynchrone `create_session()` n'a pas été appelée avec `await`).
*   A suggéré des modifications et une gestion des réponses dans plusieurs fichiers.

Ensuite, le CLI attend une entrée de l'utilisateur pour évaluer les modifications. Si l'utilisateur est d'accord, il appliquera les modifications suggérées.

#### Implémentation et test du correctif
Implémentons et testons maintenant les correctifs suggérés par Gemini.

**Invite :** `Écrivez un test unitaire pour cette modification dans pytest dans le fichier test_shared.py.`

Gemini CLI :
*   A inséré `json.dumps()` avant d'envoyer la charge utile de la tâche.
*   A créé `test_agents.py` pour ajouter des tests unitaires.
*   A ajouté un nouveau cas de test pour vérifier le schéma et le transfert des messages d'agent imbriqués.

#### Génération de la documentation
Maintenant que les correctifs ont été apportés, résumons les modifications et écrivons-les en Markdown dans un fichier `.txt`.

**Invite :** `Rédigez un résumé markdown du bogue, du correctif et de la couverture des tests. Formatez-le comme une entrée de journal des modifications sous la version "v0.2.0".`

Ensuite, pour enregistrer le résumé dans un document, j'ai utilisé l'invite suivante :

**Invite :** `Enregistrez ce résumé dans un fichier .txt et nommez-le summary.txt`

Gemini CLI utilise l'outil `WriteFile` pour enregistrer le fichier `summary.txt` dans le répertoire du projet.

#### Génération d'un organigramme à l'aide de MCP
Cette section développe les expériences précédentes où j'explore comment Gemini CLI utilise le **Protocole de contexte de modèle (MCP)** pour maintenir des résumés au niveau des fichiers et un historique des tâches entre les invites. Cela donne à Gemini une "mémoire de travail" au sein d'une session.

**Invite :** `Générez un organigramme qui montre comment les agents communiquent via A2A (agent à agent) et comment main.py gère le système. Mettez en surbrillance l'endroit où le problème s'est produit et comment il a été résolu.`

Cette visualisation a été rendue possible par la mémoire persistante de Gemini, qui a conservé le contexte complet de notre correctif de bogue précédent et de la structure de l'agent sans avoir à recharger les fichiers.

### Outils Gemini CLI disponibles
L'appel de la commande `/tools` dans Gemini CLI affichera une liste des outils disponibles qui peuvent être utilisés pour effectuer diverses tâches, telles que la modification de code, la génération de tests, la création de documentation, et bien plus encore.
![Tools](assets/gemini_cli_1/tools.png)

**ReadFolder (ls)**
Liste les fichiers et les dossiers d'un répertoire - analogue à la commande `ls` en ligne de commande.

**ReadFile (read-file)**
Lit le contenu complet d'un seul fichier, ce qui est utile pour créer des résumés ou des analyses.

**ReadManyFiles (read-many-files)**
Lit plusieurs fichiers à la fois, généralement par un modèle (par exemple, tous les fichiers `.js`).

**FindFiles (glob)**
Recherche des fichiers par un modèle (par exemple, trouver tous les fichiers `config.json` dans votre projet).

**SearchText (grep)**
Recherche du texte dans les fichiers, par exemple, pour trouver tous les commentaires `TODO`.

**Edit (edit)**
Applique les modifications de code à l'aide d'un `diff`. Gemini affiche un aperçu des modifications et demande une confirmation avant de les appliquer.

**WriteFile (write-file)**
Crée de nouveaux fichiers (par exemple, `README.md`) avec le contenu fourni par l'utilisateur.

**Shell (shell)**
Exécute des commandes directement dans le terminal si vous les préfixez avec `!` (par exemple, `!npm test`).

**WebFetch (web-fetch)**
Télécharge du contenu depuis le Web (HTML ou JSON), permettant à Gemini d'analyser des données externes.

**GoogleSearch (web-search)**
Effectue une recherche Google pour baser les réponses sur des informations réelles (par exemple, pour trouver une explication à une erreur).

**Save Memory (memoryTool)**
Enregistre des faits ou des préférences pendant une session (par exemple, "je préfère async/await") pour améliorer la cohérence et la cohésion des réponses.

### Fonctionnalités avancées

Vous pouvez ajouter des instructions spéciales pour l'IA pour un projet spécifique en
créant un fichier `GEMINI.md` dans le répertoire racine de votre projet.
À l'intérieur de ce fichier, vous pouvez définir les règles du projet,
les styles de code et les outils que l'agent doit utiliser. Cela garantit que le code généré respecte les normes de votre projet.

[Exemple d'instruction système](https://github.com/hypo69/hypotez/blob/master/src/endpoints/hypo69/code_assistant/instructions/CODE_RULES.EN.MD)

### Intégration de Google CLI avec MCP

Pour la plupart des tâches quotidiennes, les outils intégrés seront suffisants. Mais que se passe-t-il si vous voulez que Gemini CLI fasse quelque chose de très spécialisé, comme interagir avec des API spécifiques ou utiliser un modèle spécialisé (disons, un générateur d'images ou un outil d'analyse de sécurité) ? C'est là que MCP (Model Context Protocol) entre en jeu.

En substance, MCP est une norme ouverte qui permet aux développeurs d'ajouter de nouveaux outils et de nouvelles fonctionnalités à l'IA en exécutant un serveur avec lequel le CLI peut interagir. Dans Gemini CLI, vous pouvez configurer des "serveurs MCP" dans un fichier de paramètres JSON, et le CLI les traitera comme des outils supplémentaires qu'il peut utiliser.

#### Comment configurer un serveur MCP dans Google CLI

À titre d'exemple, je vais vous montrer comment configurer un serveur MCP pour GitHub dans Gemini CLI.

À l'intérieur de votre dossier de projet, créez un dossier à l'aide de la commande :

```bash
mkdir -p .gemini && touch .gemini/settings.json
```
Remplissez le fichier avec ce code :
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "[YOUR-TOKEN]" }
    }
  }
}
```
[instructions sur la façon d'obtenir un jeton](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic)
Après cela, tapez `/quit` dans Gemini CLI pour quitter, puis ouvrez-le à nouveau.
Vous verrez que le serveur MCP GitHub est en cours d'exécution et prêt à être utilisé.
![MCP](assets/gemini_cli_1/mcp.png)
Entrez la commande `/mcp`, et vous verrez une liste d'outils GitHub.
![Mcp Commands](assets/gemini_cli_1/mcp_commands.png)