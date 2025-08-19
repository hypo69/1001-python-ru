"""
<BLKJAK>:
=================
Сложность: 7
-----------------
Блэкджек - это карточная игра, в которой игрок соревнуется с дилером. Цель игры - набрать 21 очко или как можно ближе к 21, но не превысить это значение. Карты с номерами приносят очки по своему номиналу, валет, дама и король - 10 очков, а туз - 1 или 11 очков, в зависимости от ситуации. Игрок играет против дилера. Игрок может взять ещё карту или остановиться. После того как игрок остановился, дилер берёт карты, пока его сумма не станет больше 16. Игрок побеждает, если сумма его карт больше чем у дилера, но меньше или равна 21.

Правила игры:
1.  Игрок и дилер получают по две карты. Одна из карт дилера открыта.
2.  Игрок смотрит на свои карты и решает, хочет ли он взять еще одну карту (HIT) или остановиться (STAND).
3.  Если сумма карт игрока больше 21, он проигрывает.
4.  Когда игрок останавливается, дилер начинает брать карты до тех пор, пока его сумма не станет больше 16.
5.  Если сумма карт дилера больше 21, он проигрывает, и игрок выигрывает.
6.  Если сумма карт дилера не превышает 21, сравниваются суммы карт игрока и дилера. Побеждает тот, у кого сумма ближе к 21, но не больше 21.
7.  При равенстве очков объявляется ничья (PUSH).
-----------------
Алгоритм:
1. Инициализация колоды: Создать колоду из 52 карт. Каждая карта имеет значение от 1 до 10 (валет, дама, король = 10, туз = 1 или 11).
2. Перемешать колоду.
3. Раздать по две карты игроку и дилеру. Одна карта дилера открыта, другая - закрыта.
4. Вывести на экран карты игрока и открытую карту дилера.
5. Игрок делает ход:
   5.1. Спросить у игрока, хочет ли он взять еще карту (HIT) или остановиться (STAND).
   5.2. Если игрок выбирает HIT, дать ему еще одну карту и перейти к шагу 5.3.
   5.3. Если сумма карт игрока больше 21, игрок проигрывает. Перейти к шагу 7.
   5.4. Если игрок выбирает STAND, перейти к шагу 6.
6. Ход дилера:
   6.1. Пока сумма карт дилера меньше или равна 16, дать ему еще одну карту.
   6.2. Если сумма карт дилера больше 21, дилер проигрывает, игрок выигрывает. Перейти к шагу 7.
7. Определение победителя:
   7.1. Сравнить суммы карт игрока и дилера.
   7.2. Если сумма карт игрока больше суммы карт дилера и не больше 21, игрок выигрывает.
   7.3. Если сумма карт дилера больше суммы карт игрока и не больше 21, дилер выигрывает.
   7.4. Если суммы равны, ничья.
8. Вывести результат игры.
9. Конец игры
-----------------
Блок-схема:
```mermaid
flowchart TD
    Start["Начало"] --> InitializeDeck["<p align='left'>Инициализация колоды: 
    <code><b>deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4</b></code></p>"]
    InitializeDeck --> ShuffleDeck["Перемешивание колоды: <code><b>random.shuffle(deck)</b></code>"]
    ShuffleDeck --> DealInitialCards["<p align='left'>Раздача карт:
    <code><b>
    playerHand = [deal_card(deck), deal_card(deck)]
    dealerHand = [deal_card(deck), deal_card(deck)]
    </b></code></p>"]
    DealInitialCards --> ShowHands["<p align='left'>Отображение карт игрока и одной карты дилера</p>"]
    ShowHands --> PlayerTurnStart{"Начало хода игрока"}
    PlayerTurnStart --> PlayerActionChoice{"Ввод действия игрока: HIT или STAND"}
    PlayerActionChoice -- HIT --> PlayerHit["<p align='left'>Игрок берет карту: <code><b>playerHand.append(deal_card(deck))</b></code></p>"]
    PlayerHit --> CalculatePlayerHandValue["<p align='left'>Вычисление суммы карт игрока: <code><b>player_value = calculate_hand_value(playerHand)</b></code></p>"]
    CalculatePlayerHandValue --> CheckPlayerBust{"<p align='left'>Проверка: <code><b>player_value > 21?</b></code></p>"}
    CheckPlayerBust -- Да --> PlayerBust["<p align='left'>Игрок проиграл: <code><b>print('Игрок проиграл!')</b></code></p>"]
    PlayerBust --> End["Конец"]
    CheckPlayerBust -- Нет --> PlayerTurnStart
    PlayerActionChoice -- STAND --> DealerTurnStart{"Начало хода дилера"}
    DealerTurnStart --> DealerHit{"<p align='left'>Дилер берет карту, пока <code><b>dealer_value <= 16</b></code></p>"}
    DealerHit --> CalculateDealerHandValue["<p align='left'>Вычисление суммы карт дилера: <code><b>dealer_value = calculate_hand_value(dealerHand)</b></code></p>"]
    CalculateDealerHandValue --> CheckDealerBust{"<p align='left'>Проверка: <code><b>dealer_value > 21?</b></code></p>"}
    CheckDealerBust -- Да --> DealerBust["<p align='left'>Дилер проиграл: <code><b>print('Дилер проиграл!')</b></code></p>"]
    DealerBust --> End
    CheckDealerBust -- Нет --> DetermineWinner["<p align='left'>Определение победителя и вывод результата</p>"]
    DetermineWinner --> End
    

```
**Legenda**
    Start - Начало игры.
    InitializeDeck - Инициализация колоды, создание списка карт (числовые значения и туз, повторенные 4 раза для каждой масти).
    ShuffleDeck - Перемешивание колоды в случайном порядке.
    DealInitialCards - Раздача начальных карт игроку и дилеру (по две карты каждому).
    ShowHands - Отображение карт игрока и одной открытой карты дилера.
    PlayerTurnStart - Начало хода игрока.
    PlayerActionChoice - Запрос действия игрока: HIT (взять карту) или STAND (остановиться).
    PlayerHit - Игрок берет еще одну карту из колоды.
    CalculatePlayerHandValue - Вычисление общей суммы очков карт игрока.
    CheckPlayerBust - Проверка, не превысила ли сумма очков игрока 21.
    PlayerBust - Вывод сообщения о проигрыше игрока, если сумма очков больше 21.
    DealerTurnStart - Начало хода дилера.
    DealerHit - Дилер берет карту, пока сумма очков его карт не превысит 16.
    CalculateDealerHandValue - Вычисление суммы очков карт дилера.
    CheckDealerBust - Проверка, не превысила ли сумма очков дилера 21.
    DealerBust - Вывод сообщения о проигрыше дилера, если сумма очков больше 21.
    DetermineWinner - Определение победителя путем сравнения очков игрока и дилера, вывод результата.
    End - Конец игры.
"""

import random

def deal_card(deck):
    """Выдает карту из колоды."""
    return deck.pop()

def calculate_hand_value(hand):
    """Вычисляет значение руки."""
    ace_count = hand.count(11) # Считаем количество тузов (11)
    total = sum(hand) # Считаем общую сумму очков

    # Если общая сумма больше 21 и есть туз, который можно посчитать как 1
    while total > 21 and ace_count > 0:
        total -= 10 #  Превращаем туз из 11 в 1
        ace_count -= 1
    return total


def display_cards(player_hand, dealer_hand, show_dealer_full=False):
  """Отображает карты игрока и дилера."""
  print("\nКарты дилера:")
  if show_dealer_full:
    print(" ".join(map(str, dealer_hand)), f"Сумма: {calculate_hand_value(dealer_hand)}")
  else:
    print("<закрытая карта> ", dealer_hand[1]) # Показываем первую карту дилера, вторая скрыта
  
  print("Карты игрока:", " ".join(map(str, player_hand)), f"Сумма: {calculate_hand_value(player_hand)}")
 
def play_blackjack():
    """Запускает игру в блэкджек."""
    # Создание колоды из 52 карт: числовые значения (2-10) и туз (11)
    deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4 
    random.shuffle(deck) # Перемешиваем колоду

    # Раздача карт игроку и дилеру (по 2 карты)
    player_hand = [deal_card(deck), deal_card(deck)] 
    dealer_hand = [deal_card(deck), deal_card(deck)]

    # Отображение карт (одна карта дилера скрыта)
    display_cards(player_hand, dealer_hand)
    
    # Ход игрока
    while True:
        player_value = calculate_hand_value(player_hand)
        if player_value == 21: # Если у игрока сразу 21
          print("Блэкджек! Вы выиграли!")
          return
        
        if player_value > 21: # Если игрок проиграл
          print("Перебор! Вы проиграли!")
          return

        action = input("Хотите взять еще карту? (HIT/STAND): ").upper()
        if action == "HIT":
            player_hand.append(deal_card(deck)) # Даем карту игроку
            display_cards(player_hand, dealer_hand)
        elif action == "STAND":
            break # Переходим к ходу дилера
        else:
            print("Некорректный ввод. Пожалуйста, введите HIT или STAND.")

    # Ход дилера
    print("\nХод дилера:")
    while calculate_hand_value(dealer_hand) <= 16:
        dealer_hand.append(deal_card(deck)) # Дилер берет карту
        
    display_cards(player_hand, dealer_hand, True) # показываем все карты дилера

    player_value = calculate_hand_value(player_hand) # Сумма игрока
    dealer_value = calculate_hand_value(dealer_hand) # Сумма дилера

    # Проверка условий победы
    if dealer_value > 21: # Если у дилера перебор
      print("Дилер перебрал! Вы выиграли!")
    elif player_value > dealer_value or dealer_value > 21: # Если у игрока больше очков
      print("Вы выиграли!")
    elif dealer_value > player_value : # Если у дилера больше очков
      print("Вы проиграли!")
    else:
        print("Ничья!") # Ничья


if __name__ == "__main__":
    play_blackjack() # Запуск игры

"""
Объяснение кода:
1.  **Импорт модуля `random`**:
   -  `import random`: Импортирует модуль `random`, который используется для генерации случайного порядка карт.
2.  **Функция `deal_card(deck)`**:
    -  `def deal_card(deck):`: Определяет функцию для взятия карты из колоды.
    -  `return deck.pop()`: Удаляет и возвращает последнюю карту из колоды.
3.  **Функция `calculate_hand_value(hand)`**:
    -   `def calculate_hand_value(hand):`: Определяет функцию для вычисления суммы очков карт.
    -   `ace_count = hand.count(11)`: Подсчитывает количество тузов в руке (туз = 11).
    -   `total = sum(hand)`: Вычисляет общую сумму очков карт.
    -   `while total > 21 and ace_count > 0`: Если сумма больше 21 и есть тузы.
    -   `total -= 10`:  Заменяет туз с 11 на 1.
    -   `ace_count -= 1`: Уменьшаем количество тузов.
    -   `return total`: Возвращает общую сумму очков.
4.  **Функция `display_cards(player_hand, dealer_hand, show_dealer_full=False)`**:
    -   `def display_cards(player_hand, dealer_hand, show_dealer_full=False):`: Определяет функцию для отображения карт.
    -  `show_dealer_full=False`: показывает только 1 карту дилера.
    -  Если `show_dealer_full=True`: показывает все карты дилера.
5.  **Функция `play_blackjack()`**:
    -  `def play_blackjack():`: Определяет функцию, содержащую основную логику игры.
    -  `deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11] * 4`: Создает колоду из 52 карт (числовые значения и туз).
    -  `random.shuffle(deck)`: Перемешивает колоду.
    -  `player_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты игроку.
    -  `dealer_hand = [deal_card(deck), deal_card(deck)]`: Раздает 2 карты дилеру.
    -  `display_cards(player_hand, dealer_hand)`: Отображает начальные карты.
    -   **Ход игрока**:
         -   `while True:`: Основной цикл хода игрока.
        - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.
        - `if player_value == 21:`: Проверка на блэкджек.
        - `if player_value > 21:`: Проверка на проигрыш игрока.
         -   `action = input("Хотите взять еще карту? (HIT/STAND): ").upper()`: Запрашивает действие игрока (HIT или STAND).
         -   `if action == "HIT":`: Если игрок выбирает HIT:
            -   `player_hand.append(deal_card(deck))`: Добавляет карту в руку игрока.
            -    `display_cards(player_hand, dealer_hand)`: Отображает карты.
         -   `elif action == "STAND":`: Если игрок выбирает STAND, переходит к ходу дилера.
    -   **Ход дилера**:
        -  `while calculate_hand_value(dealer_hand) <= 16:`: Дилер берет карту пока сумма меньше 16.
         -    `dealer_hand.append(deal_card(deck))`: Даем карту дилеру.
        -  `display_cards(player_hand, dealer_hand, True)`: Отображаем карты дилера.
     -    **Определение победителя**:
         - `player_value = calculate_hand_value(player_hand)`: Вычисляем сумму игрока.
         -`dealer_value = calculate_hand_value(dealer_hand)`: Вычисляем сумму дилера.
        - `if dealer_value > 21: `: Проверка на перебор у дилера.
        - `elif player_value > dealer_value or dealer_value > 21`: Проверка победы игрока.
        -`elif dealer_value > player_value`: Проверка победы дилера.
    -`if __name__ == "__main__":`: Запуск игры.
    -`play_blackjack()`: Вызов функции игры.
"""
