## Jak nauczyć sieć neuronową pracować rękami: tworzenie pełnowartościowego agenta AI z MCP i LangGraph w godzinę


Przyjaciele, witam! Mam nadzieję, że stęskniliście się.

Przez ostatnie kilka miesięcy byłem głęboko zaangażowany w badanie integracji agentów AI we własnych projektach Python. W tym procesie zgromadziłem sporo praktycznej wiedzy i obserwacji, którymi po prostu grzechem byłoby się nie podzielić. Dlatego dziś wracam na Habr – z nowym tematem, świeżym spojrzeniem i zamiarem częstszego pisania.

Na porządku dziennym są LangGraph i MCP: narzędzia, za pomocą których można tworzyć naprawdę użyteczne agenty AI.

Jeśli wcześniej spieraliśmy się o to, która sieć neuronowa lepiej odpowiada po rosyjsku, to dziś pole bitwy przesunęło się w stronę bardziej praktycznych zadań: kto lepiej radzi sobie z rolą agenta AI? Jakie frameworki naprawdę upraszczają rozwój? I jak zintegrować to wszystko w prawdziwym projekcie?

Ale zanim zanurkujemy w praktykę i kod, przyjrzyjmy się podstawowym pojęciom. Zwłaszcza dwóm kluczowym: **agentom AI i MCP**. Bez nich rozmowa o LangGraph będzie niekompletna.

### Agenty AI w prostych słowach

Agenty AI to nie tylko „ulepszone” chatboty. Są to bardziej złożone, autonomiczne byty, które posiadają dwie najważniejsze cechy:

1.  **Umiejętność interakcji i koordynacji**

    Współczesne agenty potrafią dzielić zadania na podzadania, wywoływać inne agenty, żądać danych zewnętrznych, pracować w zespole. To już nie samotny asystent, ale rozproszony system, w którym każdy komponent może wnieść swój wkład.

2.  **Dostęp do zasobów zewnętrznych**

    Agent AI nie jest już ograniczony ramami dialogu. Może uzyskiwać dostęp do baz danych, wykonywać wywołania API, wchodzić w interakcje z plikami lokalnymi, wektorowymi bazami wiedzy, a nawet uruchamiać polecenia w terminalu. Wszystko to stało się możliwe dzięki pojawieniu się MCP – nowego poziomu integracji między modelem a środowiskiem.

---

Jeśli mówić prosto: **MCP to most między siecią neuronową a jej otoczeniem**. Pozwala modelowi „rozumieć” kontekst zadania, uzyskiwać dostęp do danych, wykonywać wywołania i formułować uzasadnione działania, a nie tylko wydawać odpowiedzi tekstowe.

**Wyobraźmy sobie analogię:**

*   Masz **sieć neuronową** – potrafi rozumować i generować teksty.
*   Są **dane i narzędzia** – dokumenty, API, bazy wiedzy, terminal, kod.
*   I jest **MCP** – to interfejs, który pozwala modelowi wchodzić w interakcje z tymi zewnętrznymi źródłami tak, jakby były częścią jego wewnętrznego świata.

**Bez MCP:**

Model to izolowany silnik dialogowy. Podajesz mu tekst – odpowiada. I tyle.

**Z MCP:**

Model staje się pełnoprawnym **wykonawcą zadań**:

*   uzyskuje dostęp do struktur danych i API;
*   wywołuje funkcje zewnętrzne;
*   orientuje się w bieżącym stanie projektu lub aplikacji;
*   może zapamiętywać, śledzić i zmieniać kontekst w trakcie dialogu;
*   wykorzystuje rozszerzenia, takie jak narzędzia wyszukiwania, uruchamiacze kodu, bazę osadzeń wektorowych itp.

Technicznie rzecz biorąc, **MCP to protokół interakcji między LLM a jego otoczeniem**, gdzie kontekst jest dostarczany w postaci ustrukturyzowanych obiektów (zamiast „surowego” tekstu), a wywołania są formalizowane jako operacje interaktywne (np. wywoływanie funkcji, użycie narzędzi lub akcje agenta). To właśnie to przekształca zwykły model w **prawdziwego agenta AI**, zdolnego do zrobienia czegoś więcej niż tylko „rozmowy”.

### A teraz – do dzieła!

Teraz, gdy omówiliśmy podstawowe pojęcia, logiczne jest zadać sobie pytanie: „Jak to wszystko zaimplementować w praktyce w Pythonie?”

Tutaj wkracza **LangGraph** – potężny framework do budowania grafów stanów, zachowań agentów i łańcuchów myślowych. Pozwala on „zszyć” logikę interakcji między agentami, narzędziami i użytkownikiem, tworząc żywą architekturę AI, która dostosowuje się do zadań.

W kolejnych sekcjach przyjrzymy się, jak:

*   buduje się agenta od podstaw;
*   tworzy się stany, przejścia i zdarzenia;
*   integruje się funkcje i narzędzia;
*   i jak cały ten ekosystem działa w prawdziwym projekcie.

### Trochę teorii: co to jest LangGraph

Zanim przejdziemy do praktyki, trzeba powiedzieć kilka słów o samym frameworku.

**LangGraph** to projekt zespołu **LangChain**, tych samych, którzy jako pierwsi zaproponowali koncepcję „łańcuchów” (chains) interakcji z LLM. Jeśli wcześniej główny nacisk kładziono na liniowe lub warunkowo rozgałęzione potoki (langchain.chains), to teraz deweloperzy stawiają na **model grafowy**, i to właśnie LangGraph polecają jako nowe „jądro” do budowania złożonych systemów AI.

**LangGraph** to framework do budowania skończonych automatów stanów i grafów stanów, w których każdy **węzeł** reprezentuje część logiki agenta: wywołanie modelu, narzędzie zewnętrzne, warunek, dane wejściowe użytkownika itp.

### Jak to działa: grafy i węzły

Konceptualnie LangGraph opiera się na następujących ideach:

*   **Graf** – to struktura, która opisuje możliwe ścieżki wykonania logiki. Można o nim myśleć jak o mapie: z jednego punktu można przejść do drugiego w zależności od warunków lub wyniku wykonania.
*   **Węzły** – to konkretne kroki w grafie. Każdy węzeł wykonuje jakąś funkcję: wywołuje model, wywołuje zewnętrzne API, sprawdza warunek lub po prostu aktualizuje stan wewnętrzny.
*   **Przejścia między węzłami** – to logika routingu: jeśli wynik poprzedniego kroku jest taki, to idziemy tam.
*   **Stan** – jest przekazywany między węzłami i gromadzi wszystko, co potrzebne: historię, pośrednie wnioski, dane wejściowe użytkownika, wyniki działania narzędzi itp.

W ten sposób uzyskujemy **elastyczny mechanizm sterowania logiką agenta**, w którym można opisywać zarówno proste, jak i bardzo złożone scenariusze: pętle, warunki, działania równoległe, zagnieżdżone wywołania i wiele innych.

### Dlaczego to jest wygodne?

LangGraph pozwala budować **przejrzystą, odtwarzalną i rozszerzalną logikę**:

*   łatwe do debugowania;
*   łatwe do wizualizacji;
*   łatwe do skalowania do nowych zadań;
*   łatwe do integracji narzędzi zewnętrznych i protokołów MCP.

Zasadniczo LangGraph to **„mózg” agenta**, gdzie każdy krok jest udokumentowany, kontrolowany i może być zmieniony bez chaosu i „magii”.

### No dobrze, wystarczy teorii!

Można jeszcze długo opowiadać o grafach, stanach, kompozycji logiki i zaletach LangGraph nad klasycznymi potokami. Ale, jak pokazuje praktyka, lepiej raz zobaczyć w kodzie.

**Czas przejść do praktyki.** Dalej – przykład w Pythonie: stworzymy prostego, ale użytecznego agenta AI opartego na LangGraph, który będzie używał narzędzi zewnętrznych, pamięci i sam podejmował decyzje.

### Przygotowanie: sieci neuronowe w chmurze i lokalne

Aby rozpocząć tworzenie agentów AI, potrzebujemy przede wszystkim **mózgu** – modelu językowego. Tutaj są dwa podejścia:

*   **używać rozwiązań chmurowych**, gdzie wszystko jest gotowe „od razu”;
*   lub **podnieść model lokalnie** – dla pełnej autonomii i poufności.

Rozważmy obie opcje.

#### Usługi chmurowe: szybko i wygodnie

Najprostszym sposobem jest wykorzystanie mocy dużych dostawców: OpenAI, Anthropic i użycie...

### Gdzie zdobyć klucze i tokeny:

*   **OpenAI** – ChatGPT i inne produkty;
*   **Anthropic** – Claude;
*   **OpenRouter.ai** – dziesiątki modeli (jeden token – wiele modeli przez API kompatybilne z OpenAI);
*   **Amvera Cloud** – możliwość podłączenia LLAMA z płatnością w rublach i wbudowanym proxy do OpenAI i Anthropic.

Ta ścieżka jest wygodna, zwłaszcza jeśli:

*   nie chcesz konfigurować infrastruktury;
*   rozwijasz z naciskiem na szybkość;
*   pracujesz z ograniczonymi zasobami.

### Modele lokalne: pełna kontrola

Jeśli ważna jest dla Ciebie **prywatność, praca offline** lub chcesz budować **w pełni autonomiczne agenty**, to warto wdrożyć sieć neuronową lokalnie.

**Główne zalety:**

*   **Poufność** – dane pozostają u Ciebie;
*   **Praca offline** – przydatne w izolowanych sieciach;
*   **Brak subskrypcji i tokenów** – bezpłatnie po konfiguracji.

**Wady są oczywiste:**

*   Wymagania dotyczące zasobów (zwłaszcza pamięci wideo);
*   Konfiguracja może zająć trochę czasu;
*   Niektóre modele są trudne do wdrożenia bez doświadczenia.

Niemniej jednak istnieją narzędzia, które ułatwiają lokalne uruchamianie. Jednym z najlepszych obecnie jest **Ollama**.

### Wdrażanie lokalnego LLM przez Ollama + Docker

Przygotujemy lokalne uruchomienie modelu Qwen 2.5 (qwen2.5:32b) za pomocą kontenera Docker i systemu Ollama. Pozwoli to na integrację sieci neuronowej z MCP i wykorzystanie jej we własnych agentach opartych na LangGraph.

Jeśli zasoby obliczeniowe Twojego komputera lub serwera okażą się niewystarczające do pracy z tą wersją modelu, zawsze możesz wybrać mniej „zasobożerną” sieć neuronową – proces instalacji i uruchamiania pozostanie podobny.

**Szybka instalacja (podsumowanie kroków)**

1.  **Zainstaluj Docker + Docker Compose**
2.  **Utwórz strukturę projektu:**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **Utwórz `docker-compose.yml`**
(opcja uniwersalna, GPU jest wykrywane automatycznie)

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

4.  **Uruchom kontener:**
```bash
docker compose up -d
```

5.  **Pobierz model:**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **Sprawdź działanie przez API:**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "Witaj!", "stream": false}'
```
*(Obraz z wynikiem wykonania polecenia curl)*

7.  **Integracja z Pythonem:**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:32b",
        "prompt": prompt,
        "stream": False
    })
    return res.json()['response']

print(query("Wyjaśnij splątanie kwantowe"))
```
Teraz masz pełnoprawnego lokalnego LLM, gotowego do pracy z MCP i LangGraph.

**Co dalej?**

Możemy wybierać między modelami chmurowymi a lokalnymi, a także nauczyliśmy się, jak podłączyć oba. Najciekawsze przed nami – **tworzenie agentów AI na LangGraph**, którzy wykorzystują wybrany model, pamięć, narzędzia i własną logikę.

**Przejdźmy do najsmaczniejszej części – kodu i praktyki!**

---

Zanim przejdziemy do praktyki, ważne jest, aby przygotować środowisko pracy. Zakładam, że znasz już podstawy Pythona, wiesz, czym są biblioteki i zależności, oraz rozumiesz, dlaczego warto używać środowiska wirtualnego.

Jeśli to wszystko jest dla Ciebie nowością – polecam najpierw przejść krótki kurs lub przewodnik po podstawach Pythona, a następnie wrócić do artykułu.

#### Krok 1: Tworzenie środowiska wirtualnego

Utwórz nowe środowisko wirtualne w folderze projektu:
```bash
python -m venv venv
source venv/bin/activate  # dla Linuxa/macOS
venv\Scripts\activate   # dla Windows
```

#### Krok 2: Instalacja zależności

Utwórz plik `requirements.txt` i dodaj do niego następujące wiersze:
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

> ⚠️ **Aktualne wersje są podane na dzień 21 lipca 2025 r.** Mogły się zmienić od czasu publikacji – **sprawdź aktualność przed instalacją.**

Następnie zainstaluj zależności:
```bash
pip install -r requirements.txt```

#### Krok 3: Konfiguracja zmiennych środowiskowych

Utwórz w katalogu głównym projektu plik `.env` i dodaj do niego potrzebne klucze API:
```
OPENAI_API_KEY=sk-proj-1234
DEEPSEEK_API_KEY=sk-123
OPENROUTER_API_KEY=sk-or-v1-123
BRAVE_API_KEY=BSAj123K1bvBGpH1344tLwc
```

**Przeznaczenie zmiennych:**

*   **OPENAI_API_KEY** – klucz do dostępu do modeli GPT od OpenAI;
*   **DEEPSEEK_API_KEY** – klucz do używania modeli Deepseek;
*   **OPENROUTER_API_KEY** – pojedynczy klucz do dostępu do wielu modeli przez OpenRouter

---
Niektóre narzędzia MCP (np. `brave-web-search`) wymagają klucza do działania. Bez niego po prostu się nie aktywują.

**A jeśli nie masz kluczy API?**

Nie ma problemu. Możesz rozpocząć rozwój z modelem lokalnym (np. przez Ollama), bez podłączania żadnych zewnętrznych usług. W takim przypadku plik `.env` można w ogóle nie tworzyć.

Gotowe! Teraz mamy wszystko, czego potrzebujemy, aby zacząć – izolowane środowisko, zależności i, w razie potrzeby, dostęp do chmurowych sieci neuronowych i integracji MCP.

Następnie – uruchomimy naszego agenta LLM na różne sposoby.

### Proste uruchamianie agentów LLM przez LangGraph: podstawowa integracja

Zacznijmy od najprostszego: jak „podłączyć mózg” do przyszłego agenta. Przeanalizujemy podstawowe sposoby uruchamiania modeli językowych (LLM) za pomocą LangChain, aby w następnym kroku przejść do integracji z LangGraph i budowania pełnoprawnego agenta AI.

#### Importy
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` i `load_dotenv()` – do ładowania zmiennych z pliku `.env`.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` – opakowania do łączenia modeli językowych przez LangChain.

> 💡 Jeśli używasz alternatywnych podejść do pracy z konfiguracjami (np. Pydantic Settings), możesz zastąpić `load_dotenv()` swoją zwykłą metodą.

#### Ładowanie zmiennych środowiskowych
```python
load_dotenv()
```
Spowoduje to załadowanie wszystkich zmiennych z `.env`, w tym kluczy dostępu do OpenAI, DeepSeek, OpenRouter i innych API.

#### Proste funkcje do pobierania LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
Jeśli zmienna `OPENAI_API_KEY` jest poprawnie ustawiona, LangChain automatycznie ją podstawi – jawne określenie `api_key=...` jest tutaj opcjonalne.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
Podobnie, ale używając opakowania `ChatDeepSeek`.

**OpenRouter (i inne kompatybilne API)**
```python
def get_openrouter_llm(model="moonshotai/kimi-k2:free"):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
```
**Cechy:**

*   `ChatOpenAI` jest używany, mimo że model nie pochodzi z OpenAI – ponieważ OpenRouter używa tego samego protokołu.
*   `base_url` jest obowiązkowy: wskazuje na API OpenRouter.
*   Model `moonshotai/kimi-k2:free` został wybrany jako jedna z najbardziej zrównoważonych opcji pod względem jakości i szybkości w momencie pisania.
*   Klucz API `OpenRouter` musi być przekazany jawnie – automatyczne podstawienie tutaj nie działa.

#### Mini-test: sprawdzanie działania modelu
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("Kim jesteś?")
    print(response.content)
```
*(Obraz z wynikiem wykonania: `Jestem asystentem AI stworzonym przez firmę Moonshot AI...`)*

Jeśli wszystko jest poprawnie skonfigurowane, otrzymasz sensowną odpowiedź od modelu. Gratulacje – pierwszy krok został wykonany!

### Ale to jeszcze nie agent

Na obecnym etapie podłączyliśmy LLM i wykonaliśmy proste wywołanie. To bardziej przypomina chatbota konsolowego niż agenta AI.

**Dlaczego?**

*   Pisujemy **synchroniczny, liniowy kod** bez logiki stanu ani celów.
*   Agent nie podejmuje decyzji, nie pamięta kontekstu i nie używa narzędzi.
*   MCP i LangGraph nie są jeszcze zaangażowane.

**Co dalej?**

Następnie zaimplementujemy **pełnoprawnego agenta AI** za pomocą **LangGraph** – najpierw bez MCP, aby skupić się na architekturze, stanach i logice samego agenta.

Zanurzmy się w prawdziwą mechanikę agentów. Zaczynamy!

### Agent klasyfikacji ofert pracy: od teorii do praktyki

...koncepcje LangGraph w praktyce i stworzyć użyteczne narzędzie dla platform HR i giełd freelancerów.

#### Zadanie agenta

Nasz agent przyjmuje jako dane wejściowe tekstowy opis oferty pracy lub usługi i wykonuje trójpoziomową klasyfikację:

1.  **Typ pracy**: praca projektowa lub stała oferta pracy
2.  **Kategoria zawodu**: z ponad 45 predefiniowanych specjalności
3.  **Typ wyszukiwania**: czy osoba szuka pracy, czy szuka wykonawcy

Wynik jest zwracany w ustrukturyzowanym formacie JSON z oceną pewności dla każdej klasyfikacji.

#### 📈 Architektura agenta na LangGraph

Zgodnie z zasadami LangGraph tworzymy **graf stanów** z czterech węzłów:

- Opis wejściowy
- ↓
- Węzeł klasyfikacji typu pracy
- ↓
- Węzeł klasyfikacji kategorii
- ↓
- Węzeł określania typu wyszukiwania
- ↓
- Węzeł obliczania pewności
- ↓
- Wynik JSON

Każdy węzeł to **wyspecjalizowana funkcja**, która:

*   Odbiera bieżący stan agenta
*   Wykonuje swoją część analizy
*   Aktualizuje stan i przekazuje go dalej

#### Zarządzanie stanem

Definiujemy **strukturę pamięci agenta** za pomocą `TypedDict`:

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """Stan agenta do przechowywania informacji o procesie klasyfikacji"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

To jest **pamięć robocza agenta** – wszystko, co pamięta i gromadzi podczas analizy. Podobnie jak ekspert ludzki, który podczas analizy dokumentu ma na uwadze kontekst zadania.

Przyjrzyjmy się pełnemu kodowi, a następnie skupmy się na głównych punktach.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Kategorie zawodów
CATEGORIES = [
    "Animator 2D", "Animator 3D", "Modelarz 3D",
    "Analityk biznesowy", "Deweloper Blockchain", ...
]

class JobType(Enum):
    PROJECT = "praca projektowa"
    PERMANENT = "praca stała"

class SearchType(Enum):
    LOOKING_FOR_WORK = "szukanie pracy"
    LOOKING_FOR_PERFORMER = "szukanie wykonawcy"

class State(TypedDict):
    """Stan agenta do przechowywania informacji o procesie klasyfikacji"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool

class VacancyClassificationAgent:
    """Asynchroniczny agent do klasyfikacji ofert pracy i usług"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Inicjalizacja agenta"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Tworzy przepływ pracy agenta oparty na LangGraph"""
        workflow = StateGraph(State)
        
        # Dodaj węzły do grafu
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Zdefiniuj sekwencję wykonywania węzłów
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Węzeł do określania typu pracy: projektowa lub stała"""
        # ... (implementacja poniżej)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Węzeł do określania kategorii zawodu"""
        # ... (implementacja poniżej)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Węzeł do określania typu wyszukiwania"""
        # ... (implementacja poniżej)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Węzeł do obliczania poziomu pewności w klasyfikacji"""
        # ... (implementacja poniżej)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Znajduje najbliższą kategorię z listy dostępnych"""
        # ... (implementacja poniżej)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Główna metoda do klasyfikacji ofert pracy/usług"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Uruchom przepływ pracy
        result = await self.workflow.ainvoke(initial_state)
        
        # Sformułuj końcową odpowiedź JSON
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Demonstracja działania agenta"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Wymagany programista Python do tworzenia aplikacji webowej w Django. Praca stała.",
        "Szukam zleceń na tworzenie logo i identyfikacji wizualnej. Pracuję w Adobe Illustrator.",
        "Potrzebny animator 3D do krótkoterminowego projektu tworzenia reklamy.",
        "CV: doświadczony marketer, szukam pracy zdalnej w dziedzinie marketingu cyfrowego",
        "Szukamy programisty frontend React do naszego zespołu na stałe"
    ]
    
    print("🤖 Demonstracja działania agenta klasyfikacji ofert pracy\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Test {i}: ---")
        print(f"Opis: {description}")
        try:
            result = await agent.classify(description)
            print("Wynik klasyfikacji:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Błąd: {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...reszta kodu z implementacją metod została przedstawiona w artykule...)*

### Kluczowe zalety architektury
1.  **Modułowość** – każdy węzeł rozwiązuje jedno zadanie, łatwe do testowania i ulepszania oddzielnie
2.  **Rozszerzalność** – nowe funkcje są dodawane deklaratywnie
3.  **Przejrzystość** – cały proces podejmowania decyzji jest udokumentowany i możliwy do śledzenia
4.  **Wydajność** – asynchroniczne przetwarzanie wielu żądań
5.  **Niezawodność** – wbudowana obsługa błędów i odzyskiwanie

### Rzeczywiste korzyści
Taki agent może być używany w:
*   **Platformach HR** do automatycznej kategoryzacji CV i ofert pracy
*   **Giełdach freelancerów** do poprawy wyszukiwania i rekomendacji
*   **Systemach wewnętrznych** firm do przetwarzania wniosków i projektów
*   **Rozwiązaniach analitycznych** do badania rynku pracy

### MCP w akcji: tworzenie agenta z systemem plików i wyszukiwaniem w sieci
Po tym, jak omówiliśmy podstawowe zasady LangGraph i stworzyliśmy prostego agenta klasyfikującego, rozszerzmy jego możliwości, łącząc go ze światem zewnętrznym za pośrednictwem MCP.

Teraz stworzymy pełnoprawnego asystenta AI, który będzie mógł:
*   Pracować z systemem plików (czytać, tworzyć, modyfikować pliki)
*   Wyszukiwać aktualne informacje w Internecie
*   Zapamiętywać kontekst dialogu
*   Obsługiwać błędy i odzyskiwać po awariach

#### Od teorii do prawdziwych narzędzi
Pamiętasz, jak na początku artykułu mówiliśmy o tym, że **MCP jest mostem między siecią neuronową a jej otoczeniem**? Teraz zobaczysz to w praktyce. Nasz agent uzyska dostęp do **prawdziwych narzędzi**:
```
# Narzędzia systemu plików
- read_file – czytanie plików
- write_file – zapisywanie i tworzenie plików
- list_directory – przeglądanie zawartości folderów
- create_directory – tworzenie folderów

# Narzędzia wyszukiwania w sieci
- brave_web_search – wyszukiwanie w Internecie
- get_web_content – pobieranie zawartości stron
```
To już nie jest agent „zabawka” – to **narzędzie pracy**, które może rozwiązywać prawdziwe problemy.

#### 📈 Architektura: od prostego do złożonego

**1. Konfiguracja jako podstawa stabilności**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Uproszczona konfiguracja agenta AI"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Walidacja konfiguracji"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"Ścieżka nie istnieje: {self.filesystem_path}")
```
**Dlaczego to jest ważne?** W przeciwieństwie do przykładu klasyfikacji, tutaj agent wchodzi w interakcje z systemami zewnętrznymi. Jeden błąd w ścieżce pliku lub brakujący klucz API – i cały agent przestaje działać. **Walidacja na starcie** oszczędza godziny debugowania.

**2. Fabryka modeli: elastyczność wyboru**
```python
def create_model(config: AgentConfig):
    """Tworzy model zgodnie z konfiguracją"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... inni dostawcy
```
Jeden kod – wiele modeli. Chcesz darmowy model lokalny? Użyj Ollamy. Potrzebujesz maksymalnej dokładności? Przełącz się na GPT-4. Ważna jest szybkość? Wypróbuj DeepSeek. Kod pozostaje ten sam.

**3. Integracja MCP: połączenie z prawdziwym światem**
```python
async def _init_mcp_client(self):
    """Inicjalizacja klienta MCP"""
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
Tutaj odbywa się kluczowa praca MCP: podłączamy zewnętrzne serwery MCP do agenta, które zapewniają zestaw narzędzi i funkcji. Agent z kolei otrzymuje nie tylko pojedyncze funkcje, ale pełne kontekstowe zrozumienie, jak pracować z systemem plików i Internetem.

#### Odporność na błędy
W prawdziwym świecie wszystko się psuje: sieć jest niedostępna, pliki są zablokowane, klucze API wygasły. Nasz agent jest na to gotowy:
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
Dekorator `@retry_on_failure` automatycznie ponawia operacje w przypadku tymczasowych awarii. Użytkownik nawet nie zauważy, że coś poszło nie tak.

### Podsumowanie: od teorii do praktyki agentów AI

Dziś przeszliśmy drogę od podstawowych koncepcji do tworzenia działających agentów AI. Podsumujmy, czego się nauczyliśmy i co osiągnęliśmy.

**Co opanowaliśmy**

**1. Podstawowe koncepcje**
*   Zrozumieliśmy różnicę między chatbotami a prawdziwymi agentami AI
*   Zrozumieliśmy rolę **MCP (Model Context Protocol)** jako mostu między modelem a światem zewnętrznym
*   Poznaliśmy architekturę **LangGraph** do budowania złożonej logiki agentów

**2. Umiejętności praktyczne**
*   Skonfigurowaliśmy środowisko pracy z obsługą modeli chmurowych i lokalnych
*   Stworzyliśmy **agenta klasyfikującego** z asynchroniczną architekturą i zarządzaniem stanem
*   Zbudowaliśmy **agenta MCP** z dostępem do systemu plików i wyszukiwania w sieci

**3. Wzorce architektoniczne**
*   Opanowaliśmy modułową konfigurację i fabryki modeli
*   Wdrożyliśmy obsługę błędów i **mechanizmy ponawiania prób** dla rozwiązań gotowych do produkcji

### Kluczowe zalety podejścia
**LangGraph + MCP** dają nam:
*   **Przejrzystość** – każdy krok agenta jest udokumentowany i możliwy do śledzenia
*   **Rozszerzalność** – nowe funkcje są dodawane deklaratywnie
*   **Niezawodność** – wbudowana obsługa błędów i odzyskiwanie
*   **Elastyczność** – obsługa wielu modeli i dostawców od razu

### Wniosek

Agenty AI to nie futurystyczna fantazja, ale **prawdziwa technologia dzisiejszych czasów**. Dzięki LangGraph i MCP możemy tworzyć systemy, które rozwiązują konkretne problemy biznesowe, automatyzują rutynę i otwierają nowe możliwości.

**Najważniejsze – zacząć.** Weź kod z przykładów, dostosuj go do swoich zadań, eksperymentuj. Każdy projekt to nowe doświadczenie i krok w kierunku mistrzostwa w dziedzinie rozwoju AI.

Powodzenia w Twoich projektach!

---
*Tagi: python, ai, mcp, langchain, ai-assistant, ollama, ai-agents, local llm, langgraph, mcp-server*
*Huby: Blog firmy Amvera, Przetwarzanie języka naturalnego, Sztuczna inteligencja, Python, Programowanie*
