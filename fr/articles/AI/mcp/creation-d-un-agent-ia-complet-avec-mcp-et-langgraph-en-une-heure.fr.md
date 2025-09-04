# Comment apprendre à un réseau neuronal à travailler de ses mains : création d'un agent IA complet avec MCP et LangGraph en une heure


Amis, salutations ! J'espère que vous m'avez manqué.

Ces deux derniers mois, je me suis plongé dans la recherche sur l'intégration des agents IA dans mes propres projets Python. Au cours de ce processus, j'ai accumulé de nombreuses connaissances pratiques et observations qu'il serait dommage de ne pas partager. C'est pourquoi je reviens aujourd'hui sur Habr, avec un nouveau sujet, un regard neuf et l'intention d'écrire plus souvent.

À l'ordre du jour : LangGraph et MCP : des outils avec lesquels vous pouvez créer des agents IA vraiment utiles.

Si auparavant nous discutions de la meilleure façon pour un réseau neuronal de répondre en russe, aujourd'hui le champ de bataille s'est déplacé vers des tâches plus appliquées : qui gère le mieux le rôle d'un agent IA ? Quels frameworks simplifient réellement le développement ? Et comment intégrer tout cela dans un projet réel ?

Mais avant de plonger dans la pratique et le code, comprenons les concepts de base. Surtout deux clés : **les agents IA et le MCP**. Sans eux, la conversation sur LangGraph serait incomplète.

### Les agents IA en termes simples

Les agents IA ne sont pas de simples chatbots "améliorés". Ce sont des entités plus complexes et autonomes qui possèdent deux caractéristiques cruciales :

1.  **Capacité d'interagir et de se coordonner**

    Les agents modernes peuvent décomposer les tâches en sous-tâches, appeler d'autres agents, demander des données externes et travailler en équipe. Ce n'est plus un assistant solitaire, mais un système distribué où chaque composant peut apporter sa contribution.

2.  **Accès aux ressources externes**

    Un agent IA n'est plus limité par les contraintes d'un dialogue. Il peut accéder à des bases de données, effectuer des appels API, interagir avec des fichiers locaux, des bases de connaissances vectorielles et même exécuter des commandes dans le terminal. Tout cela est devenu possible grâce à l'émergence du MCP, un nouveau niveau d'intégration entre le modèle et l'environnement.

---

Pour le dire simplement : **le MCP est un pont entre un réseau neuronal et son environnement**. Il permet au modèle de « comprendre » le contexte de la tâche, d'accéder aux données, d'effectuer des appels et de former des actions raisonnées, plutôt que de simplement émettre des réponses textuelles.

**Imaginons une analogie :**

*   Vous avez un **réseau neuronal** : il sait raisonner et générer des textes.
*   Il y a des **données et des outils** : documents, API, bases de connaissances, terminal, code.
*   Et il y a le **MCP** : c'est une interface qui permet au modèle d'interagir avec ces sources externes comme si elles faisaient partie de son monde interne.

**Sans MCP :**

Le modèle est un moteur de dialogue isolé. Vous lui donnez du texte, et il répond. Et c'est tout.

**Avec MCP :**

Le modèle devient un **exécuteur de tâches** à part entière :

*   obtient l'accès aux structures de données et aux API ;
*   appelle des fonctions externes ;
*   s'oriente dans l'état actuel du projet ou de l'application ;
*   peut mémoriser, suivre et modifier le contexte au fur et à mesure du dialogue ;
*   utilise des extensions telles que des outils de recherche, des exécuteurs de code, des bases de données d'embeddings vectoriels, etc.

Au sens technique, **le MCP est un protocole d'interaction entre le LLM et son environnement**, où le contexte est fourni sous forme d'objets structurés (au lieu de texte « brut »), et les appels sont formalisés comme des opérations interactives (par exemple, l'appel de fonctions, l'utilisation d'outils ou les actions d'agent). C'est ce qui transforme un modèle ordinaire en un **véritable agent IA**, capable de faire plus que simplement « parler ».

### Et maintenant, au travail !

Maintenant que nous avons abordé les concepts de base, il est logique de se poser la question : « Comment mettre tout cela en pratique en Python ? »

C'est là qu'intervient **LangGraph** – un framework puissant pour la construction de graphes d'états, de comportements d'agents et de chaînes de pensée. Il permet de « coudre » la logique d'interaction entre les agents, les outils et l'utilisateur, créant une architecture IA vivante qui s'adapte aux tâches.

Dans les sections suivantes, nous verrons comment :

*   construire un agent à partir de zéro ;
*   créer des états, des transitions et des événements ;
*   intégrer des fonctions et des outils ;
*   et comment tout cet écosystème fonctionne dans un projet réel.

### Un peu de théorie : qu'est-ce que LangGraph ?

Avant de passer à la pratique, il faut dire quelques mots sur le framework lui-même.

**LangGraph** est un projet de l'équipe **LangChain**, ceux-là mêmes qui ont les premiers proposé le concept de « chaînes » (chains) d'interaction avec les LLM. Si auparavant l'accent était mis sur les pipelines linéaires ou à embranchements conditionnels (langchain.chains), les développeurs misent désormais sur un **modèle de graphe**, et LangGraph est ce qu'ils recommandent comme le nouveau « cœur » pour la construction de systèmes IA complexes.

**LangGraph** est un framework pour la construction de machines à états finis et de graphes d'états, où chaque **nœud** représente une partie de la logique de l'agent : un appel de modèle, un outil externe, une condition, une entrée utilisateur, etc.

### Comment ça marche : graphes et nœuds

Conceptuellement, LangGraph est construit sur les idées suivantes :

*   **Graphe** : c'est une structure qui décrit les chemins d'exécution possibles de la logique. On peut le considérer comme une carte : d'un point, on peut passer à un autre en fonction des conditions ou du résultat de l'exécution.
*   **Nœuds** : ce sont des étapes spécifiques au sein du graphe. Chaque nœud exécute une fonction : appelle un modèle, appelle une API externe, vérifie une condition ou met simplement à jour l'état interne.
*   **Transitions entre les nœuds** : c'est la logique de routage : si le résultat de l'étape précédente est tel, alors on va là.
*   **État** : il est transmis entre les nœuds et accumule tout ce qui est nécessaire : historique, conclusions intermédiaires, entrée utilisateur, résultat du travail des outils, etc.

Ainsi, nous obtenons un **mécanisme flexible de contrôle de la logique de l'agent**, dans lequel des scénarios simples et très complexes peuvent être décrits : boucles, conditions, actions parallèles, appels imbriqués et bien plus encore.

### Pourquoi est-ce pratique ?

LangGraph permet de construire une **logique transparente, reproductible et extensible** :

*   facile à déboguer ;
*   facile à visualiser ;
*   facile à adapter à de nouvelles tâches ;
*   facile à intégrer des outils externes et des protocoles MCP.

En substance, LangGraph est le **« cerveau » de l'agent**, où chaque étape est documentée, contrôlable et peut être modifiée sans chaos ni « magie ».

### Bon, ça suffit la théorie !

On pourrait encore longtemps parler des graphes, des états, de la composition logique et des avantages de LangGraph par rapport aux pipelines classiques. Mais, comme le montre la pratique, il vaut mieux le voir une fois dans le code.

**Il est temps de passer à la pratique.** Ensuite, un exemple en Python : nous allons créer un agent IA simple mais utile basé sur LangGraph qui utilisera des outils externes, la mémoire et prendra des décisions par lui-même.

### Préparation : réseaux neuronaux cloud et locaux

Pour commencer à créer des agents IA, nous avons d'abord besoin d'un **cerveau** – un modèle linguistique. Il existe deux approches ici :

*   **utiliser des solutions cloud**, où tout est prêt « clé en main » ;
*   ou **monter le modèle localement** – pour une autonomie et une confidentialité complètes.

Examinons les deux options.

#### Services cloud : rapides et pratiques

Le moyen le plus simple est d'utiliser la puissance des grands fournisseurs : OpenAI, Anthropic, et d'utiliser...

### Où obtenir les clés et les jetons :

*   **OpenAI** – ChatGPT et autres produits ;
*   **Anthropic** – Claude ;
*   **OpenRouter.ai** – des dizaines de modèles (un jeton – de nombreux modèles via une API compatible OpenAI) ;
*   **Amvera Cloud** – la possibilité de connecter LLAMA avec un paiement en roubles et un proxy intégré vers OpenAI et Anthropic.

Ce chemin est pratique, surtout si vous :

*   ne voulez pas configurer l'infrastructure ;
*   développez en mettant l'accent sur la vitesse ;
*   travaillez avec des ressources limitées.

### Modèles locaux : contrôle total

Si la **confidentialité, le travail hors ligne** sont importants pour vous, ou si vous souhaitez créer des **agents entièrement autonomes**, il est judicieux de déployer le réseau neuronal localement.

**Principaux avantages :**

*   **Confidentialité** – les données restent chez vous ;
*   **Travail hors ligne** – utile dans les réseaux isolés ;
*   **Pas d'abonnements ni de jetons** – gratuit après la configuration.

**Les inconvénients sont évidents :**

*   Exigences en matière de ressources (en particulier pour la mémoire vidéo) ;
*   La configuration peut prendre du temps ;
*   Certains modèles sont difficiles à déployer sans expérience.

Néanmoins, il existe des outils qui facilitent le lancement local. L'un des meilleurs aujourd'hui est **Ollama**.

### Déploiement de LLM local via Ollama + Docker

Nous allons préparer un lancement local du modèle Qwen 2.5 (qwen2.5:32b) à l'aide d'un conteneur Docker et du système Ollama. Cela permettra d'intégrer le réseau neuronal avec le MCP et de l'utiliser dans vos propres agents basés sur LangGraph.

Si les ressources informatiques de votre ordinateur ou de votre serveur sont insuffisantes pour travailler avec cette version du modèle, vous pouvez toujours choisir un réseau neuronal moins « gourmand en ressources » – le processus d'installation et de lancement restera similaire.

**Installation rapide (résumé des étapes)**

1.  **Installer Docker + Docker Compose**
2.  **Créer la structure du projet :**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **Créer `docker-compose.yml`**
(option universelle, le GPU est détecté automatiquement)

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama_qwen
    ports:
      - "11434:11434"
    volumes:
      - ./ollama_data:/root/.ollama
      - /tmp:/tmp
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_ORIGINS=*
    restart: unless-stopped
```

4.  **Démarrer le conteneur :**
```bash
docker compose up -d
```

5.  **Télécharger le modèle :**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **Vérifier le fonctionnement via l'API :**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "Bonjour !", "stream": false}'
```
*(Image avec le résultat de l'exécution de la commande curl)*

7.  **Intégration avec Python :**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:32b",
        "prompt": prompt,
        "stream": False
    })
    return res.json()['response']

print(query("Expliquez l'intrication quantique"))
```
Vous disposez maintenant d'un LLM local complet, prêt à fonctionner avec MCP et LangGraph.

**Et ensuite ?**

Nous avons le choix entre les modèles cloud et locaux, et nous avons appris à connecter les deux. Le plus intéressant est à venir : **créer des agents IA sur LangGraph**, qui utilisent le modèle sélectionné, la mémoire, les outils et leur propre logique.

**Passons à la partie la plus savoureuse : le code et la pratique !**

---

Avant de passer à la pratique, il est important de préparer l'environnement de travail. Je suppose que vous êtes déjà familiarisé avec les bases de Python, que vous savez ce que sont les bibliothèques et les dépendances, et que vous comprenez pourquoi utiliser un environnement virtuel.

Si tout cela est nouveau pour vous, je vous recommande de suivre d'abord un cours court ou un guide sur les bases de Python, puis de revenir à l'article.

#### Étape 1 : Création d'un environnement virtuel

Créez un nouvel environnement virtuel dans le dossier du projet :
```bash
python -m venv venv
source venv/bin/activate  # pour Linux/macOS
virtualenv\Scripts\activate   # pour Windows
```

#### Étape 2 : Installation des dépendances

Créez un fichier `requirements.txt` et ajoutez-y les lignes suivantes :
```
langchain==0.3.26
langchain-core==0.3.69
langchain-deepseek==0.1.3
langchain-mcp-adapters==0.1.9
langchain-ollama==0.3.5
langchain-openai==0.3.28
langgraph==0.5.3
langgraph-checkpoint==2.1.1
langgraph-prebuilt==0.5.2
langgraph-sdk==0.1.73
langsmith==0.4.8
mcp==1.12.0
ollama==0.5.1
openai==1.97.0
```

> ⚠️ **Les versions actuelles sont indiquées au 21 juillet 2025.** Elles peuvent avoir changé depuis la publication – **vérifiez la pertinence avant l'installation.**

Ensuite, installez les dépendances :
```bash
pip install -r requirements.txt```

#### Étape 3 : Configuration des variables d'environnement

Créez un fichier `.env` à la racine du projet et ajoutez-y les clés API nécessaires :
```
OPENAI_API_KEY=sk-proj-1234
DEEPSEEK_API_KEY=sk-123
OPENROUTER_API_KEY=sk-or-v1-123
BRAVE_API_KEY=BSAj123K1bvBGpH1344tLwc
```

**Objectif des variables :**

*   **OPENAI_API_KEY** – clé pour accéder aux modèles GPT d'OpenAI ;
*   **DEEPSEEK_API_KEY** – clé pour utiliser les modèles Deepseek ;
*   **OPENROUTER_API_KEY** – clé unique pour accéder à de nombreux modèles via OpenRouter

---

Certains outils MCP (par exemple, `brave-web-search`) nécessitent une clé pour fonctionner. Sans elle, ils ne s'activeront tout simplement pas.

**Et si vous n'avez pas de clés API ?**

Pas de problème. Vous pouvez commencer le développement avec un modèle local (par exemple, via Ollama), sans connecter aucun service externe. Dans ce cas, vous n'avez pas du tout besoin de créer le fichier `.env`.

C'est fait ! Nous avons maintenant tout ce dont nous avons besoin pour commencer – un environnement isolé, des dépendances et, si nécessaire, l'accès aux réseaux neuronaux cloud et aux intégrations MCP.

Ensuite, nous lancerons notre agent LLM de différentes manières.

### Lancement simple des agents LLM via LangGraph : intégration de base

Commençons par le plus simple : comment « connecter le cerveau » à un futur agent. Nous analyserons les méthodes de base pour lancer des modèles de langage (LLM) à l'aide de LangChain, afin qu'à l'étape suivante, nous puissions passer à l'intégration avec LangGraph et à la construction d'un agent IA complet.

#### Importations
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` et `load_dotenv()` – pour charger les variables du fichier `.env`.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` – des wrappers pour connecter les modèles de langage via LangChain.

> 💡 Si vous utilisez des approches alternatives pour travailler avec les configurations (par exemple, Pydantic Settings), vous pouvez remplacer `load_dotenv()` par votre méthode habituelle.

#### Chargement des variables d'environnement
```python
load_dotenv()
```
Cela chargera toutes les variables de `.env`, y compris les clés pour accéder aux API OpenAI, DeepSeek, OpenRouter et autres.

#### Fonctions simples pour obtenir LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
Si la variable `OPENAI_API_KEY` est correctement définie, LangChain la substituera automatiquement – l'indication explicite `api_key=...` est ici facultative.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
De même, mais en utilisant le wrapper `ChatDeepSeek`.

**OpenRouter (et autres API compatibles)**
```python
def get_openrouter_llm(model="moonshotai/kimi-k2:free"):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
```
**Caractéristiques :**

*   `ChatOpenAI` est utilisé, bien que le modèle ne provienne pas d'OpenAI – car OpenRouter utilise le même protocole.
*   `base_url` est obligatoire : il pointe vers l'API OpenRouter.
*   Le modèle `moonshotai/kimi-k2:free` a été choisi comme l'une des options les plus équilibrées en termes de qualité et de vitesse au moment de la rédaction.
*   La clé API `OpenRouter` doit être passée explicitement – la substitution automatique ne fonctionne pas ici.

#### Mini-test : vérification du fonctionnement du modèle
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("Qui es-tu ?")
    print(response.content)
```
*(Image avec le résultat de l'exécution : `Je suis un assistant IA créé par Moonshot AI...`)*

Si tout est configuré correctement, vous recevrez une réponse significative du modèle. Félicitations – la première étape est franchie !

### Mais ce n'est pas encore un agent

À l'étape actuelle, nous avons connecté le LLM et effectué un simple appel. Cela ressemble plus à un chatbot de console qu'à un agent IA.

**Pourquoi ?**

*   Nous écrivons du **code synchrone et linéaire** sans logique d'état ni objectifs.
*   L'agent ne prend pas de décisions, ne mémorise pas le contexte et n'utilise pas d'outils.
*   Le MCP et LangGraph ne sont pas encore impliqués.

**Et ensuite ?**

Ensuite, nous allons implémenter un **agent IA complet** en utilisant **LangGraph** – d'abord sans MCP, pour nous concentrer sur l'architecture, les états et la logique de l'agent.

Plongeons dans la véritable mécanique des agents. C'est parti !

### Agent de classification des emplois : de la théorie à la pratique

...concepts de LangGraph en pratique et créer un outil utile pour les plateformes RH et les bourses de freelances.

#### Tâche de l'agent

Notre agent prend en entrée une description textuelle d'une offre d'emploi ou d'un service et effectue une classification à trois niveaux :

1.  **Type de travail** : travail de projet ou poste permanent
2.  **Catégorie de profession** : parmi plus de 45 spécialités prédéfinies
3.  **Type de recherche** : si une personne cherche un emploi ou cherche un prestataire

Le résultat est renvoyé dans un format JSON structuré avec un score de confiance pour chaque classification.

#### 📈 Architecture de l'agent sur LangGraph

Suivant les principes de LangGraph, nous créons un **graphe d'états** de quatre nœuds :

- Description d'entrée
- ↓
- Nœud de classification du type de travail
- ↓
- Nœud de classification de la catégorie
- ↓
- Nœud de détermination du type de recherche
- ↓
- Nœud de calcul de la confiance
- ↓
- Résultat JSON

Chaque nœud est une **fonction spécialisée** qui :

*   Reçoit l'état actuel de l'agent
*   Effectue sa partie de l'analyse
*   Met à jour l'état et le transmet

#### Gestion de l'état

Nous définissons la **structure de la mémoire de l'agent** via `TypedDict` :

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """État de l'agent pour stocker les informations sur le processus de classification"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

C'est la **mémoire de travail de l'agent** – tout ce qu'il mémorise et accumule pendant l'analyse. Similaire à la façon dont un expert humain garde le contexte de la tâche à l'esprit lors de l'analyse d'un document.

Examinons le code complet, puis concentrons-nous sur les points principaux.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Catégories de professions
CATEGORIES = [
    "Animateur 2D", "Animateur 3D", "Modeleur 3D",
    "Analyste commercial", "Développeur Blockchain", ...
]

class JobType(Enum):
    PROJECT = "travail de projet"
    PERMANENT = "travail permanent"

class SearchType(Enum):
    LOOKING_FOR_WORK = "recherche d'emploi"
    LOOKING_FOR_PERFORMER = "recherche de prestataire"

class State(TypedDict):
    """État de l'agent pour stocker les informations sur le processus de classification"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool

class VacancyClassificationAgent:
    """Agent asynchrone pour la classification des offres d'emploi et des services"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Initialisation de l'agent"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Crée le flux de travail de l'agent basé sur LangGraph"""
        workflow = StateGraph(State)
        
        # Ajouter des nœuds au graphe
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Définir la séquence d'exécution des nœuds
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Nœud pour déterminer le type de travail : projet ou permanent"""
        # ... (l'implémentation suit)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Nœud pour déterminer la catégorie de profession"""
        # ... (l'implémentation suit)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Nœud pour déterminer le type de recherche"""
        # ... (l'implémentation suit)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Nœud pour calculer le niveau de confiance dans la classification"""
        # ... (l'implémentation suit)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Trouve la catégorie la plus proche dans la liste des catégories disponibles"""
        # ... (l'implémentation suit)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Méthode principale pour classer les offres d'emploi/services"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Exécuter le flux de travail
        result = await self.workflow.ainvoke(initial_state)
        
        # Former la réponse JSON finale
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Démonstration du fonctionnement de l'agent"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Recherche développeur Python pour créer une application web en Django. Poste permanent.",
        "Recherche commandes pour créer des logos et une identité d'entreprise. Je travaille avec Adobe Illustrator.",
        "Besoin d'un animateur 3D pour un projet à court terme de création d'une publicité.",
        "CV : marketeur expérimenté, recherche travail à distance dans le domaine du marketing digital",
        "Recherche développeur frontend React pour notre équipe à temps plein"
    ]
    
    print("🤖 Démonstration du fonctionnement de l'agent de classification des offres d'emploi\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Test {i} : ---")
        print(f"Description : {description}")
        try:
            result = await agent.classify(description)
            print("Résultat de la classification :")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Erreur : {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...le reste du code avec les implémentations des méthodes a été présenté dans l'article...)*

### Avantages clés de l'architecture
1.  **Modularité** - chaque nœud résout une tâche, facile à tester et à améliorer séparément
2.  **Extensibilité** - de nouvelles fonctionnalités sont ajoutées de manière déclarative
3.  **Transparence** - l'ensemble du processus de prise de décision est documenté et traçable
4.  **Performance** - traitement asynchrone de multiples requêtes
5.  **Fiabilité** - gestion des erreurs et récupération intégrées

### Avantages réels
Un tel agent peut être utilisé dans :
*   **Les plateformes RH** pour la catégorisation automatique des CV et des offres d'emploi
*   **Les bourses de freelances** pour améliorer la recherche et les recommandations
*   **Les systèmes internes** des entreprises pour le traitement des demandes et des projets
*   **Les solutions analytiques** pour l'étude du marché du travail

### MCP en action : création d'un agent avec un système de fichiers et une recherche web
Après avoir abordé les principes de base de LangGraph et créé un agent classificateur simple, étendons ses capacités en le connectant au monde extérieur via le MCP.

Nous allons maintenant créer un assistant IA complet qui pourra :
*   Travailler avec le système de fichiers (lire, créer, modifier des fichiers)
*   Rechercher des informations pertinentes sur Internet
*   Mémoriser le contexte du dialogue
*   Gérer les erreurs et récupérer après des pannes

#### De la théorie aux outils réels
Vous vous souvenez comment, au début de l'article, nous avons parlé du fait que **le MCP est un pont entre un réseau neuronal et son environnement** ? Vous allez maintenant le voir en pratique. Notre agent aura accès à des **outils réels** :
```
# Outils du système de fichiers
- read_file – lecture de fichiers
- write_file – écriture et création de fichiers
- list_directory – affichage du contenu des dossiers
- create_directory – création de dossiers

# Outils de recherche web
- brave_web_search – recherche sur Internet
- get_web_content – obtention du contenu des pages
```
Ce n'est plus un agent « jouet » – c'est un **outil de travail** qui peut résoudre des problèmes réels.

#### 📈 Architecture : du simple au complexe

**1. Configuration comme base de la stabilité**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Configuration simplifiée de l'agent IA"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Validation de la configuration"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"Le chemin n'existe pas : {self.filesystem_path}")
```
**Pourquoi est-ce important ?** Contrairement à l'exemple de classification, ici l'agent interagit avec des systèmes externes. Une erreur dans le chemin du fichier ou une clé API manquante – et tout l'agent cesse de fonctionner. La **validation au démarrage** permet d'économiser des heures de débogage.

**2. Fabrique de modèles : flexibilité du choix**
```python
def create_model(config: AgentConfig):
    """Crée un modèle selon la configuration"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... autres fournisseurs
```
Un seul code – de nombreux modèles. Vous voulez un modèle local gratuit ? Utilisez Ollama. Besoin d'une précision maximale ? Passez à GPT-4. La vitesse est importante ? Essayez DeepSeek. Le code reste le même.

**3. Intégration MCP : connexion au monde réel**
```python
async def _init_mcp_client(self):
    """Initialisation du client MCP"""
    mcp_config = {
        "filesystem": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", self.filesystem_path],
            "transport": "stdio"
        },
        "brave-search": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search@latest"],
            "transport": "stdio",
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        }
    }
    self.mcp_client = MultiServerMCPClient(mcp_config)
    self.tools = await self.mcp_client.get_tools()
```
Ici, le travail clé du MCP a lieu : nous connectons des serveurs MCP externes à l'agent, qui fournissent un ensemble d'outils et de fonctions. L'agent, à son tour, ne reçoit pas seulement des fonctions individuelles, mais une compréhension contextuelle complète de la façon de travailler avec le système de fichiers et Internet.

#### Résilience aux erreurs
Dans le monde réel, tout tombe en panne : le réseau est indisponible, les fichiers sont verrouillés, les clés API sont expirées. Notre agent est prêt pour cela :
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
Le décorateur `@retry_on_failure` réessaie automatiquement les opérations en cas de défaillances temporaires. L'utilisateur ne remarquera même pas que quelque chose s'est mal passé.

### Résumé : de la théorie à la pratique des agents IA

Aujourd'hui, nous avons parcouru le chemin des concepts de base à la création d'agents IA fonctionnels. Résumons ce que nous avons appris et réalisé.

**Ce que nous avons maîtrisé**

**1. Concepts fondamentaux**
*   Compris la différence entre les chatbots et les véritables agents IA
*   Compris le rôle du **MCP (Model Context Protocol)** comme pont entre le modèle et le monde extérieur
*   Étudié l'architecture de **LangGraph** pour la construction d'une logique d'agent complexe

**2. Compétences pratiques**
*   Configuré un environnement de travail avec prise en charge des modèles cloud et locaux
*   Créé un **agent classificateur** avec une architecture asynchrone et une gestion d'état
*   Construit un **agent MCP** avec accès au système de fichiers et à la recherche web

**3. Modèles architecturaux**
*   Maîtrisé la configuration modulaire et les fabriques de modèles
*   Implémenté la gestion des erreurs et les **mécanismes de réessai** pour les solutions prêtes pour la production

### Avantages clés de l'approche
**LangGraph + MCP** nous offrent :
*   **Transparence** – chaque étape de l'agent est documentée et traçable
*   **Extensibilité** – de nouvelles fonctionnalités sont ajoutées de manière déclarative
*   **Fiabilité** – gestion des erreurs et récupération intégrées
*   **Flexibilité** – prise en charge de plusieurs modèles et fournisseurs prêts à l'emploi

### Conclusion

Les agents IA ne sont pas une fiction futuriste, mais une **technologie réelle d'aujourd'hui**. Avec LangGraph et MCP, nous pouvons créer des systèmes qui résolvent des problèmes commerciaux spécifiques, automatisent les routines et ouvrent de nouvelles possibilités.

**L'essentiel est de commencer.** Prenez le code des exemples, adaptez-le à vos tâches, expérimentez. Chaque projet est une nouvelle expérience et un pas vers la maîtrise dans le domaine du développement IA.

Bonne chance dans vos projets !

---
*Tags : python, ia, mcp, langchain, assistant ia, ollama, agents ia, llm local, langgraph, mcp-server*
*Hubs : Blog de la société Amvera, Traitement du langage naturel, Intelligence artificielle, Python, Programmation*
