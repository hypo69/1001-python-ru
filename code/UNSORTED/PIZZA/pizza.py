"""
PIZZA:
=================
Сложность: 5
-----------------
Игра "Пицца" моделирует процесс заказа и доставки пиццы. Игрок должен ответить на ряд вопросов о количестве пицц, их стоимости, размере чаевых и т.д.  В конце программа выводит полную стоимость заказа, включая налог и чаевые.

Правила игры:
1. Программа запрашивает количество пицц.
2. Затем запрашивает стоимость каждой пиццы.
3. Далее запрашивает величину чаевых в процентах.
4. Вычисляется общая стоимость пицц.
5. Вычисляется налог (5% от общей стоимости).
6. Вычисляется сумма чаевых.
7. Выводится общая стоимость заказа, включая налог и чаевые.
-----------------
Алгоритм:
1. Ввести количество пицц (QUANTITY).
2. В цикле от 1 до QUANTITY:
   2.1. Ввести стоимость пиццы (COST).
   2.2. Увеличить общую стоимость пицц (TOTAL) на COST.
3. Ввести процент чаевых (TIP).
4. Вычислить налог (TAX) как 5% от TOTAL.
5. Вычислить сумму чаевых (TIP) как TIP% от TOTAL.
6. Вычислить полную стоимость заказа (GRAND) как TOTAL + TAX + TIP.
7. Вывести:
   7.1. Общую стоимость пицц (TOTAL).
   7.2. Налог (TAX).
   7.3. Сумму чаевых (TIP).
   7.4. Полную стоимость заказа (GRAND).
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InputQuantity["Ввод количества пицц: <code><b>quantity</b></code>"]
    InputQuantity --> InitializeTotal["<code><b>totalCost = 0</b></code>"]
    InitializeTotal --> LoopStart{"Начало цикла: для каждой пиццы"}
    LoopStart -- Да --> InputCost["Ввод стоимости пиццы: <code><b>pizzaCost</b></code>"]
    InputCost --> UpdateTotal["<code><b>totalCost = totalCost + pizzaCost</b></code>"]
    UpdateTotal --> LoopEnd{"Конец цикла: все пиццы обработаны"}
    LoopEnd -- Да --> InputTipPercent["Ввод процента чаевых: <code><b>tipPercent</b></code>"]
    LoopEnd -- Нет --> InputTipPercent
    InputTipPercent --> CalculateTax["<code><b>tax = totalCost * 0.05</b></code>"]
    CalculateTax --> CalculateTip["<code><b>tipAmount = totalCost * tipPercent / 100</b></code>"]
    CalculateTip --> CalculateGrandTotal["<code><b>grandTotal = totalCost + tax + tipAmount</b></code>"]
    CalculateGrandTotal --> OutputTotal["Вывод: <b>Общая стоимость пицц: <code>totalCost</code></b>"]
    OutputTotal --> OutputTax["Вывод: <b>Налог: <code>tax</code></b>"]
    OutputTax --> OutputTip["Вывод: <b>Чаевые: <code>tipAmount</code></b>"]
    OutputTip --> OutputGrandTotal["Вывод: <b>Полная стоимость заказа: <code>grandTotal</code></b>"]
    OutputGrandTotal --> End["Конец"]

```

Legenda:
    Start - Начало программы.
    InputQuantity - Запрос у пользователя количества пицц и сохранение значения в переменной quantity.
    InitializeTotal - Установка начального значения общей стоимости (totalCost) в 0.
    LoopStart - Начало цикла для ввода стоимости каждой пиццы.
    InputCost - Запрос у пользователя стоимости текущей пиццы и сохранение значения в переменной pizzaCost.
    UpdateTotal - Добавление стоимости текущей пиццы к общей стоимости (totalCost).
    LoopEnd - Конец цикла, проверяет, обработаны ли все пиццы.
    InputTipPercent - Запрос у пользователя процента чаевых и сохранение значения в переменной tipPercent.
    CalculateTax - Вычисление налога как 5% от общей стоимости (totalCost).
    CalculateTip - Вычисление суммы чаевых на основе введенного процента от общей стоимости (totalCost).
    CalculateGrandTotal - Вычисление полной стоимости заказа путем сложения общей стоимости, налога и чаевых.
    OutputTotal - Вывод общей стоимости пицц (totalCost).
    OutputTax - Вывод суммы налога (tax).
    OutputTip - Вывод суммы чаевых (tipAmount).
    OutputGrandTotal - Вывод полной стоимости заказа (grandTotal).
    End - Конец программы.
"""


# Запрашиваем у пользователя количество пицц
while True:
    try:
        quantity = int(input("Сколько пицц вы хотите заказать? "))
        if quantity > 0:
            break  # Выходим из цикла, если введено корректное значение
        else:
            print("Пожалуйста, введите положительное число.")
    except ValueError:
        print("Пожалуйста, введите целое число.")

# Инициализируем общую стоимость
totalCost = 0

# Цикл для ввода стоимости каждой пиццы
for i in range(quantity):
    while True:
        try:
           pizzaCost = float(input(f"Введите стоимость пиццы {i + 1}: "))
           if pizzaCost > 0:
                totalCost += pizzaCost # Добавляем стоимость пиццы к общей сумме
                break  # Выходим из цикла, если введено корректное значение
           else:
              print("Пожалуйста, введите положительную стоимость.")
        except ValueError:
           print("Пожалуйста, введите числовое значение.")


# Запрашиваем процент чаевых
while True:
    try:
        tipPercent = float(input("Какой процент чаевых вы хотите оставить? "))
        if 0 <= tipPercent <= 100:
            break  # Выходим из цикла, если процент в диапазоне от 0 до 100
        else:
            print("Пожалуйста, введите процент от 0 до 100.")
    except ValueError:
        print("Пожалуйста, введите числовое значение.")

# Вычисляем налог (5%)
tax = totalCost * 0.05
# Вычисляем сумму чаевых
tipAmount = totalCost * tipPercent / 100
# Вычисляем полную стоимость заказа
grandTotal = totalCost + tax + tipAmount

# Выводим результаты
print(f"Общая стоимость пицц: {totalCost:.2f}")
print(f"Налог: {tax:.2f}")
print(f"Чаевые: {tipAmount:.2f}")
print(f"Полная стоимость заказа: {grandTotal:.2f}")

"""
Объяснение кода:
1.  **Инициализация**:
    -   `totalCost = 0`: Инициализирует переменную `totalCost` для хранения общей стоимости всех пицц.
    -   Цикл `while True:`: используется для проверки ввода корректных данных от пользователя.
2.  **Ввод количества пицц**:
    -   `quantity = int(input("Сколько пицц вы хотите заказать? "))`: Запрашивает у пользователя количество пицц и сохраняет его в переменную `quantity`.
    -   Проверка на положительное число: проверяем, что количество пицц больше нуля, иначе просим ввести значение заново.
3.  **Цикл для ввода стоимости каждой пиццы**:
    -   `for i in range(quantity):`: Цикл выполняется `quantity` раз для каждой пиццы.
    -   `pizzaCost = float(input(f"Введите стоимость пиццы {i + 1}: "))`: Запрашивает стоимость каждой пиццы и сохраняет ее в переменной `pizzaCost`.
    -   `totalCost += pizzaCost`: Добавляет стоимость текущей пиццы к общей стоимости `totalCost`.
4. **Ввод процента чаевых**:
    -   `tipPercent = float(input("Какой процент чаевых вы хотите оставить? "))`: Запрашивает у пользователя процент чаевых.
    - Проверяем, что процент чаевых находится в диапазоне от 0 до 100, иначе просим ввести значение заново.
5.  **Расчеты**:
    -   `tax = totalCost * 0.05`: Вычисляет налог как 5% от общей стоимости.
    -   `tipAmount = totalCost * tipPercent / 100`: Вычисляет сумму чаевых.
    -   `grandTotal = totalCost + tax + tipAmount`: Вычисляет полную стоимость заказа, включая стоимость пицц, налог и чаевые.
6.  **Вывод результатов**:
    -   `print(f"Общая стоимость пицц: {totalCost:.2f}")`: Выводит общую стоимость пицц, форматированную до двух знаков после запятой.
    -   `print(f"Налог: {tax:.2f}")`: Выводит сумму налога.
    -   `print(f"Чаевые: {tipAmount:.2f}")`: Выводит сумму чаевых.
    -   `print(f"Полная стоимость заказа: {grandTotal:.2f}")`: Выводит полную стоимость заказа.
"""
