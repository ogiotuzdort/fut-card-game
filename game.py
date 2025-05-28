import random
import pickle

class Card:
    def __init__(self, name, pas, shot, fin, speed, defense, endurance):
        self.name = name
        self.pas = pas
        self.shot = shot
        self.fin = fin
        self.speed = speed
        self.defense = defense
        self.endurance = endurance

    def __str__(self):
        return (f"{self.name}: PASS={self.pas}, SHOT={self.shot}, FIN={self.fin}, "
                f"SPEED={self.speed}, DEF={self.defense}, END={self.endurance}")

    def to_dict(self):
        return {
            'name': self.name,
            'pas': self.pas,
            'shot': self.shot,
            'fin': self.fin,
            'speed': self.speed,
            'defense': self.defense,
            'endurance': self.endurance
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data['name'],
            data['pas'],
            data['shot'],
            data['fin'],
            data['speed'],
            data['defense'],
            data['endurance']
        )


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw_cards(self, deck, number=5):
        for _ in range(number):
            if deck:
                card = deck.pop()
                self.hand.append(card)

    def remove_card(self, card):
        self.hand.remove(card)

    def has_cards(self):
        return len(self.hand) > 0

    def total_cards(self):
        return len(self.hand)


def display_hand(player):
    print(f"\n{player.name}'s Cards:")
    for idx, card in enumerate(player.hand):
        print(f"{idx + 1}. {card}")


def choose_stat():
    stats = ["pass", "shot", "fin", "speed", "def", "end", "all"]
    while True:
        choice = input("Choose a stat to compare (pass, shot, fin, speed, def, end, all): ").strip().lower()
        if choice in stats:
            return choice
        print("Invalid choice. Try again.")


def compare_cards(card1, card2, stat):
    attr_map = {
        "pass": "pas",
        "shot": "shot",
        "fin": "fin",
        "speed": "speed",
        "def": "defense",
        "end": "endurance"
    }

    if stat == "all":
        total1 = card1.pas + card1.shot + card1.fin + card1.speed + card1.defense + card1.endurance
        total2 = card2.pas + card2.shot + card2.fin + card2.speed + card2.defense + card2.endurance
    else:
        total1 = getattr(card1, attr_map[stat])
        total2 = getattr(card2, attr_map[stat])

    print(f"\n{card1.name} → {stat.upper()} = {total1}")
    print(f"{card2.name} → {stat.upper()} = {total2}")

    if total1 > total2:
        print("⭐ Winner:", card1.name)
        return "player"
    elif total2 > total1:
        print("❌ Winner:", card2.name)
        return "opponent"
    else:
        print("🤝 It's a draw!")
        return "draw"


def save_game(filename, player, opponent, deck, is_bot):
    with open(filename, 'wb') as f:
        pickle.dump({
            'player': player,
            'opponent': opponent,
            'deck': deck,
            'is_bot': is_bot
        }, f)
    print(f"Game saved to '{filename}'.")


def load_game(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
        print(f"Game loaded from '{filename}'.")
        return data['player'], data['opponent'], data['deck'], data.get('is_bot', True)
    except FileNotFoundError:
        print(f"'{filename}' not found. Starting a new game.")
        return None, None, None, None


def play_game(player, opponent, deck, filename, is_bot=True):
    turn = 0

    while player.total_cards() < 20 and opponent.total_cards() < 20:
        if not player.has_cards():
            player.draw_cards(deck, 5)
            print(f"{player.name} drew new cards.")
        if not opponent.has_cards():
            opponent.draw_cards(deck, 5)
            print(f"{opponent.name} drew new cards.")

        current_player = player if turn % 2 == 0 else opponent
        other_player = opponent if turn % 2 == 0 else player

        display_hand(current_player)
        stat = choose_stat()

        while True:
            try:
                idx = int(input(f"{current_player.name}, which card do you want to play? ")) - 1
                chosen_card = current_player.hand[idx]
                break
            except (ValueError, IndexError):
                print("Invalid choice! Please enter a valid card number.")

        if is_bot and other_player.name == "Bot":
            opponent_card = random.choice(other_player.hand)
            print(f"Bot chose: {opponent_card.name}")
        else:
            display_hand(other_player)
            while True:
                try:
                    idx = int(input(f"{other_player.name}, which card do you want to play? ")) - 1
                    opponent_card = other_player.hand[idx]
                    break
                except (ValueError, IndexError):
                    print("Invalid choice! Please enter a valid card number.")

        # Compare cards according to who is current player
        if turn % 2 == 0:
            winner = compare_cards(chosen_card, opponent_card, stat)
        else:
            winner = compare_cards(opponent_card, chosen_card, stat)

        # Winner takes the opponent's card
        if winner == "player" or (winner == "opponent" and turn % 2 == 1):
            other_player.remove_card(opponent_card)
            current_player.hand.append(opponent_card)
        elif winner == "opponent" or (winner == "player" and turn % 2 == 1):
            current_player.remove_card(chosen_card)
            other_player.hand.append(chosen_card)
        else:
            # draw: no card changes
            pass

        print(f"Score: {player.name} = {player.total_cards()} cards, {opponent.name} = {opponent.total_cards()} cards")

        save = input("Do you want to save the game? (y/n): ").strip().lower()
        if save == 'y':
            save_game(filename, player, opponent, deck, is_bot)

        turn += 1

    if player.total_cards() >= 20:
        print(f"🏆 {player.name} WON! YOU ARE MOURINHO?")
    else:
        print(f"💀 {opponent.name} WON! HAHAHA YOU LOSE")
