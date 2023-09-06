import math

n = int(input('Введите количество секунд: '))
hours = n // 3600
minutes = (n % 3600)/60
rounded_minutes = math.floor(minutes)
print(hours, 'час (а/ов)', rounded_minutes, 'минут (a/ы)')