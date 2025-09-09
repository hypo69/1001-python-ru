# Wie man einem neuronalen Netzwerk beibringt, mit den Händen zu arbeiten: Erstellung eines vollwertigen KI-Agenten mit MCP und LangGraph in einer Stunde

Freunde, Grüße! Ich hoffe, ihr habt mich vermisst.

In den letzten Monaten habe ich mich intensiv mit der Integration von KI-Agenten in meine eigenen Python-Projekte beschäftigt. Dabei habe ich viele praktische Kenntnisse und Beobachtungen gesammelt, die ich einfach teilen muss. Deshalb kehre ich heute zu Habr zurück – mit einem neuen Thema, einer frischen Perspektive und der Absicht, häufiger zu schreiben.

Auf der Tagesordnung stehen LangGraph und MCP: Tools, mit denen Sie wirklich nützliche KI-Agenten erstellen können.

Wenn wir uns früher darüber gestritten haben, welches neuronale Netzwerk auf Russisch besser antwortet, hat sich das Schlachtfeld heute auf anwendungsbezogenere Aufgaben verlagert: Wer bewältigt die Rolle eines KI-Agenten besser? Welche Frameworks vereinfachen die Entwicklung wirklich? Und wie integriert man all das Gute in ein reales Projekt?

Doch bevor wir in die Praxis und den Code eintauchen, klären wir die grundlegenden Konzepte. Insbesondere zwei Schlüsselkonzepte: **KI-Agenten und MCP**. Ohne sie wäre das Gespräch über LangGraph unvollständig.

### KI-Agenten einfach erklärt

KI-Agenten sind nicht nur „aufgepumpte“ Chatbots. Sie stellen komplexere, autonome Entitäten dar, die zwei entscheidende Merkmale besitzen:

1.  **Fähigkeit zur Interaktion und Koordination**

    Moderne Agenten können Aufgaben in Unteraufgaben zerlegen, andere Agenten aufrufen, externe Daten anfordern, im Team arbeiten. Dies ist kein einzelner Assistent mehr, sondern ein verteiltes System, in dem jede Komponente ihren Beitrag leisten kann.

2.  **Zugriff auf externe Ressourcen**

    Ein KI-Agent ist nicht mehr auf die Grenzen eines Dialogs beschränkt. Er kann auf Datenbanken zugreifen, API-Aufrufe tätigen, mit lokalen Dateien, vektorbasierten Wissensdatenbanken interagieren und sogar Befehle im Terminal ausführen. All dies wurde durch die Entstehung von MCP möglich – einer neuen Ebene der Integration zwischen Modell und Umgebung.

---

Einfach ausgedrückt: **MCP ist eine Brücke zwischen einem neuronalen Netzwerk und seiner Umgebung**. Es ermöglicht dem Modell, den Kontext der Aufgabe zu „verstehen“, auf Daten zuzugreifen, Aufrufe zu tätigen und begründete Aktionen zu bilden, anstatt nur Textantworten auszugeben.

**Stellen wir uns eine Analogie vor:**

*   Sie haben ein **neuronales Netzwerk** – es kann denken und Texte generieren.
*   Es gibt **Daten und Tools** – Dokumente, APIs, Wissensdatenbanken, Terminal, Code.
*   Und es gibt **MCP** – es ist eine Schnittstelle, die es dem Modell ermöglicht, mit diesen externen Quellen zu interagieren, als wären sie Teil seiner inneren Welt.

**Ohne MCP:**

Modell – ist eine isolierte Dialog-Engine. Sie geben ihm Text – es antwortet. Und das war's.

**Mit MCP:**

Das Modell wird zu einem vollwertigen **Aufgabenausführer**:

*   erhält Zugriff auf Datenstrukturen und APIs;
*   ruft externe Funktionen auf;
*   navigiert im aktuellen Zustand des Projekts oder der Anwendung;
*   kann den Kontext während des Dialogs speichern, verfolgen und ändern;
*   verwendet Erweiterungen wie Suchwerkzeuge, Code-Runner, Vektor-Embedding-Datenbanken usw.

Im technischen Sinne ist **MCP ein Protokoll für die Interaktion zwischen einem LLM und seiner Umgebung**, wobei der Kontext als strukturierte Objekte (anstelle von „rohem“ Text) bereitgestellt wird und Aufrufe als interaktive Operationen (z. B. Funktionsaufrufe, Tool-Nutzung oder Agentenaktionen) formatiert werden. Dies ist es, was ein gewöhnliches Modell in einen **echten KI-Agenten** verwandelt, der mehr als nur „reden“ kann.

### Und nun – zur Sache!

Nachdem wir die grundlegenden Konzepte behandelt haben, ist es logisch zu fragen: „Wie setzen wir das alles in der Praxis in Python um?“

Hier kommt **LangGraph** ins Spiel – ein leistungsstarkes Framework zum Erstellen von Zustandsgraphen, Agentenverhalten und Denkketten. Es ermöglicht Ihnen, die Logik der Interaktion zwischen Agenten, Tools und dem Benutzer zu „verknüpfen“ und eine lebendige KI-Architektur zu schaffen, die sich an Aufgaben anpasst.

In den folgenden Abschnitten werden wir uns ansehen, wie man:

*   einen Agenten von Grund auf neu erstellt;
*   Zustände, Übergänge und Ereignisse erstellt;
*   Funktionen und Tools integriert;
*   und wie dieses gesamte Ökosystem in einem realen Projekt funktioniert.

### Ein wenig Theorie: Was ist LangGraph

Bevor wir in die Praxis eintauchen, ein paar Worte zum Framework selbst.

**LangGraph** ist ein Projekt des **LangChain**-Teams, genau derjenigen, die als erste das Konzept der „Ketten“ (chains) für die Interaktion mit LLMs vorgeschlagen haben. Wenn der Schwerpunkt früher auf linearen oder bedingt verzweigten Pipelines (langchain.chains) lag, setzen die Entwickler nun auf ein **Graphenmodell**, und LangGraph ist das, was sie als neuen „Kern“ für den Aufbau komplexer KI-Systeme empfehlen.

**LangGraph** ist ein Framework zum Erstellen von endlichen Automaten und Zustandsgraphen, wobei jeder **Knoten** einen Teil der Agentenlogik darstellt: einen Modellaufruf, ein externes Tool, eine Bedingung, Benutzereingaben usw.

### Wie es funktioniert: Graphen und Knoten

Konzeptionell basiert LangGraph auf den folgenden Ideen:

*   **Graph** – ist eine Struktur, die die möglichen Ausführungspfade der Logik beschreibt. Man kann ihn sich wie eine Karte vorstellen: Von einem Punkt kann man je nach Bedingungen oder Ausführungsergebnis zu einem anderen wechseln.
*   **Knoten** – sind spezifische Schritte innerhalb des Graphen. Jeder Knoten führt eine Funktion aus: ruft ein Modell auf, ruft eine externe API auf, prüft eine Bedingung oder aktualisiert einfach den internen Zustand.
*   **Übergänge zwischen Knoten** – ist die Routing-Logik: Wenn das Ergebnis des vorherigen Schritts so und so ist, dann gehen Sie dorthin.
*   **Zustand** – wird zwischen Knoten übergeben und sammelt alles Notwendige: Verlauf, Zwischenergebnisse, Benutzereingaben, Ergebnisse von Tool-Operationen usw.

So erhalten wir einen **flexiblen Mechanismus zur Steuerung der Agentenlogik**, in dem sowohl einfache als auch sehr komplexe Szenarien beschrieben werden können: Schleifen, Bedingungen, parallele Aktionen, verschachtelte Aufrufe und vieles mehr.

### Warum ist das praktisch?

LangGraph ermöglicht den Aufbau einer **transparenten, reproduzierbaren und erweiterbaren Logik**:

*   einfach zu debuggen;
*   einfach zu visualisieren;
*   einfach an neue Aufgaben anzupassen;
*   einfach externe Tools und MCP-Protokolle zu integrieren.

Im Wesentlichen ist LangGraph das **„Gehirn“ des Agenten**, wobei jeder Schritt dokumentiert, kontrollierbar und ohne Chaos und „Magie“ geändert werden kann.

### Und nun – genug Theorie!

Wir könnten noch lange über Graphen, Zustände, Logikkomposition und die Vorteile von LangGraph gegenüber klassischen Pipelines sprechen. Aber, wie die Praxis zeigt, ist es besser, es einmal im Code zu sehen.

**Zeit, zur Praxis überzugehen.** Als Nächstes – ein Python-Beispiel: Wir erstellen einen einfachen, aber nützlichen KI-Agenten auf Basis von LangGraph, der externe Tools, Speicher und eigene Entscheidungen verwendet.

### Vorbereitung: Cloud- und lokale neuronale Netze

Um mit der Erstellung von KI-Agenten zu beginnen, benötigen wir zunächst ein **Gehirn** – ein Sprachmodell. Hier gibt es zwei Ansätze:

*   **Cloud-Lösungen verwenden**, bei denen alles „out of the box“ fertig ist;
*   oder **das Modell lokal hochfahren** – für vollständige Autonomie und Vertraulichkeit.

Betrachten wir beide Optionen.

#### Cloud-Dienste: schnell und bequem

Der einfachste Weg ist, die Leistung großer Anbieter zu nutzen: OpenAI, Anthropic und zu verwenden...

### Woher man Schlüssel und Token bekommt:

*   **OpenAI** – ChatGPT und andere Produkte;
*   **Anthropic** – Claude;
*   **OpenRouter.ai** – Dutzende von Modellen (ein Token – viele Modelle über eine OpenAI-kompatible API);
*   **Amvera Cloud** – Möglichkeit, LLAMA mit Rubelzahlung und integriertem Proxy zu OpenAI und Anthropic zu verbinden.

Dieser Weg ist bequem, besonders wenn Sie:

*   keine Infrastruktur konfigurieren möchten;
*   mit Fokus auf Geschwindigkeit entwickeln;
*   mit begrenzten Ressourcen arbeiten.

#### Lokale Modelle: volle Kontrolle

Wenn Ihnen **Datenschutz, Offline-Arbeit** wichtig sind oder Sie **vollständig autonome Agenten** erstellen möchten, ist es sinnvoll, das neuronale Netzwerk lokal bereitzustellen.

**Hauptvorteile:**

*   **Vertraulichkeit** – Daten bleiben bei Ihnen;
*   **Offline-Arbeit** – nützlich in isolierten Netzwerken;
*   **Keine Abonnements und Token** – nach der Einrichtung kostenlos.

**Nachteile sind offensichtlich:**

*   Ressourcenanforderungen (insbesondere für den Videospeicher);
*   Die Einrichtung kann Zeit in Anspruch nehmen;
*   Einige Modelle sind ohne Erfahrung schwer bereitzustellen.

Dennoch gibt es Tools, die den lokalen Start erleichtern. Eines der besten heute ist **Ollama**.

### Bereitstellung eines lokalen LLM über Ollama + Docker

Wir werden eine lokale Bereitstellung des Qwen 2.5-Modells (qwen2.5:32b) unter Verwendung eines Docker-Containers und des Ollama-Systems vorbereiten. Dies ermöglicht die Integration des neuronalen Netzwerks mit MCP und dessen Verwendung in Ihren eigenen Agenten auf Basis von LangGraph.

Sollten die Rechenressourcen Ihres Computers oder Servers für die Arbeit mit dieser Version des Modells nicht ausreichen, können Sie jederzeit ein weniger „ressourcenhungriges“ neuronales Netzwerk wählen – der Installations- und Startvorgang bleibt ähnlich.

**Schnelle Installation (Zusammenfassung der Schritte)**

1.  **Docker + Docker Compose installieren**
2.  **Projektstruktur erstellen:**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **`docker-compose.yml` erstellen**
(universelle Option, GPU wird automatisch erkannt)

```yaml
services:
  ollama:
    image: ollama/ollama:latest
    container_name: ollama_qwen
    ports:
      - "11434:11434"
    volumes:
      - ./ollama_data:/root/.ollama
      - /tmp:/tmp
    environment:
      - OLLAMA_HOST=0.0.0.0
      - OLLAMA_ORIGINS=*
    restart: unless-stopped
```

4.  **Container starten:**
```bash
docker compose up -d
```

5.  **Modell herunterladen:**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **API-Betrieb prüfen:**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "Hallo!", "stream": false}'
```
*(Bild mit dem Ergebnis der Befehlsausführung)*

7.  **Integration mit Python:**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:32b",
        "prompt": prompt,
        "stream": False
    })
    return res.json()['response']

print(query("Erklären Sie die Quantenverschränkung"))
```
Jetzt haben Sie ein vollwertiges lokales LLM, das bereit ist, mit MCP und LangGraph zu arbeiten.

**Was kommt als Nächstes?**

Wir haben die Wahl zwischen Cloud- und lokalen Modellen, und wir haben gelernt, wie man beide verbindet. Das Interessanteste steht noch bevor – **die Erstellung von KI-Agenten auf LangGraph**, die das ausgewählte Modell, den Speicher, die Tools und ihre eigene Logik verwenden.

**Kommen wir zum leckersten Teil – Code und Praxis!**

---

Bevor wir zur Praxis übergehen, ist es wichtig, die Arbeitsumgebung vorzubereiten. Ich gehe davon aus, dass Sie bereits mit den Grundlagen von Python vertraut sind, wissen, was Bibliotheken und Abhängigkeiten sind, und verstehen, warum eine virtuelle Umgebung verwendet werden sollte.

Wenn all dies neu für Sie ist – empfehle ich Ihnen, zuerst einen kurzen Kurs oder Leitfaden zu den Python-Grundlagen zu absolvieren und dann zum Artikel zurückzukehren.

#### Schritt 1: Erstellen einer virtuellen Umgebung

Erstellen Sie einen neuen virtuellen Umgebung im Projektordner:
```bash
python -m venv venv
source venv/bin/activate  # für Linux/macOS
virtualenv\Scripts\activate   # für Windows
```

#### Schritt 2: Installieren von Abhängigkeiten

Erstellen Sie eine Datei `requirements.txt` und fügen Sie die folgenden Zeilen hinzu:
```
langchain==0.3.26
langchain-core==0.3.69
langchain-deepseek==0.1.3
langchain-mcp-adapters==0.1.9
langchain-ollama==0.3.5
langchain-openai==0.3.28
langgraph==0.5.3
langgraph-checkpoint==2.1.1
langgraph-prebuilt==0.5.2
langgraph-sdk==0.1.73
langsmith==0.4.8
mcp==1.12.0
ollama==0.5.1
openai==1.97.0
```

> ⚠️ **Aktuelle Versionen sind vom 21. Juli 2025.** Sie könnten sich seit der Veröffentlichung geändert haben – **prüfen Sie die Relevanz vor der Installation.**

Installieren Sie dann die Abhängigkeiten:
```bash
pip install -r requirements.txt```

#### Schritt 3: Konfigurieren von Umgebungsvariablen

Erstellen Sie eine `.env`-Datei im Projektstammverzeichnis und fügen Sie die erforderlichen API-Schlüssel hinzu:
```
OPENAI_API_KEY=sk-proj-1234
DEEPSEEK_API_KEY=sk-123
OPENROUTER_API_KEY=sk-or-v1-123
BRAVE_API_KEY=BSAj123K1bvBGpH1344tLwc
```

**Zweck der Variablen:**

*   **OPENAI_API_KEY** – Schlüssel für den Zugriff auf GPT-Modelle von OpenAI;
*   **DEEPSEEK_API_KEY** – Schlüssel für die Verwendung von Deepseek-Modellen;
*   **OPENROUTER_API_KEY** – Einzelschlüssel für den Zugriff auf viele Modelle über OpenRouter

---

Einige MCP-Tools (z. B. `brave-web-search`) benötigen einen Schlüssel, um zu funktionieren. Ohne ihn werden sie einfach nicht aktiviert.

**Was ist, wenn Sie keine API-Schlüssel haben?**

Kein Problem. Sie können die Entwicklung mit einem lokalen Modell (z. B. über Ollama) beginnen, ohne externe Dienste zu verbinden. In diesem Fall muss die `.env`-Datei überhaupt nicht erstellt werden.

Fertig! Jetzt haben wir alles, was wir brauchen, um zu beginnen – eine isolierte Umgebung, Abhängigkeiten und, falls erforderlich, Zugriff auf Cloud-neuronale Netze und MCP-Integrationen.

Als Nächstes – lassen Sie uns unseren LLM-Agenten auf verschiedene Arten ausführen.

### Einfacher Start von LLM-Agenten über LangGraph: grundlegende Integration

Beginnen wir mit dem Einfachsten: wie man dem zukünftigen Agenten „ein Gehirn anschließt“. Wir werden die grundlegenden Möglichkeiten zum Starten von Sprachmodellen (LLMs) mit LangChain analysieren, um im nächsten Schritt zur Integration mit LangGraph und zum Aufbau eines vollwertigen KI-Agenten überzugehen.

#### Importe
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` und `load_dotenv()` – zum Laden von Variablen aus der `.env`-Datei.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` – Wrapper zum Verbinden von Sprachmodellen über LangChain.

> 💡 Wenn Sie alternative Ansätze zur Arbeit mit Konfigurationen verwenden (z. B. Pydantic Settings), können Sie `load_dotenv()` durch Ihre übliche Methode ersetzen.

#### Laden von Umgebungsvariablen
```python
load_dotenv()
```
Dadurch werden alle Variablen aus `.env` geladen, einschließlich der Schlüssel für den Zugriff auf die OpenAI-, DeepSeek-, OpenRouter-APIs und andere.

#### Einfache Funktionen zum Abrufen von LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
Wenn die Variable `OPENAI_API_KEY` korrekt gesetzt ist, ersetzt LangChain sie automatisch – die explizite Angabe von `api_key=...` ist hier optional.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
Ähnlich, aber wir verwenden den `ChatDeepSeek`-Wrapper.

**OpenRouter (und andere kompatible APIs)**
```python
def get_openrouter_llm(model="moonshotai/kimi-k2:free"):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
```
**Merkmale:**

*   `ChatOpenAI` wird verwendet, obwohl das Modell nicht von OpenAI stammt – weil OpenRouter dasselbe Protokoll verwendet.
*   `base_url` ist erforderlich: Es verweist auf die OpenRouter-API.
*   Das Modell `moonshotai/kimi-k2:free` wurde zum Zeitpunkt der Erstellung als eine der ausgewogensten Optionen in Bezug auf Qualität und Geschwindigkeit ausgewählt.
*   Der `OpenRouter`-API-Schlüssel muss explizit übergeben werden – die automatische Ersetzung funktioniert hier nicht.

#### Mini-Test: Überprüfung des Modellbetriebs
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("Wer bist du?")
    print(response.content)
```
*(Bild mit Ausführungsergebnis: `Ich bin ein KI-Assistent, erstellt von Moonshot AI...`)*

Wenn alles richtig konfiguriert ist, erhalten Sie eine sinnvolle Antwort vom Modell. Herzlichen Glückwunsch – der erste Schritt ist getan!

### Aber das ist noch kein Agent

Im aktuellen Stadium haben wir LLM verbunden und einen einfachen Aufruf getätigt. Das ähnelt eher einem Konsolen-Chatbot als einem KI-Agenten.

**Warum?**

*   Wir schreiben **synchronen, linearen Code** ohne Zustandslogik oder Ziele.
*   Der Agent trifft keine Entscheidungen, speichert keinen Kontext und verwendet keine Tools.
*   MCP und LangGraph sind noch nicht beteiligt.

**Was kommt als Nächstes?**

Als Nächstes werden wir einen **vollwertigen KI-Agenten** mit **LangGraph** implementieren – zunächst ohne MCP, um uns auf die Architektur, Zustände und Logik des Agenten selbst zu konzentrieren.

Tauchen wir ein in die echte Agentenmechanik. Los geht's!

### Stellenklassifizierungsagent: von der Theorie zur Praxis

...Konzepte von LangGraph in der Praxis und ein nützliches Tool für HR-Plattformen und Freelance-Börsen erstellen.

#### Agentenaufgabe

Unser Agent nimmt eine Textbeschreibung einer Vakanz oder Dienstleistung als Eingabe entgegen und führt eine dreistufige Klassifizierung durch:

1.  **Art der Arbeit**: Projektarbeit oder Festanstellung
2.  **Berufskategorie**: aus über 45 vordefinierten Spezialitäten
3.  **Art der Suche**: ob eine Person Arbeit sucht oder einen Ausführenden sucht

Das Ergebnis wird in einem strukturierten JSON-Format mit einem Konfidenzwert für jede Klassifizierung zurückgegeben.

#### 📈 Agentenarchitektur auf LangGraph

Nach den Prinzipien von LangGraph erstellen wir einen **Zustandsgraphen** aus vier Knoten:

- Eingabebeschreibung
- ↓
- Knoten zur Klassifizierung der Arbeitsart
- ↓
- Knoten zur Klassifizierung der Kategorie
- ↓
- Knoten zur Bestimmung der Suchart
- ↓
- Knoten zur Konfidenzberechnung
- ↓
- JSON-Ergebnis

Jeder Knoten ist eine **spezialisierte Funktion**, die:

*   Den aktuellen Zustand des Agenten empfängt
*   Ihren Teil der Analyse durchführt
*   Den Zustand aktualisiert und weitergibt

#### Zustandsverwaltung

Definieren Sie die **Speicherstruktur des Agenten** über `TypedDict`:

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """Agentenzustand zum Speichern von Informationen über den Klassifizierungsprozess"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

Dies ist der **Arbeitsspeicher des Agenten** – alles, was er während der Analyse speichert und ansammelt. Ähnlich wie ein menschlicher Experte den Aufgabenkontext bei der Analyse eines Dokuments im Kopf behält.

Schauen wir uns den vollständigen Code an und konzentrieren uns dann auf die Hauptpunkte.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Berufskategorien
CATEGORIES = [
    "2D-Animator", "3D-Animator", "3D-Modellierer",
    "Business Analyst", "Blockchain-Entwickler", ...
]

class JobType(Enum):
    PROJECT = "Projektarbeit"
    PERMANENT = "Festanstellung"

class SearchType(Enum):
    LOOKING_FOR_WORK = "Arbeitssuchend"
    LOOKING_FOR_PERFORMER = "Suche nach einem Ausführenden"

class State(TypedDict):
    """Agentenzustand zum Speichern von Informationen über den Klassifizierungsprozess"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool

class VacancyClassificationAgent:
    """Asynchroner Agent zur Klassifizierung von Vakanzen und Dienstleistungen"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Agenteninitialisierung"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Erstellt den Workflow des Agenten basierend auf LangGraph"""
        workflow = StateGraph(State)
        
        # Knoten zum Graphen hinzufügen
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Reihenfolge der Knotenausführung definieren
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Knoten zur Bestimmung der Arbeitsart: Projekt oder Festanstellung"""
        # ... (Implementierung folgt)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Knoten zur Bestimmung der Berufskategorie"""
        # ... (Implementierung folgt)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Knoten zur Bestimmung der Suchart"""
        # ... (Implementierung folgt)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Knoten zur Berechnung des Konfidenzniveaus in der Klassifizierung"""
        # ... (Implementierung folgt)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Findet die nächstgelegene Kategorie aus der Liste der verfügbaren"""
        # ... (Implementierung folgt)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Hauptmethode zur Klassifizierung von Vakanzen/Dienstleistungen"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Workflow starten
        result = await self.workflow.ainvoke(initial_state)
        
        # Endgültige JSON-Antwort erstellen
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Demonstration des Agentenbetriebs"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Benötigt Python-Entwickler zur Erstellung einer Webanwendung mit Django. Festanstellung.",
        "Suche Aufträge zur Erstellung von Logos und Corporate Identity. Ich arbeite in Adobe Illustrator.",
        "Benötige 3D-Animator für ein kurzfristiges Projekt zur Erstellung eines Werbespots.",
        "Lebenslauf: erfahrener Marketingexperte, suche Remote-Arbeit im Bereich Digitalmarketing",
        "Suchen React-Frontend-Entwickler für unser Team auf Festanstellung"
    ]
    
    print("🤖 Demonstration des Betriebs des Stellenklassifizierungsagenten\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Test {i}: ---")
        print(f"Beschreibung: {description}")
        try:
            result = await agent.classify(description)
            print("Klassifizierungsergebnis:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Fehler: {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...der Rest des Codes mit der Implementierung der Methoden wurde im Artikel vorgestellt...)*

### Hauptvorteile der Architektur
1.  **Modularität** – jeder Knoten löst eine Aufgabe, leicht separat zu testen und zu verbessern
2.  **Erweiterbarkeit** – neue Analyseknoten können hinzugefügt werden, ohne bestehende zu ändern
3.  **Transparenz** – der gesamte Entscheidungsprozess ist dokumentiert und nachvollziehbar
4.  **Leistung** – asynchrone Verarbeitung mehrerer Anfragen
5.  **Zuverlässigkeit** – integrierte Fallback-Mechanismen und Fehlerbehandlung

### Echter Nutzen
Ein solcher Agent kann verwendet werden in:
*   **HR-Plattformen** zur automatischen Kategorisierung von Lebensläufen und Vakanzen
*   **Freelance-Börsen** zur Verbesserung der Suche und Empfehlungen
*   **Internen Systemen** von Unternehmen zur Bearbeitung von Anfragen und Projekten
*   **Analytischen Lösungen** zur Arbeitsmarktforschung

### MCP in Aktion: Erstellung eines Agenten mit Dateisystem und Websuche
Nachdem wir die Grundprinzipien von LangGraph verstanden und einen einfachen Klassifizierungsagenten erstellt haben, erweitern wir seine Fähigkeiten, indem wir ihn über MCP mit der Außenwelt verbinden.

Jetzt werden wir einen vollwertigen KI-Assistenten erstellen, der Folgendes kann:
*   Mit dem Dateisystem arbeiten (Dateien lesen, erstellen, ändern)
*   Relevante Informationen im Internet suchen
*   Den Kontext des Dialogs speichern
*   Fehler behandeln und sich von Ausfällen erholen

#### Von der Theorie zu realen Tools
Erinnern Sie sich, wie wir am Anfang des Artikels darüber gesprochen haben, dass **MCP eine Brücke zwischen einem neuronalen Netzwerk und seiner Umgebung** ist? Jetzt werden Sie dies in der Praxis sehen. Unser Agent erhält Zugriff auf **reale Tools**:
```
# Dateisystem-Tools
- read_file – Dateien lesen
- write_file – Dateien schreiben und erstellen
- list_directory – Ordnerinhalte anzeigen
- create_directory – Ordner erstellen

# Websuch-Tools
- brave_web_search – im Internet suchen
- get_web_content – Seiteninhalte abrufen
```
Dies ist kein „Spielzeug“-Agent mehr – es ist ein **Arbeitswerkzeug**, das reale Probleme lösen kann.

#### 📈 Architektur: vom Einfachen zum Komplexen

**1. Konfiguration als Basis der Stabilität**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Vereinfachte KI-Agentenkonfiguration"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Konfigurationsvalidierung"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"Pfad existiert nicht: {self.filesystem_path}")
```
**Warum ist das wichtig?** Im Gegensatz zum Klassifizierungsbeispiel interagiert der Agent hier mit externen Systemen. Ein Fehler im Dateipfad oder ein fehlender API-Schlüssel – und der gesamte Agent funktioniert nicht mehr. **Die Validierung beim Start** spart Stunden beim Debuggen.

**2. Modellfabrik: flexible Auswahl**
```python
def create_model(config: AgentConfig):
    """Erstellt ein Modell gemäß der Konfiguration"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... andere Anbieter
```
Ein Code – viele Modelle. Möchten Sie ein kostenloses lokales Modell? Verwenden Sie Ollama. Benötigen Sie maximale Genauigkeit? Wechseln Sie zu GPT-4. Ist Geschwindigkeit wichtig? Probieren Sie DeepSeek. Der Code bleibt derselbe.

**3. MCP-Integration: Verbindung zur realen Welt**
```python
async def _init_mcp_client(self):
    """MCP-Client-Initialisierung"""
    mcp_config = {
        "filesystem": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-filesystem", self.filesystem_path],
            "transport": "stdio"
        },
        "brave-search": {
            "command": "npx",
            "args": ["-y", "@modelcontextprotocol/server-brave-search@latest"],
            "transport": "stdio",
            "env": {"BRAVE_API_KEY": os.getenv("BRAVE_API_KEY")}
        }
    }
    self.mcp_client = MultiServerMCPClient(mcp_config)
    self.tools = await self.mcp_client.get_tools()
```
Hier findet die entscheidende MCP-Arbeit statt: Wir verbinden externe MCP-Server mit dem Agenten, die eine Reihe von Tools und Funktionen bereitstellen. Der Agent erhält dabei nicht nur einzelne Funktionen, sondern ein vollständiges kontextuelles Verständnis dafür, wie er mit dem Dateisystem und dem Internet arbeiten kann.

#### Fehlertoleranz
In der realen Welt geht alles kaputt: Das Netzwerk ist nicht verfügbar, Dateien sind blockiert, API-Schlüssel sind abgelaufen. Unser Agent ist darauf vorbereitet:
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
Der `@retry_on_failure`-Decorator wiederholt Operationen bei temporären Fehlern automatisch. Der Benutzer wird nicht einmal bemerken, dass etwas schiefgelaufen ist.

### Ergebnisse: von der Theorie zur Praxis der KI-Agenten

Heute haben wir den Weg von den grundlegenden Konzepten bis zur Erstellung funktionierender KI-Agenten zurückgelegt. Fassen wir zusammen, was wir gelernt und erreicht haben.

**Was wir gemeistert haben**

**1. Grundlegende Konzepte**
*   Den Unterschied zwischen Chatbots und echten KI-Agenten verstanden
*   Die Rolle von **MCP (Model Context Protocol)** als Brücke zwischen dem Modell und der Außenwelt verstanden
*   Die Architektur von **LangGraph** zum Aufbau komplexer Agentenlogik studiert

**2. Praktische Fähigkeiten**
*   Eine Arbeitsumgebung mit Unterstützung für Cloud- und lokale Modelle konfiguriert
*   Einen **Klassifizierungsagenten** mit asynchroner Architektur und Zustandsverwaltung erstellt
*   Einen **MCP-Agenten** mit Zugriff auf das Dateisystem und die Websuche erstellt

**3. Architekturmuster**
*   Modulare Konfiguration und Modellfabriken beherrscht
*   Fehlerbehandlung und **Wiederholungsmechanismen** für produktionsreife Lösungen implementiert

### Hauptvorteile des Ansatzes
**LangGraph + MCP** bieten uns:
*   **Transparenz** – jeder Agentenschritt ist dokumentiert und nachvollziehbar
*   **Erweiterbarkeit** – neue Funktionen werden deklarativ hinzugefügt
*   **Zuverlässigkeit** – integrierte Fehlerbehandlung und Wiederherstellung
*   **Flexibilität** – Unterstützung für mehrere Modelle und Anbieter out of box

### Fazit

KI-Agenten sind keine futuristische Fiktion, sondern **reale Technologie von heute**. Mit LangGraph und MCP können wir Systeme erstellen, die spezifische Geschäftsprobleme lösen, Routinen automatisieren und neue Möglichkeiten eröffnen.

**Das Wichtigste ist, anzufangen.** Nehmen Sie den Code aus den Beispielen, passen Sie ihn an Ihre Aufgaben an, experimentieren Sie. Jedes Projekt ist eine neue Erfahrung und ein Schritt zur Meisterschaft im Bereich der KI-Entwicklung.

Viel Erfolg bei Ihren Projekten!

---
*Tags: python, ki, mcp, langchain, ki-assistent, ollama, ki-agenten, local llm, langgraph, mcp-server*
*Hubs: Amvera Unternehmensblog, Natural Language Processing, Künstliche Intelligenz, Python, Programmierung*
