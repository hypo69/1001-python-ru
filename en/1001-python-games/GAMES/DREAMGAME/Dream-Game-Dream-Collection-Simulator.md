Author of the original code:
https://github.com/Mstislav95/CashFlow_101/blob/main/CashFlow_model.ipynb

https://ok4u.club/cashflow101-rules/

https://www.youtube.com/watch?v=sG_RWsvYT7k&ab_channel=MstislavEfimov


# Dream Game: Dream Collection Simulator

## Description

Simulation of a game in which the player moves around the game board, rolling two six-sided dice.
On some cells of the board are "dreams" that the player can "collect".
The goal of the game is to understand which "dreams" are most likely to be collected under the given rules.

## Game rules

1.  The player starts the game at the initial position (assume it is 0).
2.  In one turn, the player rolls two six-sided dice and moves a number of cells equal to the sum of the rolled values.
3.  The game board has 48 cells. If the player moves beyond the 48th cell, they return to the beginning, "looping" around the board (for example, if the current position is 47 and a 4 is rolled, the new position will be 3).
4.  On some cells (specified in the `dream_numbers` list) are "dreams".
5.  If the player lands on a cell with a "dream" and has not yet visited it in the current iteration, the "dream" is considered collected.
6.  The game continues for a specified number of moves (`moves`).
7.  The game is simulated a specified number of times (`num_iterations`).
8.  As a result of the program, the frequency of collecting each "dream" and the probability of its collection are calculated.

## Code features

*   **Modeling**: The code simulates the player's movement on the game board using dice rolls.
*   **Collecting "Dreams"**: The code tracks when the player lands on cells with "dreams" and counts their number.
*   **Analysis**: The program analyzes the simulation results and calculates the frequency and probability of collecting each "dream".
*   **`DreamGame` class**: The code is encapsulated in the `DreamGame` class, which makes it more structured and reusable.
*   **Generating dream names**: "Dream" names are generated using the Gemini model, which makes each game unique.
*   **Optimization**: The code is optimized using `collections.Counter` for counting frequencies and generators for iterating through simulations.

## Capabilities

*   **Parameter customization**: You can easily customize the number of moves per game (`moves`) and the number of game simulations (`num_iterations`).
*   **Dynamic names**: "Dream" names are generated dynamically using the Gemini model, which adds variety to the game.
*   **Probability analysis**: Obtaining the probability of collecting each "dream" allows you to analyze and compare their availability.
*   **Extensibility**: The code is easily extensible and can be modified to add new game mechanics.

## Code breakdown

### `DreamGame` class

The `DreamGame` class encapsulates all game logic.

#### `__init__(self, dream_numbers: List[int], moves: int = 3, num_iterations: int = 100_000)`

Class constructor that initializes the game:

*   `dream_numbers`: List of numbers representing "dream" positions.
*   `moves`: Number of moves per game.
*   `num_iterations`: Number of game simulations.
*   `self.dreams`: Dictionary mapping dream numbers to their names. Populated using `_generate_dream_names`.

#### `_generate_dream_names(self) -> None`

Method that generates "dream" names using the Gemini model.

*   Forms a request to the Gemini model to generate a specified number of unique "dream" names.
*   Processes the response and creates a `self.dreams` dictionary, mapping "dream" numbers to their names.
*   Raises an error if the model does not return text or cannot generate the required number of names.

#### `_simulate_game(self) -> Counter[str]`

Method that simulates one game:

*   Initializes a `dreams_frequency` counter to track the frequency of "dream" collection.
*   Initializes the `square` variable, representing the player's current position on the board, and `visited_dreams` to track collected dreams.
*   Performs a specified number of moves (`moves`), moving the player around the game board.
*   If the player lands on a cell with a "dream" and has not yet visited it, increments the counter for that "dream".
*   Returns a `Counter` object with the frequency of "dream" collection.

#### `run_experiment(self) -> pd.DataFrame`

Method that runs the game simulation multiple times and returns a DataFrame with the results:

*   Runs the game simulation a specified number of times (`num_iterations`).
*   Sums the frequencies of "dream" collection from each simulation.
*   Converts the results to a DataFrame, where columns are "Dream" and "Frequency".
*   Sorts the DataFrame by frequency in descending order.
*   Adds a "Probability" column, calculated as the ratio of "Frequency" to the total number of simulations.
*   Returns a DataFrame with the results.

### Usage

At the end of the script, an instance of the `DreamGame` class is created and the experiment is run. The result is printed to the screen as a DataFrame.

```python
if __name__ == '__main__':
    dream_numbers = [1, 3, 5, 7, 10, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47]
    game = DreamGame(dream_numbers, moves=3, num_iterations=10_000)
    df_result = game.run_experiment()
    print(df_result)
```

## Requirements

*   Python 3.6+
*   Libraries: `pandas`, `google-generativeai`
*   Environment variable `GOOGLE_API_KEY` with your Gemini API key

## Installation

1.  Install Python 3.6+
2.  Install libraries: `pip install pandas google-generativeai`
3.  Set environment variable `GOOGLE_API_KEY` with your Gemini API key.
4.  Run the script `python your_script_name.py`

## Usage examples
```python
    dream_numbers = [2,4,8,16,32,44]
    game = DreamGame(dream_numbers, moves=5, num_iterations=1000)
    df_result = game.run_experiment()
    print(df_result)
```
In this example:
 * A game object is created
 * 10,000 games are simulated with three moves
 * The simulation result is displayed as a pandas DataFrame.

```python
    dream_numbers = [2,4,8,16,32,44]
    game = DreamGame(dream_numbers, moves=5, num_iterations=1000)
    df_result = game.run_experiment()
    print(df_result)
```
In this example:
 * A game object is created with different dream numbers
 * 1000 games are simulated with five moves
 * The simulation result is displayed as a pandas DataFrame.

## License

MIT
