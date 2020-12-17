import random

suits = ('H', 'D', 'S', 'C')
ranks = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10, 'A':11}

class Card:
  def __init__(self, rank, suit):
    self.suit = suit
    self.rank = rank
    self.value = values[rank]

  def __str__(self):
    return f'{self.rank}'

class Deck:
  def __init__(self):
    self.cards = []
    self.refill_deck()

  def shuffle(self):
    random.shuffle(self.cards)

  def refill_deck(self):
    for suit in suits:
      for rank in ranks:
        self.cards.append(Card(rank, suit))
    self.shuffle()

  def deal_one(self):
    if len(self.cards) == 0:
      self.refill_deck()
    return self.cards.pop()

class Player:
  def __init__(self, money):
    self.money = money
    self.hand = []

  def clear_hand(self):
    self.hand = []

  def add_card(self, new_card):
    self.hand.append(new_card)

  def place_bet(self, bet):
    self.money-=bet

  def add_money(self, bet):
    self.money+=bet
  
  def __str__(self):
    return f"Your hand: {[x.rank for x in self.hand]}"

class Dealer:
  def __init__(self):
    self.hand = []
    self.hidden = None

  def clear_hand(self):
    self.hand = []
    self.hidden = None

  def add_card(self, new_card):
    if len(self.hand) > 0 and self.hidden == None:
      self.hidden = new_card
    else:
      self.hand.append(new_card)

  def show_hand(self):
    self.add_card(self.hidden)
  
  def __str__(self):
    return f"Dealer has a {[x.rank for x in self.hand]}"

def black_jack():
  player = Player(1000)
  dealer = Dealer()

  new_deck = Deck()

  while True:
    player.clear_hand()
    dealer.clear_hand()
    print(f'Your balance is ${player.money}')
    bet = int(input('Please place your bet: '))

    if bet > player.money:
      print('Insufficient funds...')
      continue
    
    player.place_bet(bet)
    player.add_card(new_deck.deal_one())
    dealer.add_card(new_deck.deal_one())
    player.add_card(new_deck.deal_one())
    dealer.add_card(new_deck.deal_one())

    if player.hand[0].value + player.hand[1].value == 21:
      print(player)
      print('BLACKJACK, you won!')
      player.add_money(bet*2.5)
      continue

    print(player)
    print(dealer)

    while True:
      action = input('Would you like to "hit" or "stand"?')
      if action != 'hit' and action != 'stand':
        print('Please enter "hit" or "stand"..')
        continue
      player_total = 0
      dealer_total = 0
      for i in player.hand: player_total+=i.value
      if action == 'hit':
        card = new_deck.deal_one()
        player.add_card(card)
        print(player)
        player_total+=card.value
        if player_total > 21:
          print('BUSTED')
          break
      if action == 'stand':
        dealer.show_hand()
        for i in dealer.hand: dealer_total+=i.value
        print(dealer)
        while dealer_total < 17:
          card = new_deck.deal_one()
          dealer.add_card(card)
          dealer_total+=card.value
          print(dealer)
        if dealer_total > 21 or dealer_total < player_total:
          print('YOU WIN')
          player.add_money(bet*2)
          break
        elif dealer_total > player_total:
          print('YOU LOSE')
          break
        else:
          player.add_money(bet)
          break

black_jack()