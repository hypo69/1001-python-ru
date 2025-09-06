### **Cycle "PAS Selenium". Introduction**

Ceux qui s'occupent du web scraping, des tests et de l'automatisation connaissent Selenium, le plus moderne Playwright et/ou le framework Crawlee. Ils sont puissants, ils peuvent presque tout faire, et ils... ne sont pas toujours nécessaires. De plus, dans de nombreux cas, utiliser ces outils, c'est comme enfoncer des clous avec un microscope : le travail sera certes fait, mais au prix de dépenses injustifiées – vitesse, ressources système et complexité de configuration.

Bienvenue dans le cycle d'articles "PAS Selenium". Ici, je vous montrerai d'autres façons (pas toujours évidentes) d'interagir avec le contenu d'Internet.

#### Paradigme n°1 : Communication directe. Clients HTTP

*   **`Requests`** — Forme et envoie une requête réseau à l'adresse cible (URL), exactement comme le fait votre navigateur au tout premier moment du chargement de la page, mais sans le navigateur lui-même. Dans cette requête, il emballe la méthode (par exemple, `GET` pour obtenir des données), les en-têtes (`Headers`) qui se présentent au site (par exemple, `User-Agent: "je-suis-un-navigateur"`), et d'autres paramètres. En réponse du serveur, il reçoit des données brutes — le plus souvent, c'est le code HTML original de la page ou une chaîne au format JSON, ainsi qu'un code de statut (par exemple, `200 OK`).

*   **`HTTPX`** — est un successeur moderne de `Requests`. Fondamentalement, il fait la même chose : envoie les mêmes requêtes HTTP avec les mêmes en-têtes et reçoit les mêmes réponses. Mais il y a une différence clé : `Requests` fonctionne **de manière synchrone** — il envoie une requête, attend la réponse, reçoit la réponse, envoie la suivante. `HTTPX`, en revanche, peut fonctionner **de manière asynchrone** — il peut "lancer" une centaine de requêtes à la fois sans attendre les réponses, puis les traiter efficacement au fur et à mesure qu'elles arrivent.

Ils sont excellents pour collecter des données sur des sites statiques, travailler avec des API, analyser des milliers de pages où l'exécution de JavaScript n'est pas requise.

*   **Avantages :** **Vitesse et efficacité.** Grâce à la nature asynchrone de `HTTPX`, là où `Requests` ferait séquentiellement 100 requêtes pendant plusieurs minutes, `HTTPX` s'en chargera en quelques secondes.
*   **Inconvénients :** Ne conviennent pas aux sites où le contenu est généré à l'aide de JavaScript.

#### Paradigme n°2 : Protocole Chrome DevTools (CDP)

Que faire si le site est dynamique et que le contenu est généré à l'aide de JavaScript ? Les navigateurs modernes (Chrome, Chromium, Edge) disposent d'un protocole intégré pour le débogage et le contrôle — **Chrome DevTools Protocol (CDP)**. Il permet d'envoyer des commandes directement au navigateur, en contournant la couche lourde de WebDriver utilisée par Selenium.

*   **Outils :** Le principal représentant de cette approche aujourd'hui est `Pydoll`, qui a remplacé le `pyppeteer`, autrefois populaire mais désormais non pris en charge.
*   **Quand l'utiliser :** Lorsque le rendu JavaScript est nécessaire, mais que l'on souhaite maintenir une vitesse élevée et éviter les complexités liées aux pilotes.
*   **Avantages :** **Équilibre.** Vous obtenez la puissance d'un vrai navigateur, mais avec des frais généraux beaucoup plus faibles et souvent avec des mécanismes intégrés de contournement des protections.
*   **Inconvénients :** Peut être plus difficile à déboguer que Playwright et nécessite une compréhension plus approfondie du fonctionnement du navigateur.

#### Paradigme n°3 : Agents LLM autonomes

C'est la pointe de la technologie. Et si, au lieu d'écrire du code qui dit "clique ici, tape ça", nous donnions simplement une tâche en langage naturel ? "Trouve-moi tous les fournisseurs sur ce site et collecte leurs catégories de produits".

C'est exactement le problème que résolvent les agents LLM. En utilisant un "cerveau" sous la forme d'un grand modèle linguistique (GPT, Gemini) et des "mains" sous la forme d'un ensemble d'outils (navigateur, recherche Google), ces agents peuvent planifier et exécuter de manière autonome des tâches complexes sur le web.

*   **Outils :** Des ensembles comme `LangChain` + `Pydoll` ou des solutions personnalisées, comme dans `simple_browser.py`, que nous analyserons plus tard.
*   **Quand l'utiliser :** Pour des tâches de recherche complexes où les étapes sont inconnues à l'avance et où une adaptation en temps réel est requise.
*   **Avantages :** **Intelligence.** La capacité à résoudre des problèmes non structurés et à s'adapter aux changements à la volée.
*   **Inconvénients :** "Non-déterminisme" (les résultats peuvent varier d'une exécution à l'autre), coût des appels API aux LLM, vitesse inférieure par rapport au code direct.

#### Paradigme n°4 : Scraping sans code

Parfois, la tâche est si simple qu'écrire du code est superflu. Besoin d'extraire rapidement un tableau d'une page ? Il existe des solutions élégantes pour cela qui ne nécessitent pas de programmation.

*   **Outils :** Fonctions Google Sheets (`IMPORTXML`, `IMPORTHTML`), extensions de navigateur.
*   **Quand l'utiliser :** Pour des tâches ponctuelles, un prototypage rapide, ou lorsque vous ne voulez tout simplement pas écrire de code.
*   **Avantages :** **Simplicité.** Ouvert, spécifié ce qu'il faut collecter — obtenu le résultat.
*   **Inconvénients :** Fonctionnalité limitée, ne conviennent pas aux tâches complexes ou aux grands volumes de données.

### Et ensuite ?

Cet article n'est qu'une introduction. Dans les prochains numéros de notre série "PAS Selenium", nous passerons de la théorie à la pratique. Nous approfondirons chacun de ces paradigmes et montrerons comment ils fonctionnent avec des exemples concrets :

*   Nous analyserons **Pydoll** et verrons comment il contourne Cloudflare.
*   Nous organiserons une bataille entre **JavaScript vs Python** pour le titre du meilleur langage pour le web scraping.
*   Nous apprendrons à tirer le maximum de vitesse de l'analyse avec **lxml**.
*   Nous écrirons un script qui collecte des données d'**Amazon** et les enregistre dans **Excel**.
*   Nous montrerons comment **Google Sheets** peut devenir votre premier scraper.
*   Et, bien sûr, nous analyserons en détail comment créer et utiliser un **agent LLM autonome** pour contrôler le navigateur.

Préparez-vous à changer votre vision de l'automatisation et de la collecte de données sur le web. Ce sera rapide, efficace et très intéressant. Abonnez-vous
