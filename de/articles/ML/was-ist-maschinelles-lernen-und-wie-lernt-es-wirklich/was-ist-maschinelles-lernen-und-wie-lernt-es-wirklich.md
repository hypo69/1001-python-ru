# Was ist maschinelles Lernen – und wie „lernt“ es wirklich?
![1](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/1.png)

*Vier Katzen, auf denen maschinelles Lernen ruht*

Wie unterscheidet sich maschinelles Lernen von traditioneller Programmierung mit ihrem „es funktioniert, bis man es anfasst“? Wo enden klare Algorithmen – und wo beginnt die Magie der „Black Box“, wie im Fall von ChatGPT?

*Dies ist der erste Artikel einer populärwissenschaftlichen Reihe, in der wir die Grundlagen der KI analysieren – ohne leere Worte, ohne Klischees, ohne akademischen Nebel und, idealerweise, ohne Gleichungen (wie Stephen Hawking einmal schrieb: Jede Formel in einem populärwissenschaftlichen Buch halbiert dessen Verkaufszahlen).*

Heute sprechen wir über das Fundament: Welche Arten des Lernens verwenden KI-Modelle, warum werden sie überhaupt benötigt und wie bestimmen sie, wozu ein Modell fähig ist.

Ja, es wird Katzen geben. Und ein bisschen Sarkasmus. Aber ausschließlich zu edlen Zwecken – um starke und einprägsame Assoziationen zu schaffen.

Dieser Artikel richtet sich an alle, die sich mit KI vertraut machen möchten: an technische und nicht-technische Leser, Lösungsarchitekten, Startup-Gründer, erfahrene Entwickler und alle, die sich endlich ein klares Bild davon machen möchten, was maschinelles Lernen ist und wo alles beginnt.

In diesem Teil behandeln wir die Grundlagen:
Was ML ist, wie es sich grundlegend von traditioneller Programmierung unterscheidet, und vier Schlüssel-Lernparadigmen, die die gesamte moderne KI-Landschaft untermauern.

#### Klassische Programmierung vs. maschinelles Lernen

Wenn Sie bereits sicher sind, wie sich maschinelles Lernen von traditioneller Programmierung unterscheidet, können Sie diesen Abschnitt gerne überspringen. Aber wenn Sie diese Unterscheidung klären möchten – es könnte helfen.

Beginnen wir mit einer einfachen Analogie.

Ein Taschenrechner führt eine arithmetische Operation nach der anderen aus – und nur auf direkte Anweisung. Ein Computer mit traditionellem Code geht einen Schritt weiter: Er führt vordefinierte Programme aus, trifft Entscheidungen mithilfe von Kontrollstrukturen, speichert Zwischenwerte und verarbeitet mehrere Eingaben. Dies funktioniert hervorragend, wenn die Eingaben vorhersehbar sind und das Verhalten durch starre, deterministische Logik beschrieben werden kann.

Doch dieser Ansatz scheitert in verwirrenden, mehrdeutigen oder unsicheren Situationen.

Versuchen Sie zum Beispiel, einen vollständigen Satz von `if/else`-Regeln zu schreiben, um:
*   den Mond von einer runden Deckenleuchte zu unterscheiden,
*   unordentliche Handschrift zu entziffern,
*   oder Sarkasmus in einem Tweet zu erkennen.

Das skaliert nicht. Sie stoßen schnell auf eine kombinatorische Explosion von Sonderfällen.

Hier stößt die klassische Programmierung an ihre Grenzen, und das maschinelle Lernen beginnt.

Man kann ML als die nächste Abstraktionsebene betrachten: Wenn Taschenrechner mit Arithmetik und Code mit strukturierter Logik arbeiten, dann bewältigt ML unstrukturierte Unsicherheit. Selbst Fuzzy-Logik – mit ihren Gradienten und Schwellenwerten – versagt oft bei der Komplexität der realen Welt. ML verlässt sich überhaupt nicht auf vorab geschriebene Regeln; stattdessen lernt es Verhalten aus Daten.

Anstatt der Maschine zu sagen, *was sie tun soll*, zeigen Sie ihr, *was Sie erhalten möchten*, und sie findet statistisch heraus, *wie* sie es tun kann. Das Lernen erfolgt nicht durch fest codierte Anweisungen, sondern durch Muster, Wahrscheinlichkeiten und Verallgemeinerung.
![2](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/2.png)

*Handschrift- und Bilderkennung sind nur zwei Beispiele für Aufgaben, bei denen es unmöglich ist, alle Szenarien vorherzusagen.*

Abhängig von seinem Training kann ein ML-Modell einen Buchstaben sehen, den es noch nie zuvor gesehen hat, und ihn trotzdem erkennen – basierend auf Tausenden ähnlicher handschriftlicher Proben. Es kann feststellen, dass ein Benutzer einen Dinosaurier gezeichnet hat, selbst wenn diese genaue Silhouette nicht in den Trainingsdaten enthalten war – weil es Formen, Proportionen und Texturen nicht als Regeln, sondern als Verteilungen versteht. Anstatt starr einem vorgegebenen Skript zu folgen – rät es.

#### Paradigmen des maschinellen Lernens

Was ein KI-Modell leisten kann, hängt stark davon ab, wie es trainiert wurde.

Zunächst werden KI-Modelle nach ihren Lernparadigmen klassifiziert. Das Paradigma bestimmt die Stärken und Schwächen des Modells.

Die meisten Methoden des maschinellen Lernens fallen in eines von vier Hauptparadigmen:
*   Überwachtes Lernen
*   Unüberwachtes Lernen
*   Bestärkendes Lernen
*   Selbstüberwachtes Lernen (manchmal auch „selbstlernend“ genannt)

#### Überwachtes Lernen (Supervised Learning)
![3](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/3.png)

Wie trainiert man ein Modell, um Katzen von Hunden auf Fotos zu unterscheiden? Man zeigt ihm Zehntausende von Bildern – jedes mit der richtigen Beschriftung: „Das ist eine Katze“ oder „Das ist ein Hund“. Das Modell beginnt, nach Mustern zu suchen: „Aha, Katzen haben dreieckige Ohren und Hunde haben lange Schnauzen.“ Es weiß nicht, was eine Katze oder ein Hund ist, aber es sieht, dass einige Bilder einander ähneln und andere nicht. Und mit jedem neuen Beispiel wird es besser darin, diese Muster zu erkennen. Nach Tausenden von Iterationen beginnt das Modell, selbst etwas zu bemerken: Katzen haben dreieckige Ohren, einen misstrauischen Blick und die Tendenz, sich fest auf die Tastatur zu setzen. Dies ist überwachtes Lernen – Training an beschrifteten Beispielen, bei denen die „richtige“ Antwort im Voraus bekannt ist.

Im Wesentlichen sagen Sie: „Hier ist die Eingabe – und hier ist die erwartete Ausgabe.“ Die Aufgabe des Modells besteht darin, Muster zu finden und sie auf neue, ungesehene Daten zu verallgemeinern.

![4](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/4.png)

*Nach tausend Katzenfotos hat das Modell das Wesentliche erfasst: Dreieckige Ohren sind wichtig. Jetzt nutzt es dies, um Katzen von Hunden zu unterscheiden.*

**Typische Anwendungsfälle:**
*   **Klassifizierung** (z. B. Spam vs. Nicht-Spam)
*   **Regression** (z. B. Preisvorhersage)
*   **Wahrscheinlichkeitsschätzung** (z. B. Kundenabwanderungswahrscheinlichkeit)

**Überwachtes Lernen in der realen Welt:**
*   **Sentiment-Analyse:** *Eingabe:* Bewertungstext → *Ausgabe:* positiv / negativ
*   **Spam-Filterung:** *Eingabe:* E-Mail-Text → *Ausgabe:* Spam / kein Spam
*   **Medizinische Diagnose:** *Eingabe:* Testergebnisse → *Ausgabe:* gesund / krank
*   **Inhaltsmoderation:** *Eingabe:* Text oder Bild → *Ausgabe:* erlaubt / verstößt gegen Regeln
*   **Produktkategorisierung:** *Eingabe:* Produktbeschreibung → *Ausgabe:* Katalogkategorie
*   **OCR (Optische Zeichenerkennung):** *Eingabe:* Dokumentenfoto → *Ausgabe:* extrahierter Text

#### Unüberwachtes Lernen (Unsupervised Learning)
![5](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/5.png)

*Manchmal scheint es, dass Dinosaurier nur übermütige Frösche sind.*

In diesem Paradigma lernt das Modell aus unbeschrifteten Daten, d.h. es wird ihm nie gesagt, welche Antwort „richtig“ ist. Stattdessen versucht es, selbstständig verborgene Strukturen, Muster oder Beziehungen zu entdecken. Stellen Sie es sich so vor, als würde man versuchen, Chaos in Kategorien zu ordnen, obwohl Ihnen niemand jemals gesagt hat, welche Kategorien das sein sollten.

Stellen Sie sich vor, Sie zeigen dem Modell Tausende von Bildern – Katzen, Hunde, Frösche und Dinosaurier (nehmen wir der Einfachheit halber an, wir hätten irgendwie klare Fotos von ausgestorbenen Reptilien erhalten). Aber wir sagen dem Modell nicht, wer wer ist. Tatsächlich weiß das Modell nicht einmal, wie viele Kategorien es gibt: drei? fünf? fünfzig? Es sucht einfach nach visuellen Mustern. Schließlich beginnt es, pelzige Kreaturen in einem Cluster zu gruppieren, und solche mit glatter Haut, Augen an den Seiten und einem ominös kalten Blick – in einem anderen.

![6](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/6.png)

Nach Tausenden von Beispielen entscheidet das Modell schließlich: „Legen wir alle pelzigen Dinge in Kiste Nr. 1,
und alles mit glänzender Haut und Augen an den Seiten – in Kiste Nr. 2.“ Die Beschriftungen selbst sind nicht wichtig – wichtig ist, dass der Inhalt jeder Kiste homogener wird.

Unüberwachte Modelle versuchen nicht, Beschriftungen vorherzusagen. Stattdessen:
*   **Gruppieren sie ähnliche Objekte (Clustering)**
*   **Erkennen sie Ausreißer oder Anomalien**
*   **Reduzieren sie die Dimensionalität (vereinfachen komplexe Daten)**

Dieses Paradigma ist besonders nützlich, wenn:
*   Die Datenbeschriftung zu teuer oder unpraktisch ist
*   Sie noch nicht wissen, wonach Sie suchen
*   Sie Segmente oder Verhaltensmuster ohne vordefinierte Kategorien entdecken möchten

#### Bestärkendes Lernen (Reinforcement Learning)

In diesem Paradigma lernt das Modell – genannt Agent – durch Interaktion mit der Umgebung mittels Versuch und Irrtum. Der Agent probiert verschiedene Aktionen aus und beobachtet die Reaktion der Umgebung. Aktionen, die zum gewünschten Ergebnis führen, bringen Belohnungen; ineffektive oder schädliche Aktionen führen zu Strafen.

Versuchen wir, eine Katze zu trainieren. (Ja, wir wissen, dass das im wirklichen Leben fast unmöglich ist, aber wir haben uns schon mit dem Katzenthema befasst, also sind wir hier.)
Die Katze ist der Agent. Die Wohnung ist die Umgebung. Die Katze probiert verschiedene Aktionen aus: Eine Fliege gefangen → Leckerli bekommen (Belohnung) Fernseher umgeworfen → kein Abendessen (Strafe)
Durch wiederholte Erfahrungen beginnt die Katze, sich nützlich zu verhalten – nicht, weil sie versteht, was Sie wollen, sondern weil sie eine Strategie gelernt hat: eine Reihe von Aktionen, die am häufigsten zu Futter führen. Sie braucht keine Regeln – sie lernt aus den Konsequenzen.

![7](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/7.png)

*Wie die Grafik zeigt – Schreien bringt nichts.)*

**Bestärkendes Lernen wird verwendet, wenn:**
*   Das Verhalten sich im Laufe der Zeit verbessern muss
*   Es keine vordefinierten „richtigen“ Antworten gibt
*   Konsequenzen verzögert und nicht sofort eintreten

#### Selbstüberwachtes Lernen (Self-Supervised Learning)

Bei diesem Ansatz lernt das Modell aus unbeschrifteten Daten, aber die Lernaufgabe wird aus den Daten selbst extrahiert – ohne menschliches Eingreifen bei der Beschriftung. Das Modell lernt, einen Teil der Eingabedaten basierend auf einem anderen Teil vorherzusagen.

**Beispiel**
Originalsatz: *„Die Katze sprang auf die Tastatur und committete unfertigen Code in die Produktion.“*

Wir können dies in eine Lernaufgabe umwandeln. Zum Beispiel:
*   **Ein Wort maskieren:** *Eingabe:* „Die Katze sprang auf die \*\*\* und deployte unfertigen Code...“, *Ziel:* das Wort **Tastatur** vorhersagen.
*   **Satz abbrechen:** *Eingabe:* „Die Katze sprang auf...“, *Ziel:* den Satz fortsetzen.

![8](../assets/Что_такое_машинное_обучение_и_как_оно_на_самом_деле_учится/8.png)

*Für eine Tensor-Katze ist das Schreiben auf dem Kopf nur eine Frage der Wahl des richtigen Koordinatensystems.*

Diese „Eingabe + Ziel“-Paare werden automatisch generiert, ohne manuelle Beschriftung. Dieselbe Idee gilt für verschiedene Datentypen, wie Bilder (Vorhersage fehlender Fragmente) oder Audio.

**Reale Anwendungen des selbstüberwachten Lernens:**
*   **Sprachmodelle** (GPT, LLaMA, Claude)
*   **Computer Vision** (CLIP, DINO)
*   **Audio und Sprache** (Wav2Vec 2.0)
*   **Multimodale Modelle** (Gemini, CLIP)
*   **Vortraining (Grundlagenmodelle)**

**Hauptidee**
Das Modell lernt aus automatisch generierten Aufgaben, bei denen die „richtige Antwort“ direkt aus den Daten selbst extrahiert wird. Dies verleiht uns Skalierbarkeit, Verallgemeinerungsfähigkeit und die Grundlage für die meisten modernen generativen und Sprachsysteme.

#### Zusammenfassung der Lernparadigmen

| Paradigma                 | Wie das Modell lernt                                         |
|---------------------------|--------------------------------------------------------------|
| Überwachtes Lernen        | An beschrifteten Daten (Eingabe → richtige Antwort)          |
| Unüberwachtes Lernen      | An unbeschrifteten Daten (Modell findet Struktur selbst)     |
| Bestärkendes Lernen       | Durch Interaktion mit der Umgebung über Belohnungen und Strafen |
| Selbstüberwachtes Lernen | An unbeschrifteten Daten, wobei Aufgaben aus diesen generiert werden |

#### Was gibt es sonst noch?

Neben diesen vier gibt es noch andere Ansätze (semi-überwachtes, aktives, Online-Lernen usw.). Sie werden selten als eigenständige Paradigmen betrachtet, da sie in der Regel Hybride oder Variationen der bereits besprochenen Hauptstrategien sind. Um das Wesen des maschinellen Lernens zu verstehen, genügt es, diese vier zu beherrschen.

Im nächsten Teil werden wir uns damit befassen, was ein neuronales Netzwerk wirklich ist: Neuronen, Gewichte, Verbindungen. Wie „lernt“ es? Warum braucht es überhaupt Schichten? Und was hat ein Haufen Zahlen mit dem Verständnis von Sprache, Bildern oder… der Realität zu tun?

Wir werden Schicht für Schicht abtragen – und versuchen, die einzige Frage zu beantworten, die zählt:

**Gibt es hier also irgendeine Magie… oder ist es nur verkleidete Mathematik?**

https://medium.com/@paul.ilvez/how-ai-learns-no-formulas-but-plenty-of-cats-fc43471add24
