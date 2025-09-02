Using lists and dictionaries to represent product data. I will break down an abstract product by characteristics and show how to use a list to represent products in a category.

*   **Dictionary (`dict`)** – is an ideal way to represent the *characteristics* of a single product, where there are "key-value" pairs.
*   **List (`list`)** – is an excellent way to represent a *set* of similar products, where each product can be represented by a dictionary.

**1. Dictionary (`dict`) to represent product characteristics**

A dictionary to represent the characteristics of a single product. In this case, the keys of the dictionary will be the names of the characteristics, and the values will be their corresponding values.

```python
product = {
    "id": "12345",
    "name": "Smartphone SuperPhone X",
    "brand": "SuperTech",
    "price": 999.99,
    "color": "Space Gray",
    "screen_size": 6.7,
    "storage": "256 GB",
    "camera": "108 MP",
    "os": "Android 13",
    "available": True
}

print("--- Product Characteristics ---")
for key, value in product.items():
    print(f"{key}: {value}")

print("\n--- Accessing specific characteristics ---")
print(f"Name: {product['name']}")
print(f"Price: ${product['price']}")
print(f"Available: {'Yes' if product['available'] else 'No'}")

```

**Code explanation:**

*   `product` dictionary, where the keys are the names of the product characteristics (id, name, brand, price, etc.), and the values are their corresponding values.
*   `product.items()` to iterate over all "key-value" pairs and print them to the screen.

**2. List (`list`) to represent products in a category**

A list to represent a list of products in a specific category.
In this case, each element of the list will represent a separate product, which, in turn, can be represented by a dictionary.

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
        "name": "Tablet TabPro S",
        "brand": "TechGenius",
        "price": 799.99,
        "available": False
    },
    {
        "id": "13579",
        "name": "Headphones SoundBeats Pro",
        "brand": "AudioMax",
        "price": 199.99,
        "available": True
    }
]
print("\n--- List of products in category ---")

for product in products:
   print(f"{product['name']} ({product['brand']}), Price: ${product['price']}, Available: {'Yes' if product['available'] else 'No'}")

print("\n--- Accessing the first product ---")

first_product = products[0]
print(f"ID: {first_product['id']}, Name: {first_product['name']}")

print("\n--- Displaying only product names ---")
for product in products:
  print(f"Name: {product['name']}")
```

**Code explanation:**

*   The `products` list, where each element is a dictionary representing a separate product.
*   I iterated through the list and displayed information about each product, using dictionary keys to access product characteristics.
*   I showed how to access the first product in the list using index `0`.
*   I iterated through the list again, and showed how to display only product names.


```