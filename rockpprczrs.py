player1,player2 = input('Камень, ножницы, бумага? ').split()

player1 = player1.lower()
player2 = player2.lower()

if player1 == 'камень' and player2 == 'ножницы':
    print('Игрок 1 победил!')
elif player1 == 'ножницы' and player2 == 'бумага':
    print('Игрок 1 победил!')
elif player1 == 'бумага' and player2 == 'камень':
    print('Игрок 1 победил!')
elif player2 == 'камень' and player1 == 'ножницы':
    print('Игрок 2 победил!')
elif player2 == 'ножницы' and player1 == 'бумага':
    print('Игрок 2 победил!')
elif player2 == 'бумага' and player1 == 'камень':
    print('Игрок 2 победил!')
elif player1==player2:
    print('Ничья!')
else:
    print('Кто-то ошибся!')