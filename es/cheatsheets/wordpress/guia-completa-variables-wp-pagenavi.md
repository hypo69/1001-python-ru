# Guía completa de variables WP-PageNavi para WordPress

La navegación por páginas es una parte importante de cualquier blog o sitio de noticias de WordPress. Una de las herramientas más populares para una paginación cómoda es el plugin **WP-PageNavi**. Permite reemplazar los enlaces estándar "Anterior / Siguiente" por una paginación más flexible y atractiva.

Una de las características clave es la capacidad de personalizar el texto de los enlaces utilizando **variables** que sustituyen automáticamente el número de página actual, el número total de páginas y otra información.

En este artículo, analizaremos **todas las variables disponibles**, ejemplos de su uso y mostraremos con capturas de pantalla dónde insertarlas.

---

## Dónde encontrar la configuración de WP-PageNavi

Después de instalar el plugin, vaya al panel de administración de WordPress:

**Ajustes → PageNavi**

Allí verá un menú para personalizar el texto de los enlaces (ejemplo en la captura de pantalla a continuación):

![Configuración de WP-PageNavi en WordPress](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 En cada campo, puede usar variables para mostrar dinámicamente la página actual, el número total de páginas y otros elementos de navegación.

---

## Variables WP-PageNavi disponibles

El plugin proporciona un conjunto de marcadores de posición (variables de plantilla) que se pueden usar en la configuración:

### 🔹 %CURRENT_PAGE%
Muestra el **número de la página actual**.

Ejemplo:
```

Estás en la página %CURRENT_PAGE%

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

Total de páginas: %TOTAL_PAGES%

```
👉 Si hay 10 páginas en total, la salida será:
```

Total de páginas: 10

```

---

### 🔹 %PAGE_NUMBER%
Se utiliza para mostrar el **número de cada página** en la lista.

Ejemplo:
```

Página %PAGE_NUMBER%

```
👉 En la navegación, aparecerán los enlaces:
```

Página 1 | Página 2 | Página 3 | ...

```

---

## Tabla de variables WP-PageNavi

| Variable          | Descripción                               | Ejemplo de configuración           | Resultado (si es la 3ª página de 10) |
|-------------------|-------------------------------------------|------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Número de la página actual                | `Actualmente estás en la página %CURRENT_PAGE%` | `Actualmente estás en la página 3` |
| **%TOTAL_PAGES%**  | Número total de páginas                   | `Total de páginas: %TOTAL_PAGES%`  | `Total de páginas: 10` |
| **%PAGE_NUMBER%**  | Número de cada página en la lista         | `Página %PAGE_NUMBER%`             | `Página 1 | Página 2 | Página 3 …` |
| **1 (estático)**  | Primera página (sin variable)             | `Primera` o `Página 1`             | `Primera` |
| **%TOTAL_PAGES%**  | Última página                             | `Página %TOTAL_PAGES%`             | `Página 10` |
| **← / → / …**      | Símbolos para flechas y abreviaturas      | `← Atrás`, `Siguiente →`, `…`      | `← Atrás | 1 | 2 | 3 | … | 10 | Siguiente →` |

---

## Ejemplo de configuración completa

En la captura de pantalla anterior, puede rellenar los campos de la siguiente manera:

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
  `← Atrás`

- **Text For Next Page**:  
  `Siguiente →`

- **Text For Previous …**:  
  `…`

- **Text For Next …**:  
  `…`

👉 Como resultado, los visitantes verán aproximadamente la siguiente navegación:
```

← Atrás | Primera | 1 | 2 | 3 | … | Página 10 | Siguiente →

```

---

## Resumen

Las variables de WP-PageNavi son simples pero brindan flexibilidad en la configuración de la navegación:

- `%CURRENT_PAGE%` — página actual  
- `%TOTAL_PAGES%` — total de páginas  
- `%PAGE_NUMBER%` — número de página específico  

Para la primera página, use `1`, y para la última página, use `%TOTAL_PAGES%`.

Gracias a esta configuración, puede hacer que la navegación del sitio web sea más comprensible y conveniente para los visitantes.