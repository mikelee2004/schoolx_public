# Ввод: любое натуральное число
# Вывод: корень из этого числа, если он целый
#

def guess(num: int) -> int | str:
    for i in range(1, num+1):
        if i**2 == num:
            return i
        else:
            i = i + 1

num = int(input('Введи целое натуральное число: '))

print(guess(num))
