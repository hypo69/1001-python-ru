### Game Name: **Acey-Ducey Card Game**

#### Description
This is a simulation of the Acey-Ducey card game. The player places bets based on the probability that the next card will fall between two already open cards.

- **Starting Capital:** The player starts with $100.
- **Game Rules:**
  1. The computer deals two cards.
  2. The player can decide whether to place a bet or not.
  3. If a bet is placed, a third card is drawn.
  4. If the value of the third card falls between the first two cards, the player wins the bet. Otherwise, the bet is lost.
- The game ends when the player loses all capital or manually ends it.

#### Implementation

**Input Data:**
- User input for:
  - Initial bet size.
  - Decision to place a bet or skip.

**Output Data:**
- Message about the player's current capital.
- Information about bet results (win/loss).
- Card status in each round.

#### Step-by-step instructions for implementation:

1. **Game Initialization**:
   - Set the player's starting capital ($100).
   - Announce game rules.

2. **Main Game Loop**:
   - Generate two random cards (range 2–14, where 11 = Jack, 12 = Queen, 13 = King, 14 = Ace).
   - Display cards to the player.
   - Request a bet (can skip the round by betting 0).
   - Check: the bet must not exceed the current capital.

3. **Round Result**:
   - Generate a third card.
   - Check if its value falls within the range between the first two cards.
   - Change player's capital depending on the result.

4. **Game End**:
   - If the player's capital is 0, the game ends with an appropriate message.
   - Offer the player to start a new game or exit.

#### Limitations
- All cards are unique within a single round.
- Support for basic game functionality without complex visual effects.
