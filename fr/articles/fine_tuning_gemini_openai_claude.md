## Aide-mémoire. Personnalisation des LLM : prompts, réglage fin des modèles, exemples de code.

Dans cet article :

1.  Comment l&#39;"effet mémoire" est créé dans les LLM (bref aperçu).
2.  Pourquoi et quand le réglage fin (Fine-tuning) d&#39;un modèle est nécessaire.
3.  Quand le réglage fin n&#39;est pas la meilleure solution.
4.  Préparation des données.
5.  Exemples de réglage fin pour **OpenAI (GPT)**, **Google (Gemini)** et **Anthropic (Claude)** (diffère).

### 1. Comment les LLM "se souviennent" et "s'adaptent" : L'illusion du contexte

Avant de parler du réglage fin, il est important de comprendre comment les LLM parviennent généralement à créer un sentiment de personnalisation.
Ceci est important pour ne pas se lancer dans un réglage fin coûteux si la tâche peut être résolue par des méthodes plus simples :

*   Via la **Fenêtre de Contexte (Mémoire à Court Terme) :** Dans le cadre d&#39;un seul dialogue, vous envoyez au modèle non seulement une nouvelle question, mais aussi **tout ou partie de la correspondance précédente**. Le modèle traite tout ce texte comme un "contexte" unique. C&#39;est grâce à cela qu&#39;il "se souvient" des remarques précédentes et poursuit la pensée. La limitation ici est la longueur de la fenêtre de contexte (nombre de jetons).
*   Composition des **Instructions Système (System Prompt) :** Vous pouvez définir le rôle, le ton et les règles de comportement du modèle au début de chaque dialogue. Par exemple : "Tu es un expert Python, réponds brièvement."
*   Inclusion de plusieurs exemples du comportement souhaité dans la requête **Apprentissage en Quelques Exemples (Few-Shot Learning) :** (paires entrée/sortie) permet au modèle d&#39;"apprendre" ce modèle directement dans la requête actuelle.
*   **Gestion de l&#39;état côté application :** Le moyen le plus puissant. L&#39;application (qui accède à l&#39;API) peut stocker des informations sur l&#39;utilisateur (préférences, historique, données de profil) et les ajouter dynamiquement au prompt avant de l&#39;envoyer au modèle.

### 2.

Le réglage fin est le processus de formation supplémentaire d&#39;un LLM de base déjà préparé sur votre propre ensemble de données spécifique. Cela permet au modèle de :

*   **Adapter le style et le ton :** Le modèle parlera "votre langue" – qu&#39;il s&#39;agisse d&#39;un langage scientifique strict, d&#39;un marketing amical ou de l&#39;argot d&#39;une communauté spécifique.
*   **Suivre des instructions et des formats spécifiques :** Si vous avez besoin de réponses dans une structure JSON strictement définie, ou toujours avec un ensemble de champs spécifique.
*   **Comprendre le langage spécifique au domaine :** La formation sur votre documentation interne ou vos textes industriels aidera le modèle à mieux gérer la terminologie de votre niche.
*   **Améliorer les performances sur des tâches spécifiques :** Pour certains types de requêtes (par exemple, la classification des sentiments, la génération de code dans un framework spécifique), le réglage fin peut fournir des réponses plus précises et pertinentes que le modèle de base.
*   **Réduire la longueur des prompts :** Si le modèle "connaît" déjà le comportement souhaité grâce au réglage, vous n&#39;avez pas besoin de le lui rappeler à chaque fois dans le prompt, ce qui économise des jetons et réduit la latence.

### 3.

Le réglage fin est un outil puissant mais non universel. Vous ne devriez pas l&#39;utiliser si :

*   **Le modèle doit accéder à de nouvelles connaissances :** Le réglage fin modifie les poids du modèle, mais il ne "charge" pas de nouveaux faits en temps réel. Si votre tâche est de répondre à des questions basées sur une base de connaissances en constante évolution (documents d&#39;entreprise, dernières nouvelles), il est préférable d&#39;utiliser la **Génération Augmentée par Récupération (RAG)**. Ici, le modèle de base obtient le contexte de votre base de données *pendant l&#39;exécution de la requête*.
*   **Une tâche simple peut être résolue par l&#39;ingénierie de prompts :** Commencez toujours par l&#39;ingénierie de prompts la plus efficace. Si la tâche peut être résolue avec des instructions simples et des exemples en quelques coups, le réglage fin est redondant et plus coûteux.
*   **Vous ne disposez pas de suffisamment de données de haute qualité :** De mauvaises données = un modèle mal réglé.

### 4. Préparation des données.

La qualité et la quantité de vos données sont d&#39;une importance capitale. Le modèle apprend de vos exemples, ils doivent donc être précis, diversifiés et cohérents.

*   **Format :** Le plus souvent JSON Lines (<code>.jsonl</code>) ou CSV (<code>.csv</code>).
*   **Structure des données :** Dépend de la tâche.
    *   **Réglage d&#39;instructions (Instruction Tuning - Instruction-Réponse) :** Convient aux tâches généralisées telles que les questions-réponses, la reformulation, la synthèse.
        ```json
        {"input_text": "Reformulez la phrase : 'La technologie de l&#39;IA se développe rapidement.'", "output_text": "L&#39;intelligence artificielle progresse rapidement."}
        {"input_text": "Nommez la capitale de la France.", "output_text": "La capitale de la France est Paris."}
        ```
    *   **Réglage de chat (Chat Tuning - Chat) :** Idéal pour entraîner le modèle à mener un dialogue dans un rôle ou un style spécifique.
        ```json
        {"messages": [{"author": "user", "content": "Salut ! Que me recommandez-vous pour le dîner ?"}, {"author": "model", "content": "Bonsoir ! Aujourd&#39;hui est un excellent jour pour des pâtes Carbonara, ou, si vous préférez quelque chose de léger, une salade César."}]}
        {"messages": [{"author": "user", "content": "Parlez-moi des nouvelles fonctionnalités de Python 3.12."}, {"author": "model", "content": "Python 3.12 a introduit les f-strings avec indentation, une nouvelle syntaxe pour les génériques universels et une meilleure gestion des erreurs Unicode."}]}
        ```
*   **Quantité :** Minimum 100-200 exemples de haute qualité, mais plus il y en a, mieux c&#39;est (des milliers pour des tâches sérieuses).
*   **Qualité :** Précision, cohérence du style, du ton et du format dans l&#39;ensemble des données.

### 5. Modèles et plateformes

#### 5.1. OpenAI

OpenAI fournit une API assez simple et intuitive pour le réglage fin.

**Processus :**

1.  Préparez les données au format JSONL, où chaque ligne est un objet avec un tableau de <code>messages</code> (comme dans l&#39;API Chat Completions).
2.  Téléchargez le fichier de données via l&#39;API.
3.  Créez une tâche de réglage fin, en spécifiant le fichier téléchargé et le modèle de base.
4.  Surveillez la progression.
5.  Utilisez le nouveau modèle réglé par son ID.

**Exemple de données (fichier <code>training_data.jsonl</code>) :**

```json
{"messages": [{"role": "system", "content": "Vous êtes un assistant amical pour le support client d&#39;une entreprise informatique."}, {"role": "user", "content": "Mon internet ne fonctionne pas."}, {"role": "assistant", "content": "Oh, je m&#39;excuse pour le désagrément ! Essayons de comprendre. Comment êtes-vous connecté à internet – via Wi-Fi ou par câble ?"}]}
{"messages": [{"role": "system", "content": "Vous êtes un assistant amical pour le support client d&#39;une entreprise informatique."}, {"role": "user", "content": "Comment puis-je réinitialiser mon mot de passe ?"}, {"role": "assistant", "content": "Bien sûr ! Pour réinitialiser votre mot de passe, veuillez vous rendre sur la page de connexion et cliquer sur 'Mot de passe oublié ?' sous le champ de saisie. Suivez ensuite les instructions à l&#39;écran."}]}
```

**Exemple de code Python :**

Installez au préalable : <code>pip install openai</code>

```python
import openai
from openai import OpenAI
import os

# Définissez votre clé API OpenAI. Il est recommandé d&#39;utiliser une variable d&#39;environnement.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Télécharger le fichier de données
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"Fichier téléchargé avec succès. ID du fichier : {file_id}")
except openai.APIStatusError as e:
    print(f"Erreur de téléchargement du fichier : {e.status_code} - {e.response}")
    exit()

# 2. Créer une tâche de réglage fin
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # Vous pouvez spécifier une version spécifique, par exemple, "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Tâche de réglage fin créée. ID de la tâche : {job_id}")
    print("Surveillez l&#39;état de la tâche via l&#39;API ou dans OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Erreur de création de la tâche : {e.status_code} - {e.response}")
    exit()

# Exemple de surveillance de l&#39;état et d&#39;obtention du nom du modèle (à exécuter après la création de la tâche) :
# # job_id = "ftjob-..." # Remplacez par l&#39;ID de votre tâche
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"État actuel de la tâche : {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Nom du modèle réglé : {fine_tuned_model_name}")

# 3. Utilisation du modèle réglé (une fois qu&#39;il est prêt)
# # Remplacez par le nom réel de votre modèle, obtenu après un réglage fin réussi
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "J&#39;ai un problème de connexion."}
# #             ]
# #         )
# #         print("\nRéponse du modèle réglé :")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Erreur lors de l&#39;utilisation du modèle : {e.status_code} - {e.response}")
```</pre>
<h4>5.2. Anthropic</h4>
<p>Anthropic <strong>ne fournit pas d&#39;API publique pour le réglage fin de ses modèles Claude 3 (Opus, Sonnet, Haiku) dans le même sens qu&#39;OpenAI ou Google.</strong></p>
<p>Anthropic se concentre sur la création de modèles de base très puissants qui, selon eux, fonctionnent parfaitement avec l&#39;ingénierie de prompts avancée et les modèles RAG, minimisant le besoin de réglage fin dans la plupart des cas.
Pour les grands clients d&#39;entreprise ou les partenaires, il peut exister des programmes pour créer "custom" modèles ou intégrations spécialisées, mais ce n&#39;est pas une fonction de réglage fin disponible publiquement via l&#39;API.</p>
<p>If you are working with Claude 3, your primary focus should be on:</p>
<ul>
<li><strong>High-quality prompt engineering:</strong> Experiment with system instructions, few-shot examples, clear request formatting. Claude is known for its ability to strictly follow instructions, especially in XML tags.</li>
<li><strong>RAG systems:</strong> Use external knowledge bases to provide the model with relevant context.</li>
</ul>
<h4>5.3. Google (Gemini)</h4>
<p>Google développe activement les capacités de réglage fin via sa plateforme <strong>Google Cloud Vertex AI</strong>.
This is a full-fledged ML platform that provides tools for data preparation, running training jobs, and deploying models.
Fine-tuning is available for the Gemini family of models.</p>
<p><strong>Process:</strong></p>
<ol>
<li>Prepare data (JSONL or CSV) in <code>input_text</code>/<code>output_text</code> format (for instruction tuning) or <code>messages</code> (for chat tuning).</li>
<li>Upload data to Google Cloud Storage (GCS).</li>
<li>Create and run a fine-tuning job via the Vertex AI Console or SDK.</li>
<li>Deploy the fine-tuned model to an Endpoint.</li>
<li>Use the fine-tuned model via this Endpoint.</li>
</ol>
<p><strong>Example data (file <code>gemini_tuning_data.jsonl</code>):</strong></p>
<pre class="line-numbers"><code class="language-json">{"input_text": "Résumez les idées principales de ce livre : 'Le livre raconte le voyage d&#39;un héros qui surmonte les obstacles et se trouve lui-même.'", "output_text": "Le personnage principal du livre se lance dans un voyage transformateur, faisant face à des défis et acquérant la découverte de soi."}</code></pre>
<pre class="line-numbers"><code class="language-json">{"input_text": "Expliquez le principe d&#39;un réacteur thermonucléaire en termes simples.", "output_text": "Un réacteur thermonucléaire tente de reproduire le processus qui se produit sur le Soleil : la fusion de noyaux atomiques légers à très hautes températures, libérant d&#39;énormes quantités d&#39;énergie."}</code></pre>
<p><strong>Example Python code (nécessite <code>google-cloud-aiplatform</code>):</strong></p>
<p>Installez au préalable : <code>pip install google-cloud-aiplatform</code> et <code>pip install google-cloud-storage</code></p>
<pre class="line-numbers"><code class="language-python">import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Paramètres ---
# REMPLACEZ par vos valeurs :
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Choisissez une région qui prend en charge Gemini et Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Nom de votre bucket GCS (doit être créé au préalable)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- Fin des paramètres ---

# Initialiser Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Créer le fichier de données (s&#39;il n&#39;existe pas)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Résumez les idées principales de ce livre : \'Le livre raconte le voyage d\'un héros qui surmonte les obstacles et se trouve lui-même.'", "output_text": "Le personnage principal du livre se lance dans un voyage transformateur, faisant face à des défis et acquérant la découverte de soi."}\n')
    f.write('{"input_text": "Expliquez le principe d&#39;un réacteur thermonucléaire en termes simples.", "output_text": "Un réacteur thermonucléaire tente de reproduire le processus qui se produit sur le Soleil : la fusion de noyaux atomiques légers à très hautes températures, libérant d&#39;énormes quantités d&#39;énergie."}\n')
print(f"Fichier de données '{DATA_FILE_LOCAL_PATH}' créé.")


# 2. Télécharger les données vers Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Télécharge un fichier vers un bucket GCS."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"Fichier '{source_file_name}' téléchargé vers 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Erreur lors du téléchargement du fichier vers GCS. Assurez-vous que le bucket existe et que vous avez les autorisations : {e}")
    exit()

# 3. Créer et exécuter une tâche de réglage fin
print(f"\nDémarrage du réglage fin du modèle '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` démarre la tâche et renvoie le modèle réglé une fois terminé
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Modèle de base Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Nombre d&#39;étapes d&#39;entraînement. La valeur optimale dépend de la taille des données.
        # batch_size=16, # Peut être spécifié
        # learning_rate_multiplier=1.0 # Peut être spécifié
    )
    print(f"Modèle '{TUNED_MODEL_DISPLAY_NAME}' réglé avec succès. ID du modèle : {tuned_model.name}")
    print("Le processus de réglage fin peut prendre un temps considérable.")
except Exception as e:
    print(f"Erreur de réglage fin. Vérifiez les journaux dans la console Vertex AI : {e}")
    exit()

# 4. Déployer le modèle réglé (pour utilisation)
print(f"\nDéploiement du modèle réglé '{TUNED_MODEL_DISPLAY_NAME}' sur le point de terminaison...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Type de machine pour le point de terminaison. Choisissez le plus approprié.
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
prompt = "Parlez-moi de vos capacités après l&#39;entraînement."
instances = [{"prompt": prompt}] # Pour le réglage d&#39;instructions. Si réglage de chat, alors {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nRéponse du modèle réglé :")
    print(response.predictions[0])
except Exception as e:
    print(f"Erreur lors de l&#39;utilisation du modèle réglé : {e}")

# Après avoir terminé, n&#39;oubliez pas de supprimer le point de terminaison et le modèle pour éviter les coûts inutiles :
# endpoint.delete()
# tuned_model.delete()
</code></pre>
<h3>6. Recommandations générales</h3>
<ul>
<li><strong>Commencez petit :</strong> N&#39;essayez pas d&#39;entraîner le modèle sur des milliers d&#39;exemples tout de suite. Commencez par un ensemble de données petit mais de haute qualité.</li>
<li><strong>Itérez :</strong> Le réglage fin est un processus itératif. Entraînez, évaluez, ajustez les données ou les hyperparamètres, répétez.</li>
<li><strong>Surveillance :</strong> Surveillez attentivement les métriques d&#39;entraînement (perte) et utilisez un ensemble de données de validation pour éviter le surapprentissage.</li>
<li><strong>Évaluation :</strong> Testez toujours le modèle réglé sur des données qu&#39;il n&#39;a *jamais vues* pendant l&#39;entraînement pour évaluer sa capacité de généralisation.</li>
<li><strong>Coût :</strong> N&#39;oubliez pas que le réglage fin et le déploiement des points de terminaison sont payants. Tenez-en compte dans votre budget.</li>
<li><strong>Documentation :</strong> Référez-vous toujours à la documentation officielle du fournisseur de LLM. Les API et les capacités évoluent constamment.</li>
</ul>