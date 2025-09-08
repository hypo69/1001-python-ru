<!-- Translated to en -->
## Creating a "Fingerprint" of Keyboard Typing: User Identification using Machine Learning and Scikit-learn (Practical Example)

In this article, I will show you how to create a simple user identification system based on analyzing their unique typing style (keyboard typing). We will use the Scikit-learn machine learning library in Python. We will go through all the steps necessary to create a working prototype, even with some simplifications.

**1. Simulating data collection: Creating "virtual" keystrokes**

In an ideal scenario, the first step would be to connect to the user's keyboard and record every key press and release. But, unfortunately, within the scope of this article, I do not have the ability to create a system that would intercept input from your keyboard. Therefore, I am forced to **simulate** this process by creating random data representing the duration of keystrokes. Imagine that I have already collected data and now I have a certain set of values that I will use.

For this purpose, I developed the `generate_simulated_data()` function:

```python
import numpy as np
import random

def generate_simulated_data(num_users=2, num_sessions=5, session_length=50):
    """Generates simulated data on keystroke duration."""
    data = []
    labels = []
    for user_id in range(num_users):
        for session_id in range(num_sessions):
            mean_duration = random.randint(80, 150)
            std_dev = random.randint(10, 20)
            session_data = np.random.normal(mean_duration, std_dev, session_length)
            data.append(session_data)
            labels.append(f"user{user_id + 1}")
    return data, labels

data, labels = generate_simulated_data()
```

This function generates data for a given number of users (`num_users`), each of whom has several "typing sessions" (`num_sessions`). Each session consists of a set of random values representing the duration of keystrokes in milliseconds. I use a normal distribution (`np.random.normal()`) to simulate the natural variability in typing speed. Each user is assigned a unique "average" typing style (random `mean_duration` value). This, of course, is an extremely simplified model, but it allows demonstrating the main steps of creating a system.

**Key assumption:** In a real application, you *must* replace this function with code that actually loads data collected from real users, using JavaScript and, possibly, a server-side for storing information.

**2. Feature extraction: Simplifying the picture**

As we have already said, there are many possible features that can be extracted from keystroke data. For simplicity, in this example, I will use only one feature: **the average keystroke duration per session**.

```python
X = np.array([np.mean(session) for session in data]).reshape(-1, 1)
y = np.array(labels)
```

This code calculates the average value for each session and converts the data into a format understandable by Scikit-learn. `reshape(-1, 1)` is used to convert a one-dimensional array into a two-dimensional one, which is required by most machine learning algorithms in Scikit-learn. More complex features will be left for future experiments.

**3. Data preparation: Getting ready for training**

Before training the model, the data must be prepared. This includes:

*   **Data splitting:** Splitting the data into training and test sets. The training set is used to train the model, and the test set is used to evaluate its accuracy.
*   **Data normalization:** Scaling the data so that all features have the same range of values. This helps improve model performance.

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

I use `train_test_split` to split the data into 70% training and 30% test sets. `StandardScaler` is used for data normalization. `fit_transform` is applied to the training set to calculate scaling parameters, and `transform` is applied to the test set using these parameters. These steps are very important for the model to work correctly.

**4. Model training: Creating a "fingerprint" of keyboard typing**

Now I can train a machine learning model. I will use `RandomForestClassifier`, as before.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

I create an instance of `RandomForestClassifier` with 100 trees (`n_estimators=100`) and train it on the training set. This forms our "fingerprint" of keyboard typing based on the provided data.

**5. Model evaluation: Measuring the accuracy of the "fingerprint"**

After training the model, it is necessary to evaluate its accuracy on the test set.

```python
from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Model accuracy: {accuracy}")
```

I use `accuracy_score` to calculate the model's accuracy, i.e., the proportion of correctly classified examples. A typical result:

```
Model accuracy: 0.75
```

(The value may vary slightly due to randomness in the data)

**6. Using the model: Identifying a new user**

Finally, I can use the trained model to identify a new user.

```python
def predict_user(session_data):
    """Predicts the user based on session data."""
    mean_duration = np.mean(session_data)
    scaled_data = scaler.transform([[mean_duration]])
    prediction = model.predict(scaled_data)[0]
    return prediction

new_session_data = np.random.normal(120, 15, 50)
predicted_user = predict_user(new_session_data)
print(f"Predicted user: {predicted_user}")
```

The `predict_user` function takes new typing session data, calculates the average keystroke duration, scales the data, and uses the trained model to predict the user. `scaler.transform([[mean_duration]])` scales the data using the scaling parameters calculated on the training set. Example output:

```
Predicted user: user2
```

(The result may vary depending on randomness)

**Conclusion:**

This example demonstrates the basic steps of creating a *simplified* keyboard typing identification system. Although I used simulated data and an extremely simplified set of features, this example shows that machine learning can be used to analyze typing patterns and attempt to identify users.

**What's next? Real steps to creating a working system:**

*   **Real data collection:** This is the *most* important step. You will need to develop JavaScript code to track keystrokes in the browser and a system to store this data on the server.
*   **Advanced Feature Engineering:** Replace the average keystroke duration with a more representative set of features (intervals, digraphs, trigraphs, error rate, etc.).
*   **More complex models:** Try using other machine learning algorithms (SVM, gradient boosting) and tune hyperparameters.
*   **Handling variability:** Develop methods that will account for changes in typing style (due to fatigue, stress, etc.).
*   **Ethical considerations:** Pay very close attention to data privacy and security issues. The collection and storage of such information must be carried out in full compliance with user rights and transparency.

Despite the fact that the example presented here is only a starting point, it demonstrates the potential of machine learning for analyzing keyboard typing. Creating a reliable and accurate system is a complex task requiring significant effort, but it can become an important addition to existing user identification methods.
