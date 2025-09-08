# Complete Guide to Variables in WP-PageNavi for WordPress

Page navigation is an important part of any WordPress blog or news site. One of the most popular tools for convenient paginated navigation is the **WP-PageNavi** plugin. It allows you to replace the standard "Previous / Next" links with more flexible and attractive pagination.

One of its key features is the ability to customize link text using **variables** that automatically insert the current page number, total number of pages, and other information.

In this article, we will break down **all available variables**, provide examples of their use, and show screenshots of where to insert them.

---

## Where to Find WP-PageNavi Settings

After installing the plugin, navigate in the WordPress admin area to:

**Settings → PageNavi**

There you will see a menu for configuring link text (example in the screenshot below):

![PageNavi Settings in WordPress](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 In each field, you can use variables to dynamically display the current page, total number of pages, and other navigation elements.

---

## Available WP-PageNavi Variables

The plugin provides a set of placeholders (template variables) that can be used in the settings:

### 🔹 %CURRENT_PAGE%
Displays the **current page number**.

Example:
```
You are on page %CURRENT_PAGE%
```
👉 If you are on page 3, the result will be:
```
You are on page 3
```

---

### 🔹 %TOTAL_PAGES%
Shows the **total number of pages**.

Example:
```
Total pages: %TOTAL_PAGES%
```
👉 If there are 10 pages in total, the output will be:
```
Total pages: 10
```

---

### 🔹 %PAGE_NUMBER%
Used to display the **number of each page** in the list.

Example:
```
Page %PAGE_NUMBER%
```
👉 The navigation will show links:
```
Page 1 | Page 2 | Page 3 | ...
```

---

## WP-PageNavi Variables Table

| Variable           | Description                           | Example Setting                     | Result (if 3rd page out of 10)       |
|--------------------|---------------------------------------|-------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Current page number                   | `You are currently on page %CURRENT_PAGE%` | `You are currently on page 3` |
| **%TOTAL_PAGES%**  | Total number of pages                 | `Total pages: %TOTAL_PAGES%`        | `Total pages: 10` |
| **%PAGE_NUMBER%**  | Number of each page in the list       | `Page %PAGE_NUMBER%`                | `Page 1 | Page 2 | Page 3 …` |
| **1 (static)**     | First page (no variable)              | `First` or `Page 1`                 | `First` |
| **%TOTAL_PAGES%**  | Last page                             | `Page %TOTAL_PAGES%`                | `Page 10` |
| **← / → / …**      | Symbols for arrows and ellipses       | `← Back`, `Forward →`, `…`          | `← Back | 1 | 2 | 3 | … | 10 | Forward →` |

---

## Full Configuration Example

In the screenshot above, the fields can be filled as follows:

- **Text For Number Of Pages**:
  `Page %CURRENT_PAGE% of %TOTAL_PAGES%`

- **Text For Current Page**:
  `%PAGE_NUMBER%`

- **Text For Page**:
  `%PAGE_NUMBER%`

- **Text For First Page**:
  `First`

- **Text For Last Page**:
  `Page %TOTAL_PAGES%`

- **Text For Previous Page**:
  `← Back`

- **Text For Next Page**:
  `Forward →`

- **Text For Previous …**:
  `…`

- **Text For Next …**:
  `…`

👉 As a result, visitors will see navigation similar to this:
```
← Back | First | 1 | 2 | 3 | … | Page 10 | Forward →
```

---

## Summary

Variables in WP-PageNavi are simple but provide flexibility in navigation customization:

- `%CURRENT_PAGE%` — current page
- `%TOTAL_PAGES%` — total pages
- `%PAGE_NUMBER%` — specific page number

For the first page, use `1`, and for the last page, use `%TOTAL_PAGES%`.

Thanks to these settings, you can make your website's navigation more intuitive and convenient for visitors.
