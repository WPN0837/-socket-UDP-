'''
返回一个扑克列表，52项，每一项是一个元组
'''
import random
def generate_card():#生成扑克牌组
    card = {}
    B = ['♦', '♣', '♥', '♠']
    A = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    num = 0
    for i in A:
        for j in B:
            card[num] = (i, j)
            num += 1
    card[52] = ('JOKER', 'BLACK')
    card[53] = ('JOKER', 'RED')
    return card
def deal(card):#发牌
    key = [i for i in range(0, 54)]
    random.shuffle(key)#洗牌
    player1 = key[0: 17]
    player2 = key[17: 34]
    player3 = key[34: 51]
    lucky_card = key[51: 54]
    return {'player1': player1, 'player2': player2, 'player3': player3, 'lucky_card': lucky_card}
def show(player, card):
    player.sort()
    for i in player:
        print(card[i], end=' ')
    print()
if __name__ == '__main__':
    card = generate_card()
    card_ed = deal(card)
    show(card_ed['player1'], card)
    show(card_ed['player2'], card)
    show(card_ed['player3'], card)
    show(card_ed['lucky_card'], card)