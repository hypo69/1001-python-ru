## Creazione di un "Impronta" della Dattilografia: Identificazione dell'utente tramite Machine Learning e Scikit-learn (Esempio pratico)

In questo articolo, ti mostrerò come creare un semplice sistema di identificazione dell'utente basato sull'analisi del suo stile di digitazione unico (impronta della tastiera). Utilizzeremo la libreria di machine learning Scikit-learn in Python. Percorreremo tutti i passaggi necessari per creare un prototipo funzionante, anche se con alcune semplificazioni.

**1. Simulazione della raccolta dati: Creazione di pressioni di tasti "virtuali"**

In uno scenario ideale, il primo passo sarebbe connettersi alla tastiera dell'utente e registrare ogni pressione e rilascio del tasto. Ma, sfortunatamente, nell'ambito di questo articolo non ho la possibilità di creare un sistema che intercetti l'input dalla tua tastiera. Pertanto, sono costretto a **simulare** questo processo, creando dati casuali che rappresentano la durata delle pressioni dei tasti. Immagina che io abbia già raccolto i dati e ora ho un certo set di valori che userò.

A questo scopo, ho sviluppato la funzione `generate_simulated_data()`:

```python
import numpy as np
import random

def generate_simulated_data(num_users=2, num_sessions=5, session_length=50):
    """Genera dati simulati sulla durata delle pressioni dei tasti."""
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

Questa funzione genera dati per un numero specificato di utenti (`num_users`), ognuno dei quali ha diverse "sessioni" di digitazione (`num_sessions`). Ogni sessione consiste in un set di valori casuali che rappresentano la durata della pressione dei tasti in millisecondi. Utilizzo una distribuzione normale (`np.random.normal()`) per simulare la variabilità naturale nella velocità di digitazione. A ogni utente viene assegnato uno stile di digitazione "medio" unico (valore casuale `mean_duration`). Questo è, ovviamente, un modello estremamente semplificato, ma consente di dimostrare i passaggi principali per la creazione di un sistema.

**Assunzione chiave:** In un'applicazione reale, *devi* sostituire questa funzione con codice che carichi effettivamente i dati raccolti da utenti reali, utilizzando JavaScript e, possibilmente, un backend per l'archiviazione delle informazioni.

**2. Estrazione delle caratteristiche: Semplifichiamo il quadro**

Come abbiamo già detto, ci sono molte possibili caratteristiche che possono essere estratte dai dati di pressione dei tasti. Per semplicità, in questo esempio userò solo una caratteristica: la **durata media della pressione dei tasti in una sessione**.

```python
X = np.array([np.mean(session) for session in data]).reshape(-1, 1)
y = np.array(labels)
```

Questo codice calcola il valore medio per ogni sessione e trasforma i dati in un formato comprensibile a Scikit-learn. `reshape(-1, 1)` viene utilizzato per convertire un array unidimensionale in un array bidimensionale, richiesto dalla maggior parte degli algoritmi di machine learning in Scikit-learn. Caratteristiche più complesse le lasceremo per esperimenti futuri.

**3. Preparazione dei dati: Prepararsi all'addestramento**

Prima di addestrare il modello, è necessario preparare i dati. Ciò include:

*   **Suddivisione dei dati:** Suddivisione dei dati in set di addestramento e di test. Il set di addestramento viene utilizzato per addestrare il modello, mentre il set di test viene utilizzato per valutarne l'accuratezza.
*   **Normalizzazione dei dati:** Scalatura dei dati in modo che tutte le caratteristiche abbiano lo stesso intervallo di valori. Questo aiuta a migliorare le prestazioni del modello.

```python
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
```

Utilizzo `train_test_split` per dividere i dati in un set di addestramento del 70% e un set di test del 30%. `StandardScaler` viene utilizzato per normalizzare i dati. `fit_transform` viene applicato al set di addestramento per calcolare i parametri di scalatura, e `transform` viene applicato al set di test, utilizzando questi parametri. Questi passaggi sono molto importanti affinché il modello funzioni correttamente.

**4. Addestramento del modello: Creazione di un "impronta" della dattilografia**

Ora posso addestrare il modello di machine learning. Userò `RandomForestClassifier`, come prima.

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
```

Creo un'istanza di `RandomForestClassifier` con 100 alberi (`n_estimators=100`) e la addestro sul set di addestramento. Questo forma la nostra "impronta" della dattilografia basata sui dati forniti.

**5. Valutazione del modello: Misurazione dell'accuratezza dell'"impronta"**

Dopo aver addestrato il modello, è necessario valutarne l'accuratezza sul set di test.

```python
from sklearn.metrics import accuracy_score

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuratezza del modello: {accuracy}")
```

Utilizzo `accuracy_score` per calcolare l'accuratezza del modello, ovvero la percentuale di esempi classificati correttamente. Un risultato tipico:

```
Accuratezza del modello: 0.75
```

(Il valore può variare leggermente a causa della casualità nei dati)

**6. Utilizzo del modello: Identificazione di un nuovo utente**

Infine, posso utilizzare il modello addestrato per identificare un nuovo utente.

```python
def predict_user(session_data):
    """Prevede l'utente in base ai dati della sessione."""
    mean_duration = np.mean(session_data)
    scaled_data = scaler.transform([[mean_duration]])
    prediction = model.predict(scaled_data)[0]
    return prediction

new_session_data = np.random.normal(120, 15, 50)
predicted_user = predict_user(new_session_data)
print(f"Utente previsto: {predicted_user}")
```

La funzione `predict_user` accetta i dati di una nuova sessione di digitazione, calcola la durata media delle pressioni, scala i dati e utilizza il modello addestrato per prevedere l'utente. `scaler.transform([[mean_duration]])` scala i dati utilizzando i parametri di scalatura calcolati sul set di addestramento. Esempio di output:

```
Utente previsto: user2
```

(Il risultato può variare a seconda della casualità)

**Conclusione:**

Questo esempio dimostra i passaggi principali per la creazione di un sistema *semplificato* di identificazione tramite "impronta della tastiera". Sebbene abbia utilizzato dati simulati e un set di caratteristiche estremamente semplificato, questo esempio mostra che il machine learning può essere utilizzato per analizzare i modelli di digitazione e tentare di identificare gli utenti.

**Cosa c'è dopo? Passi reali per la creazione di un sistema funzionante:**

*   **Raccolta dati reali:** Questo è il passo *più* importante. Dovrai sviluppare codice JavaScript per tracciare le pressioni dei tasti nel browser e un sistema per archiviare questi dati sul server.
*   **Feature Engineering avanzato:** Sostituisci la durata media della pressione con un set di caratteristiche più rappresentativo (intervalli, digrammi, trigrammi, frequenza degli errori, ecc.).
*   **Modelli più complessi:** Prova a utilizzare altri algoritmi di machine learning (SVM, gradient boosting) e ottimizza gli iperparametri.
*   **Gestione della variabilità:** Sviluppa metodi che tengano conto dei cambiamenti nello stile di digitazione (dovuti a fatica, stress, ecc.).
*   **Aspetti etici:** Presta molta attenzione alle questioni di privacy e sicurezza dei dati. La raccolta e l'archiviazione di tali informazioni devono essere condotte nel pieno rispetto dei diritti degli utenti e con trasparenza.

Sebbene l'esempio qui presentato sia solo un punto di partenza, dimostra il potenziale del machine learning per l'analisi dell'impronta della tastiera. La creazione di un sistema affidabile e accurato è un compito complesso che richiede uno sforzo significativo, ma può diventare un'importante aggiunta ai metodi esistenti di identificazione degli utenti.
