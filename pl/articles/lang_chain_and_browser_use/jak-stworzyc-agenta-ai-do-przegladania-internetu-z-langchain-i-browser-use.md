## Jak stworzyć agenta AI do przeglądania internetu za pomocą LangChain i Browser-Use: przewodnik krok po kroku

Ten przewodnik krok po kroku pokaże Ci, jak stworzyć agenta AI zdolnego do wyszukiwania informacji w Google i analizowania stron internetowych za pomocą LangChain i Browser-Use.

**Krok 1: Instalacja niezbędnych bibliotek**

Najpierw musisz zainstalować niezbędne biblioteki Pythona. Otwórz terminal lub wiersz poleceń i wykonaj następujące polecenie:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Krok 2: Konfiguracja kluczy API**

Do pracy z OpenAI i SerpAPI potrzebne są klucze API.

*   **Klucz API OpenAI:** Uzyskaj swój klucz API na stronie OpenAI (openai.com).
*   **Klucz API SerpAPI:** SerpAPI udostępnia API do pracy z wynikami wyszukiwania. Zarejestruj się na stronie serpapi.com (dostępna jest bezpłatna wersja próbna), zaloguj się na swoje konto i znajdź swój klucz API na stronie Dashboard.

Utwórz plik `.env` w tym samym katalogu, w którym będzie znajdował się Twój skrypt Pythona, i dodaj tam klucze w następującym formacie:

```
OPENAI_API_KEY=twój_klucz_openai
SERPAPI_API_KEY=twój_klucz_serpapi
```

**Krok 3: Tworzenie skryptu Pythona (browser_agent.py)**

Utwórz plik `browser_agent.py` i wklej do niego następujący kod:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Konfiguracja logowania
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Ładowanie kluczy API z pliku .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Inicjalizacja modelu językowego
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Możesz wypróbować inne modele

    # Definicja narzędzia wyszukiwania (prosty przykład, bez faktycznego wyszukiwania w Google)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Wyszukiwanie w Google: {query}",  # Zastąp rzeczywistym wyszukiwaniem z SerpAPI, jeśli to konieczne
        description="Wyszukuje informacje w Google."
    )


    # Definicja zadania dla agenta
    task = """
    Znajdź w Google najnowsze wiadomości o firmie OpenAI.
    Następnie odwiedź jedną ze znalezionych stron internetowych i znajdź nazwiska założycieli.
    """

    # Tworzenie agenta
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Uruchomienie agenta
    try:
        result = await agent.arun(task)
        print(f"Wynik: {result}")
    except Exception as e:
        logging.error(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Krok 4: Uruchomienie agenta**

Otwórz terminal lub wiersz poleceń, przejdź do katalogu z plikiem `browser_agent.py` i uruchom go:

```bash
python browser_agent.py
```

**Krok 5: Ulepszanie agenta (zaawansowane funkcje)**

*   **Rzeczywiste wyszukiwanie w Google:** Zastąp funkcję `lambda` w `search_tool` kodem, który używa SerpAPI do rzeczywistego wyszukiwania w Google. Będzie to wymagało przestudiowania dokumentacji SerpAPI.

*   **Interakcja ze stronami internetowymi (Browser-Use):** Aby dodać funkcjonalność interakcji ze stronami internetowymi (otwieranie linków, wyodrębnianie tekstu itp.), będziesz musiał użyć biblioteki `browser-use`. Dokumentacja tej biblioteki pomoże Ci dodać odpowiednie narzędzia do Twojego agenta.

*   **Używanie pamięci:** Aby zachować kontekst między zapytaniami, możesz użyć mechanizmów pamięci LangChain.

*   **Bardziej złożone łańcuchy działań:** LangChain pozwala tworzyć bardziej złożone łańcuchy działań (Chains) do rozwiązywania bardziej złożonych problemów.


Ten przykład demonstruje podstawową strukturę. Aby zaimplementować pełnoprawnego agenta, który wchodzi w interakcje z przeglądarką i wyszukiwarką Google, wymagana będzie dodatkowa praca z SerpAPI i `browser-use`. Nie zapomnij zapoznać się z dokumentacją tych bibliotek, aby uzyskać bardziej szczegółowe informacje.
