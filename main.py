from game import Player, play_game, load_game
from card_data import cards
import random

def main():
    filename = "savegame.pkl"

    while True:
        print("\n=== FUT-CARD GAME ===")
        print("1. Start New Game (vs Bot)")
        print("2. Start New Game (vs Real Player)")
        print("3. Load Saved Game")
        print("4. Exit")

        choice = input("Your Choice: ").strip()

        if choice in ["1", "2"]:
            is_bot = choice == "1"
            deck = cards[:]  # copy the list
            random.shuffle(deck)
            player = Player("Player 1")
            opponent = Player("Bot" if is_bot else "Player 2")
            player.draw_cards(deck, 5)
            opponent.draw_cards(deck, 5)
            play_game(player, opponent, deck, filename, is_bot)

        elif choice == "3":
            player, opponent, deck, is_bot = load_game(filename)
            if player and opponent and deck:
                play_game(player, opponent, deck, filename, is_bot=is_bot)
            else:
                print("❌ Save not found. Please start a new game first.")

        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice! Please enter 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()

