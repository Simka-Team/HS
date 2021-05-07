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
second_my_attack = 5
second_my_hp = 10
second_my_team = 0
second_my_card = [second_my_attack, second_my_hp, second_my_team]
second_enemy_attack = 3
second_enemy_hp = 15
second_enemy_team = 1
second_enemy_card = [second_enemy_attack, second_enemy_hp, second_enemy_team]
all_my_cards = []
all_enemy_cards = []
ab = []




def count_cards(check_card, cards):
   if check_card[1] > 0:
           cards.append(check_card)
   else:
        pass


count_cards(first_my_card, all_my_cards)
count_cards(first_enemy_card, all_enemy_cards)
count_cards(second_my_card, all_my_cards)
count_cards(second_enemy_card, all_enemy_cards)
print(f'{all_my_cards} мои карты')
print(f'{all_enemy_cards} карты врага')

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
print(f'{all_my_cards} первая рандомная карта которая ударилась')
print(f'{all_enemy_cards} вторая карта которая ударилась')
