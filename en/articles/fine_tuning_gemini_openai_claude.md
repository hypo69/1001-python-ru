## Cheat Sheet. Personalizing LLM: prompts, fine-tuning models, code examples.

In this article:

1.  How the "memory effect" is created in LLM (brief overview).
2.  Why and when fine-tuning a model is needed.
3.  When fine-tuning is not the best solution.
4.  Data preparation.
5.  Fine-tuning examples for **OpenAI (GPT)**, **Google (Gemini)**, and **Anthropic (Claude)** (differs).

### 1. How LLM "remembers" and "adapts": The Illusion of Context

Before talking about fine-tuning, it's important to understand how LLM generally manages to create a sense of personalization.
This is important so as not to rush into expensive fine-tuning if the task can be solved by simpler methods:

*   Through **Context Window (Short-Term Memory):** Within a single dialogue, you send the model not only a new question but also **all or part of the previous correspondence**. The model processes all this text as a single "context". It is thanks to this that it "remembers" previous remarks and continues the thought. The limitation here is the length of the context window (number of tokens).
*   Composing **System Prompts:** You can set the model's role, tone, and behavior rules at the beginning of each dialogue. For example: "You are a Python expert, answer briefly."
*   Including several examples of desired behavior in the request **Few-Shot Learning:** (input/output pairs) allows the model to "learn" this pattern directly within the current request.
*   **Application-side state management:** The most powerful way. The application (which accesses the API) can store user information (preferences, history, profile data) and dynamically add it to the prompt before sending it to the model.

### 2.

Fine-tuning is the process of further training an already prepared base LLM on your own specific dataset. This allows the model to:

*   **Adapt style and tone:** The model will speak "your language" – be it strict scientific, friendly marketing, or the slang of a specific community.
*   **Follow specific instructions and formats:** If you need answers in a strictly defined JSON structure, or always with a specific set of fields.
*   **Understand domain-specific language:** Training on your internal documentation or industry texts will help the model better handle the terminology of your niche.
*   **Improve performance on narrow tasks:** For certain types of queries (e.g., sentiment classification, code generation in a specific framework), fine-tuning can provide more accurate and relevant answers than the base model.
*   **Reduce prompt length:** If the model already "knows" the desired behavior through fine-tuning, you don't need to remind it every time in the prompt, which saves tokens and reduces latency.

### 3.

Fine-tuning is a powerful but not universal tool. You should not use it if:

*   **The model needs to access new knowledge:** Fine-tuning changes the model's weights, but it does not "load" new facts into it in real-time. If your task is to answer questions based on a constantly changing knowledge base (company documents, latest news), it is better to use **Retrieval Augmented Generation (RAG)**. Here, the base model gets context from your database *during query execution*.
*   **A simple task can be solved by prompt engineering:** Always start with the most effective prompt engineering. If the task can be solved with simple instructions and few-shot examples, fine-tuning is redundant and more costly.
*   **You do not have enough high-quality data:** Bad data = bad fine-tuned model.

### 4. Data preparation.

The quality and quantity of your data are critically important. The model learns from your examples, so they must be accurate, diverse, and consistent.

*   **Format:** Most often JSON Lines (<code>.jsonl</code>) or CSV (<code>.csv</code>).
*   **Data structure:** Depends on the task.
    *   **Instruction Tuning (Instruction-Response):** Suitable for generalized tasks such as question-answering, rephrasing, summarization.
        ```json
        {"input_text": "Rephrase the sentence: 'AI technology is developing rapidly.'", "output_text": "Artificial intelligence is demonstrating rapid progress."}
        {"input_text": "Name the capital of France.", "output_text": "The capital of France is Paris."}
        ```
    *   **Chat Tuning (Chat):** Ideal for training the model to conduct a dialogue in a specific role or style.
        ```json
        {"messages": [{"author": "user", "content": "Hi! What do you recommend for dinner?"}, {"author": "model", "content": "Good evening! Today is a great day for pasta Carbonara, or, if you prefer something light, Caesar salad."}]}
        {"messages": [{"author": "user", "content": "Tell me about new features in Python 3.12."}, {"author": "model", "content": "Python 3.12 introduced f-strings with indentation, new syntax for universal generics, and improved Unicode error handling."}]}
        ```
*   **Quantity:** Minimum 100-200 high-quality examples, but the more the better (thousands for serious tasks).
*   **Quality:** Accuracy, consistency of style, tone, and format throughout the dataset.

### 5. Models and platforms

#### 5.1. OpenAI

OpenAI provides a fairly simple and intuitive API for fine-tuning.

**Process:**

1.  Prepare data in JSONL format, where each line is an object with an array of <code>messages</code> (as in the Chat Completions API).
2.  Upload the data file via API.
3.  Create a fine-tuning job, specifying the uploaded file and the base model.
4.  Monitor progress.
5.  Use the new, fine-tuned model by its ID.

**Example data (file <code>training_data.jsonl</code>):**

```json
{"messages": [{"role": "system", "content": "You are a friendly assistant for IT company customer support."}, {"role": "user", "content": "My internet is not working."}, {"role": "assistant", "content": "Oh, I apologize for the inconvenience! Let's try to figure it out. How are you connected to the internet – via Wi-Fi or cable?"}]}
{"messages": [{"role": "system", "content": "You are a friendly assistant for IT company customer support."}, {"role": "user", "content": "How can I reset my password?"}, {"role": "assistant", "content": "Of course! To reset your password, please go to the login page and click 'Forgot password?' below the input field. Then follow the on-screen instructions."}]}
```

**Example Python code:**

Install beforehand: <code>pip install openai</code>

```python
import openai
from openai import OpenAI
import os

# Set your OpenAI API key. It is recommended to use an environment variable.
# os.environ["OPENAI_API_KEY"] = "sk-..."
client = OpenAI()

# 1. Upload data file
try:
    file_response = client.files.create(
        file=open("training_data.jsonl", "rb"),
        purpose="fine-tune"
    )
    file_id = file_response.id
    print(f"File uploaded successfully. File ID: {file_id}")
except openai.APIStatusError as e:
    print(f"File upload error: {e.status_code} - {e.response}")
    exit()

# 2. Create fine-tuning job
try:
    ft_job_response = client.fine_tuning.jobs.create(
        training_file=file_id,
        model="gpt-3.5-turbo" # You can specify a specific version, e.g., "gpt-3.5-turbo-0125"
    )
    job_id = ft_job_response.id
    print(f"Fine-tuning job created. Job ID: {job_id}")
    print("Monitor job status via API or in OpenAI Playground.")
except openai.APIStatusError as e:
    print(f"Job creation error: {e.status_code} - {e.response}")
    exit()

# Example of monitoring status and getting model name (run after job creation):
# # job_id = "ftjob-..." # Replace with your job ID
# # job_status = client.fine_tuning.jobs.retrieve(job_id)
# # print(f"Current job status: {job_status.status}")
# # if job_status.status == "succeeded":
# #     fine_tuned_model_name = job_status.fine_tuned_model
# #     print(f"Fine-tuned model name: {fine_tuned_model_name}")

# 3. Using the fine-tuned model (after it's ready)
# # Replace with the actual name of your model, obtained after successful fine-tuning
# # fine_tuned_model_name = "ft:gpt-3.5-turbo-0125:my-org::abcd123"

# # if 'fine_tuned_model_name' in locals() and fine_tuned_model_name:
# #     try:
# #         response = client.chat.completions.create(
# #             model=fine_tuned_model_name,
# #             messages=[
# #                 {"role": "user", "content": "I have a login issue."}
# #             ]
# #         )
# #         print("\nFine-tuned model response:")
# #         print(response.choices[0].message.content)
# #     except openai.APIStatusError as e:
# #         print(f"Error using model: {e.status_code} - {e.response}")
```
<h4>5.2. Anthropic</h4>
<p>Anthropic <strong>does not provide a public API for fine-tuning its Claude 3 models (Opus, Sonnet, Haiku) in the same sense as OpenAI or Google.</strong></p>
<p>Anthropic focuses on creating very powerful base models that, they claim, work excellently with advanced prompt engineering and RAG patterns, minimizing the need for fine-tuning for most cases.
For large enterprise clients or partners, there may be programs for creating "custom" models or specialized integrations, but this is not a publicly available fine-tuning function via API.</p>
<p>If you are working with Claude 3, your primary focus should be on:</p>
<ul>
<li><strong>High-quality prompt engineering:</strong> Experiment with system instructions, few-shot examples, clear request formatting. Claude is known for its ability to strictly follow instructions, especially in XML tags.</li>
<li><strong>RAG systems:</strong> Use external knowledge bases to provide the model with relevant context.</li>
</ul>
<h4>5.3. Google (Gemini)</h4>
<p>Google is actively developing fine-tuning capabilities through its <strong>Google Cloud Vertex AI</strong> platform.
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
<pre class="line-numbers"><code class="language-json">{"input_text": "Summarize the main ideas of this book: 'The book tells about the journey of a hero who overcomes obstacles and finds himself.'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and gaining self-discovery."}
{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to reproduce the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing enormous amounts of energy."}
</code></pre>
<p><strong>Example Python code (requires <code>google-cloud-aiplatform</code>):</strong></p>
<p>Install beforehand: <code>pip install google-cloud-aiplatform</code> and <code>pip install google-cloud-storage</code></p>
<pre class="line-numbers"><code class="language-python">import os
from google.cloud import aiplatform
from google.cloud import storage

# --- Settings ---
# REPLACE with your values:
PROJECT_ID = "your-gcp-project-id"
REGION = "us-central1"               # Choose a region that supports Gemini and Vertex AI
BUCKET_NAME = "your-gcs-bucket-for-tuning" # Name of your GCS bucket (must be created beforehand)
DATA_FILE_LOCAL_PATH = "gemini_tuning_data.jsonl"
GCS_DATA_URI = f"gs://{BUCKET_NAME}/{DATA_FILE_LOCAL_PATH}"
TUNED_MODEL_DISPLAY_NAME = "my-tuned-gemini-model"
# --- End of settings ---

# Initialize Vertex AI
aiplatform.init(project=PROJECT_ID, location=REGION)

# 1. Create data file (if it doesn't exist)
with open(DATA_FILE_LOCAL_PATH, "w", encoding="utf-8") as f:
    f.write('{"input_text": "Summarize the main ideas of this book: \'The book tells about the journey of a hero who overcomes obstacles and finds himself.\'", "output_text": "The main character of the book embarks on a transformative journey, facing challenges and gaining self-discovery."}\n')
    f.write('{"input_text": "Explain the principle of a thermonuclear reactor in simple terms.", "output_text": "A thermonuclear reactor attempts to reproduce the process that occurs on the Sun: the fusion of light atomic nuclei at very high temperatures, releasing enormous amounts of energy."}\n')
print(f"Data file '{DATA_FILE_LOCAL_PATH}' created.")


# 2. Upload data to Google Cloud Storage
def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to a GCS bucket."""
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

# 3. Create and run fine-tuning job
print(f"\nStarting fine-tuning of model '{TUNED_MODEL_DISPLAY_NAME}'...")
try:
    # `tune_model` starts the job and returns the fine-tuned model upon completion
    tuned_model = aiplatform.Model.tune_model(
        model_display_name=TUNED_MODEL_DISPLAY_NAME,
        source_model_name="gemini-1.0-pro-001", # Base Gemini Pro model
        training_data_path=GCS_DATA_URI,
        tuning_method="SUPERVISED_TUNING",
        train_steps=100, # Number of training steps. Optimal value depends on data size.
        # batch_size=16, # Can be specified
        # learning_rate_multiplier=1.0 # Can be specified
    )
    print(f"Model '{TUNED_MODEL_DISPLAY_NAME}' successfully fine-tuned. Model ID: {tuned_model.name}")
    print("Fine-tuning process may take significant time.")
except Exception as e:
    print(f"Fine-tuning error. Check logs in Vertex AI Console: {e}")
    exit()

# 4. Deploy fine-tuned model (for use)
print(f"\nDeploying fine-tuned model '{TUNED_MODEL_DISPLAY_NAME}' to endpoint...")
try:
    endpoint = tuned_model.deploy(
        machine_type="n1-standard-4", # Machine type for endpoint. Choose appropriate one.
        min_replica_count=1,
        max_replica_count=1
    )
    print(f"Model deployed to endpoint: {endpoint.name}")
    print("Deployment may also take several minutes.")
except Exception as e:
    print(f"Error deploying model: {e}")
    exit()

# 5. Use fine-tuned model
print("\nTesting fine-tuned model...")
prompt = "Tell me about your capabilities after training."
instances = [{"prompt": prompt}] # For Instruction Tuning. If Chat Tuning, then {"messages": [...]}

try:
    response = endpoint.predict(instances=instances)
    print("\nFine-tuned model response:")
    print(response.predictions[0])
except Exception as e:
    print(f"Error using fine-tuned model: {e}")

# After finishing, don't forget to delete the endpoint and model to avoid unnecessary costs:
# endpoint.delete()
# tuned_model.delete()
</code></pre>
<h3>6. General recommendations</h3>
<ul>
<li><strong>Start small:</strong> Don't try to train the model on thousands of examples right away. Start with a small but high-quality dataset.</li>
<li><strong>Iterate:</strong> Fine-tuning is an iterative process. Train, evaluate, adjust data or hyperparameters, repeat.</li>
<li><strong>Monitoring:</strong> Carefully monitor training metrics (loss) and use a validation dataset to avoid overfitting.</li>
<li><strong>Evaluation:</strong> Always test the fine-tuned model on data it has <em>never seen</em> during training to assess its generalization ability.</li>
<li><strong>Cost:</strong> Remember that fine-tuning and deploying endpoints are paid. Factor this into your budget.</li>
<li><strong>Documentation:</strong> Always refer to the official LLM provider's documentation. APIs and capabilities are constantly evolving.</li>
</ul>