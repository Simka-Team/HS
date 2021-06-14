import random



my_num_attack = 0
enemy_num_attack = 0
who_start_turn = random.randint(0, 1)
c = 0
firstnum = 0
#вариант
var = 1
temp = []
way = 0
gap = 2
# create test bots
# card my 1  = 5/7
# card en 1 = 3/7
# card my 2 = 5/10
# card en 2 = 3/15


# card my 1  = 5/7
first_my_attack = 5
first_my_hp = 25
first_my_team = 0
first_my_card = [gap, first_my_team, first_my_attack, first_my_hp]


# card en 1 = 3/7
first_enemy_attack = 7
first_enemy_hp = 30
first_enemy_team = 1
first_enemy_card = [gap, first_enemy_team, first_enemy_attack, first_enemy_hp]


# card my 2 = 5/10
second_my_attack = 12
second_my_hp = 45
second_my_team = 0
second_my_card = [gap, second_my_team, second_my_attack, second_my_hp]


# card en 2 = 3/15
second_enemy_attack = 3
second_enemy_hp = 50
second_enemy_team = 1
second_enemy_card = [gap, second_enemy_team, second_enemy_attack, second_enemy_hp]



all_my_cards = []
all_enemy_cards = []
ab = []
attack_all_my_cards = []
attack_all_enemy_cards = []



def count_cards(check_card, cards):
   if check_card[3] > 0:
           cards.append(check_card)
   else:
        pass

def clear_cards(cards):
    new_cards = []
    for i in range(len(cards)):
       if cards[i][3] > 0:
           new_cards.append(cards[i])
    return new_cards



count_cards(first_my_card, all_my_cards)
count_cards(first_enemy_card, all_enemy_cards)
count_cards(second_my_card, all_my_cards)
count_cards(second_enemy_card, all_enemy_cards)
attack_all_enemy_cards = all_enemy_cards
attack_all_my_cards = all_my_cards
#print(f'{all_my_cards} мои карты')
#print(f'{all_enemy_cards} карты врага')

def attack(attack_cards, def_cards,num_attack):
    var = 0
    if num_attack > len(attack_cards):
        num_attack = 0

    while var <= len(def_cards) - 1:

 #       temp_attack_cards = attack_cards
 #       temp_def_cards = def_cards
        attack_card = num_attack
        def_card = var
        def_cards[def_card][3]-=attack_cards[attack_card][2]
        attack_cards[attack_card][3]-=def_cards[def_card][2]
        if len(attack_cards) * len(def_cards) > 0:
            attack_cards[attack_card][0] = 1
            def_cards[def_card][0] = 1
        else:
            attack_cards[attack_card][0] = 0
            def_cards[def_cards][0] = 0

        temp.append(str(def_cards))
        temp.append(str(attack_cards))
        way=+1
        print(var)
        print(temp)



        var+=1
    num_attack+=1
    var = 0




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





#print(all_my_cards)
#attack_all_my_cards = clear_cards(all_my_cards)
#print(attack_all_my_cards)
i = 0
'''
while len(attack_all_my_cards) * len(attack_all_enemy_cards) > 0:
    if len(attack_all_my_cards) > len(attack_all_enemy_cards):
        attack(attack_all_my_cards, attack_all_enemy_cards, my_num_attack)
    elif len(attack_all_enemy_cards) > len(attack_all_my_cards):
        attack(all_enemy_cards, attack_all_my_cards, enemy_num_attack)

    else:
        if who_start_turn == 0:
            attack(attack_all_my_cards, attack_all_enemy_cards, my_num_attack)
        elif who_start_turn == 1:
            attack(attack_all_my_cards, attack_all_my_cards, enemy_num_attack)
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
'''
attack(all_my_cards, all_enemy_cards, my_num_attack)
