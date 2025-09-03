import random

# Инициализация колоды карт
def create_deck():
    ranks = list(range(2, 15))  # Карты от 2 до 14 (туз = 14)
    deck = ranks * 4  # 4 масти
    random.shuffle(deck)
    return deck

# Вывод карты в читаемом формате
def card_name(value):
    if value == 11:
        return "Валет"
    elif value == 12:
        return "Дама"
    elif value == 13:
        return "Король"
    elif value == 14:
        return "Туз"
    else:
        return str(value)

# Основной игровой цикл
def play_acey_ducey():
    print("Добро пожаловать в игру Acey Ducey!")
    print("Правила: Делаете ставку, угадывая, будет ли следующая карта между двумя выложенными.")
    print("Если карта равна одной из выложенных или туз, вы проигрываете.")
    print("Введите '0', чтобы пропустить ход.\n")

    money = 100  # Стартовый капитал игрока
    deck = create_deck()

    while money > 0 and len(deck) >= 3:
        print(f"Ваш текущий баланс: ${money}")

        # Выкладываем две карты
        card1 = deck.pop()
        card2 = deck.pop()
        while card1 == card2:  # Если карты одинаковые, берем новые
            deck.insert(0, card1)
            deck.insert(0, card2)
            card1 = deck.pop()
            card2 = deck.pop()

        print(f"Первая карта: {card_name(card1)}")
        print(f"Вторая карта: {card_name(card2)}")

        # Определяем диапазон
        low_card = min(card1, card2)
        high_card = max(card1, card2)

        # Делаем ставку или пропускаем ход
        try:
            bet = int(input(f"Сделайте ставку (от 0 до {money}) или введите '0' для пропуска хода: "))
            if bet < 0 or bet > money:
                print("Неверная ставка. Попробуйте снова.")
                continue
            if bet == 0:
                print("Вы пропустили ход.\n")
                continue  # Пропускаем ход
        except ValueError:
            print("Пожалуйста, введите число.")
            continue

        # Вытягиваем следующую карту
        next_card = deck.pop()
        print(f"Следующая карта: {card_name(next_card)}")

        # Проверяем результат
        if next_card == card1 or next_card == card2 or next_card == 14:
            print("Вы проиграли!")
            money -= bet
        elif low_card < next_card < high_card:
            print("Вы выиграли!")
            money += bet
        else:
            print("Вы проиграли!")
            money -= bet

        print()

    # Завершение игры
    if money <= 0:
        print("У вас закончились деньги. Игра окончена.")
    else:
        print(f"Игра окончена. Ваш итоговый баланс: ${money}")

# Запуск игры
if __name__ == "__main__":
    play_acey_ducey()