Utilisation des listes et des dictionnaires pour représenter les données de produits. Je vais décomposer un produit abstrait par ses caractéristiques et montrer comment utiliser une liste pour représenter les produits d'une catégorie.

*   **Dictionnaire (`dict`)** – est un moyen idéal de représenter les *caractéristiques* d'un seul produit, où il y a des paires "clé-valeur".
*   **Liste (`list`)** – est un excellent moyen de représenter un *ensemble* de produits similaires, où chaque produit peut être représenté par un dictionnaire.

**1. Dictionnaire (`dict`) pour représenter les caractéristiques d'un produit**

Un dictionnaire pour représenter les caractéristiques d'un seul produit. Dans ce cas, les clés du dictionnaire seront les noms des caractéristiques, et les valeurs – leurs valeurs correspondantes.

```python
product = {
    "id": "12345",
    "name": "Smartphone SuperPhone X",
    "brand": "SuperTech",
    "price": 999.99,
    "color": "Gris sidéral",
    "screen_size": 6.7,
    "storage": "256 Go",
    "camera": "108 MP",
    "os": "Android 13",
    "available": True
}

print("--- Caractéristiques du produit ---")
for key, value in product.items():
    print(f"{key}: {value}")

print("\n--- Accès aux caractéristiques spécifiques ---")
print(f"Nom : {product['name']}")
print(f"Prix : ${product['price']}")
print(f"Disponible : {'Oui' if product['available'] else 'Non'}")

```

**Explication du code :**

*   dictionnaire `product`, où les clés sont les noms des caractéristiques du produit (id, nom, marque, prix, etc.), et les valeurs — leurs valeurs correspondantes.
*   `product.items()` pour itérer sur toutes les paires "clé-valeur" et les afficher à l'écran.

**2. Liste (`list`) pour représenter les produits d'une catégorie**

Une liste pour représenter une liste de produits dans une catégorie spécifique.
Dans ce cas, chaque élément de la liste représentera un produit distinct, qui, à son tour, peut être représenté par un dictionnaire.

```python
products = [
    {
        "id": "12345",
        "name": "Smartphone SuperPhone X",
        "brand": "SuperTech",
        "price": 999.99,
        "available": True
    },
    {
        "id": "67890",
        "name": "Tablette TabPro S",
        "brand": "TechGenius",
        "price": 799.99,
        "available": False
    },
    {
        "id": "13579",
        "name": "Casque SoundBeats Pro",
        "brand": "AudioMax",
        "price": 199.99,
        "available": True
    }
]
print("\n--- Liste des produits par catégorie ---")

for product in products:
   print(f"{product['name']} ({product['brand']}), Prix : ${product['price']}, Disponible : {'Oui' if product['available'] else 'Non'}")

print("\n--- Accès au premier produit ---")

first_product = products[0]
print(f"ID : {first_product['id']}, Nom : {first_product['name']}")

print("\n--- Affichage uniquement des noms de produits ---")
for product in products:
  print(f"Nom : {product['name']}")
```

**Explication du code :**

*   La liste `products`, où chaque élément est un dictionnaire représentant un produit distinct.
*   J'ai itéré sur la liste et affiché les informations sur chaque produit, en utilisant les clés du dictionnaire pour accéder aux caractéristiques du produit.
*   J'ai montré comment accéder au premier produit de la liste en utilisant l'index `0`.
*   J'ai itéré à nouveau sur la liste et montré comment afficher uniquement les noms des produits.


