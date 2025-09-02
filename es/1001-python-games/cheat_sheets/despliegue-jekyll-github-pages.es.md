## Despliegue automático de un sitio Jekyll en GitHub Pages

Para automatizar el proceso de despliegue, utilizaremos GitHub Actions, que permiten realizar diversas tareas, incluida la construcción y publicación de sitios web, directamente en su repositorio.

### 1: Resumen del archivo de flujo de trabajo
Primero, veamos el archivo de flujo de trabajo principal que controla el proceso de construcción y despliegue. Este archivo está escrito en YAML y normalmente se encuentra en el directorio `.github/workflows`. Aquí está su contenido:

```yaml
# Ejemplo de flujo de trabajo para construir y desplegar un sitio Jekyll en GitHub Pages
name: Desplegar Jekyll con dependencias de GitHub Pages preinstaladas

on:
  # Se ejecuta en los pushs dirigidos a la rama predeterminada
  push:
    branches: ["master"]

  # Permite ejecutar este flujo de trabajo manualmente desde la pestaña Acciones
  workflow_dispatch:

# Establece los permisos del GITHUB_TOKEN para permitir el despliegue en GitHub Pages
permissions:
  contents: read
  pages: write
  id-token: write

# Permitir solo un despliegue concurrente, omitiendo las ejecuciones en cola entre la ejecución en curso y la última en cola.
# Sin embargo, NO cancelar las ejecuciones en curso, ya que queremos permitir que estos despliegues de producción se completen.
concurrency:
  group: "pages"
  cancel-in-progress: false

jobs:
  # Tarea de construcción
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Configurar páginas
        uses: actions/configure-pages@v5
      - name: Construir con Jekyll
        uses: actions/jekyll-build-pages@v1
        with:
          source: ./docs/gemini/consultant/ru/src
          destination: ./_site
      - name: Cargar artefacto
        uses: actions/upload-pages-artifact@v3

  # Tarea de despliegue
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    needs: build
    steps:
      - name: Desplegar en GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

### 2: Desglose de la estructura del flujo de trabajo
Ahora, analicemos cada sección de este archivo:

#### 2.1. Información general

-   `name: Desplegar Jekyll con dependencias de GitHub Pages preinstaladas`: El nombre del flujo de trabajo que verá en la lista de Acciones en el repositorio.
-   `on`: Describe cuándo debe ejecutarse el flujo de trabajo:
    -   `push`: El flujo de trabajo se ejecuta en cada push a la rama `master`.
    -   `workflow_dispatch`: Le permite ejecutar manualmente el flujo de trabajo a través de la interfaz de GitHub.
-   `permissions`: Configura los permisos para la ejecución del flujo de trabajo:
    -   `contents: read`: Permiso para leer código del repositorio.
    -   `pages: write`: Permiso para publicar en GitHub Pages.
    -   `id-token: write`: Permiso para obtener un token de autenticación (requerido para GitHub Actions).
-   `concurrency`: Configura la ejecución paralela del flujo de trabajo:
    -   `group: "pages"`: Garantiza que solo un flujo de trabajo para GitHub Pages se ejecute a la vez.
    -   `cancel-in-progress: false`: Evita la cancelación de la ejecución actual del flujo de trabajo cuando se inicia una nueva.

#### 2.2. Sección `jobs`
Esta sección describe las tareas que deben realizarse. Tenemos dos trabajos: `build` y `deploy`.

##### 2.2.1. `build`: Construcción del sitio
    -   `runs-on: ubuntu-latest`: Indica que el trabajo se ejecuta en un servidor Ubuntu.
    -   `steps`: Enumera los pasos que se ejecutan durante la construcción:
        -   `name: Checkout`: Extrae el código fuente del repositorio.
        -   `uses: actions/checkout@v4`: Utiliza una acción predefinida para extraer el código.
        -   `name: Configurar páginas`: Configura el entorno para trabajar con GitHub Pages.
        -    `uses: actions/configure-pages@v5`: Utiliza una acción predefinida para la configuración.
        -   `name: Construir con Jekyll`: Inicia la construcción del sitio Jekyll.
        -   `uses: actions/jekyll-build-pages@v1`: Utiliza una acción predefinida para la construcción.
        -   `with:`: Configura los parámetros de la acción:
            -   `source: ./docs/gemini/consultant/ru/src`: Especifica dónde se encuentran los archivos fuente de su sitio. **Nota**: la ruta a sus archivos `docs/gemini/consultant/ru/src`.
            -    `destination: ./_site`: Especifica dónde colocar los archivos construidos.
        -   `name: Cargar artefacto`: Carga los archivos construidos para pasarlos al siguiente trabajo.
        -   `uses: actions/upload-pages-artifact@v3`: Utiliza una acción predefinida para cargar artefactos.
    
##### 2.2.2. `deploy`: Publicación del sitio
    -   `environment`: Configura el entorno para la publicación.
        -  `name: github-pages`: Nombre del entorno.
        -   `url: ${{ steps.deployment.outputs.page_url }}`: Obtiene la URL del sitio publicado.
    -   `runs-on: ubuntu-latest`: Indica que el trabajo se ejecuta en un servidor Ubuntu.
    -   `needs: build`: Indica que el trabajo `deploy` debe ejecutarse después de que el trabajo `build` se haya completado con éxito.
    -   `steps`: Enumera los pasos que se ejecutan durante la publicación:
        -   `name: Desplegar en GitHub Pages`: Realiza la publicación del sitio en GitHub Pages.
        -   `id: deployment`: Establece el identificador para la acción.
        -    `uses: actions/deploy-pages@v4`: Utiliza una acción predefinida para el despliegue.

### 3: ¿Qué hacen los archivos Markdown?

Los archivos con la extensión `.md` (Markdown) son la base de un sitio Jekyll. Markdown es un lenguaje de marcado simple que le permite formatear texto.
Jekyll procesa automáticamente los archivos `.md`, convirtiéndolos en páginas HTML. Sus archivos deben estar ubicados en la carpeta especificada en el flujo de trabajo `docs/gemini/consultant/ru/src`.

### 4: Diagrama de flujo


```mermaid
graph TD
    A[Inicio: Push o activación manual] --> B(Verificación del repositorio);
    B --> C[Construir sitio en la carpeta _site];
    C --> D[Cargar artefacto];
    D --> E[Publicar en GitHub Pages];
    E --> F[Fin: Sitio publicado];
    
    style A fill:#D46A6A,stroke:#333,stroke-width:2px
    style B fill:#D46A6A,stroke:#333,stroke-width:2px
    style C fill:#D46A6A,stroke:#333,stroke-width:2px
    style D fill:#D46A6A,stroke:#333,stroke-width:2px
    style E fill:#D46A6A,stroke:#333,stroke-width:2px
    style F fill:#D46A6A,stroke:#333,stroke-width:2px
    
    linkStyle 0,1,2,3,4 stroke:#333,stroke-width:2px
```

### 5: Cómo funciona
1.  **Cambio de código:** Realiza cambios en sus archivos `.md` o `.html`, que se encuentran en la carpeta `docs/gemini/consultant/ru/src`.
2.  **Push:** Envía (push) sus cambios a la rama `master` de su repositorio de GitHub.
3.  **Ejecución del flujo de trabajo:** GitHub Actions ejecuta automáticamente el flujo de trabajo descrito en el archivo YAML.
4.  **Construcción:** El flujo de trabajo primero descarga el código del repositorio, luego construye el sitio Jekyll a partir de sus archivos fuente en la carpeta `_site`.
5.  **Publicación:** El sitio construido se publica en GitHub Pages.
6.  **Sitio listo:** Después de eso, su sitio es accesible en la URL especificada en la configuración de GitHub Pages.

