import random


first = 0
my_num_attack = 0
enemy_num_attack = 0
wst = 2 #who start turn
c = 0
firstnum = 0
temp_of_my = []
temp_of_enemy = []
died_my_cards = []
died_enemy_cards = []
result = 0
# вариант
var = 1
temp = []
way = 0
gap = 2
result_of_checking = []
# create test bots
# card my 1  = 5/7
# card en 1 = 3/7
# card my 2 = 5/10
# card en 2 = 3/15


# card my 1  = 5/7
first_my_attack = 5
first_my_hp = 25
first_my_team = 0
first_my_reality = -1
first_my_card = [gap, first_my_team, first_my_attack, first_my_hp, first_my_reality]


# card en 1 = 3/7
first_enemy_attack = 7
first_enemy_hp = 30
first_enemy_team = 1
first_enemy_reality = -1
first_enemy_card = [gap, first_enemy_team, first_enemy_attack, first_enemy_hp, first_enemy_reality]


# card my 2 = 5/10
second_my_attack = 12
second_my_hp = 45
second_my_team = 0
second_my_reality = -1
second_my_card = [gap, second_my_team, second_my_attack, second_my_hp, second_my_reality]


# card en 2 = 3/15
second_enemy_attack = 3
second_enemy_hp = 50
second_enemy_team = 1
second_enemy_reality = -1
second_enemy_card = [gap, second_enemy_team, second_enemy_attack, second_enemy_hp,second_enemy_reality]

#card my 3 = 11/22
#third_my_attack =

all_my_cards = [first_my_card, second_my_card]
all_enemy_cards = [first_enemy_card, second_enemy_card]
ab = []
attack_all_my_cards = []
attack_all_enemy_cards = []


'''
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
'''

#count_cards(first_my_card, all_my_cards)
#count_cards(first_enemy_card, all_enemy_cards)
#count_cards(second_my_card, all_my_cards)
#count_cards(second_enemy_card, all_enemy_cards)
#attack_all_enemy_cards = all_enemy_cards
#attack_all_my_cards = all_my_cards


# print(f'{all_my_cards} мои карты')
# print(f'{all_enemy_cards} карты врага')
#сделано
def who_start_turn(my_cards, enemy_cards):
    global wst
    if len(my_cards) > len(enemy_cards):
        wst = 0
    elif len(my_cards) < len(enemy_cards):
        wst = 1
    else:
        wst = random.randint(0, 1)
    return wst


# сделано
def attack(attack_cards, def_cards ,num_attack):
    global way, temp, temp_of_attack, temp_of_def, wst, my_num_attack, enemy_num_attack, result

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
    num_attack+=1
    result = [attack_cards, def_cards]
    if wst == 0:
        wst = 1
    elif wst == 1:
        wst = 0
    return attack_cards, def_cards
# сделано
def check_for_add(attack_cards, def_cards):
    global result_of_checking
    temp_of_attack = []
    temp_of_def = []
    died_attack = []
    died_def = []
    if len(attack_cards) * len(def_cards) > 0:
        temp_of_attack.append(attack_cards)
        temp_of_def.append(def_cards)
        result_of_checking = temp_of_attack, temp_of_def, 1
    elif len(attack_cards) * len(def_cards) == 0:
        died_attack.append(attack_cards)
        died_def.append(def_cards)
        result_of_checking = died_attack, died_def, 0
    
# сделано
def adding(attack_cards, def_cards, life):
    global wst, temp_of_my, temp_of_enemy, died_my_cards, died_enemy_cards
    if life == 1:
        if wst == 0:
            temp_of_my.append(attack_cards)
            temp_of_enemy.append(def_cards)
        elif wst == 1:
            temp_of_my.append(def_cards)
            temp_of_enemy.append(attack_cards)
    elif life == 0:
        if wst == 0:
            died_my_cards.append(attack_cards)
            died_enemy_cards.append(def_cards)
        elif wst == 1:
            died_my_cards.append(def_cards)
            died_enemy_cards.append(attack_cards)





    #temp.append(str(def_cards))
   # temp.append(str(attack_cards))
   # list(temp)
#            temp[len(temp) - 1] = l
            #            ist(temp[len(temp) - 1])
 #           temp[def_len] = list(temp[def_len])

       #     temp[len(temp) - 1] = list(temp[len(temp) - 1])
 #           temp[attack_len] = list(temp[attack_len])
#            way+=1
 #           var+=1
#            print(way)
#            print(temp)

#вроде сделано))
def sort_for_attack(my_cards, enemy):
    global wst
    if wst == 0:
        attack_cards = my_cards[0]
        def_cards = enemy[0]

    else:
        attack_cards = enemy[0]
        def_cards = my_cards[0]
    my_cards.pop(0)
    enemy.pop(0)
    return attack_cards, def_cards




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
wst = who_start_turn(all_my_cards, all_enemy_cards)
if first == 0:

    if wst == 0:
        attack(all_my_cards, all_enemy_cards, my_num_attack)


    elif wst == 1:
        attack(all_enemy_cards,all_my_cards,enemy_num_attack)
    check_for_add(result[0], result[1])
    adding(result_of_checking[0], result_of_checking[1], result_of_checking[2])
else:
    while len(temp_of_my) * len(temp_of_enemy) > 0:
        attack(sort_for_attack(temp_of_my, temp_of_enemy))
        check_for_add(result[0], result[1])
        adding(result_of_checking[0], result_of_checking[1], result_of_checking[2])
print(temp_of_my)
print(temp_of_enemy)
