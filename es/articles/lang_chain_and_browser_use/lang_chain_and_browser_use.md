## Cómo crear un agente de IA para interactuar con el navegador web usando LangChain y Browser-Use: una guía paso a paso

Esta guía paso a paso te mostrará cómo crear un agente de IA capaz de buscar información en Google y analizar páginas web usando LangChain y Browser-Use.

**Paso 1: Instalar las bibliotecas necesarias**

Primero, debes instalar las bibliotecas de Python requeridas. Abre tu terminal o símbolo del sistema y ejecuta el siguiente comando:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Paso 2: Configurar las claves API**

Se requieren claves API para trabajar con OpenAI y SerpAPI.

*   **Clave API de OpenAI:** Obtén tu clave API en el sitio web de OpenAI (openai.com).
*   **Clave API de SerpAPI:** SerpAPI proporciona una API para trabajar con resultados de búsqueda. Regístrate en serpapi.com (hay una prueba gratuita disponible), inicia sesión en tu cuenta y encuentra tu clave API en la página de Dashboard.

Crea un archivo `.env` en el mismo directorio que tu script de Python y agrega las claves en el siguiente formato:

```
OPENAI_API_KEY=tu_clave_openai
SERPAPI_API_KEY=tu_clave_serpapi
```

**Paso 3: Crear el script de Python (browser_agent.py)**

Crea un archivo llamado `browser_agent.py` y pega el siguiente código en él:

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

# Cargar claves API del archivo .env
os.environ["SERPAPI_API_KEY"] = os.getenv("SERPAPI_API_KEY")
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

async def main():
    # Inicializar el modelo de lenguaje
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0) # Puedes probar otros modelos

    # Definir la herramienta de búsqueda (ejemplo simple, sin búsqueda real en Google)
    search_tool = Tool(
        name="Google Search",
        func=lambda query: f"Buscando en Google: {query}",  # Reemplazar con búsqueda real de SerpAPI si es necesario
        description="Busca información en Google."
    )


    # Definir la tarea del agente
    task = """
    Encuentra las últimas noticias sobre la empresa OpenAI en Google.
    Luego visita uno de los sitios web encontrados y busca los nombres de los fundadores.
    """

    # Crear el agente
    agent = initialize_agent(
        tools=[search_tool],
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True,
    )

    # Ejecutar el agente
    try:
        result = await agent.arun(task)
        print(f"Resultado: {result}")
    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")

if __name__ == "__main__":
    asyncio.run(main())
```

**Paso 4: Ejecutar el agente**

Abre tu terminal o símbolo del sistema, navega hasta el directorio que contiene `browser_agent.py` y ejecútalo:

```bash
python browser_agent.py
```

**Paso 5: Mejorar el agente (funciones avanzadas)**

*   **Búsqueda real en Google:** Reemplaza la función `lambda` en `search_tool` con código que use SerpAPI para búsquedas reales en Google. Esto requerirá estudiar la documentación de SerpAPI.

*   **Interacción con páginas web (Browser-Use):** Para agregar funcionalidad para interactuar con páginas web (abrir enlaces, extraer texto, etc.), deberás usar la biblioteca `browser-use`. La documentación de esta biblioteca te ayudará a agregar las herramientas adecuadas a tu agente.

*   **Uso de memoria:** Para mantener el contexto entre solicitudes, puedes usar los mecanismos de memoria de LangChain.

*   **Cadenas de acciones más complejas:** LangChain te permite crear cadenas de acciones más complejas (Chains) para resolver tareas más intrincadas.


Este ejemplo demuestra la estructura básica. Para implementar un agente completo que interactúe con un navegador y la Búsqueda de Google, se requerirá trabajo adicional con SerpAPI y `browser-use`. No olvides consultar la documentación de estas bibliotecas para obtener información más detallada.
