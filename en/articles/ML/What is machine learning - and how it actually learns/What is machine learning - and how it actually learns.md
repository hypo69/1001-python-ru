# What is machine learning — and how does it actually "learn"?
![1](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/1.png)

*Four cats on which machine learning rests*

How does machine learning differ from traditional programming with its "it works until you touch it"? Where do clear algorithms end — and where does the magic of the "black box" begin, as in the case of ChatGPT?

*This is the first article in a popular science series where we will analyze the basics of AI — without empty words, without clichés, without academic fog, and, ideally, without equations (as Stephen Hawking once wrote: every formula in a popular science book halves its sales).*

Today we will talk about the very foundation: what types of learning AI models use, why they are needed at all, and how they determine what a model is capable of.

Yes, there will be cats. And a little sarcasm. But exclusively for noble purposes — to create strong and memorable associations.

This article is for everyone who is starting to get acquainted with AI: for technical and non-technical readers, solution architects, startup founders, experienced developers, and everyone who wants to finally form a clear mental picture of what machine learning is and where it all begins.

In this part, we will cover the basics:
What ML is, how it fundamentally differs from traditional programming, and four key learning paradigms that underpin the entire modern AI landscape.

#### Classical programming vs. machine learning

If you are already confident in your understanding of how machine learning differs from traditional programming, feel free to skip this section. But if you want to clarify this distinction — it might help.

Let's start with a simple analogy.

A calculator performs one arithmetic operation at a time — and only by direct command. A computer with traditional code goes a step further: it executes predefined programs, makes decisions using control structures, stores intermediate values, and processes multiple inputs. This works great when inputs are predictable and behavior can be described by rigid, deterministic logic.

But this approach fails in confusing, ambiguous, or uncertain situations.

For example, try writing a full set of `if/else` rules to:
*   distinguish the Moon from a round ceiling light,
*   decipher messy handwriting,
*   or detect sarcasm in a tweet.

This doesn't scale. You quickly run into a combinatorial explosion of edge cases.

This is where classical programming hits its ceiling, and machine learning begins.

You can think of ML as the next level of abstraction: if calculators work with arithmetic, and code with structured logic, then ML handles unstructured uncertainty. Even fuzzy logic — with its gradients and thresholds — often fails to cope with the complexity of the real world. ML does not rely on pre-written rules at all; instead, it learns behavior from data.

Instead of telling the machine *what to do*, you show it *what you want to get*, and it statistically figures out *how* to do it. Learning happens not through hard-coded instructions, but through patterns, probabilities, and generalization.
![2](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/2.png)

*Handwriting and image recognition are just two examples of tasks where it is impossible to predict all scenarios.*

Depending on its training, an ML model can see a letter it has never encountered before and still recognize it — based on thousands of similar handwritten samples. It can determine that a user has drawn a dinosaur, even if that exact silhouette was not in the training data — because it understands shapes, proportions, and texture not as rules, but as distributions. Instead of rigidly following a pre-written script — it guesses.

#### Machine learning paradigms

What an AI model can do depends heavily on how it was trained.

First and foremost, AI models are classified by their learning paradigms. The paradigm determines the strengths and weaknesses of the model.

Most machine learning methods fall into one of four main paradigms:
*   Supervised Learning
*   Unsupervised Learning
*   Reinforcement Learning
*   Self-Supervised Learning (sometimes also called "self-learning")

#### Supervised Learning
![3](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/3.png)

How to train a model to distinguish cats from dogs in photos? You show it tens of thousands of images — each with the correct label: "This is a cat" or "This is a dog." The model begins to look for patterns: "Aha, cats have triangular ears, and dogs have long snouts." It doesn't know what a cat or a dog is, but it sees that some images are similar to each other, and others are not. And with each new example, it gets better at recognizing these patterns. After thousands of iterations, the model begins to notice something itself: cats have triangular ears, a suspicious look, and a tendency to settle firmly on the keyboard. This is supervised learning — training on labeled examples where the "correct" answer is known in advance.

Essentially, you say: "Here's the input — and here's the expected output." The model's task is to find patterns and generalize them to new, unseen data.

![4](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/4.png)

*After a thousand photos of cats, the model grasped the essence: triangular ears are important. Now it uses this to distinguish cats from dogs.*

**Typical use cases:**
*   **Classification** (e.g., spam vs. non-spam)
*   **Regression** (e.g., price prediction)
*   **Probability estimation** (e.g., customer churn probability)

**Supervised learning in the real world:**
*   **Sentiment analysis:** *Input:* review text → *Output:* positive / negative
*   **Spam filtering:** *Input:* email text → *Output:* spam / not spam
*   **Medical diagnosis:** *Input:* test results → *Output:* healthy / sick
*   **Content moderation:** *Input:* text or image → *Output:* allowed / violates rules
*   **Product categorization:** *Input:* product description → *Output:* catalog category
*   **OCR (Optical Character Recognition):** *Input:* document photo → *Output:* extracted text

#### Unsupervised Learning
![5](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/5.png)

*Sometimes it seems that dinosaurs are just overconfident frogs.*

In this paradigm, the model learns from unlabeled data, meaning it is never told what the "correct" answer is. Instead, it tries to independently discover hidden structure, patterns, or relationships. Think of it as trying to organize chaos into categories when no one has ever told you what those categories should be.

Imagine you show the model thousands of images — cats, dogs, frogs, and dinosaurs (let's assume, for clarity, that we somehow got clear photos of extinct reptiles). But we don't tell the model who is who. In fact, the model doesn't even know how many categories there are: three? five? fifty? It just looks for visual patterns. Eventually, it starts grouping furry creatures into one cluster, and those with smooth skin, eyes on the sides, and an ominously cold gaze — into another.

![6](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/6.png)

After thousands of examples, the model eventually decides: "Let's put all the furry stuff in box #1,
and everything with shiny skin and eyes on the sides — in box #2." The labels themselves don't matter — what matters is that the contents of each box become more homogeneous.

Unsupervised models do not try to predict labels. Instead, they:
*   **Group similar objects (clustering)**
*   **Detect outliers or anomalies**
*   **Reduce dimensionality (simplify complex data)**

This paradigm is especially useful when:
*   Data labeling is too expensive or impractical
*   You don't yet know what you're looking for
*   You want to discover segments or behavioral patterns without predefined categories

#### Reinforcement Learning

In this paradigm, the model — called an agent — learns by interacting with the environment through trial and error. The agent tries different actions and observes the environment's reaction. Actions that lead to the desired outcome bring rewards; ineffective or harmful actions lead to penalties.

Let's try training a cat. (Yes, we know it's almost impossible in real life, but we've already started with the cat theme, so here we are.)
The cat is the agent. The apartment is the environment. The cat tries different actions: Caught a fly → got a treat (reward) Knocked over the TV → no dinner (penalty)
Through repeated experience, the cat begins to behave in a useful way — not because it understands what you want, but because it has learned a policy: a set of actions that most often lead to food. It doesn't need rules — it learns from consequences.

![7](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/7.png)

*As the graph shows — screaming won't get you anywhere.)*

**Reinforcement learning is used when:**
*   Behavior needs to improve over time
*   There are no predefined "correct" answers
*   Consequences are delayed, not immediate

#### Self-Supervised Learning

In this approach, the model learns from unlabeled data, but the learning task is extracted from the data itself — without human involvement in labeling. The model learns to predict one part of the input data based on another.

**Example**
Original sentence: *"The cat jumped on the keyboard and committed unfinished code to production."*

We can turn this into a learning task. For example:
*   **Mask a word:** *input:* "The cat jumped on the \*\*\* and deployed unfinished code...", *target:* predict the word **keyboard**.
*   **Break off a sentence:** *input:* "The cat jumped on...", *target:* continue the sentence.

![8](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/8.png)

*For a Tensor Cat, writing upside down is just a matter of choosing the right coordinate system.*

These "input + target" pairs are generated automatically, without manual labeling. The same idea applies to different types of data, such as images (predicting missing fragments) or audio.

**Real-world applications of self-supervised learning:**
*   **Language models** (GPT, LLaMA, Claude)
*   **Computer vision** (CLIP, DINO)
*   **Audio and speech** (Wav2Vec 2.0)
*   **Multimodal models** (Gemini, CLIP)
*   **Pre-training (foundational models)**

**Main idea**
The model learns from automatically generated tasks, where the "correct answer" is extracted directly from the data itself. This gives us scalability, generalization ability, and the foundation for most modern generative and language systems.

#### Summary of learning paradigms

| Paradigm                 | How the model learns                                         |
|--------------------------|--------------------------------------------------------------|
| Supervised Learning      | On labeled data (input → correct answer)                     |
| Unsupervised Learning    | On unlabeled data (model finds structure itself)             |
| Reinforcement Learning   | Through interaction with the environment via rewards and penalties |
| Self-Supervised Learning | On unlabeled data, where tasks are generated from it         |

#### What else exists?

Besides these four, there are other approaches (semi-supervised, active, online learning, etc.). They are rarely considered as independent paradigms because they are usually hybrids or variations of the main strategies we have already discussed. To understand the essence of machine learning — it is enough to master these four.

In the next part, we will delve into what a neural network actually is: neurons, weights, connections. How does it "learn"? Why does it need layers at all? And what does a bunch of numbers have to do with understanding language, images, or... reality?

We will peel back layer by layer — and try to answer the only question that matters:

**So, is there any magic here... or is it just disguised mathematics?**

https://medium.com/@paul.ilvez/how-ai-learns-no-formulas-but-plenty-of-cats-fc43471add24
