Inside the `game` directory, using the context from the file @life.py, create a file with tests `test_life.py`. Use the pytest framework.

The test should check the correct evolution of a simple "Blinker" oscillator (three cells in a row).

Test scenario:
1.  Import the `Game` class from `life`.
2.  Create a test function, e.g., `test_blinker_oscillation`.
3.  Inside the test, create a `Game` instance with a fixed size (e.g., 5x5).
4.  Manually set the initial state of the field so that there is a horizontal line of three living cells (Blinker) in the center.
5.  Call the `game.step()` method.
6.  Using `assert` and `numpy.array_equal`, check that the field has changed to a vertical line of three cells.
7.  Call the `game.step()` method again.
8.  Check that the field has returned to its original horizontal state.