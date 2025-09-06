## Comment créer un agent IA pour interagir avec un navigateur web en utilisant LangChain et Browser-Use : un guide étape par étape

Ce guide étape par étape vous montrera comment créer un agent IA capable de rechercher des informations sur Google et d'analyser des pages web en utilisant LangChain et Browser-Use.

**Étape 1 : Installer les bibliothèques nécessaires**

Tout d'abord, vous devez installer les bibliothèques Python requises. Ouvrez votre terminal ou votre invite de commande et exécutez la commande suivante :

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Étape 2 : Configurer les clés API**

Des clés API sont nécessaires pour travailler avec OpenAI et SerpAPI.

*   **Clé API OpenAI :** Obtenez votre clé API sur le site web d'OpenAI (openai.com).
*   **Clé API SerpAPI :** SerpAPI fournit une API pour travailler avec les résultats de recherche. Inscrivez-vous sur serpapi.com (un essai gratuit est disponible), connectez-vous à votre compte et trouvez votre clé API sur la page du tableau de bord.

Créez un fichier `.env` dans le même répertoire que votre script Python et ajoutez les clés au format suivant :

```
OPENAI_API_KEY=votre_clé_openai
SERPAPI_API_KEY=votre_clé_serpapi
```

**Étape 3 : Créer le script Python (browser_agent.py)**

Créez un fichier nommé `browser_agent.py` et collez le code suivant :

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Configurer la journalisation
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Charger les clés API du fichier .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Initialiser le modèle de langage
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Vous pouvez essayer d'autres modèles

    # Définir l'outil de recherche (exemple simple, sans recherche Google réelle)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Recherche Google pour : {query}",  # Remplacer par une recherche SerpAPI réelle si nécessaire
        description="Recherche des informations sur Google."
    )


    # Définir la tâche de l'agent
    task = """
    Trouvez les dernières nouvelles sur OpenAI sur Google.
    Ensuite, visitez l'un des sites web trouvés et trouvez les noms des fondateurs.
    """

    # Créer l'agent
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Exécuter l'agent
    try:
        result = await agent.arun(task)
        print(f"Résultat : {result}")
    except Exception as e:
        logging.error(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Étape 4 : Exécuter l'agent**

Ouvrez votre terminal ou votre invite de commande, naviguez jusqu'au répertoire contenant `browser_agent.py` et exécutez-le :

```bash
python browser_agent.py
```

**Étape 5 : Améliorer l'agent (fonctionnalités avancées)**

*   **Recherche Google réelle :** Remplacez la fonction `lambda` dans `search_tool` par du code qui utilise SerpAPI pour des recherches Google réelles. Cela nécessitera d'étudier la documentation de SerpAPI.

*   **Interaction avec les pages web (Browser-Use) :** Pour ajouter des fonctionnalités d'interaction avec les pages web (ouverture de liens, extraction de texte, etc.), vous devrez utiliser la bibliothèque `browser-use`. La documentation de cette bibliothèque vous aidera à ajouter les outils appropriés à votre agent.

*   **Utilisation de la mémoire :** Pour maintenir le contexte entre les requêtes, vous pouvez utiliser les mécanismes de mémoire de LangChain.

*   **Chaînes d'actions plus complexes :** LangChain vous permet de créer des chaînes d'actions plus complexes (Chains) pour résoudre des tâches plus complexes.


Cet exemple démontre la structure de base. Pour implémenter un agent complet qui interagit avec un navigateur et Google Search, un travail supplémentaire avec SerpAPI et `browser-use` sera nécessaire. N'oubliez pas de vous référer à la documentation de ces bibliothèques pour des informations plus détaillées.
