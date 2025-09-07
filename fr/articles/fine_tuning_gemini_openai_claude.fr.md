## Aide-mémoire. Personnalisation des LLM: Prompts, réglage fin des modèles, exemples de code.

Dans cet article:

1.  Comment l'"effet mémoire" est créé dans les LLM (bref aperçu).
2.  Pourquoi et quand un réglage fin (Fine-tuning) du modèle est nécessaire.
3.  Quand le réglage fin n'est pas la meilleure solution.
4.  Préparation des données.
5.  Exemples de réglage fin pour **OpenAI (GPT)**, **Google (Gemini)** et **Anthropic (Claude)** (diffère).

### 1. Comment les LLM "se souviennent" et "s'adaptent": L'illusion du contexte

Avant de parler du réglage fin, il est important de comprendre comment les LLM parviennent à créer une sensation de personnalisation.
Ceci est important pour ne pas se lancer dans un réglage fin coûteux si la tâche peut être résolue par des méthodes plus simples:

*   Via la **Fenêtre de Contexte (Mémoire à Court Terme):** Dans un seul dialogue, vous envoyez au modèle non seulement une nouvelle question, mais aussi **tout ou partie de la conversation précédente**. Le modèle traite tout ce texte comme un seul "contexte". C'est grâce à cela qu'il "se souvient" des remarques précédentes et poursuit la pensée. La limitation ici est la longueur de la fenêtre de contexte (nombre de jetons).
*   Composition des **Instructions Système (System Prompt):** Vous pouvez définir le rôle, le ton et les règles de comportement du modèle au début de chaque dialogue. Par exemple: "Tu es un expert Python, réponds de manière concise."
*   Inclusion de plusieurs exemples de comportement souhaité dans la requête **Few-Shot Learning:** (paires entrée/sortie) permet au modèle d'"apprendre" ce modèle directement dans la requête actuelle.
*   **Gestion de l'état côté application:** Le moyen le plus puissant. L'application (qui accède à l'API) peut stocker des informations sur l'utilisateur (préférences, historique, données de profil) et les ajouter dynamiquement au prompt avant de l'envoyer au modèle.


### 2.

Le réglage fin est le processus de formation supplémentaire d'un LLM de base déjà existant sur votre propre ensemble de données spécifique. Cela permet au modèle de:

*   **Adapter le style et le ton:** Le modèle parlera "votre langue" – qu'il s'agisse d'un langage strictement scientifique, d'un langage marketing amical ou de l'argot d'une communauté spécifique.
*   **Suivre des instructions et des formats spécifiques:** Si vous avez besoin de réponses dans une structure JSON strictement définie, ou toujours avec un ensemble spécifique de champs.
*   **Comprendre le langage spécifique au domaine:** La formation sur votre documentation interne ou des textes de l'industrie aidera le modèle à mieux gérer la terminologie de votre niche.
*   **Améliorer les performances sur des tâches spécifiques:** Pour certains types de requêtes (par exemple, classification des sentiments, génération de code dans un framework spécifique), le réglage fin peut fournir des réponses plus précises et pertinentes que le modèle de base.
*   **Réduire la longueur des prompts:** Si le modèle "connaît" déjà le comportement souhaité grâce au réglage, vous n'avez pas besoin de le lui rappeler à chaque fois dans le prompt, ce qui économise des jetons et réduit la latence.

### 3.

Le réglage fin est un outil puissant mais non universel. Vous ne devriez pas l'utiliser si:

*   **Le modèle a besoin d'accéder à de nouvelles connaissances:** Le réglage fin modifie les poids du modèle, mais il ne "charge" pas de nouveaux faits en temps réel. Si votre tâche est de répondre à des questions basées sur une base de connaissances en constante évolution (documents d'entreprise, dernières nouvelles), il est préférable d'utiliser la **Génération Augmentée par Récupération (RAG)**. Ici, le modèle de base reçoit le contexte de votre base de données *au moment de la requête*.
*   **Une tâche simple peut être résolue par l'ingénierie des prompts:** Commencez toujours par l'ingénierie des prompts la plus efficace. Si la tâche peut être résolue avec des instructions simples et des exemples de quelques tirs, le réglage fin est redondant et plus coûteux.
*   **Vous n'avez pas suffisamment de données de haute qualité:** Mauvaises données = mauvais modèle réglé.

### 4. Préparation des données.

La qualité et la quantité de vos données sont d'une importance capitale. Le modèle apprend de vos exemples, ils doivent donc être précis, diversifiés et cohérents.

*   **Format:** Le plus souvent JSON Lines (`.jsonl`) ou CSV (`.csv`).
*   **Structure des données:** Dépend de la tâche.
    *   **Réglage des instructions (Instruction-Réponse):** Convient aux tâches généralisées telles que "question-réponse", paraphrase, résumé.
        ```json
        {"input_text": "Перефразируй предложение: 'Технология ИИ стремительно развивается.'", "output_text": "Искусственный интеллект демонстрирует стремительный прогресс."}
        {"input_text": "Назови столицу Франции.", "output_text": "Столица Франции — Париж."}
        ```
    *   **Réglage du chat (Chat):** Idéal pour entraîner le modèle à mener un dialogue dans un rôle ou un style spécifique.
        ```json
        {"messages": [{"author": "user", "content": "Привет! Что порекомендуешь на ужин?"}, {"author": "model", "content": "Добрый вечер! Сегодня отличный день для пасты Карбонара, или, если вы предпочитаете что-то легкое, салат Цезарь."}]}
        {"messages": [{"author": "user", "content": "Расскажи про новые фичи в Python 3.12."}, {"author": "model", "content": "В Python 3.12 появились f-строки с отступами, новый синтаксис для универсальных генериков и улучшенная обработка ошибок Unicode."}]}
        ```
*   **Quantité:** Minimum 100-200 exemples de haute qualité, mais plus il y en a, mieux c'est (des milliers pour les tâches sérieuses).
*   **Qualité:** Précision, style, ton et format cohérents dans l'ensemble des données.

### 5. Modèles et Plateformes


#### 5.1. OpenAI

OpenAI fournit une API assez simple et intuitive pour le réglage fin.

**Processus:**

1.  Préparez les données au format JSONL, où chaque ligne est un objet avec un tableau `messages` (comme dans l'API Chat Completions).
2.  Téléchargez le fichier de données via l'API.
3.  Créez une tâche de réglage fin, en spécifiant le fichier téléchargé et le modèle de base.
4.  Surveillez la progression.
5.  Utilisez le nouveau modèle réglé par son ID.

**Exemple de données (fichier `training_data.jsonl`):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let\'s try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**Exemple de code Python:**

Installez au préalable: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Définissez votre clé API OpenAI. Il est recommandé d'utiliser une variable d'environnement.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Télécharger le fichier de données
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Fichier téléchargé avec succès. ID du fichier: {file_id}")
except openai.APIStatusError as e:
    print(f"Erreur de téléchargement du fichier: {e.status_code} - {e.response}")
    exit()

# 2. Créer une tâche de réglage fin
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Vous pouvez spécifier une version spécifique, par exemple, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Tâche de réglage fin créée. ID de la tâche: {job_id}")
    print("Surveillez l\'état de la tâche via l\'API ou dans OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Erreur de création de la tâche: {e.status_code} - {e.response}")
    exit()

# Exemple de surveillance de l\'état et d\'obtention du nom du modèle (à exécuter après la création de la tâche):
# # job_id = "ftjob-..." # Remplacez par l\'ID de votre tâche
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"État actuel de la tâche: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nom du modèle réglé: {fine_tuned_model_name}")

# 3. Utilisation du modèle réglé (une fois prêt)
# # Remplacez par le nom réel de votre modèle, obtenu après un réglage fin réussi
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "J\'ai un problème de connexion."}
# #             ]
# #         )
# #         print("\nRéponse du modèle réglé:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Erreur lors de l\'utilisation du modèle: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **ne fournit pas d'API publique pour le réglage fin de ses modèles Claude 3 (Opus, Sonnet, Haiku) de la même manière qu'OpenAI ou Google.**

Anthropic se concentre sur la création de modèles de base très puissants qui, selon eux, fonctionnent parfaitement avec l'ingénierie de prompts avancée et les modèles RAG, minimisant le besoin de réglage fin dans la plupart des cas.
Pour les grands clients d'entreprise ou les partenaires, il peut exister des programmes pour la création de modèles "personnalisés" ou d'intégrations spécialisées, mais ce n'est pas une fonctionnalité de réglage fin accessible au public via l'API.

Si vous travaillez avec Claude 3, votre objectif principal devrait être :

*   **Ingénierie des prompts de haute qualité :** Expérimentez avec les instructions système, les exemples de quelques tirs, le formatage clair des requêtes. Claude est connu pour sa capacité à suivre strictement les instructions, en particulier dans les balises XML.
*   **Systèmes RAG :** Utilisez des bases de connaissances externes pour fournir au modèle un contexte pertinent.

#### 5.3. Google (Gemini)

Google développe activement les capacités de réglage fin via sa plateforme **Google Cloud Vertex AI**.
Il s'agit d'une plateforme ML complète qui fournit des outils pour la préparation des données, l'exécution des tâches d'entraînement et le déploiement des modèles.
Le réglage fin est disponible pour la famille de modèles Gemini.

**Processus :**

1.  Préparez les données (JSONL ou CSV) au format `input_text`/`output_text` (pour le réglage des instructions) ou `messages` (pour le réglage du chat).
2.  Téléchargez les données vers Google Cloud Storage (GCS).
3.  Créez et exécutez une tâche de réglage fin via la console ou le SDK de Vertex AI.
4.  Déployez le modèle réglé sur un point de terminaison (Endpoint).
5.  Utilisez le modèle réglé via ce point de terminaison.

**Exemple de données (fichier `gemini_tuning_data.jsonl`):**

```json
{"input_text": "Summarize the main ideas of this book: 'The book tells the story of a hero's journey, who overcomes obstacles and finds himself.'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}
{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}
```

**Exemple de code Python (nécessite `google-cloud-aiplatform`):**

Installez au préalable: `pip install google-cloud-aiplatform` et `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Paramètres ---
# REMPLACEZ par vos valeurs:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Choisissez une région qui prend en charge Gemini et Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Nom de votre bucket GCS (doit être créé au préalable)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Fin des paramètres ---

# Initialisation de Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Créer le fichier de données (s'il n'existe pas)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Summarize the main ideas of this book: \'The book tells the story of a hero\'s journey, who overcomes obstacles and finds himself.\'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and achieving self-discovery."}\n')
    f.write('{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to replicate the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}\n')
print(f"Fichier de données '{DATA_FILE_LOCAL_PATH}' créé.")


# 2. Télécharger les données vers Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Télécharge un fichier vers le bucket GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Fichier '{source_file_name}' téléchargé vers 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Erreur de téléchargement du fichier vers GCS. Assurez-vous que le bucket existe et que vous avez les autorisations: {e}")
    exit()

# 3. Créer et exécuter la tâche de réglage fin
print(f"\nDémarrage du réglage fin du modèle '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` démarre la tâche et renvoie le modèle réglé après achèvement
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Modèle de base Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Nombre d'étapes d'entraînement. La valeur optimale dépend de la taille des données.
        # batch_size=16, # Peut être spécifié
        # learning_rate_multiplier=1.0 # Peut être spécifié
    )
    print(f"Modèle '{TUNED_MODEL_DISPLAY_NAME}' réglé avec succès. ID du modèle: {tuned_model.name}")
    print("Le processus de réglage fin peut prendre un temps considérable.")
except Exception as e:
    print(f"Erreur de réglage fin. Vérifiez les journaux dans la console Vertex AI: {e}")
    exit()

# 4. Déployer le modèle réglé (pour utilisation)
print(f"\nDéploiement du modèle réglé '{TUNED_MODEL_DISPLAY_NAME}' vers le point de terminaison...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Type de machine pour le point de terminaison. Choisissez celui qui convient.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modèle déployé vers le point de terminaison: {endpoint.name}")
    print("Le déploiement peut également prendre plusieurs minutes.")
except Exception as e:
    print(f"Erreur de déploiement du modèle: {e}")
    exit()

# 5. Utilisation du modèle réglé
print("\nTest du modèle réglé...")
prompt = "Parlez-moi de vos capacités après l'entraînement."
instances = [{"prompt": prompt}] # Pour le réglage des instructions. Si réglage du chat, alors {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nRéponse du modèle réglé:")
    print(response.predictions[0])
except Exception as e:
    print(f"Erreur lors de l\'utilisation du modèle réglé: {e}")

# Une fois terminé, n'oubliez pas de supprimer le point de terminaison et le modèle pour éviter des coûts inutiles:
# endpoint.delete()
# tuned_model.delete()
```

### 6. Recommandations générales

*   **Commencez petit :** N'essayez pas d'entraîner le modèle sur des milliers d'exemples tout de suite. Commencez par un petit ensemble de données de haute qualité.
*   **Itérez :** Le réglage fin est un processus itératif. Entraînez, évaluez, ajustez les données ou les hyperparamètres, répétez.
*   **Surveillance :** Surveillez attentivement les métriques d'entraînement (pertes) et utilisez un ensemble de données de validation pour éviter le surapprentissage.
*   **Évaluation :** Testez toujours le modèle réglé sur des données qu'il n'a *jamais vues* pendant l'entraînement pour évaluer sa capacité de généralisation.
*   **Coût :** N'oubliez pas que le réglage fin et le déploiement des points de terminaison sont payants. Tenez-en compte dans votre budget.
*   **Documentation :** Référez-vous toujours à la documentation officielle du fournisseur de LLM. Les API et les capacités évoluent constamment.
