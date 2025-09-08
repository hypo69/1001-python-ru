# Guide complet des variables dans WP-PageNavi pour WordPress

La navigation par pages est une partie importante de tout blog ou site d'actualités WordPress. L'un des outils les plus populaires pour une navigation paginée pratique est le plugin **WP-PageNavi**. Il permet de remplacer les liens standard « Précédent / Suivant » par une pagination plus flexible et esthétique.

L'une des fonctionnalités clés est la personnalisation du texte des liens via des **variables**, qui insèrent automatiquement le numéro de page actuel, le nombre total de pages et d'autres informations.

Dans cet article, nous allons examiner **toutes les variables disponibles**, des exemples de leur utilisation et montrerons avec des captures d'écran où les insérer.

---

## Où trouver les paramètres de WP-PageNavi

Après l'installation du plugin, allez dans l'administration de WordPress :

**Réglages → PageNavi**

Vous y verrez un menu pour configurer le texte des liens (exemple dans la capture d'écran ci-dessous) :

![Paramètres PageNavi dans WordPress](https://raw.githubusercontent.com/hypo69/1001-python-ru/master/ru/assets/wordpress-pagenavi-guide/a34df3db-dcb3-4815-ac1c-a73c693fce39.png)

👉 Dans chaque champ, vous pouvez utiliser des variables pour afficher dynamiquement la page actuelle, le nombre total de pages et d'autres éléments de navigation.

---

## Variables disponibles dans WP-PageNavi

Le plugin fournit un ensemble de placeholders (variables de modèle) qui peuvent être utilisés dans les paramètres :

### 🔹 %CURRENT_PAGE%
Affiche le **numéro de la page actuelle**.

Exemple :
```

Vous êtes sur la page %CURRENT\_PAGE%

```
👉 Si vous êtes sur la page 3, le résultat sera :
```

Vous êtes sur la page 3

```

---

### 🔹 %TOTAL_PAGES%
Affiche le **nombre total de pages**.

Exemple :
```

Nombre total de pages : %TOTAL\_PAGES%

```
👉 S'il y a 10 pages au total, la sortie sera :
```

Nombre total de pages : 10

```

---

### 🔹 %PAGE_NUMBER%
Utilisé pour afficher le **numéro de chaque page** dans la liste.

Exemple :
```

Page %PAGE\_NUMBER%

```
👉 La navigation affichera des liens :
```

Page 1 | Page 2 | Page 3 | ...

```

---

## Tableau des variables WP-PageNavi

| Variable           | Description                               | Exemple de configuration                   | Résultat (si 3ème page sur 10)       |
|--------------------|-------------------------------------------|--------------------------------------------|--------------------------------------|
| **%CURRENT_PAGE%** | Numéro de la page actuelle                | `Vous êtes actuellement sur la page %CURRENT_PAGE%` | `Vous êtes actuellement sur la page 3` |
| **%TOTAL_PAGES%**  | Nombre total de pages                     | `Nombre total de pages : %TOTAL_PAGES%`    | `Nombre total de pages : 10`         |
| **%PAGE_NUMBER%**  | Numéro de chaque page dans la liste       | `Page %PAGE_NUMBER%`                       | `Page 1 | Page 2 | Page 3 …`         |
| **1 (statique)**   | Première page (pas de variable)           | `Première` ou `Page 1`                     | `Première`                           |
| **%TOTAL_PAGES%**  | Dernière page                             | `Page %TOTAL_PAGES%`                       | `Page 10`                            |
| **← / → / …**      | Symboles pour les flèches et abréviations | `← Précédent`, `Suivant →`, `…`            | `← Précédent | 1 | 2 | 3 | … | 10 | Suivant →` |

---

## Exemple de configuration complète

Dans la capture d'écran ci-dessus, vous pouvez remplir les champs comme suit :

- **Text For Number Of Pages**:
  `Page %CURRENT_PAGE% sur %TOTAL_PAGES%`

- **Text For Current Page**:
  `%PAGE_NUMBER%`

- **Text For Page**:
  `%PAGE_NUMBER%`

- **Text For First Page**:
  `Première`

- **Text For Last Page**:
  `Page %TOTAL_PAGES%`

- **Text For Previous Page**:
  `← Précédent`

- **Text For Next Page**:
  `Suivant →`

- **Text For Previous …**:
  `…`

- **Text For Next …**:
  `…`

👉 En fin de compte, les visiteurs verront une navigation similaire à celle-ci :
```

← Précédent | Première | 1 | 2 | 3 | … | Page 10 | Suivant →

```

---

## Résumé

Les variables dans WP-PageNavi sont simples, mais offrent une flexibilité dans la configuration de la navigation :

- `%CURRENT_PAGE%` — page actuelle
- `%TOTAL_PAGES%` — nombre total de pages
- `%PAGE_NUMBER%` — numéro de page spécifique

Pour la première page, utilisez `1`, et pour la dernière, utilisez `%TOTAL_PAGES%`.

Grâce à ces paramètres, vous pouvez rendre la navigation de votre site plus claire et plus pratique pour les visiteurs.
