## Jak stworzyć agenta AI do pracy z przeglądarką internetową za pomocą LangChain i Browser-Use: przewodnik krok po kroku

Ten przewodnik krok po kroku pokaże Ci, jak stworzyć agenta AI zdolnego do wyszukiwania informacji w Google i analizowania stron internetowych za pomocą LangChain i Browser-Use.

**Krok 1: Zainstaluj niezbędne biblioteki**

Najpierw musisz zainstalować wymagane biblioteki Python. Otwórz terminal lub wiersz poleceń i wykonaj następujące polecenie:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Krok 2: Skonfiguruj klucze API**

Klucze API są wymagane do pracy z OpenAI i SerpAPI.

*   **Klucz API OpenAI:** Uzyskaj swój klucz API ze strony OpenAI (openai.com).
*   **Klucz API SerpAPI:** SerpAPI udostępnia API do pracy z wynikami wyszukiwania. Zarejestruj się na stronie serpapi.com (dostępna jest bezpłatna wersja próbna), zaloguj się na swoje konto i znajdź swój klucz API na stronie Dashboard.

Utwórz plik `.env` w tym samym katalogu, w którym będzie znajdował się Twój skrypt Python, i dodaj do niego klucze w następującym formacie:

```
OPENAI_API_KEY=twój_klucz_openai
SERPAPI_API_KEY=twój_klucz_serpapi
```

**Krok 3: Utwórz skrypt Python (browser_agent.py)**

Utwórz plik o nazwie `browser_agent.py` i wklej do niego następujący kod:

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

    # Definiowanie narzędzia wyszukiwania (prosty przykład, bez faktycznego wyszukiwania w Google)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Wyszukiwanie w Google: {query}",  # Zastąp rzeczywistym wyszukiwaniem SerpAPI, jeśli to konieczne
        description="Wyszukuje informacje w Google."
    )


    # Definiowanie zadania agenta
    task = """
    Znajdź najnowsze wiadomości o firmie OpenAI w Google.
    Następnie odwiedź jedną ze znalezionych stron internetowych i znajdź nazwiska założycieli.
    """

    # Tworzenie agenta
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Uruchamianie agenta
    try:
        result = await agent.arun(task)
        print(f"Wynik: {result}")
    except Exception as e:
        logging.error(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Krok 4: Uruchom agenta**

Otwórz terminal lub wiersz poleceń, przejdź do katalogu zawierającego `browser_agent.py` i uruchom go:

```bash
python browser_agent.py
```

**Krok 5: Ulepsz agenta (zaawansowane funkcje)**

*   **Rzeczywiste wyszukiwanie w Google:** Zastąp funkcję `lambda` w `search_tool` kodem, który używa SerpAPI do rzeczywistych wyszukiwań w Google. Będzie to wymagało przestudiowania dokumentacji SerpAPI.

*   **Interakcja ze stronami internetowymi (Browser-Use):** Aby dodać funkcjonalność interakcji ze stronami internetowymi (otwieranie linków, wyodrębnianie tekstu itp.), będziesz musiał użyć biblioteki `browser-use`. Dokumentacja tej biblioteki pomoże Ci dodać odpowiednie narzędzia do Twojego agenta.

*   **Użycie pamięci:** Aby zachować kontekst między żądaniami, możesz użyć mechanizmów pamięci LangChain.

*   **Bardziej złożone łańcuchy akcji:** LangChain pozwala tworzyć bardziej złożone łańcuchy akcji (Chains) do rozwiązywania bardziej skomplikowanych zadań.


Ten przykład demonstruje podstawową strukturę. Aby zaimplementować pełnoprawnego agenta, który wchodzi w interakcje z przeglądarką i wyszukiwarką Google, wymagana będzie dodatkowa praca z SerpAPI i `browser-use`. Nie zapomnij zapoznać się z dokumentacją tych bibliotek, aby uzyskać bardziej szczegółowe informacje.
