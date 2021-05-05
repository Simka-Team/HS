import random


who_start_turn = random.randint(0, 1)
c = 0
# create test bots
# card 1 = 5/7
# card 2 = 3/7

first_my_attack = 5
first_my_hp = 7
first_my_team = 0
first_enemy_attack = 3
first_enemy_hp = 7
first_enemy_team = 1
first_my_card = [first_my_attack, first_my_hp, first_my_team]
first_enemy_card = [first_enemy_attack, first_enemy_hp, first_enemy_team]
all_my_cards = []
all_enemy_cards = []
ab = []




def count_cards(check_card):
   if check_card[1] > 0:
       if check_card[2] == 0:
            all_my_cards.append(check_card)
       elif check_card[2] == 1:
           all_enemy_cards.append(check_card)
   else:
        pass


count_cards(first_my_card)
count_cards(first_enemy_card)
print(all_my_cards)
print(all_enemy_cards)

def attack(all_my_cards, all_enemy_cards):
    a = random.randint(0 ,len(all_my_cards)-1)
    b = random.randint(0, len(all_enemy_cards)-1)
    all_my_cards[a][1] = all_my_cards[a][1] - all_enemy_cards[b][0]
    all_enemy_cards[b][1] = all_enemy_cards[b][1] - all_my_cards[a][0]
    ab = all_my_cards[a], all_enemy_cards[b]
    return ab

zxc = attack(all_my_cards, all_enemy_cards)
all_my_cards = zxc[0]
all_enemy_cards = zxc[1]
print(all_my_cards)
print(all_enemy_cards)




