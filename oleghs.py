import random

# выбор- кто начинает из num количества игроков
def Who_Is_Started(num):
    return random.randint(1,num)


#num = 2
#print(Who_Is_Started(num))
#print(random.randint(1,2))

# initialization hands
a=[[1,5],[2,3],[1,6],[3,3],[2,7],[4,2],[1,5]]

# вывод пятого элемента второго разряда ( от нуля счет)
print(a[4][1])