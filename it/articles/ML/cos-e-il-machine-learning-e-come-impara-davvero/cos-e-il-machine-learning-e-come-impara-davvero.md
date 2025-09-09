# Cos'è il machine learning — e come "impara" davvero?
![1](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/1.png)

*Quattro gatti su cui si basa il machine learning*

In cosa differisce il machine learning dalla programmazione tradizionale con il suo "funziona finché non lo tocchi"? Dove finiscono gli algoritmi chiari — e dove inizia la magia della "scatola nera", come nel caso di ChatGPT?

*Questo è il primo articolo di una serie di divulgazione scientifica in cui analizzeremo le basi dell'IA — senza parole vuote, senza cliché, senza nebbia accademica e, idealmente, senza equazioni (come Stephen Hawking scrisse una volta: ogni formula in un libro di divulgazione scientifica dimezza le sue vendite).*

Oggi parleremo delle fondamenta stesse: quali tipi di apprendimento utilizzano i modelli di IA, perché sono necessari e come determinano di cosa è capace un modello.

Sì, ci saranno gatti. E un po' di sarcasmo. Ma esclusivamente per scopi nobili — per creare associazioni forti e memorabili.

Questo articolo è per tutti coloro che stanno iniziando a familiarizzare con l'IA: per lettori tecnici e non tecnici, architetti di soluzioni, fondatori di startup, sviluppatori esperti e tutti coloro che vogliono finalmente formarsi un'idea chiara di cosa sia il machine learning e da dove tutto inizia.

In questa parte, tratteremo le basi:
Cos'è il ML, come si differenzia fondamentalmente dalla programmazione tradizionale, e quattro paradigmi di apprendimento chiave che sono alla base dell'intero panorama dell'IA moderna.

#### Programmazione classica vs. machine learning

Se sei già sicuro della tua comprensione di come il machine learning differisce dalla programmazione tradizionale, sentiti libero di saltare questa sezione. Ma se vuoi chiarire questa distinzione, potrebbe aiutarti.

Cominciamo con una semplice analogia.

Una calcolatrice esegue un'operazione aritmetica alla volta — e solo su comando diretto. Un computer con codice tradizionale fa un passo avanti: esegue programmi predefiniti, prende decisioni usando strutture di controllo, memorizza valori intermedi ed elabora più input. Questo funziona alla grande quando gli input sono prevedibili e il comportamento può essere descritto da una logica rigida e deterministica.

Ma questo approccio fallisce in situazioni confuse, ambigue o incerte.

Ad esempio, prova a scrivere un set completo di regole `if/else` per:
*   distinguere la Luna da una plafoniera rotonda,
*   decifrare una calligrafia disordinata,
*   o rilevare il sarcasmo in un tweet.

Questo non scala. Ti imbatterai rapidamente in un'esplosione combinatoria di casi particolari.

È qui che la programmazione classica raggiunge il suo limite, e inizia il machine learning.

Si può pensare al ML come al livello successivo di astrazione: se le calcolatrici lavorano con l'aritmetica e il codice con la logica strutturata, il ML gestisce l'incertezza non strutturata. Anche la logica fuzzy — con i suoi gradienti e le sue soglie — spesso non riesce a far fronte alla complessità del mondo reale. Il ML non si basa affatto su regole pre-scritte; invece, impara il comportamento dai dati.

Invece di dire alla macchina *cosa fare*, le mostri *cosa vuoi ottenere*, e lei scopre statisticamente *come* farlo. L'apprendimento non avviene tramite istruzioni codificate, ma tramite pattern, probabilità e generalizzazione.
![2](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/2.png)

*Il riconoscimento della scrittura a mano e delle immagini sono solo due esempi di compiti in cui è impossibile prevedere tutti gli scenari.*

A seconda del suo addestramento, un modello ML può vedere una lettera che non ha mai incontrato prima e riconoscerla comunque — basandosi su migliaia di campioni scritti a mano simili. Può determinare che un utente ha disegnato un dinosauro, anche se quella esatta silhouette non era nei dati di addestramento — perché comprende forme, proporzioni e texture non come regole, ma come distribuzioni. Invece di seguire rigidamente uno script pre-scritto — indovina.

#### Paradigmi di machine learning

Ciò che un modello AI può fare dipende fortemente da come è stato addestrato.

Innanzitutto, i modelli AI sono classificati in base ai loro paradigmi di apprendimento. Il paradigma determina i punti di forza e di debolezza del modello.

La maggior parte dei metodi di machine learning rientra in uno dei quattro paradigmi principali:
*   Apprendimento supervisionato
*   Apprendimento non supervisionato
*   Apprendimento per rinforzo
*   Apprendimento auto-supervisionato (a volte chiamato anche "autoapprendimento")

#### Apprendimento supervisionato (Supervised Learning)
![3](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/3.png)

Come addestrare un modello a distinguere i gatti dai cani nelle foto? Gli mostri decine di migliaia di immagini — ognuna con l'etichetta corretta: "Questo è un gatto" o "Questo è un cane". Il modello inizia a cercare schemi: "Ah, i gatti hanno le orecchie triangolari e i cani hanno il muso lungo". Non sa cos'è un gatto o un cane, ma vede che alcune immagini sono simili tra loro e altre no. E con ogni nuovo esempio, migliora nel riconoscere questi schemi. Dopo migliaia di iterazioni, il modello inizia a notare qualcosa da solo: i gatti hanno le orecchie triangolari, uno sguardo sospettoso e la tendenza a sistemarsi saldamente sulla tastiera. Questo è l'apprendimento supervisionato — addestramento su esempi etichettati in cui la risposta "corretta" è nota in anticipo.

In sostanza, dici: "Ecco l'input — ed ecco l'output atteso". Il compito del modello è trovare schemi e generalizzarli a nuovi dati, mai visti.

![4](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/4.png)

*Dopo mille foto di gatti, il modello ha colto l'essenza: le orecchie triangolari sono importanti. Ora le usa per distinguere i gatti dai cani.*

**Casi d'uso tipici:**
*   **Classificazione** (ad esempio, spam vs. non-spam)
*   **Regressione** (ad esempio, previsione dei prezzi)
*   **Stima della probabilità** (ad esempio, probabilità di abbandono dei clienti)

**Apprendimento supervisionato nel mondo reale:**
*   **Analisi del sentiment:** *Input:* testo della recensione → *Output:* positivo / negativo
*   **Filtro antispam:** *Input:* testo dell'email → *Output:* spam / non-spam
*   **Diagnosi medica:** *Input:* risultati dei test → *Output:* sano / malato
*   **Moderazione dei contenuti:** *Input:* testo o immagine → *Output:* consentito / viola le regole
*   **Categorizzazione dei prodotti:** *Input:* descrizione del prodotto → *Output:* categoria del catalogo
*   **OCR (Riconoscimento ottico dei caratteri):** *Input:* foto del documento → *Output:* testo estratto

#### Apprendimento non supervisionato (Unsupervised Learning)
![5](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/5.png)

*A volte sembra che i dinosauri siano solo rane troppo sicure di sé.*

In questo paradigma, il modello apprende da dati non etichettati, il che significa che non gli viene mai detto quale sia la risposta "corretta". Invece, cerca di scoprire autonomamente la struttura nascosta, i modelli o le relazioni. Pensala come un tentativo di organizzare il caos in categorie quando nessuno ti ha mai detto quali dovrebbero essere quelle categorie.

Immagina di mostrare al modello migliaia di immagini — gatti, cani, rane e dinosauri (supponiamo, per chiarezza, di aver in qualche modo ottenuto foto chiare di rettili estinti). Ma non diciamo al modello chi è chi. In effetti, il modello non sa nemmeno quante categorie ci sono: tre? cinque? cinquanta? Cerca semplicemente schemi visivi. Alla fine, inizia a raggruppare le creature pelose in un cluster, e quelle con la pelle liscia, gli occhi ai lati e uno sguardo minacciosamente freddo — in un altro.

![6](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/6.png)

Dopo migliaia di esempi, il modello alla fine decide: "Mettiamo tutte le cose pelose nella scatola n. 1,
e tutto ciò che ha la pelle lucida e gli occhi ai lati — nella scatola n. 2". Le etichette stesse non contano — ciò che conta è che il contenuto di ogni scatola diventi più omogeneo.

I modelli non supervisionati non cercano di prevedere le etichette. Invece, essi:
*   **Raggruppano oggetti simili (clustering)**
*   **Rilevano outlier o anomalie**
*   **Riducono la dimensionalità (semplificano dati complessi)**

Questo paradigma è particolarmente utile quando:
*   L'etichettatura dei dati è troppo costosa o impraticabile
*   Non sai ancora cosa stai cercando
*   Vuoi scoprire segmenti o modelli di comportamento senza categorie predefinite

#### Apprendimento per rinforzo (Reinforcement Learning)

In questo paradigma, il modello — chiamato agente — apprende interagendo con l'ambiente tramite tentativi ed errori. L'agente prova diverse azioni e osserva la reazione dell'ambiente. Le azioni che portano al risultato desiderato portano ricompense; le azioni inefficaci o dannose portano a penalità.

Proviamo ad addestrare un gatto. (Sì, sappiamo che è quasi impossibile nella vita reale, ma abbiamo già iniziato con il tema dei gatti, quindi eccoci qui.)
Il gatto è l'agente. L'appartamento è l'ambiente. Il gatto prova diverse azioni: Ha catturato una mosca → ha ricevuto un premio (ricompensa) Ha fatto cadere la TV → niente cena (penalità)
Attraverso esperienze ripetute, il gatto inizia a comportarsi in modo utile — non perché capisce cosa vuoi, ma perché ha imparato una politica: un insieme di azioni che più spesso portano al cibo. Non ha bisogno di regole — impara dalle conseguenze.

![7](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/7.png)

*Come mostra il grafico — urlare non ti porterà da nessuna parte.)*

**L'apprendimento per rinforzo viene utilizzato quando:**
*   Il comportamento deve migliorare nel tempo
*   Non ci sono risposte "corrette" predefinite
*   Le conseguenze sono ritardate, non immediate

#### Apprendimento auto-supervisionato (Self-Supervised Learning)

In questo approccio, il modello apprende da dati non etichettati, ma il compito di apprendimento viene estratto dai dati stessi — senza intervento umano nell'etichettatura. Il modello impara a prevedere una parte dei dati di input basandosi su un'altra.

**Esempio**
Frase originale: *"Il gatto è saltato sulla tastiera e ha commesso codice incompleto in produzione."*

Possiamo trasformare questo in un compito di apprendimento. Ad esempio:
*   **Mascherare una parola:** *input:* "Il gatto è saltato sulla \*\*\* e ha distribuito codice incompleto...", *obiettivo:* prevedere la parola **tastiera**.
*   **Interrompere una frase:** *input:* "Il gatto è saltato su...", *obiettivo:* continuare la frase.

![8](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/8.png)

*Per un Gatto Tensore, scrivere a testa in giù è solo una questione di scegliere il sistema di coordinate corretto.*

Queste coppie "input + obiettivo" vengono generate automaticamente, senza etichettatura manuale. La stessa idea si applica a diversi tipi di dati, come immagini (previsione di frammenti mancanti) o audio.

**Applicazioni reali dell'apprendimento auto-supervisionato:**
*   **Modelli linguistici** (GPT, LLaMA, Claude)
*   **Visione artificiale** (CLIP, DINO)
*   **Audio e parlato** (Wav2Vec 2.0)
*   **Modelli multimodali** (Gemini, CLIP)
*   **Pre-addestramento (modelli fondamentali)**

**Idea principale**
Il modello apprende da compiti generati automaticamente, dove la "risposta corretta" viene estratta direttamente dai dati stessi. Questo ci offre scalabilità, capacità di generalizzazione e le basi per la maggior parte dei sistemi generativi e linguistici moderni.

#### Riepilogo dei paradigmi di apprendimento

| Paradigma                 | Come impara il modello                                       |
|---------------------------|--------------------------------------------------------------|
| Apprendimento supervisionato | Su dati etichettati (input → risposta corretta)              |
| Apprendimento non supervisionato | Su dati non etichettati (il modello trova la struttura da solo) |
| Apprendimento per rinforzo | Attraverso l'interazione con l'ambiente tramite ricompense e penalità |
| Apprendimento auto-supervisionato | Su dati non etichettati, dove i compiti vengono generati da essi stessi |

#### Cos'altro esiste?

Oltre a questi quattro, esistono altri approcci (semi-supervisionato, attivo, apprendimento online, ecc.). Raramente sono considerati paradigmi indipendenti perché di solito sono ibridi o variazioni delle strategie principali che abbiamo già esaminato. Per comprendere l'essenza del machine learning — è sufficiente padroneggiare questi quattro.

Nella prossima parte, approfondiremo cos'è realmente una rete neurale: neuroni, pesi, connessioni. Come "impara"? Perché ha bisogno di strati? E cosa c'entra un mucchio di numeri con la comprensione del linguaggio, delle immagini o... della realtà?

Sbucceremo strato dopo strato — e cercheremo di rispondere all'unica domanda che conta:

**Quindi, c'è qualche magia qui... o è solo matematica mascherata?**

https://medium.com/@paul.ilvez/how-ai-learns-no-formulas-but-plenty-of-cats-fc43471add24
