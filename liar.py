import random

# Class to represent a single player
class Player:
    def __init__(self, name, num_dice):
        self.name = name
        self.num_dice = num_dice
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]

    def roll_dice(self):
        """Roll the player's dice."""
        self.dice = [random.randint(1, 6) for _ in range(self.num_dice)]

    def show_dice(self):
        """Returns the dice the player has."""
        return self.dice

    def remove_die(self):
        """Remove one die from the player's dice pool."""
        if self.num_dice > 0:
            self.num_dice -= 1
            self.dice.pop(random.randint(0, len(self.dice) - 1))

    def give_die(self, other_player):
        """Give one die to the other player."""
        if self.num_dice > 0:
            self.num_dice -= 1
            other_player.num_dice += 1

# Class to represent the AI player
class AIPlayer(Player):
    def __init__(self, name, num_dice):
        super().__init__(name, num_dice)

    def make_decision(self, last_guess, last_player_dice_count, player_dice):
        """
        AI makes a decision to either:
        1) Raise the bid by either increasing the number of dice of the same value
        2) Raise by switching to a higher value (same count of dice)
        3) Call the previous player a liar if the guess seems unrealistic.
        """
        # Count the occurrences of each value in the current AI dice pool
        ai_dice_counts = {i: self.dice.count(i) for i in range(1, 7)}

        # Analyze the current guess
        guessed_value, guessed_count = last_guess

        # Consider the total number of dice in the game (AI's dice and player's dice)
        total_dice_in_game = self.num_dice + last_player_dice_count

        # Combine player and AI dice pools to see if the guessed number is reasonable
        total_guessed_dice = sum(1 for die in player_dice + self.dice if die == guessed_value)

        # If the guess is more than the total number of dice in the game, it's unrealistic
        if guessed_count > total_dice_in_game:
            return "LIAR"

        # Consider if the guess is reasonable based on both the player's and AI's dice
        if total_guessed_dice < guessed_count:
            return "LIAR"

        # If the AI has enough dice of the guessed value, it will raise the bid
        if guessed_count < self.num_dice:
            return "RAISE", (guessed_value, guessed_count + 1)

        # Otherwise, try to raise to a higher value if the AI has any of those dice
        for value in range(guessed_value + 1, 7):
            if ai_dice_counts.get(value, 0) > 0:
                return "RAISE", (value, guessed_count)

        # If there are no compelling reasons to raise, call LIAR
        return "LIAR"

# Function to simulate the game
def play_liars_dice():
    # Initialize game
    num_dice = 5
    player = Player("Player", num_dice)
    ai = AIPlayer("AI", num_dice)
    game_over = False
    last_guess = (1, 0)
    last_player_dice_count = 0

    round_num = 1  # Starting round number
    player_dice_lost = 0  # Track dice the player will lose in the next round
    ai_dice_lost = 0  # Track dice the AI will lose in the next round
    player_dice_won = 0  # Track dice the player will win in the next round
    ai_dice_won = 0  # Track dice the AI will win in the next round

    while not game_over:
        print(f"\n--- Round {round_num} ---")

        # Apply dice changes from the previous round before the new round starts
        player.num_dice -= player_dice_lost
        ai.num_dice -= ai_dice_lost
        player.num_dice += player_dice_won
        ai.num_dice += ai_dice_won

        # Update their dice pools immediately to reflect the changes
        player.dice = [random.randint(1, 6) for _ in range(player.num_dice)]
        ai.dice = [random.randint(1, 6) for _ in range(ai.num_dice)]

        # Reset dice lost/won trackers for the new round
        player_dice_lost = 0
        ai_dice_lost = 0
        player_dice_won = 0
        ai_dice_won = 0

        # Game continues until either player runs out of dice
        while not game_over:
            print(f"\n--- Round {round_num} ---")
            print(f"Player has {player.num_dice} dice.")
            print(f"AI has {ai.num_dice} dice (hidden).")

            # Player always starts the round
            print(f"Player's dice: {player.dice}")  # Show player's dice

            # Input validation for the guess value and count
            while True:
                try:
                    guess_value = int(input("Enter the value of the dice you are guessing (1-6): "))
                    if guess_value < 1 or guess_value > 6:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 6.")

            while True:
                try:
                    guess_count = int(input(f"How many {guess_value}s are there? Enter a number: "))
                    if guess_count < 1:
                        raise ValueError
                    break
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")

            last_guess = (guess_value, guess_count)
            last_player_dice_count = player.num_dice

            # AI's decision based on the last guess
            ai_decision = ai.make_decision(last_guess, last_player_dice_count, player.dice)
            print(f"AI's decision: {ai_decision}")

            if ai_decision == "LIAR":
                print(f"AI calls you a liar! Let's reveal the dice...")

                # Count total number of guessed dice
                total_dice = player.dice + ai.dice
                actual_count = sum(1 for die in total_dice if die == guess_value)

                print(f"Player's dice: {player.dice}")
                print(f"AI's dice: {ai.dice}")
                if actual_count < guess_count:
                    print("You were the liar! You lose a die!")
                    player_dice_lost += 1
                    ai_dice_won += 1  # AI wins a die
                else:
                    print("The AI was the liar! The AI loses a die.")
                    ai_dice_lost += 1
                    player_dice_won += 1  # Player wins a die
                # End the round after the liar call
                break
            else:
                action, new_guess = ai_decision
                if action == "RAISE":
                    guess_value, guess_count = new_guess
                    print(f"AI raises the bid to {guess_count} {guess_value}s.")

                    # Now the player must decide whether to call the AI a liar
                    player_decision = input(f"Do you call AI a liar (yes/no)? ").strip().lower()

                    if player_decision == "yes":
                        print(f"Player calls AI a liar! Let's reveal the dice...")

                        # Count total number of guessed dice
                        total_dice = player.dice + ai.dice
                        actual_count = sum(1 for die in total_dice if die == guess_value)

                        print(f"Player's dice: {player.dice}")
                        print(f"AI's dice: {ai.dice}")
                        if actual_count < guess_count:
                            print("AI was the liar! AI loses a die.")
                            ai_dice_lost += 1
                            player_dice_won += 1  # Player wins a die
                        else:
                            print("Player was the liar! You lose a die.")
                            player_dice_lost += 1
                            ai_dice_won += 1  # AI wins a die
                        # End the round after the liar call
                        break
                    else:
                        print(f"Player accepts the guess. The round continues.")

            # Check if either player is out of dice
            if player.num_dice == 0:
                print("Player has no dice left. AI wins!")
                game_over = True
                break
            elif ai.num_dice == 0:
                print("AI has no dice left. Player wins!")
                game_over = True
                break

        round_num += 1  # Increment the round number

if __name__ == "__main__":
    play_liars_dice()
