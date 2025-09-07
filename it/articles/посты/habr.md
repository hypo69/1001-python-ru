https://habr.com/ru/articles/667008/

Ottimo! Ecco un tutorial dettagliato basato sul tuo articolo. L'ho trasformato in una guida strutturata passo-passo con spiegazioni e consigli per ogni fase dello sviluppo di un chatbot autoapprendente in Python con la possibilità di cercare informazioni su Wikipedia.

---

# 🧠 Chatbot autoapprendente in Python con ricerca Wikipedia e integrazione Telegram

## 🎯 Obiettivo

Imparare a creare un bot Telegram in Python che:

*   Comprende le domande dell'utente e risponde ad esse utilizzando un semplice machine learning.
*   È in grado di cercare informazioni su Wikipedia in russo.
*   Autoapprendimento: può memorizzare le risposte corrette che l'utente gli suggerisce.

---

## 🧰 Passaggio 1. Installazione delle librerie necessarie

Avremo bisogno delle seguenti librerie:

*   **pyTelegramBotAPI** — per l'interazione con Telegram.
*   **scikit-learn** — per il machine learning.
*   **wikipedia** — per la ricerca di informazioni su Wikipedia.

Installale con il comando:

```bash
pip install pyTelegramBotAPI wikipedia scikit-learn
```

---

## 🛠 Passaggio 2. Configurazione dell'ambiente

Crea un file Python (ad esempio `bot.py`) e incolla il seguente codice:

```python
import telebot, wikipedia, re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
```

### Imposta la lingua di Wikipedia e crea il bot

```python
wikipedia.set_lang("ru")
bot = telebot.TeleBot('IL_TUO_TOKEN_DA_BOTFATHER')
```

Sostituisci `'IL_TUO_TOKEN_DA_BOTFATHER'` con il tuo token ottenuto da [BotFather](https://t.me/botfather) in Telegram.

---

## ✂️ Passaggio 3. Pulizia del testo

Il bot funzionerà meglio se rimuoviamo i caratteri extra dal testo di input:

```python
alphabet = ' 1234567890-йцукенгшщзхъфывапролджэячсмитьбюёqwertyuiopasdfghjklzxcvbnm?%.,()!:;'

def clean_str(r):
    r = r.lower()
    r = [c for c in r if c in alphabet]
    return ''.join(r)
```

---

## 📁 Passaggio 4. Preparazione dei dati di addestramento

Crea un file `dialogues.txt` accanto a `bot.py`. Esempio di contenuto:

```
ciao\ciao!
come stai\bene.
chi sei\sono Jarvis.
```

Formato: **domanda\risposta**

---

## 🤖 Passaggio 5. Addestramento del modello

Aggiungiamo una funzione che carica `dialogues.txt`, elabora i dati e addestra il modello:

```python
def update():
    with open('dialogues.txt', encoding='utf-8') as f:
        content = f.read()

    blocks = content.strip().split('\n')
    dataset = []

    for block in blocks:
        replicas = block.split('\\')[:2]
        if len(replicas) == 2:
            pair = [clean_str(replicas[0]), clean_str(replicas[1])]
            if pair[0] and pair[1]:
                dataset.append(pair)

    X_text = [q for q, _ in dataset]
    y = [a for _, a in dataset]

    global vectorizer, clf
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(X_text)

    clf = LogisticRegression()
    clf.fit(X, y)

update()
```

---

## 💬 Passaggio 6. Generazione delle risposte

Una funzione che selezionerà la migliore risposta in base al modello addestrato:

```python
def get_generative_replica(text):
    text_vector = vectorizer.transform([clean_str(text)]).toarray()[0]
    return clf.predict([text_vector])[0]
```

---

## 🌐 Passaggio 7. Ricerca su Wikipedia

Il bot utilizzerà Wikipedia se non trova una risposta adeguata:

```python
def getwiki(s):
    try:
        page = wikipedia.page(s)
        text = page.content[:1000]
        sentences = text.split('.')[:-1]

        summary = ''
        for sentence in sentences:
            if '==' not in sentence and len(sentence.strip()) > 3:
                summary += sentence.strip() + '.'
            else:
                break

        summary = re.sub(r'\([^()]*\)', '', summary)
        summary = re.sub(r'\{[^\{\}]*\}', '', summary)
        return summary
    except Exception:
        return 'Nessuna informazione trovata su Wikipedia'
```

---

## 🤝 Passaggio 8. Interazione con gli utenti

Gestione dei comandi e dei messaggi degli utenti:

```python
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Buongiorno, Signore.")

question = ""

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global question
    command = message.text.lower()

    if command == "non così":
        bot.send_message(message.from_user.id, "e come?")
        bot.register_next_step_handler(message, wrong)
    else:
        question = command
        reply = get_generative_replica(command)
        if reply.strip() == "wiki":
            bot.send_message(message.from_user.id, getwiki(command))
        else:
            bot.send_message(message.from_user.id, reply)

def wrong(message):
    correction = message.text.lower()
    with open('dialogues.txt', "a", encoding='utf-8') as f:
        f.write(f"{question}\\{correction}\n")
    bot.send_message(message.from_user.id, "Fatto, ho memorizzato.")
    update()
```

---

## ▶️ Passaggio 9. Avvio del bot

Alla fine del file aggiungi:

```python
bot.polling(none_stop=True)
```

Avvia il bot:

```bash
python bot.py
```

---

## 💡 Consigli per il miglioramento

*   Usa modelli più potenti, ad esempio `transformers`, per una comprensione avanzata del testo.
*   Aggiungi la registrazione degli errori.
*   Proteggi il token del bot tramite variabili d'ambiente (`os.environ.get(...)`).
*   Supporto per più lingue e rilevamento della lingua.

---

## ✅ Cosa hai imparato

*   Come creare un bot Telegram in Python.
*   Come implementare un semplice machine learning con `scikit-learn`.
*   Come connettere Wikipedia e filtrare il suo contenuto.
*   Come creare un bot che autoapprende da nuovi dati.

---

Se necessario, posso formattarlo come PDF, guida HTML o post di blog. Vuoi continuare?
