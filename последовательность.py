multiple = [int(n) for n in input('Enter numbers: ').split()]
lenght = len(multiple)
count = 0
indexes = []
for i in range(0, lenght):
    if multiple[i] - multiple[i-1] > 1:
        count = count + 1
        indexes.append(i)
if count == 0:
    print('Нарушений не найдено.')
elif count == 1:
    print(multiple[indexes[0]])
else:
    print(indexes)
    

    