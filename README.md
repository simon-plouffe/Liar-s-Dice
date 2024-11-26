# Liar's Dice with smart AI
#### Video Demo:  <https://youtu.be/4Doi7zIGb7g?si=Uhz_Ef1o7Qkiu8zT>
#### Description:
This Python project simulates a classic game of Liar's Dice, which involves bluffing and strategy. The game is played between two participants: a human player and an AI (artificial intelligence) player. The core objective is to guess how many dice of a particular value are present across all players’ dice, with the option to call the opponent a liar if the guess seems unreasonable. Each player has a set of dice, and through each round, they either raise the bid, change the guessed value, or challenge the previous player’s guess, all while trying to outsmart the opponent.
How does it work? Liar's Dice is a dice game that involves bluffing and deduction. Each player starts with a set of dice (in this case, five dice each), and they take turns making a "guess" about the total number of dice showing a particular value (1 through 6) across all players' dice. For example, one might guess, "There are three 4s among all the dice." The other player then has the option to either accept the bid, raise the bid (either by increasing the number of dice or by switchng to a higher value), or call the first player a liar. If the liar call is correct (i.e., the actual count of dice with the guessed value is lower than the bid), the player who made the false guess loses a die. If the liar call is incorrect, the challenger loses a die instead. The game continues until one player has no dice left, and the other is declared the winner.

The **Player class** represent a single participant in the game. Each player has a name, a set number of dice (initialized to 5), and a collection of dice values that are represented as a list of random integers between 1 and 6. Players can roll their dice (changing the dice values), show their dice (to display the dice they have), and perform actions like removing dice or transferring dice between players.

The key methods of the Player class are:
- **`__init__()`**: Initializes the player with a name and a number of dice. It also generates a list of random dice values.
- **`roll_dice()`**: Re-rolls all of the players dice, generating new random values for each.
- **`show_dice()`**: Returns a list of the dice the player currently holds.
- **`remove_die()`**: Removes a die from the players dice pool.
- **`give_die()`**: Transfers a die from one player to another.

The **AIPlayer class** extends the basic Player class, adding decision-making logic to simulate an intelligent opponent. The AI can analyze the current game state and make one of three decisions:
1. **Raise the bid**: The AI may increase the number of dice of the guessed value if it holds enough dice of that value.
2. **Switch the guessed value**: If the AI does not have enough dice of the current value, it may decide to raise the bid using a higher value (e.g., switching from guessing 3 dice showing "4" to guessing 2 dice showing "5").
3. **Call the previous player a liar**: If the AI believes the previous bid is too high based on the total dice in the game, it may challenge the guess by calling the player a liar.

The decision-making process involves:
- Analyzing the current guessed value and the number of dice guessed.
- Counting how many dice of the guessed value exist in both the AI's and the player's dice pools.
- Considering the total number of dice in the game (the sum of both the player’s and AI’s dice).
- If the guess is unrealistic, the AI calls the previous player a liar.
- If the AI has enough dice of the guessed value, it raises the bid by increasing the count.
- If the AI doesn't have enough dice, it may switch to a higher value or call the player a liar.

The AI’s logic adds a challenging dynamic to the game, forcing the player to make strategic decisions and try to outguess the AI. It is challenging to beat the AI witch makes it fun and engaging to keep going.

The **play_liars_dice() function** simulates the flow of the game. At the start of the game, both the player and the AI are given five dice each. The game proceeds in a loop, with each round consisting of a series of events:
1. The player makes a guess about the total number of dice showing a certain value.
2. The AI evaluates the guess and makes a decision to either raise the bid, switch to a higher value, or call the player a liar.
3. If the AI calls the player a liar, the game reveals the dice, and the liar is penalized by losing a die. Conversely, if the player calls the AI a liar, the same process occurs.
4. After each round, dice are updated: dice are either lost or won based on the outcome of the liar call.

The game ends when one player runs out of dice. If the player has no dice left, the AI wins. If the AI has no dice left, the player wins. The loop continues until eithre player loses all their dice, and the winner has all the 10 dices.

The AI’s decision-making introduces a stratgic layer to the game. It doesn’t just blindly raise the bid or call the player a liar but carefully analyzes the game state. The AI can bluff, deceive, or call the player’s bluff, making the game engaging and challenging. The player must carefully evaluate the AI’s behavior and anticipate its moves to stay competitive. its a game of luck but the AI makes all the right decision to keep you guessing. i truly love playing against it.

In conclusion, this Python project simulates Liar's Dice, combining randomness (from the dice rolls) with strategy and bluffing. The AI player makes decisions based on its dice pool and the current game state, adding an intelligent adversary for the human player to face. The game provides an opportunity to engage in a fun bluffing game, where both players use deduction and strategy to outsmart each other. The project demonstrates how artificial intelligence can be applied in simple games to create challenging and interactive experiences. Anyway hope you enjoy. Been a pleasure experimenting my first CS50 course.

TODO
python liar.py
