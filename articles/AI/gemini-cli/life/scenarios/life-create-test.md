Внутри директории `game` используя контекст из файла @life.py, создай файл с тестами test_life.py. Используй фреймворк pytest.

Тест должен проверять правильность эволюции простого осциллятора "Блинкер" (три клетки в ряд).

Сценарий теста:
1.  Импортируй класс `Game` из `life`.
2.  Создай функцию теста, например `test_blinker_oscillation`.
3.  Внутри теста создай экземпляр `Game` с фиксированным размером (например, 5x5).
4.  Вручную установи начальное состояние поля так, чтобы в центре была горизонтальная линия из трех живых клеток (Блинкер).
5.  Вызови метод `game.step()`.
6.  С помощью `assert` и `numpy.array_equal` проверь, что поле изменилось на вертикальную линию из трех клеток.
7.  Вызови метод `game.step()` еще раз.
8.  Проверь, что поле вернулось в исходное горизонтальное состояние.