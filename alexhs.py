import random



my_num_attack = 0
enemy_num_attack = 0
who_start_turn = random.randint(0, 1)
c = 0
firstnum = 0
# вариант
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

#card my 3 = 11/22
#third_my_attack =

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


# print(f'{all_my_cards} мои карты')
# print(f'{all_enemy_cards} карты врага')

def attack(attack_cards, def_cards ,num_attack):
    global way, temp
    var = 0
    if way == 0:
        i = 0
        for i in range(len(def_cards) -1):

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
            way += 1
            var += 1

def check_for_add(def_cards, attack_cards):
    global
def adding(def_cards, attack_cards):

    temp.append(str(def_cards))
    temp.append(str(attack_cards))
    list(temp)
#            temp[len(temp) - 1] = l
            #            ist(temp[len(temp) - 1])
 #           temp[def_len] = list(temp[def_len])

       #     temp[len(temp) - 1] = list(temp[len(temp) - 1])
 #           temp[attack_len] = list(temp[attack_len])
#            way+=1
 #           var+=1
#            print(way)
#            print(temp)


def sort_for_attack():
    temp_attack_cards = []
    temp_def_cards = []
    temp_def_cards_continue = []
    temp_attack_cards_continue = []
    # sort if can continue

    i = 0

    for i in range(len(temp)):
            int(temp[i])
    for i in temp:
        temp_def_cards_continue.append(temp[i][0].sort(1))
    i = 0
    for i in temp_def_cards_continue:
        temp_def_cards.append(temp_def_cards_continue[i][1].sort(1))
    temp_def_cards = temp_def_cards[0]
    # sort if can continue
    i = 0

    for i in temp:
        temp_attack_cards_continue.append(temp[i][0].sort(1))
    i = 0
    for i in temp_attack_cards_continue:
        temp_attack_cards.append(temp_attack_cards_continue[i][1].sort(0))
    temp_attack_cards = temp_attack_cards[0]
    '''
def attack(attack_cards, def_cards, num_attack):
    global way, war
    for var in range(len(def_cards)) - 1:
        attack_card = num_attack
        def_card = var
        def_cards[def_card][3] -= attack_cards[attack_card][2]
        attack_cards[attack_card][3] -= def_cards[def_card][2]
        if len(attack_cards) * len(def_cards) > 0:
                attack_cards[attack_card][0] = 1
                def_cards[def_card][0] = 1
            else:
                attack_cards[attack_card][0] = 0
                def_cards[def_cards][0] = 0
            temp.append(str(def_cards))
#            temp[len(temp) - 1] = list(temp[len(temp) - 1])
            temp.append(str(attack_cards))
            list(temp)


#            temp[len(temp) - 1] = list(temp[len(temp) - 1])
            way+=1
            print(var)
            print(temp)


            var+=1
    num_attack+=1
    var = 0



'''
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
