# Cómo enseñar a una red neuronal a trabajar con sus manos: creación de un agente de IA completo con MCP y LangGraph en una hora

¡Amigos, saludos! Espero que me hayan extrañado.

Durante los últimos dos meses, me he sumergido profundamente en la investigación de la integración de agentes de IA en mis propios proyectos de Python. En el proceso, he acumulado una gran cantidad de conocimientos prácticos y observaciones que sería un pecado no compartir. Así que hoy regreso a Habr, con un nuevo tema, una perspectiva fresca y la intención de escribir más a menudo.

En la agenda están LangGraph y MCP: herramientas con las que puedes crear agentes de IA realmente útiles.

Si antes discutíamos sobre qué red neuronal responde mejor en ruso, hoy el campo de batalla se ha desplazado hacia tareas más aplicadas: ¿quién se desenvuelve mejor en el papel de un agente de IA? ¿Qué frameworks realmente simplifican el desarrollo? ¿Y cómo integrar todo esto en un proyecto real?

Pero antes de sumergirnos en la práctica y el código, aclaremos los conceptos básicos. Especialmente dos clave: **agentes de IA y MCP**. Sin ellos, la conversación sobre LangGraph estará incompleta.

### Agentes de IA en términos sencillos

Los agentes de IA no son solo chatbots "mejorados". Representan entidades más complejas y autónomas que poseen dos características cruciales:

1.  **Capacidad de interactuar y coordinarse**

    Los agentes modernos pueden dividir tareas en subtareas, llamar a otros agentes, solicitar datos externos, trabajar en equipo. Ya no es un asistente solitario, sino un sistema distribuido donde cada componente puede contribuir.

2.  **Acceso a recursos externos**

    Un agente de IA ya no está limitado por los límites de un diálogo. Puede acceder a bases de datos, realizar llamadas a API, interactuar con archivos locales, bases de conocimiento vectoriales e incluso ejecutar comandos en el terminal. Todo esto fue posible gracias a la aparición de MCP, un nuevo nivel de integración entre el modelo y el entorno.

---

En pocas palabras: **MCP es un puente entre una red neuronal y su entorno**. Permite que el modelo "comprenda" el contexto de la tarea, acceda a los datos, realice llamadas y forme acciones razonadas, en lugar de simplemente generar respuestas de texto.

**Imaginemos una analogía:**

*   Tienes una **red neuronal** — puede razonar y generar textos.
*   Hay **datos y herramientas** — documentos, API, bases de conocimiento, terminal, código.
*   Y hay **MCP** — es una interfaz que permite al modelo interactuar con estas fuentes externas como si fueran parte de su mundo interno.

**Sin MCP:**

El modelo — es un motor de diálogo aislado. Le das texto — responde. Y eso es todo.

**Con MCP:**

El modelo se convierte en un **ejecutor de tareas** completo:

*   obtiene acceso a estructuras de datos y API;
*   llama a funciones externas;
*   navega por el estado actual del proyecto o aplicación;
*   puede recordar, rastrear y cambiar el contexto a medida que avanza el diálogo;
*   utiliza extensiones como herramientas de búsqueda, ejecutores de código, bases de datos de incrustaciones vectoriales, etc.

En un sentido técnico, **MCP es un protocolo para la interacción entre un LLM y su entorno**, donde el contexto se proporciona como objetos estructurados (en lugar de texto "en bruto"), y las llamadas se formatean como operaciones interactivas (por ejemplo, llamadas a funciones, uso de herramientas o acciones de agente). Esto es lo que convierte un modelo ordinario en un **verdadero agente de IA**, capaz de hacer más que solo "hablar".

### ¡Y ahora, al grano!

Ahora que hemos cubierto los conceptos básicos, es lógico preguntar: "¿Cómo implementamos todo esto en la práctica en Python?"

Aquí es donde entra en juego **LangGraph**, un potente framework para construir gráficos de estado, comportamientos de agente y cadenas de pensamiento. Te permite "unir" la lógica de interacción entre agentes, herramientas y el usuario, creando una arquitectura de IA viva que se adapta a las tareas.

En las siguientes secciones, veremos cómo:

*   construir un agente desde cero;
*   crear estados, transiciones y eventos;
*   integrar funciones y herramientas;
*   y cómo funciona todo este ecosistema en un proyecto real.

### Un poco de teoría: ¿qué es LangGraph?

Antes de sumergirnos en la práctica, unas palabras sobre el framework en sí.

**LangGraph** es un proyecto del equipo de **LangChain**, los mismos que propusieron por primera vez el concepto de "cadenas" de interacción con los LLM. Si antes el enfoque principal estaba en las tuberías lineales o condicionalmente ramificadas (langchain.chains), ahora los desarrolladores apuestan por un **modelo de grafo**, y LangGraph es lo que recomiendan como el nuevo "núcleo" para construir sistemas de IA complejos.

**LangGraph** es un framework para construir máquinas de estados finitos y grafos de estados, donde cada **nodo** representa una parte de la lógica del agente: una llamada a un modelo, una herramienta externa, una condición, una entrada de usuario, etc.

### Cómo funciona: grafos y nodos

Conceptualmente, LangGraph se basa en las siguientes ideas:

*   **Grafo** — es una estructura que describe las posibles rutas de ejecución de la lógica. Puedes pensarlo como un mapa: de un punto puedes moverte a otro dependiendo de las condiciones o el resultado de la ejecución.
*   **Nodos** — son pasos específicos dentro del grafo. Cada nodo realiza alguna función: llama a un modelo, llama a una API externa, verifica una condición o simplemente actualiza el estado interno.
*   **Transiciones entre nodos** — es la lógica de enrutamiento: si el resultado del paso anterior es tal y cual, entonces ve allí.
*   **Estado** — se pasa entre nodos y acumula todo lo necesario: historial, conclusiones intermedias, entrada de usuario, resultados de operaciones de herramientas, etc.

Así, obtenemos un **mecanismo flexible para controlar la lógica del agente**, en el que se pueden describir escenarios tanto simples como muy complejos: bucles, condiciones, acciones paralelas, llamadas anidadas y mucho más.

### ¿Por qué es conveniente?

LangGraph te permite construir una **lógica transparente, reproducible y extensible**:

*   fácil de depurar;
*   fácil de visualizar;
*   fácil de escalar para nuevas tareas;
*   fácil de integrar herramientas externas y protocolos MCP.

En esencia, LangGraph es el **"cerebro" del agente**, donde cada paso está documentado, controlable y puede modificarse sin caos ni "magia".

### ¡Y ahora, basta de teoría!

Podríamos hablar mucho tiempo sobre grafos, estados, composición lógica y las ventajas de LangGraph sobre las tuberías clásicas. Pero, como muestra la práctica, es mejor verlo una vez en el código.

**Es hora de pasar a la práctica.** A continuación, un ejemplo en Python: crearemos un agente de IA simple pero útil basado en LangGraph que utilizará herramientas externas, memoria y tomará sus propias decisiones.

### Preparación: redes neuronales en la nube y locales

Para empezar a crear agentes de IA, primero necesitamos un **cerebro**, un modelo de lenguaje. Aquí hay dos enfoques:

*   **usar soluciones en la nube**, donde todo está listo "de fábrica";
*   o **levantar el modelo localmente** — para una autonomía y confidencialidad completas.

Consideremos ambas opciones.

#### Servicios en la nube: rápidos y convenientes

La forma más sencilla es utilizar el poder de los grandes proveedores: OpenAI, Anthropic, y utilizar...

### Dónde obtener claves y tokens:

*   **OpenAI** — ChatGPT y otros productos;
*   **Anthropic** — Claude;
*   **OpenRouter.ai** — docenas de modelos (un token — muchos modelos a través de una API compatible con OpenAI);
*   **Amvera Cloud** — capacidad de conectar LLAMA con pago en rublos y proxy integrado a OpenAI y Anthropic.

Este camino es conveniente, especialmente si:

*   no quieres configurar la infraestructura;
*   desarrollas con un enfoque en la velocidad;
*   trabajas con recursos limitados.

### Modelos locales: control total

Si la **privacidad, el trabajo sin conexión** son importantes para ti, o quieres construir **agentes completamente autónomos**, entonces tiene sentido desplegar la red neuronal localmente.

**Principales ventajas:**

*   **Confidencialidad** — los datos permanecen contigo;
*   **Trabajo sin conexión** — útil en redes aisladas;
*   **Sin suscripciones ni tokens** — gratis después de la configuración.

**Las desventajas son obvias:**

*   Requisitos de recursos (especialmente para la memoria de video);
*   La configuración puede llevar tiempo;
*   Algunos modelos son difíciles de desplegar sin experiencia.

Sin embargo, existen herramientas que facilitan el lanzamiento local. Una de las mejores hoy en día es **Ollama**.

### Despliegue de un LLM local a través de Ollama + Docker

Prepararemos un lanzamiento local del modelo Qwen 2.5 (qwen2.5:32b) utilizando un contenedor Docker y el sistema Ollama. Esto permitirá integrar la red neuronal con MCP y usarla en tus propios agentes basados en LangGraph.

Si los recursos informáticos de tu ordenador o servidor son insuficientes para trabajar con esta versión del modelo, siempre puedes elegir una red neuronal menos "hambrienta" de recursos; el proceso de instalación y lanzamiento seguirá siendo similar.

**Instalación rápida (resumen de pasos)**

1.  **Instala Docker + Docker Compose**
2.  **Crea la estructura del proyecto:**
```bash
mkdir qwen-local && cd qwen-local
```
3.  **Crea `docker-compose.yml`**
(opción universal, GPU detectada automáticamente)

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

4.  **Inicia el contenedor:**
```bash
docker compose up -d
```

5.  **Descarga el modelo:**
```bash
docker exec -it ollama_qwen ollama pull qwen2.5:32b
```

6.  **Verifica el funcionamiento a través de la API:**
```bash
curl http://localhost:11434/api/generate \
  -H "Content-Type: application/json" \
  -d '{"model": "qwen2.5:32b", "prompt": "¡Hola!", "stream": false}'
```
*(Imagen con el resultado de la ejecución del comando curl)*

7.  **Integración con Python:**
```python
import requests

def query(prompt):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:32b",
        "prompt": prompt,
        "stream": False
    })
    return res.json()['response']

print(query("Explica el entrelazamiento cuántico"))
```
Ahora tienes un LLM local completo, listo para trabajar con MCP y LangGraph.

**¿Qué sigue?**

Tenemos la opción de elegir entre modelos en la nube y locales, y hemos aprendido a conectar ambos. Lo más interesante está por venir: **la creación de agentes de IA en LangGraph**, que utilizan el modelo seleccionado, la memoria, las herramientas y su propia lógica.

**¡Pasemos a la parte más sabrosa: el código y la práctica!**

---

Antes de pasar a la práctica, es importante preparar el entorno de trabajo. Asumo que ya estás familiarizado con los conceptos básicos de Python, sabes qué son las bibliotecas y las dependencias, y entiendes por qué usar un entorno virtual.

Si todo esto es nuevo para ti, te recomiendo que primero tomes un curso corto o una guía sobre los conceptos básicos de Python, y luego regreses al artículo.

#### Paso 1: Creación de un entorno virtual

Crea un nuevo entorno virtual en la carpeta del proyecto:
```bash
python -m venv venv
source venv/bin/activate  # para Linux/macOS
venv\Scripts\activate   # para Windows
```

#### Paso 2: Instalación de dependencias

Crea un archivo `requirements.txt` y añade las siguientes líneas:
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

> ⚠️ **Las versiones actuales son a 21 de julio de 2025.** Es posible que hayan cambiado desde la publicación; **verifica la relevancia antes de la instalación.**

Luego instala las dependencias:
```bash
pip install -r requirements.txt```

#### Paso 3: Configuración de variables de entorno

Crea un archivo `.env` en la raíz del proyecto y añade las claves API necesarias:
```
OPENAI_API_KEY=sk-proj-1234
DEEPSEEK_API_KEY=sk-123
OPENROUTER_API_KEY=sk-or-v1-123
BRAVE_API_KEY=BSAj123K1bvBGpH1344tLwc
```

**Propósito de las variables:**

*   **OPENAI_API_KEY** — clave para acceder a los modelos GPT de OpenAI;
*   **DEEPSEEK_API_KEY** — clave para usar los modelos Deepseek;
*   **OPENROUTER_API_KEY** — clave única para acceder a muchos modelos a través de OpenRouter

---
Algunas herramientas MCP (por ejemplo, `brave-web-search`) requieren una clave para funcionar. Sin ella, simplemente no se activarán.

**¿Qué pasa si no tienes claves API?**

No hay problema. Puedes comenzar el desarrollo con un modelo local (por ejemplo, a través de Ollama), sin conectar ningún servicio externo. En este caso, no es necesario crear el archivo `.env` en absoluto.

¡Listo! Ahora tenemos todo lo necesario para empezar: un entorno aislado, dependencias y, si es necesario, acceso a redes neuronales en la nube e integraciones MCP.

A continuación, ejecutaremos nuestro agente LLM de diferentes maneras.

### Lanzamiento simple de agentes LLM a través de LangGraph: integración básica

Comencemos con lo más simple: cómo "conectar el cerebro" al futuro agente. Analizaremos las formas básicas de lanzar modelos de lenguaje (LLM) usando LangChain, para que en el siguiente paso podamos pasar a la integración con LangGraph y construir un agente de IA completo.

#### Importaciones
```python
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_deepseek import ChatDeepSeek
```
*   `os` y `load_dotenv()` — para cargar variables del archivo `.env`.
*   `ChatOpenAI`, `ChatOllama`, `ChatDeepSeek` — envoltorios para conectar modelos de lenguaje a través de LangChain.

> 💡 Si utilizas enfoques alternativos para trabajar con configuraciones (por ejemplo, Pydantic Settings), puedes reemplazar `load_dotenv()` por tu método habitual.

#### Carga de variables de entorno
```python
load_dotenv()
```
Esto cargará todas las variables de `.env`, incluidas las claves para acceder a las API de OpenAI, DeepSeek, OpenRouter y otras.

#### Funciones simples para obtener LLM

**OpenAI**
```python
def get_openai_llm():
    return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
```
Si la variable `OPENAI_API_KEY` está configurada correctamente, LangChain la sustituirá automáticamente; la especificación explícita de `api_key=...` aquí es opcional.

**DeepSeek**
```python
def get_deepseek_llm():
    # ...
```
De manera similar, pero usamos el envoltorio `ChatDeepSeek`.

**OpenRouter (y otras API compatibles)**
```python
def get_openrouter_llm(model="moonshotai/kimi-k2:free"):
    return ChatOpenAI(
        model=model,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1",
        temperature=0
    )
```
**Características:**

*   Se utiliza `ChatOpenAI`, aunque el modelo no sea de OpenAI, porque OpenRouter utiliza el mismo protocolo.
*   `base_url` es obligatorio: apunta a la API de OpenRouter.
*   El modelo `moonshotai/kimi-k2:free` fue elegido como una de las opciones más equilibradas en términos de calidad y velocidad en el momento de escribir este artículo.
*   La clave API de `OpenRouter` debe pasarse explícitamente; la sustitución automática no funciona aquí.

#### Mini-prueba: comprobación del funcionamiento del modelo
```python
if __name__ == "__main__":
    llm = get_openrouter_llm(model="moonshotai/kimi-k2:free")
    response = llm.invoke("¿Quién eres?")
    print(response.content)
```
*(Imagen con el resultado de la ejecución del comando)*

Si todo está configurado correctamente, recibirás una respuesta significativa del modelo. ¡Felicidades, el primer paso está hecho!

### Pero esto aún no es un agente

En la etapa actual, hemos conectado LLM y hemos realizado una llamada simple. Esto se parece más a un chatbot de consola que a un agente de IA.

**¿Por qué?**

*   Escribimos **código síncrono y lineal** sin lógica de estado ni objetivos.
*   El agente no toma decisiones, no recuerda el contexto y no utiliza herramientas.
*   MCP y LangGraph aún no están involucrados.

**¿Qué sigue?**

A continuación, implementaremos un **agente de IA completo** utilizando **LangGraph**, primero sin MCP, para centrarnos en la arquitectura, los estados y la lógica del propio agente.

¡Sumérgete en la verdadera mecánica de los agentes! ¡Vamos!

### Agente de clasificación de vacantes: de la teoría a la práctica

...conceptos de LangGraph en la práctica y crear una herramienta útil para plataformas de RRHH e intercambios de freelancers.

#### Tarea del agente

Nuestro agente toma como entrada una descripción de texto de una vacante o servicio y realiza una clasificación de tres niveles:

1.  **Tipo de trabajo**: trabajo por proyecto o vacante permanente
2.  **Categoría profesional**: de más de 45 especialidades predefinidas
3.  **Tipo de búsqueda**: si una persona busca trabajo o busca un intérprete

El resultado se devuelve en un formato JSON estructurado con una puntuación de confianza para cada clasificación.

#### 📈 Arquitectura del agente en LangGraph

Siguiendo los principios de LangGraph, creamos un **grafo de estados** de cuatro nodos:

- Descripción de entrada
- ↓
- Nodo de clasificación del tipo de trabajo
- ↓
- Nodo de clasificación de categoría
- ↓
- Nodo de determinación del tipo de búsqueda
- ↓
- Nodo de cálculo de confianza
- ↓
- Resultado JSON

Cada nodo es una **función especializada** que:

*   Recibe el estado actual del agente
*   Realiza su parte del análisis
*   Actualiza el estado y lo pasa

#### Gestión de estados

Definimos la **estructura de memoria del agente** a través de `TypedDict`:

```python
from typing import TypedDict, Dict

class State(TypedDict):
    """Estado del agente para almacenar información sobre el proceso de clasificación"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool
```

Esta es la **memoria de trabajo del agente**, todo lo que recuerda y acumula durante el análisis. Similar a cómo un experto humano mantiene el contexto de la tarea en mente al analizar un documento.

Veamos el código completo y luego nos centraremos en los puntos principales.

```python
import asyncio
import json
from enum import Enum
from typing import TypedDict, Dict, Any, List

from langgraph.graph import StateGraph, END
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# Categorías profesionales
CATEGORIES = [
    "Animador 2D", "Animador 3D", "Modelador 3D",
    "Analista de negocios", "Desarrollador Blockchain", ...
]

class JobType(Enum):
    PROJECT = "trabajo por proyecto"
    PERMANENT = "trabajo permanente"

class SearchType(Enum):
    LOOKING_FOR_WORK = "buscando trabajo"
    LOOKING_FOR_PERFORMER = "buscando un intérprete"

class State(TypedDict):
    """Estado del agente para almacenar información sobre el proceso de clasificación"""
    description: str
    job_type: str
    category: str
    search_type: str
    confidence_scores: Dict[str, float]
    processed: bool

class VacancyClassificationAgent:
    """Agente asíncrono para clasificar vacantes y servicios"""

    def __init__(self, model_name: str = "gpt-4o-mini", temperature: float = 0.1):
        """Inicialización del agente"""
        self.llm = ChatOpenAI(model=model_name, temperature=temperature)
        self.workflow = self._create_workflow()

    def _create_workflow(self) -> StateGraph:
        """Crea el flujo de trabajo del agente basado en LangGraph"""
        workflow = StateGraph(State)
        
        # Añadir nodos al grafo
        workflow.add_node("job_type_classification", self._classify_job_type)
        workflow.add_node("category_classification", self._classify_category)
        workflow.add_node("search_type_classification", self._classify_search_type)
        workflow.add_node("confidence_calculation", self._calculate_confidence)
        
        # Definir la secuencia de ejecución de nodos
        workflow.set_entry_point("job_type_classification")
        workflow.add_edge("job_type_classification", "category_classification")
        workflow.add_edge("category_classification", "search_type_classification")
        workflow.add_edge("search_type_classification", "confidence_calculation")
        workflow.add_edge("confidence_calculation", END)
        
        return workflow.compile()

    async def _classify_job_type(self, state: State) -> Dict[str, Any]:
        """Nodo para determinar el tipo de trabajo: por proyecto o permanente"""
        # ... (la implementación sigue)
        
    async def _classify_category(self, state: State) -> Dict[str, Any]:
        """Nodo para determinar la categoría profesional"""
        # ... (la implementación sigue)
        
    async def _classify_search_type(self, state: State) -> Dict[str, Any]:
        """Nodo para determinar el tipo de búsqueda"""
        # ... (la implementación sigue)

    async def _calculate_confidence(self, state: State) -> Dict[str, Any]:
        """Nodo para calcular el nivel de confianza en la clasificación"""
        # ... (la implementación sigue)

    def _find_closest_category(self, predicted_category: str) -> str:
        """Encuentra la categoría más cercana de la lista de disponibles"""
        # ... (la implementación sigue)

    async def classify(self, description: str) -> Dict[str, Any]:
        """Método principal para clasificar vacantes/servicios"""
        initial_state = {
            "description": description,
            "job_type": "",
            "category": "",
            "search_type": "",
            "confidence_scores": {},
            "processed": False
        }
        
        # Iniciar el flujo de trabajo
        result = await self.workflow.ainvoke(initial_state)
        
        # Formar la respuesta JSON final
        classification_result = {
            "job_type": result["job_type"],
            "category": result["category"],
            "search_type": result["search_type"],
            "confidence_scores": result["confidence_scores"],
            "success": result["processed"]
        }
        return classification_result

async def main():
    """Demostración del funcionamiento del agente"""
    agent = VacancyClassificationAgent()
    
    test_cases = [
        "Se requiere desarrollador Python para crear una aplicación web en Django. Trabajo permanente.",
        "Busco pedidos para crear logotipos e identidad corporativa. Trabajo en Adobe Illustrator.",
        "Se necesita un animador 3D para un proyecto a corto plazo de creación de un spot publicitario.",
        "Currículum: comercializador experimentado, busco trabajo remoto en marketing digital",
        "Buscamos un desarrollador frontend React para nuestro equipo de forma permanente"
    ]
    
    print("🤖 Demostración del funcionamiento del agente de clasificación de vacantes\n")
    for i, description in enumerate(test_cases, 1):
        print(f"--- Prueba {i}: ---")
        print(f"Descripción: {description}")
        try:
            result = await agent.classify(description)
            print("Resultado de la clasificación:")
            print(json.dumps(result, ensure_ascii=False, indent=2))
        except Exception as e:
            print(f"❌ Error: {e}")
        print("-" * 80)

if __name__ == "__main__":
    asyncio.run(main())

```
*(...el resto del código con la implementación de los métodos se presentó en el artículo...)*

### Ventajas clave de la arquitectura
1.  **Modularidad** — cada nodo resuelve una tarea, fácil de probar y mejorar por separado
2.  **Extensibilidad** — se pueden añadir nuevos nodos de análisis sin modificar los existentes
3.  **Transparencia** — todo el proceso de toma de decisiones está documentado y es rastreable
4.  **Rendimiento** — procesamiento asíncrono de múltiples solicitudes
5.  **Fiabilidad** — mecanismos de respaldo y manejo de errores

### Beneficios reales
Un agente así puede utilizarse en:
*   **Plataformas de RRHH** para la categorización automática de currículums y vacantes
*   **Bolsas de trabajo freelance** para mejorar la búsqueda y las recomendaciones
*   **Sistemas internos** de empresas para procesar solicitudes y proyectos
*   **Soluciones analíticas** para la investigación del mercado laboral

### MCP en acción: creación de un agente con sistema de archivos y búsqueda web
Una vez que hemos comprendido los principios básicos de LangGraph y hemos creado un agente clasificador simple, ampliemos sus capacidades conectándolo al mundo exterior a través de MCP.

Ahora crearemos un asistente de IA completo que podrá:
*   Trabajar con el sistema de archivos (leer, crear, modificar archivos)
*   Buscar información relevante en Internet
*   Recordar el contexto del diálogo
*   Manejar errores y recuperarse de fallos

#### De la teoría a las herramientas reales
¿Recuerdas cómo al principio del artículo hablamos de que **MCP es un puente entre una red neuronal y su entorno**? Ahora lo verás en la práctica. Nuestro agente tendrá acceso a **herramientas reales**:
```
# Herramientas del sistema de archivos
- read_file — leer archivos
- write_file — escribir y crear archivos
- list_directory — ver el contenido de las carpetas
- create_directory — crear carpetas

# Herramientas de búsqueda web
- brave_web_search — buscar en Internet
- get_web_content — obtener el contenido de las páginas
```
Este ya no es un agente de "juguete", es una **herramienta de trabajo** que puede resolver problemas reales.

#### 📈 Arquitectura: de lo simple a lo complejo

**1. Configuración como base de la estabilidad**
```python
from dataclasses import dataclass

@dataclass
class AgentConfig:
    """Configuración simplificada del agente de IA"""
    filesystem_path: str = "/path/to/work/directory"
    model_provider: ModelProvider = ModelProvider.OLLAMA
    use_memory: bool = True
    enable_web_search: bool = True

    def validate(self) -> None:
        """Validación de la configuración"""
        if not os.path.exists(self.filesystem_path):
            raise ValueError(f"La ruta no existe: {self.filesystem_path}")
```
**¿Por qué es importante?** A diferencia del ejemplo de clasificación, aquí el agente interactúa con sistemas externos. Un error en la ruta del archivo o una clave API faltante, y todo el agente deja de funcionar. La **validación al inicio** ahorra horas de depuración.

**2. Fábrica de modelos: elección flexible**
```python
def create_model(config: AgentConfig):
    """Crea un modelo según la configuración"""
    provider = config.model_provider.value
    if provider == "ollama":
        return ChatOllama(model="qwen2.5:32b", base_url="http://localhost:11434")
    elif provider == "openai":
        return ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY"))
    # ... otros proveedores
```
Un código, muchos modelos. ¿Quieres un modelo local gratuito? Usa Ollama. ¿Necesitas la máxima precisión? Cambia a GPT-4. ¿La velocidad es importante? Prueba DeepSeek. El código sigue siendo el mismo.

**3. Integración MCP: conexión con el mundo real**
```python
async def _init_mcp_client(self):
    """Inicialización del cliente MCP"""
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
Aquí ocurre el trabajo clave de MCP: conectamos servidores MCP externos al agente, que proporcionan un conjunto de herramientas y funciones. El agente no solo recibe funciones individuales, sino una comprensión contextual completa de cómo trabajar con el sistema de archivos e Internet.

#### Resistencia a errores
En el mundo real, todo falla: la red no está disponible, los archivos están bloqueados, las claves API han caducado. Nuestro agente está preparado para esto:
```python
@retry_on_failure(max_retries=2, delay=1.0)
async def process_message(self, user_input: str, thread_id: str = "default") -> str:
    # ...
```
El decorador `@retry_on_failure` reintenta automáticamente las operaciones en caso de fallos temporales. El usuario ni siquiera notará que algo salió mal.

### Resultados: de la teoría a la práctica de los agentes de IA

Hoy hemos recorrido el camino desde los conceptos básicos hasta la creación de agentes de IA funcionales. Resumamos lo que hemos aprendido y logrado.

**Lo que hemos dominado**

**1. Conceptos fundamentales**
*   Comprendimos la diferencia entre chatbots y verdaderos agentes de IA
*   Entendimos el papel de **MCP (Protocolo de Contexto del Modelo)** como puente entre el modelo y el mundo exterior
*   Estudiamos la arquitectura de **LangGraph** para construir una lógica de agente compleja

**2. Habilidades prácticas**
*   Configuramos un entorno de trabajo con soporte para modelos en la nube y locales
*   Creamos un **agente clasificador** con arquitectura asíncrona y gestión de estados
*   Construimos un **agente MCP** con acceso al sistema de archivos y búsqueda web

**3. Patrones arquitectónicos**
*   Dominamos la configuración modular y las fábricas de modelos
*   Implementamos el manejo de errores y los **mecanismos de reintento** para soluciones listas para producción

### Ventajas clave del enfoque
**LangGraph + MCP** nos brindan:
*   **Transparencia** — cada paso del agente está documentado y es rastreable
*   **Extensibilidad** — se añaden nuevas funciones de forma declarativa
*   **Fiabilidad** — manejo de errores y recuperación integrados
*   **Flexibilidad** — soporte para múltiples modelos y proveedores de forma predeterminada

### Conclusión

Los agentes de IA no son una ficción futurista, sino una **tecnología real de hoy**. Con LangGraph y MCP, podemos crear sistemas que resuelven problemas de negocio específicos, automatizan rutinas y abren nuevas posibilidades.

**Lo principal es empezar.** Toma el código de los ejemplos, adáptalo a tus tareas, experimenta. Cada proyecto es una nueva experiencia y un paso hacia la maestría en el campo del desarrollo de IA.

¡Mucha suerte con tus proyectos!

---
*Etiquetas: python, ia, mcp, langchain, asistente de ia, ollama, agentes de ia, llm local, langgraph, mcp-server*
*Hubs: Blog de la empresa Amvera, Procesamiento del lenguaje natural, Inteligencia artificial, Python, Programación*
