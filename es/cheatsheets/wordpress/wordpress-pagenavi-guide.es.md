# Guía completa de variables en WP-PageNavi para WordPress

La navegación por páginas es una parte importante de cualquier blog o sitio de noticias en WordPress. Una de las herramientas más populares para una navegación paginada cómoda es el plugin **WP-PageNavi**. Permite reemplazar los enlaces estándar "Anterior / Siguiente" por una paginación más flexible y atractiva.

Una de sus características clave es la configuración del texto de los enlaces mediante **variables**, que sustituyen automáticamente el número de página actual, el número total de páginas y otra información.

En este artículo, analizaremos **todas las variables disponibles**, ejemplos de su uso y mostraremos con capturas de pantalla dónde deben insertarse.

---

## Dónde se encuentran los ajustes de WP-PageNavi

Después de instalar el plugin, ve al panel de administración de WordPress:

**Ajustes → PageNavi**

Allí verás un menú para configurar el texto de los enlaces (ejemplo en la captura de pantalla a continuación):

![Ajustes de PageNavi en WordPress](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 En cada campo se pueden usar variables para mostrar dinámicamente la página actual, el número total de páginas y otros elementos de navegación.

---

## Variables disponibles en WP-PageNavi

El plugin proporciona un conjunto de marcadores de posición (variables de plantilla) que se pueden usar en los ajustes:

### 🔹 %CURRENT_PAGE%
Muestra el **número de la página actual**.

Ejemplo:
```

Estás en la página %CURRENT\_PAGE%

```
👉 Si estás en la página 3, el resultado será:
```

Estás en la página 3

```

---

### 🔹 %TOTAL_PAGES%
Muestra el **número total de páginas**.

Ejemplo:
```

Total de páginas: %TOTAL\_PAGES%

```
👉 Si hay un total de 10 páginas, la salida será:
```

Total de páginas: 10

```

---

### 🔹 %PAGE_NUMBER%
Se utiliza para mostrar el **número de cada página** en la lista.

Ejemplo:
```

Página %PAGE\_NUMBER%

```
👉 En la navegación aparecerán enlaces:
```

Página 1 | Página 2 | Página 3 | ...

```

---

## Tabla de variables de WP-PageNavi

| Variable           | Descripción                               | Ejemplo de configuración                   | Resultado (si es la 3ª página de 10) |
|--------------------|-------------------------------------------|--------------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Número de la página actual                | `Ahora estás en la página %CURRENT_PAGE%` | `Ahora estás en la página 3` |
| **%TOTAL_PAGES%**  | Número total de páginas                   | `Total de páginas: %TOTAL_PAGES%`          | `Total de páginas: 10` |
| **%PAGE_NUMBER%**  | Número de cada página en la lista         | `Página %PAGE_NUMBER%`                     | `Página 1 | Página 2 | Página 3 …` |
| **1 (estático)**   | Primera página (sin variable)             | `Primera` o `Página 1`                     | `Primera` |
| **%TOTAL_PAGES%**  | Última página                             | `Página %TOTAL_PAGES%`                     | `Página 10` |
| **← / → / …**      | Símbolos para flechas y abreviaturas      | `← Anterior`, `Siguiente →`, `…`           | `← Anterior | 1 | 2 | 3 | … | 10 | Siguiente →` |

---

## Ejemplo de configuración completa

En la captura de pantalla anterior, los campos se pueden rellenar de la siguiente manera:

- **Text For Number Of Pages**:
  `Página %CURRENT_PAGE% de %TOTAL_PAGES%`

- **Text For Current Page**:
  `%PAGE_NUMBER%`

- **Text For Page**:
  `%PAGE_NUMBER%`

- **Text For First Page**:
  `Primera`

- **Text For Last Page**:
  `Página %TOTAL_PAGES%`

- **Text For Previous Page**:
  `← Anterior`

- **Text For Next Page**:
  `Siguiente →`

- **Text For Previous …**:
  `…`

- **Text For Next …**:
  `…`

👉 Al final, los visitantes verán una navegación similar a esta:
```

← Anterior | Primera | 1 | 2 | 3 | … | Página 10 | Siguiente →

```

---

## Resumen

Las variables en WP-PageNavi son sencillas, pero ofrecen flexibilidad en la configuración de la navegación:

- `%CURRENT_PAGE%` — página actual
- `%TOTAL_PAGES%` — total de páginas
- `%PAGE_NUMBER%` — número de una página específica

Para la primera página, usa `1`, y para la última, `%TOTAL_PAGES%`.

Gracias a estos ajustes, la navegación en el sitio web puede ser más clara y cómoda para los visitantes.
