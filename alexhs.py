import random




#who_start_turn = random.randint(0, 1)
c = 0
firstnum = 0
# create test bots
# card my 1  = 5/7
# card en 1 = 3/7
# card my 2 = 5/10
# card en 2 = 3/15


# card my 1  = 5/7
first_my_attack = random.randint(1,30)
first_my_hp = random.randint(20,30)
first_my_team = 0
first_my_card = [first_my_attack, first_my_hp, first_my_team]


# card en 1 = 3/7
first_enemy_attack = random.randint(1,30)
first_enemy_hp = random.randint(20,30)
first_enemy_team = 1
first_enemy_card = [first_enemy_attack, first_enemy_hp, first_enemy_team]


# card my 2 = 5/10
second_my_attack = random.randint(1,30)
second_my_hp = random.randint(20,30)
second_my_team = 0
second_my_card = [second_my_attack, second_my_hp, second_my_team]


# card en 2 = 3/15
second_enemy_attack = random.randint(1,30)
second_enemy_hp = random.randint(20,30)
second_enemy_team = 1
second_enemy_card = [second_enemy_attack, second_enemy_hp, second_enemy_team]



all_my_cards = []
all_enemy_cards = []
ab = []
attack_all_my_cards = []
attack_all_enemy_cards = []



def count_cards(check_card, cards):
   if check_card[1] > 0:
           cards.append(check_card)
   else:
        pass

def clear_cards(cards):
    new_cards = []
    for i in range(len(cards)):
       if cards[i][1] > 0:
           new_cards.append(cards[i])
    return new_cards



count_cards(first_my_card, all_my_cards)
count_cards(first_enemy_card, all_enemy_cards)
count_cards(second_my_card, all_my_cards)
count_cards(second_enemy_card, all_enemy_cards)
attack_all_enemy_cards = all_enemy_cards
attack_all_my_cards = all_my_cards
print(f'{all_my_cards} мои карты')
print(f'{all_enemy_cards} карты врага')

def attack(all_my_cards, all_enemy_cards):
    a = random.randint(0 ,len(all_my_cards)-1)
    b = random.randint(0, len(all_enemy_cards)-1)
    all_my_cards[a][1] = all_my_cards[a][1] - all_enemy_cards[b][0]
    all_enemy_cards[b][1] = all_enemy_cards[b][1] - all_my_cards[a][0]
    ab = all_my_cards[a], all_enemy_cards[b]
    return ab

''' проверка атаки
zxc = attack(all_my_cards, all_enemy_cards)
after_attack_my = zxc[0]
after_attack_enemy = zxc[1]
print(f'{after_attack_my} моя рандомная карта которая ударилась')
print(f'{after_attack_enemy} вражеская карта которая ударилась')
'''

#attack(all_my_cards, all_enemy_cards)
#print(all_my_cards)
#print(all_enemy_cards)





print(all_my_cards)
attack_all_my_cards = clear_cards(all_my_cards)
print(attack_all_my_cards)
i = 0


while len(attack_all_my_cards) * len(attack_all_enemy_cards) > 0:
    attack(attack_all_my_cards, attack_all_enemy_cards)
    attack_all_my_cards = clear_cards(attack_all_my_cards)
    attack_all_enemy_cards = clear_cards(attack_all_enemy_cards)
    print(f'{attack_all_my_cards} мои карты')
    print(f'{attack_all_enemy_cards} карты врага')
    i+=1
    print(i)

if len(attack_all_my_cards) + len(attack_all_enemy_cards) == 0:
    print("draw")
elif len(attack_all_my_cards) > len(attack_all_enemy_cards):
    print('win')
elif len(attack_all_my_cards) < len(attack_all_enemy_cards):
    print("lose")
