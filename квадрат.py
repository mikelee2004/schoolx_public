a = int(input("Введите натуральное число: "))
result = []
for num in range(-a, a + 1):
    result.append(num**2)

print(result)