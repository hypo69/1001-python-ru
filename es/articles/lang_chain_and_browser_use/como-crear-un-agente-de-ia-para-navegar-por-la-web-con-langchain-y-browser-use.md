## Cómo crear un agente de IA para navegar por la web con LangChain y Browser-Use: guía paso a paso

Esta guía paso a paso te mostrará cómo crear un agente de IA capaz de buscar información en Google y analizar páginas web utilizando LangChain y Browser-Use.

**Paso 1: Instalar las bibliotecas necesarias**

Primero, debes instalar las bibliotecas de Python necesarias. Abre una terminal o línea de comandos y ejecuta el siguiente comando:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Paso 2: Configurar las claves API**

Se requieren claves API para trabajar con OpenAI y SerpAPI.

*   **Clave API de OpenAI:** Obtén tu clave API en el sitio web de OpenAI (openai.com).
*   **Clave API de SerpAPI:** SerpAPI proporciona una API para trabajar con los resultados de búsqueda. Regístrate en serpapi.com (hay una prueba gratuita disponible), inicia sesión en tu cuenta y encuentra tu clave API en la página de Dashboard.

Crea un archivo `.env` en el mismo directorio donde se ubicará tu script de Python, y añade las claves en el siguiente formato:

```
OPENAI_API_KEY=tu_clave_openai
SERPAPI_API_KEY=tu_clave_serpapi
```

**Paso 3: Crear un script de Python (browser_agent.py)**

Crea un archivo `browser_agent.py` y pega el siguiente código en él:

```python
import asyncio
import logging
import os
from dotenv import load_dotenv

from langchain.agents import AgentType, initialize_agent
from langchain.tools import Tool
from langchain_openai import ChatOpenAI


# Configurar el registro
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

load_dotenv()

# Cargar las claves API del archivo .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Inicializar el modelo de lenguaje
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Puedes probar otros modelos

    # Definir la herramienta de búsqueda (ejemplo simple, sin búsqueda real en Google)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Buscando en Google: {query}",  # Reemplazar con búsqueda real con SerpAPI si es necesario
        description="Busca información en Google."
    )


    # Definir la tarea para el agente
    task = """
    Encuentra en Google las últimas noticias sobre la empresa OpenAI.
    Luego visita uno de los sitios web encontrados y busca los nombres de los fundadores.
    """

    # Crear agente
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Ejecutar agente
    try:
        result = await agent.arun(task)
        print(f"Resultado: {result}")
    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Paso 4: Ejecutar el agente**

Abre una terminal o línea de comandos, navega al directorio con el archivo `browser_agent.py` y ejecútalo:

```bash
python browser_agent.py
```

**Paso 5: Mejorar el agente (funciones avanzadas)**

*   **Búsqueda real en Google:** Reemplaza la función `lambda` en `search_tool` con código que use SerpAPI para una búsqueda real en Google. Esto requerirá estudiar la documentación de SerpAPI.

*   **Interacción con páginas web (Browser-Use):** Para añadir funcionalidad de interacción con páginas web (abrir enlaces, extraer texto, etc.), necesitarás usar la biblioteca `browser-use`. La documentación de esta biblioteca te ayudará a añadir las herramientas adecuadas a tu agente.

*   **Uso de memoria:** Para preservar el contexto entre solicitudes, puedes usar los mecanismos de memoria de LangChain.

*   **Cadenas de acciones más complejas:** LangChain permite crear cadenas de acciones (Chains) más complejas para resolver problemas más complejos.


Este ejemplo demuestra la estructura básica. Para implementar un agente completo que interactúe con el navegador y la Búsqueda de Google, se requerirá trabajo adicional con SerpAPI y `browser-use`. No olvides consultar la documentación de estas bibliotecas para obtener información más detallada.
