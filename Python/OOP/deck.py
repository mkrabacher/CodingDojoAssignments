import random

class Deck(object):
    def __init__(self, cards):
        self.cards = cards

    def deal(self, game, players):
        for i in range(0, game['hand_size']):
            for player in players:
                player.hand.append(self.cards.pop(0))
        print self.cards
        return self

    
    def shuffle(self):
        card_list = self.cards
        shuffled_list = []
        while len(card_list) > 0:
            shuffle_index = random.randint(0,len(card_list)-1)
            shuffled_list.append(card_list[shuffle_index])
            card_list.pop(shuffle_index)
        self.cards = shuffled_list
        print self.cards
        return self


class Card(object):
    def __init__(self, val, suit, name):
        self.val = val
        self.suit = suit
        self.name = name

class Player(object):
    def __init__(self, name):
        self.name = name
        self.hand = []

    def draw(self, deck):
        pass

    def play(self, card):
        pass

poker = {'hand_size':5, 'loss':'no more cards'}

poker['hand_size']

deck = [1,2,3,4,5,6,7,8,89,9,10]

matt = Player('Matt')
ben = Player('Ben')


players = [matt, ben]

pokedeck = Deck(deck)

# print 'deck:',pokedeck
print 'shuff deck:', pokedeck.shuffle()
print 'deck after deal', pokedeck.deal(poker, players)
for player in players:
    print player.name, "'s hand:", player.hand