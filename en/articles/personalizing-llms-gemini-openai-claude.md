## Cheatsheet: Personalizing LLMs: Prompts, Fine-tuning Models, Code Examples.


In this article:

1.  How the "memory effect" is created in LLMs (a brief overview).
2.  Why and when model fine-tuning is necessary.
3.  When fine-tuning is not the best solution.
4.  Data preparation.
5.  Fine-tuning examples for **OpenAI (GPT)**, **Google (Gemini)**, and **Anthropic (Claude)** (differs).

### 1. How LLMs "Remember" and "Adapt": The Illusion of Context

Before talking about fine-tuning, it is important to understand how LLMs manage to create a sense of personalization in the first place.
This is important so as not to rush into expensive fine-tuning if the task can be solved in simpler ways:

*   Through the **Context Window (Short-Term Memory):** Within a single dialogue, you send the model not only a new question, but also **all or part of the previous correspondence**. The model processes all this text as a single "context". It is thanks to this that it "remembers" previous remarks and continues the thought. The limitation here is the length of the context window (the number of tokens).
*   Creating **System Prompts:** You can set the model's role, tone, and rules of conduct at the beginning of each dialogue. For example: "You are a Python expert, answer briefly."
*   Including several examples of desired behavior in the query **Few-Shot Learning:** (input/output pairs) allows the model to "learn" this pattern directly within the current query.
*   **State management on the application side:** The most powerful way. The application (which accesses the API) can store information about the user (preferences, history, profile data) and dynamically add it to the prompt before sending it to the model.


### 2. 

Fine-tuning is the process of further training an already prepared base LLM on your own, specific dataset. This allows the model to:

*   **Adapt style and tone:** The model will speak "in your language" – whether it be a strict scientific, friendly marketing, or the slang of a specific community.
*   **Follow specific instructions and formats:** If you need answers in a strictly defined JSON structure, or always with a specific set of fields.
*   **Understand domain-specific language:** Training on your internal documentation or industry texts will help the model better handle the terminology of your niche.
*   **Improve performance on narrow tasks:** For certain types of queries (e.g., classifying reviews, generating code in a specific framework), fine-tuning can provide more accurate and relevant answers than the base model.
*   **Reduce the length of prompts:** If the model already "knows" the desired behavior thanks to tuning, you do not need to remind it of this in the prompt every time, which saves tokens and reduces latency.

### 3. 

Fine-tuning is a powerful, but not universal, tool. You should not use it if:

*   **The model needs to access new knowledge:** Fine-tuning changes the model's weights, but does not "load" new facts into it in real time. If your task is to answer questions based on a constantly changing knowledge base (company documents, latest news), it is better to use **Retrieval Augmented Generation (RAG)**. Here, the base model receives context from your database *at the time of the query*.
*   **A simple task is solved by prompt engineering:** Always start with the most effective prompt engineering. If the task is solved with simple instructions and few-shot examples, fine-tuning is redundant and more costly.
*   **You do not have enough high-quality data:** Bad data = bad tuned model.

### 4. Data Preparation. 

The quality and quantity of your data are critical. The model learns from your examples, so they must be accurate, diverse, and consistent.

*   **Format:** Most often JSON Lines (`.jsonl`) or CSV (`.csv`).
*   **Data structure:** Depends on the task.
    *   **Instruction Tuning (Instruction-Response):** Suitable for generalized tasks like "question-answer", paraphrasing, summarization.
        ```json
        {"input_text": "Paraphrase the sentence: 'AI technology is developing rapidly.'", "output_text": "Artificial intelligence is demonstrating rapid progress."}
        {"input_text": "Name the capital of France.", "output_text": "The capital of France is Paris."}
        ```
    *   **Chat Tuning:** Ideal for training the model to conduct a dialogue in a specific role or style.
        ```json
        {"messages": [{"author": "user", "content": "Hi! What would you recommend for dinner?"}, {"author": "model", "content": "Good evening! Today is a great day for Pasta Carbonara, or, if you prefer something light, a Caesar salad."}]}
        {"messages": [{"author": "user", "content": "Tell me about the new features in Python 3.12."}, {"author": "model", "content": "Python 3.12 introduced indented f-strings, a new syntax for universal generics, and improved handling of Unicode errors."}]}
        ```
*   **Quantity:** A minimum of 100-200 high-quality examples, but the more the better (thousands for serious tasks).
*   **Quality:** Accuracy, consistency of style, tone, format throughout the dataset.

### 5. Models and Platforms


#### 5.1. OpenAI

OpenAI provides a fairly simple and intuitive API for fine-tuning.

**Process:**

1.  Prepare data in JSONL format, where each line is an object with an array of `messages` (as in the Chat Completions API).
2.  Upload the data file via the API.
3.  Create a fine-tuning job, specifying the uploaded file and the base model.
4.  Track progress.
5.  Use the new, tuned model by its ID.

**Data Example (`training_data.jsonl` file):**

```json
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I'm sorry for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly IT company customer support assistant."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the instructions on the screen."}]}
```

**Python Code Example:**

First, install: `pip install openai`

```python
import openai
from openai import OpenAI
import os

# Set your OpenAI API key. It is recommended to use an environment variable.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Uploading the data file
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"File uploaded successfully. File ID: {file_id}")
except openai.APIStatusError as e:
    print(f"Error uploading file: {e.status_code} - {e.response}")
    exit()

# 2. Creating a fine-tuning job
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # You can specify a specific version, e.g., "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Fine-tuning job created. Job ID: {job_id}")
    print("Track the job status via the API or in the OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Error creating job: {e.status_code} - {e.response}")
    exit()

# Example of tracking the status and getting the model name (run after creating the job):
# # job_id = "ftjob-..." # Replace with your job ID
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Current job status: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Tuned model name: {fine_tuned_model_name}")

# 3. Using the tuned model (after it is ready)
# # Replace with the real name of your model, obtained after successful fine-tuning
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "I have a problem with my login."}
# #             ]
# #         )
# #         print("\nTuned model response:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Error using the model: {e.status_code} - {e.response}")
```

#### 5.2. Anthropic

Anthropic **does not provide a public API for fine-tuning its Claude 3 models (Opus, Sonnet, Haiku) in the same sense that OpenAI or Google do.**

Anthropic is focused on creating very powerful base models that, they claim, work great with advanced prompt engineering and RAG patterns, minimizing the need for fine-tuning in most cases.
For large corporate clients or partners, there may be programs to create "custom" models or specialized integrations, but this is not a publicly available fine-tuning feature via the API.

If you are working with Claude 3, your main focus should be on:

*   **Quality prompt engineering:** Experiment with system instructions, few-shot examples, and clear query formatting. Claude is known for its ability to strictly follow instructions, especially in XML tags.
*   **RAG systems:** Use external knowledge bases to provide the model with up-to-date context.

#### 5.3. Google (Gemini)

Google is actively developing fine-tuning capabilities through its **Google Cloud Vertex AI** platform.
This is a full-fledged ML platform that provides tools for data preparation, running training jobs, and deploying models.
Fine-tuning is available for the Gemini family of models.

**Process:**

1.  Prepare data (JSONL or CSV) in `input_text`/`output_text` format (for instruction tuning) or `messages` (for chat tuning).
2.  Upload data to Google Cloud Storage (GCS).
3.  Create and run a fine-tuning job via the Vertex AI Console or SDK.
4.  Deploy the tuned model to an Endpoint.
5.  Use the tuned model via this endpoint.

**Data Example (`gemini_tuning_data.jsonl` file):**

```json
{"input_text": "Summarize the main ideas of this book: 'The book is about a hero's journey, overcoming obstacles and finding himself.'", "output_text": "The main character of the book goes on a transformative journey, facing difficulties and gaining self-knowledge."}
{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor tries to reproduce the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}
```

**Python Code Example (requires `google-cloud-aiplatform`):**

First, install: `pip install google-cloud-aiplatform` and `pip install google-cloud-storage`

```python
import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Settings ---
# REPLACE with your values:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Choose a region that supports Gemini and Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # The name of your GCS bucket (must be created beforehand)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- End of settings ---

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Create a data file (if it doesn't exist)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Summarize the main ideas of this book: \'The book is about a hero\'s journey, overcoming obstacles and finding himself.\'", "output_text": "The main character of the book goes on a transformative journey, facing difficulties and gaining self-knowledge."}\n')
    f.write('{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor tries to reproduce the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing a huge amount of energy."}\n')
print(f"Data file '{DATA_FILE_LOCAL_PATH}' created.")


# 2. Upload data to Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the GCS bucket."""
    storage_client = storage.Client(project=PROJECT_ID)
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print(f"File '{source_file_name}' uploaded to 'gs://{bucket_name}/{destination_blob_name}'.")

try:
    upload_blob(BUCKET_NAME, DATA_FILE_LOCAL_PATH, DATA_FILE_LOCAL_PATH)
except Exception as e:
    print(f"Error uploading file to GCS. Make sure the bucket exists and you have permissions: {e}")
    exit()

# 3. Create and run a fine-tuning job
print(f"\nStarting fine-tuning of the model '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` starts the job and returns the tuned model after completion
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Base model Gemini Pro
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Number of training steps. The optimal value depends on the size of the data.
        # batch_size=16, # You can specify
        # learning_rate_multiplier=1.0 # You can specify
    )
    print(f"Model '{TUNED_MODEL_DISPLAY_NAME}' successfully tuned. Model ID: {tuned_model.name}")
    print("The fine-tuning process can take a significant amount of time.")
except Exception as e:
    print(f"Fine-tuning error. Check the logs in the Vertex AI Console: {e}")
    exit()

# 4. Deploy the tuned model (for use)
print(f"\nDeploying the tuned model '{TUNED_MODEL_DISPLAY_NAME}' to an endpoint...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Machine type for the endpoint. Choose a suitable one.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Model deployed to endpoint: {endpoint.name}")
    print("Deployment can also take several minutes.")
except Exception as e:
    print(f"Error deploying the model: {e}")
    exit()

# 5. Use the tuned model
print("\nTesting the tuned model...")
prompt = "Tell me about your capabilities after training."
instances = [{"prompt": prompt}] # For Instruction Tuning. If Chat Tuning, then {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nTuned model response:")
    print(response.predictions[0])
except Exception as e:
    print(f"Error using the tuned model: {e}")

# After finishing work, do not forget to delete the endpoint and the model to avoid unnecessary costs:
# endpoint.delete()
# tuned_model.delete()
```

### 6. General Recommendations

*   **Start small:** Do not try to train a model on thousands of examples right away. Start with a small but high-quality dataset.
*   **Iterate:** Fine-tuning is an iterative process. Train, evaluate, adjust the data or hyperparameters, repeat.
*   **Monitoring:** Carefully monitor the training metrics (loss) and use a validation dataset to avoid overfitting.
*   **Evaluation:** Always test the tuned model on data it has *never seen* during training to assess its generalization ability.
*   **Cost:** Remember that fine-tuning and deploying endpoints are paid services. Take this into account in your budget.
*   **Documentation:** Always consult the official documentation of the LLM provider. APIs and capabilities are constantly evolving.
