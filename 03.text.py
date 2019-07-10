# -*- coding: UTF-8 -*-


import random
import codecs
import copy


cardjockers = ('RJ', 'BJ')

cardmarks = ('S', 'H', 'C', 'D')

cardnumbers = ('2', '3', '4', '5', '6', '7', '8',
               '9', '10', 'j', 'q', 'k', 'a')

deck = []
for c in cardjockers:
    deck.append(c)

for cn in cardnumbers:
    for cm in cardmarks:
        card = cn + cm
        deck.append(card)
print('\n----------------cuttingline(1)---------------')

print('-----debug:Create my deck,total cards is %d,detail is:\n%s:' %
      (len(deck), deck))

f = codecs.open("deck-new-54.txt", "w", "utf-8")
for card in deck:
    f.write(card)
    f.write('\t')
f.close()
'''
shuffledDeck = []
count = len(deck)
for i in range(count):
    pickedCard = random.choice(deck)
    shuffledDeck.append(pickedCard)

    deck.remove(pickedCard)
'''
shuffledDeck = copy.copy(deck)
random.shuffle(shuffledDeck)

print('\n----------------cuttingline(2)---------------')
print('-----debug:shuffledmy deck,remained cards is %d,detail is:\n%s:'%(len(deck),deck))
print('-----debug:shuffledmy deck,new deck cards cards is %d,detail is:\n%s:'%(len(shuffledDeck),shuffledDeck))

f=codecs.open("deck-shuffled.txt","w","utf-8")
for card in shuffledDeck:
    f.write(card)
    f.write('\t')
f.close()
print('\n----------------cuttingline(3)---------------')
numOfPlayers=3
cardsOfPlayer=int(len(shuffledDeck)/numOfPlayers)
print('-----debug:%dplayers,every one has %d cards.'%(numOfPlayers,cardsOfPlayer))
player1Cards=[]
for i in range(cardsOfPlayer):
    pickedCard=random.choice(shuffledDeck)
    player1Cards.append(pickedCard)
    shuffledDeck.remove(pickedCard)
print('\n--debug:Player1''s%dcardsis--%s:'%(len(player1Cards),player1Cards))
print('\n--debug:Remained%dcardsinshuffleddeckis%s:'%(len(shuffledDeck),shuffledDeck))
