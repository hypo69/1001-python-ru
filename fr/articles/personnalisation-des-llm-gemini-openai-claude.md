## Aide-mémoire. Personnalisation des LLM : Prompts, réglage fin des modèles, exemples de code.


Dans cet article :

1.  Comment l'"effet de mémoire" est créé dans les LLM (un bref aperçu).
2.  Pourquoi et quand le réglage fin (Fine-tuning) du modèle est nécessaire.
3.  Quand le réglage fin n'est pas la meilleure solution.
4.  Préparation des données.
5.  Exemples de réglage fin pour **OpenAI (GPT)**, **Google (Gemini)** et **Anthropic (Claude)** (diffère).

### 1. Comment les LLM "se souviennent" et "s'adaptent" : L'illusion du contexte

Avant de parler de réglage fin, il est important de comprendre comment les LLM parviennent à créer un sentiment de personnalisation.
Ceci est important pour ne pas se précipiter dans un réglage fin coûteux si la tâche peut être résolue de manière plus simple :

*   Par la **fenêtre de contexte (mémoire à court terme) :** Dans le cadre d'un même dialogue, vous envoyez au modèle non seulement une nouvelle question, mais aussi **tout ou partie de la correspondance précédente**. Le modèle traite tout ce texte comme un seul "contexte". C'est grâce à cela qu'il "se souvient" des remarques précédentes et poursuit la pensée. La limitation ici est la longueur de la fenêtre de contexte (le nombre de jetons).
*   Création d'**instructions système (System Prompt) :** Vous pouvez définir le rôle, le ton, les règles de conduite du modèle au début de chaque dialogue. Par exemple : "Tu es un expert en Python, réponds brièvement".
*   L'inclusion dans la requête de plusieurs exemples du comportement souhaité **Apprentissage en quelques coups (Few-Shot Learning) :** (paires entrée/sortie) permet au modèle d'"apprendre" ce modèle directement dans le cadre de la requête actuelle.
*   **Gestion de l'état côté application :** Le moyen le plus puissant. L'application (qui accède à l'API) peut stocker des informations sur l'utilisateur (préférences, historique, données de profil) et les ajouter dynamiquement au prompt avant de les envoyer au modèle.


### 2.

Le réglage fin est le processus de formation continue d'un LLM de base déjà préparé sur votre propre ensemble de données spécifique. Cela permet au modèle de :

*   **Adapter le style et le ton :** Le modèle parlera "votre langue" - que ce soit un style scientifique strict, un marketing amical ou l'argot d'une communauté spécifique.
*   **Suivre des instructions et des formats spécifiques :** Si vous avez besoin de réponses dans une structure JSON strictement définie, ou toujours avec un ensemble de champs spécifique.
*   **Comprendre le langage spécifique au domaine :** La formation sur votre documentation interne ou des textes de l'industrie aidera le modèle à mieux gérer la terminologie de votre niche.
*   **Améliorer les performances sur des tâches étroites :** Pour certains types de requêtes (par exemple, la classification des avis, la génération de code dans un framework spécifique), le réglage fin peut fournir des réponses plus précises et pertinentes que le modèle de base.
*   **Réduire la longueur des prompts :** Si le modèle "connaît" déjà le comportement souhaité grâce au réglage, vous n'avez pas besoin de le lui rappeler à chaque fois dans le prompt, ce qui économise des jetons et réduit la latence.

### 3.

Le réglage fin est un outil puissant, mais pas universel. Vous ne devriez pas l'utiliser si :

*   **Le modèle doit accéder à de nouvelles connaissances :** Le réglage fin modifie les poids du modèle, mais ne "charge" pas de nouveaux faits en temps réel. Si votre tâche consiste à répondre à des questions basées sur une base de connaissances en constante évolution (documents d'entreprise, dernières nouvelles), il est préférable d'utiliser la **Génération Augmentée par Récupération (RAG)**. Ici, le modèle de base reçoit le contexte de votre base de données *au moment de la requête*.
*   **Une tâche simple est résolue par l'ingénierie de prompts :** Commencez toujours par l'ingénierie de prompts la plus efficace possible. Si la tâche est résolue avec des instructions simples et des exemples few-shot, le réglage fin est redondant et plus coûteux.
*   **Vous ne disposez pas de suffisamment de données de haute qualité :** De mauvaises données = un mauvais modèle réglé.

### 4. Préparation des données.

La qualité et la quantité de vos données sont essentielles. Le modèle apprend de vos exemples, ils doivent donc être précis, variés et cohérents.

*   **Format :** Le plus souvent JSON Lines (`.jsonl`) ou CSV (`.csv`).
*   **Structure des données :** Dépend de la tâche.
    *   **Réglage des instructions (Instruction-Réponse) :** Convient aux tâches généralisées de type "question-réponse", paraphrase, résumé.
        ```json
        {"input_text": "Paraphraser la phrase : 'La technologie de l'IA se développe rapidement.'", "output_text": "L'intelligence artificielle fait des progrès rapides."}
        {"input_text": "Nommez la capitale de la France.", "output_text": "La capitale de la France est Paris."}
        ```
    *   **Réglage du chat (Chat Tuning) :** Idéal pour entraîner le modèle à mener un dialogue dans un rôle ou un style spécifique.
        ```json
        {"messages": [{"author": "user", "content": "Salut ! Que recommandes-tu pour le dîner ?"}, {"author": "model", "content": "Bonsoir ! Aujourd'hui est un grand jour pour les pâtes à la carbonara, ou, si vous préférez quelque chose de léger, une salade César."}]}
        {"messages": [{"author": "user", "content": "Parlez-moi des nouvelles fonctionnalités de Python 3.12."}, {"author": "model", "content": "Python 3.12 a introduit les f-strings indentées, une nouvelle syntaxe pour les génériques universels et une meilleure gestion des erreurs Unicode."}]}
        ```
*   **Quantité :** Un minimum de 100 à 200 exemples de haute qualité, mais plus il y en a, mieux c'est (des milliers pour les tâches sérieuses).
*   **Qualité :** Précision, cohérence du style, du ton, du format dans l'ensemble de l'ensemble de données.

### 5. Modèles et plateformes


#### 5.1. OpenAI

OpenAI fournit une API assez simple et intuitive pour le réglage fin.

**Processus :**

1.  Préparez les données au format JSONL, où chaque ligne est un objet avec un tableau de `messages` (comme dans l'API Chat Completions).
2.  Téléchargez le fichier de données via l'API.
3.  Créez une tâche de réglage fin, en spécifiant le fichier téléchargé et le modèle de base.
4.  Suivez les progrès.
5.  Utilisez le nouveau modèle réglé par son ID.

**Exemple de données (fichier `training_data.jsonl`) :**

```json
{"messages": [{"role": "system", "content": "Vous êtes un assistant de support client amical d'une société informatique."}, {"role": "user", "content": "Mon internet ne fonctionne pas."}, {"role": "assistant", "content": "Oh, je suis désolé pour le désagrément ! Essayons de comprendre. Comment êtes-vous connecté à Internet – par Wi-Fi ou par câble ?"}]}
{"messages": [{"role": "system", "content": "Vous êtes un assistant de support client amical d'une société informatique."}, {"role": "user", "content": "Comment puis-je réinitialiser mon mot de passe ?"}, {"role": "assistant", "content": "Bien sûr ! Pour réinitialiser votre mot de passe, veuillez vous rendre sur la page de connexion et cliquer sur 'Mot de passe oublié ?' sous le champ de saisie. Suivez ensuite les instructions à l'écran."}]
```

**Exemple de code Python :**

Tout d'abord, installez : `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Définissez votre clé API OpenAI. Il est recommandé d'utiliser une variable d'environnement.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Téléchargement du fichier de données
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Fichier téléchargé avec succès. ID du fichier : {file_id}")
except openai.APIStatusError as e:
    print(f"Erreur lors du téléchargement du fichier : {e.status_code} - {e.response}")
    exit()

# 2. Création d'une tâche de réglage fin
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Vous pouvez spécifier une version spécifique, par exemple, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Tâche de réglage fin créée. ID de la tâche : {job_id}")
    print("Suivez l'état de la tâche via l'API ou dans OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Erreur lors de la création de la tâche : {e.status_code} - {e.response}")
    exit()

# Exemple de suivi de l'état et d'obtention du nom du modèle (à exécuter après la création de la tâche) :
# # job_id = "ftjob-..." # Remplacez par l'ID de votre tâche
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"État actuel de la tâche : {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nom du modèle réglé : {fine_tuned_model_name}")

# 3. Utilisation du modèle réglé (après qu'il soit prêt)
# # Remplacez par le nom réel de votre modèle, obtenu après un réglage fin réussi
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "J'ai un problème avec ma connexion."}
# #             ]
# #         )
# #         print("\nRéponse du modèle réglé :")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Erreur lors de l'utilisation du modèle : {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **ne fournit pas d'API publique pour le réglage fin de ses modèles Claude 3 (Opus, Sonnet, Haiku) dans le même sens qu'OpenAI ou Google.**

Anthropic se concentre sur la création de modèles de base très puissants qui, selon eux, fonctionnent très bien avec l'ingénierie de prompts avancée et les modèles RAG, minimisant le besoin de réglage fin dans la plupart des cas.
Pour les grands clients d'entreprise ou les partenaires, il peut exister des programmes pour créer des modèles "personnalisés" ou des intégrations spécialisées, mais ce n'est pas une fonctionnalité de réglage fin accessible au public via l'API.

Si vous travaillez avec Claude 3, votre objectif principal devrait être :

*   **Ingénierie de prompts de qualité :** Expérimentez avec des instructions système, des exemples few-shot et un formatage clair des requêtes. Claude est connu pour sa capacité à suivre strictement les instructions, en particulier dans les balises XML.
*   **Systèmes RAG :** Utilisez des bases de connaissances externes pour fournir au modèle un contexte à jour.

#### 5.3. Google (Gemini)

Google développe activement les capacités de réglage fin via sa plateforme **Google Cloud Vertex AI**.
Il s'agit d'une plateforme ML complète qui fournit des outils pour la préparation des données, l'exécution de tâches de formation et le déploiement de modèles.
Le réglage fin est disponible pour la famille de modèles Gemini.

**Processus :**

1.  Préparez les données (JSONL ou CSV) au format `input_text`/`output_text` (pour le réglage des instructions) ou `messages` (pour le réglage du chat).
2.  Téléchargez les données sur Google Cloud Storage (GCS).
3.  Créez et exécutez une tâche de réglage fin via la console Vertex AI ou le SDK.
4.  Déployez le modèle réglé sur un point de terminaison (Endpoint).
5.  Utilisez le modèle réglé via ce point de terminaison.

**Exemple de données (fichier `gemini_tuning_data.jsonl`) :**

```json
{"input_text": "Résumez les idées principales de ce livre : 'Le livre parle du voyage d'un héros, surmontant les obstacles et se trouvant lui-même.'", "output_text": "Le personnage principal du livre entreprend un voyage transformateur, faisant face à des difficultés et acquérant la connaissance de soi."}
{"input_text": "Expliquez le principe d'un réacteur thermonucléaire en termes simples.", "output_text": "Un réacteur thermonucléaire tente de reproduire le processus qui se produit sur le Soleil : la fusion de noyaux atomiques légers à des températures très élevées, libérant une énorme quantité d'énergie."}
```

**Exemple de code Python (nécessite `google-cloud-aiplatform`) :**

Tout d'abord, installez : `pip install google-cloud-aiplatform` et `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Paramètres ---
# REMPLACEZ par vos valeurs :
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Choisissez une région qui prend en charge Gemini et Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Le nom de votre bucket GCS (doit être créé au préalable)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Fin des paramètres ---

# Initialiser Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Créer un fichier de données (s'il n'existe pas)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Résumez les idées principales de ce livre : \'Le livre parle du voyage d\'un héros, surmontant les obstacles et se trouvant lui-même.\'", "output_text": "Le personnage principal du livre entreprend un voyage transformateur, faisant face à des difficultés et acquérant la connaissance de soi."}\n')
    f.write('{"input_text": "Expliquez le principe d\'un réacteur thermonucléaire en termes simples.", "output_text": "Un réacteur thermonucléaire tente de reproduire le processus qui se produit sur le Soleil : la fusion de noyaux atomiques légers à des températures très élevées, libérant une énorme quantité d\'énergie."}\n')
print(f"Fichier de données '{DATA_FILE_LOCAL_PATH}' créé.")


# 2. Télécharger les données sur Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Télécharge un fichier dans le bucket GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Fichier '{source_file_name}' téléchargé sur 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Erreur lors du téléchargement du fichier sur GCS. Assurez-vous que le bucket existe et que vous avez les autorisations : {e}")
    exit()

# 3. Créer et exécuter une tâche de réglage fin
print(f"\nDémarrage du réglage fin du modèle '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` démarre la tâche et renvoie le modèle réglé après l'achèvement
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Modèle de base Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Nombre d'étapes de formation. La valeur optimale dépend de la taille des données.
        # batch_size=16, # Vous pouvez spécifier
        # learning_rate_multiplier=1.0 # Vous pouvez spécifier
    )
    print(f"Modèle '{TUNED_MODEL_DISPLAY_NAME}' réglé avec succès. ID du modèle : {tuned_model.name}")
    print("Le processus de réglage fin peut prendre un temps considérable.")
except Exception as e:
    print(f"Erreur de réglage fin. Vérifiez les journaux dans la console Vertex AI : {e}")
    exit()

# 4. Déployer le modèle réglé (pour utilisation)
print(f"\nDéploiement du modèle réglé '{TUNED_MODEL_DISPLAY_NAME}' sur un point de terminaison...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Type de machine pour le point de terminaison. Choisissez-en un approprié.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Modèle déployé sur le point de terminaison : {endpoint.name}")
    print("Le déploiement peut également prendre plusieurs minutes.")
except Exception as e:
    print(f"Erreur lors du déploiement du modèle : {e}")
    exit()

# 5. Utiliser le modèle réglé
print("\nTest du modèle réglé...")
prompt = "Parlez-moi de vos capacités après la formation."
instances = [{"prompt": prompt}] # Pour le réglage des instructions. Si réglage du chat, alors {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nRéponse du modèle réglé :")
    print(response.predictions[0])
except Exception as e:
    print(f"Erreur lors de l'utilisation du modèle réglé : {e}")

# Après avoir terminé le travail, n'oubliez pas de supprimer le point de terminaison et le modèle pour éviter des coûts inutiles :
# endpoint.delete()
# tuned_model.delete()
```

### 6. Recommandations générales

*   **Commencez petit :** N'essayez pas d'entraîner immédiatement un modèle sur des milliers d'exemples. Commencez avec un ensemble de données petit mais de haute qualité.
*   **Itérez :** Le réglage fin est un processus itératif. Entraînez, évaluez, ajustez les données ou les hyperparamètres, répétez.
*   **Surveillance :** Surveillez attentivement les métriques de formation (perte) et utilisez un ensemble de données de validation pour éviter le surajustement.
*   **Évaluation :** Testez toujours le modèle réglé sur des données qu'il n'a *jamais vues* pendant la formation pour évaluer sa capacité de généralisation.
*   **Coût :** N'oubliez pas que le réglage fin et le déploiement de points de terminaison sont des services payants. Tenez-en compte dans votre budget.
*   **Documentation :** Consultez toujours la documentation officielle du fournisseur de LLM. Les API et les fonctionnalités évoluent constamment.
