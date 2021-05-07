import random


#who_start_turn = random.randint(0, 1)
#c = 0
#firstnum = 0
# create test bots
# card my 1  = 5/7
# card en 1 = 3/7
# card my 2 = 5/10
# card en 2 = 3/15


# card my 1  = 5/7
first_my_attack = 5
first_my_hp = 7
first_my_team = 0
first_my_card = [first_my_attack, first_my_hp, first_my_team]


# card en 1 = 3/7
first_enemy_attack = 3
first_enemy_hp = 7
first_enemy_team = 1
first_enemy_card = [first_enemy_attack, first_enemy_hp, first_enemy_team]


# card my 2 = 5/10
second_my_attack = 5
second_my_hp = 10
second_my_team = 0
second_my_card = [second_my_attack, second_my_hp, second_my_team]


# card en 2 = 3/15
second_enemy_attack = 3
second_enemy_hp = 15
second_enemy_team = 1
second_enemy_card = [second_enemy_attack, second_enemy_hp, second_enemy_team]



all_my_cards = []
all_enemy_cards = []
ab = []
def count_cards(check_card):
   if check_card[1] > 0:
       if check_card[2] == 0:
            all_my_cards.append(check_card)
            return 1
       elif check_card[2] == 1:
           all_enemy_cards.append(check_card)
           return 1
   else:
       return 0



#count_cards(first_my_card)
#count_cards(first_enemy_card)
#print(all_my_cards)
#print(all_enemy_cards)

def attack(all_my_cards, all_enemy_cards):
    a = random.randint(0 ,len(all_my_cards)-1)
    b = random.randint(0, len(all_enemy_cards)-1)
    all_my_cards[a][1] = all_my_cards[a][1] - all_enemy_cards[b][0]
    all_enemy_cards[b][1] = all_enemy_cards[b][1] - all_my_cards[a][0]
    ab = all_my_cards[a], all_enemy_cards[b]
    return ab

#zxc = attack(all_my_cards, all_enemy_cards)
#all_my_cards = zxc[0]
#all_enemy_cards = zxc[1]



while 1 == 1:
    #try:
    qwe = count_cards(all_my_cards[firstnum])
    #except:
     #   continue

    if qwe == 0:
        break
    else:
        count_cards(all_my_cards[firstnum])
        firstnum += 1



print(all_my_cards)
