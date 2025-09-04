## Comment créer un agent IA pour la navigation web avec LangChain et Browser-Use : un guide étape par étape

Ce guide étape par étape vous montrera comment créer un agent IA capable de rechercher des informations sur Google et d'analyser des pages web en utilisant LangChain et Browser-Use.

**Étape 1 : Installer les bibliothèques nécessaires**

Tout d'abord, vous devez installer les bibliothèques Python nécessaires. Ouvrez un terminal ou une invite de commande et exécutez la commande suivante :

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Étape 2 : Configurer les clés API**

Des clés API sont nécessaires pour travailler avec OpenAI et SerpAPI.

* **Clé API OpenAI :** Obtenez votre clé API sur le site web d'OpenAI (openai.com).
* **Clé API SerpAPI :** SerpAPI fournit une API pour travailler avec les résultats de recherche. Inscrivez-vous sur le site web serpapi.com (une version d'essai gratuite est disponible), connectez-vous à votre compte et trouvez votre clé API sur la page du tableau de bord.

Créez un fichier `.env` dans le même répertoire que votre script Python et ajoutez-y les clés au format suivant :

```
OPENAI_API_KEY=votre_clé_openai
SERPAPI_API_KEY=votre_clé_serpapi
```

**Étape 3 : Créer un script Python (browser_agent.py)**

Créez le fichier `browser_agent.py` et insérez-y le code suivant :

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Configuration de la journalisation
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Chargement des clés API à partir du fichier .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Initialisation du modèle linguistique
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Vous pouvez essayer d'autres modèles

    # Définition de l'outil de recherche (exemple simple, pas de recherche Google réelle)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Recherche Google : {query}",  # Remplacer par une recherche réelle utilisant SerpAPI si nécessaire
        description="Recherche des informations sur Google."
    )


    # Définition de la tâche pour l'agent
    task = """
    Trouvez les dernières nouvelles sur OpenAI sur Google.
    Ensuite, visitez l'un des sites web trouvés et trouvez les noms des fondateurs.
    """

    # Création de l'agent
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Exécution de l'agent
    try:
        result = await agent.arun(task)
        print(f"Résultat : {result}")
    except Exception as e:
        logging.error(f"Une erreur s'est produite : {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Étape 4 : Exécuter l'agent**

Ouvrez un terminal ou une invite de commande, accédez au répertoire contenant le fichier `browser_agent.py` et exécutez-le :

```bash
python browser_agent.py
```

**Étape 5 : Améliorer l'agent (fonctionnalités avancées)**

* **Recherche Google réelle :** Remplacez la fonction `lambda` dans `search_tool` par du code qui utilise SerpAPI pour des recherches Google réelles. Cela nécessitera d'étudier la documentation de SerpAPI.

* **Interaction avec les pages web (Browser-Use) :** Pour ajouter des fonctionnalités d'interaction avec les pages web (ouverture de liens, extraction de texte, etc.), vous devrez utiliser la bibliothèque `browser-use`. La documentation de cette bibliothèque vous aidera à ajouter les outils appropriés à votre agent.

* **Utilisation de la mémoire :** Les mécanismes de mémoire de LangChain peuvent être utilisés pour préserver le contexte entre les requêtes.

* **Chaînes d'action plus complexes :** LangChain vous permet de créer des chaînes d'action plus complexes pour résoudre des tâches plus complexes.


Cet exemple démontre la structure de base. Pour implémenter un agent complet qui interagit avec un navigateur et Google Search, un travail supplémentaire avec SerpAPI et `browser-use` sera nécessaire. N'oubliez pas de consulter la documentation de ces bibliothèques pour des informations plus détaillées.
