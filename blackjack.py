import random

def draw_card():
    # Карты от 2 до 11 (11 — туз)
    return random.randint(2, 11)

def print_status(player_cards, dealer_cards, hide_dealer=True):
    print(f"\nВаши карты: {player_cards} (сумма: {sum(player_cards)})")
    if hide_dealer:
        print(f"Карта дилера: [{dealer_cards[0]}, ?]")
    else:
        print(f"Карты дилера: {dealer_cards} (сумма: {sum(dealer_cards)})")

def player_turn(player_cards, dealer_cards):
    while True:
        print_status(player_cards, dealer_cards)
        choice = input("Взять карту (в) или остановиться (о)? ").strip().lower()
        if choice == 'в':
            card = draw_card()
            player_cards.append(card)
            print(f"Вы взяли карту: {card}")
            if sum(player_cards) > 21:
                print_status(player_cards, dealer_cards)
                print("Перебор! Вы проиграли.")
                return False
        elif choice == 'о':
            return True
        else:
            print("Введите 'в' или 'о'.")

def dealer_turn(dealer_cards):
    print("\nХод дилера...")
    while sum(dealer_cards) < 17:
        card = draw_card()
        dealer_cards.append(card)
        print(f"Дилер взял карту: {card} (сумма: {sum(dealer_cards)})")
        if sum(dealer_cards) > 21:
            print("У дилера перебор!")
            return False
    return True

def determine_winner(player_cards, dealer_cards):
    player_sum = sum(player_cards)
    dealer_sum = sum(dealer_cards)
    print_status(player_cards, dealer_cards, hide_dealer=False)
    if player_sum > 21:
        print("Вы проиграли!")
    elif dealer_sum > 21:
        print("Дилер проиграл. Вы выиграли!")
    elif player_sum > dealer_sum:
        print("Вы выиграли!")
    elif player_sum < dealer_sum:
        print("Вы проиграли!")
    else:
        print("Ничья!")

def play_game():
    print("Добро пожаловать в игру '21 очко'!")
    player_cards = [draw_card(), draw_card()]
    dealer_cards = [draw_card(), draw_card()]
    # Ход игрока
    if player_turn(player_cards, dealer_cards):
        # Ход дилера
        if dealer_turn([dealer_cards[0], dealer_cards[1]]):
            # Определение победителя
            determine_winner(player_cards, dealer_cards)
        else:
            print_status(player_cards, dealer_cards, hide_dealer=False)
            print("У дилера перебор. Вы выиграли!")

if __name__ == "__main__":
    while True:
        play_game()
        again = input("\nСыграть ещё раз? (д/н): ").strip().lower()
        if again != 'д':
            print("Спасибо за игру!")
            break
