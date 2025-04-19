import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = self._get_value()
    
    def _get_value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        return int(self.rank)
    
    def __str__(self):
        return f"{self.rank}{self.suit}"

class Deck:
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        suits = ['♠', '♥', '♦', '♣']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    
    def deal(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
    
    def add_card(self, card):
        self.cards.append(card)
        self._update_value()
    
    def _update_value(self):
        self.value = sum(card.value for card in self.cards)
        aces = sum(1 for card in self.cards if card.rank == 'A')
        
        while self.value > 21 and aces:
            self.value -= 10
            aces -= 1
    
    def __str__(self):
        return ' '.join(str(card) for card in self.cards)

def play_blackjack():
    print("♠♥♦♣ Добро пожаловать в Blackjack! ♠♥♦♣")
    print("Правила: Наберите 21 очко или ближе к нему, чем дилер.\n")
    
    while True:
        deck = Deck()
        player = Hand()
        dealer = Hand()
        
        # Раздача карт
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        player.add_card(deck.deal())
        dealer.add_card(deck.deal())
        
        # Проверка блекджека
        if player.value == 21:
            print("Блекджек! Вы выиграли!")
            continue
            
        # Ход игрока
        while player.value < 21:
            print(f"\nВаши карты: {player} ({player.value})")
            print(f"Карта дилера: {dealer.cards[0]} и ?")
            
            choice = input("Берём карту? (д/н): ").lower()
            if choice == 'д':
                player.add_card(deck.deal())
            elif choice == 'н':
                break
            else:
                print("Некорректный ввод! Введите 'д' или 'н'")
        
        # Ход дилера
        if player.value <= 21:
            print(f"\nКарты дилера: {dealer} ({dealer.value})")
            while dealer.value < 17:
                dealer.add_card(deck.deal())
                print(f"Дилер берёт: {dealer.cards[-1]}")
        
        # Определение победителя
        print("\nРезультат:")
        print(f"Ваши карты: {player} ({player.value})")
        print(f"Карты дилера: {dealer} ({dealer.value})")
        
        if player.value > 21:
            print("Перебор! Вы проиграли.")
        elif dealer.value > 21:
            print("Дилер перебрал! Вы выиграли!")
        elif player.value > dealer.value:
            print("Вы выиграли!")
        elif dealer.value > player.value:
            print("Дилер выиграл.")
        else:
            print("Ничья!")
        
        # Новая игра
        if input("\nСыграем ещё? (д/н): ").lower() != 'д':
            print("Спасибо за игру!")
            break

if __name__ == "__main__":
    play_blackjack()
