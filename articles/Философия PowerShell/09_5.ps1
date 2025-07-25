# Имитируем ответ от API
$jsonResponse = '{
    "product": "Laptop",
    "inventory": {
        "stock": 42,
        "locations": ["Warehouse A", "Store 5"]
    },
    "tags": ["electronics", "sale"]
}'

# Парсим JSON
$productObject = $jsonResponse | ConvertFrom-Json

# Теперь мы можем легко работать с данными как с обычным объектом
Write-Host "На складе осталось $($productObject.inventory.stock) единиц товара '$($productObject.product)'."
Write-Host "Товар находится на складе: $($productObject.inventory.locations[0])"