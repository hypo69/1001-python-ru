## Cómo crear un agente de IA para navegación web con LangChain y Browser-Use: una guía paso a paso

Esta guía paso a paso le mostrará cómo crear un agente de IA capaz de buscar información en Google y analizar páginas web utilizando LangChain y Browser-Use.

**Paso 1: Instalar las bibliotecas necesarias**

Primero, debe instalar las bibliotecas de Python necesarias. Abra una terminal o símbolo del sistema y ejecute el siguiente comando:

```bash
pip install -U langchain langchain-openai langchain-community browser-use python-dotenv serpapi google-search-results numexpr
```

**Paso 2: Configurar las claves API**

Se requieren claves API para trabajar con OpenAI y SerpAPI.

* **Clave API de OpenAI:** Obtenga su clave API del sitio web de OpenAI (openai.com).
* **Clave API de SerpAPI:** SerpAPI proporciona una API para trabajar con los resultados de búsqueda. Regístrese en el sitio web de serpapi.com (hay una prueba gratuita disponible), inicie sesión en su cuenta y encuentre su clave API en la página del Panel de control.

Cree un archivo `.env` en el mismo directorio donde se ubicará su script de Python, y agregue las claves allí en el siguiente formato:

```
OPENAI_API_KEY=su_clave_openai
SERPAPI_API_KEY=su_clave_serpapi
```

**Paso 3: Crear un script de Python (browser_agent.py)**

Cree el archivo `browser_agent.py` e inserte el siguiente código en él:

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
        func=lambda query: f"Buscando en Google: {query}",  # Reemplazar con búsqueda real usando SerpAPI si es necesario
        description="Busca información en Google."
    )


    # Definir la tarea para el agente
    task = """
    Encuentra las últimas noticias sobre OpenAI en Google.
    Luego visita uno de los sitios web encontrados y encuentra los nombres de los fundadores.
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

Abra una terminal o símbolo del sistema, navegue hasta el directorio con el archivo `browser_agent.py` y ejecútelo:

```bash
python browser_agent.py
```

**Paso 5: Mejorar el agente (funciones avanzadas)**

* **Búsqueda real en Google:** Reemplace la función `lambda` en `search_tool` con código que use SerpAPI para búsquedas reales en Google. Esto requerirá estudiar la documentación de SerpAPI.

* **Interacción con páginas web (Browser-Use):** Para agregar funcionalidad de interacción con páginas web (abrir enlaces, extraer texto, etc.), deberá usar la biblioteca `browser-use`. La documentación de esta biblioteca lo ayudará a agregar las herramientas adecuadas a su agente.

* **Uso de memoria:** Los mecanismos de memoria de LangChain se pueden usar para preservar el contexto entre solicitudes.

* **Cadenas de acción más complejas:** LangChain le permite crear cadenas de acción más complejas para resolver tareas más complejas.


Este ejemplo demuestra la estructura básica. Para implementar un agente completo que interactúe con un navegador y Google Search, se requerirá trabajo adicional con SerpAPI y `browser-use`. No olvide consultar la documentación de estas bibliotecas para obtener información más detallada.
