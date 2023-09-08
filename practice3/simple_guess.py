# Ввод: любое натуральное число
# Вывод: корень из этого числа, если он целый
#

def guess(num: int) -> int | str:
    for i in range(1, num+1):
        if i**2 == num:
            return i
        if i not in range(1, num+1):
            return 'ya tak ne mogu bolshe'
num = int(input('Введи целое натуральное число: '))

print(guess(num))
