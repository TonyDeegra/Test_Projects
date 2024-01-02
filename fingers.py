hand = input('Введите название руки: ')
if hand == 'Правая':
    finger = input('Введите название пальца: ')
    if finger == 'Большой':
        print(1)
    elif finger == 'Указательный':
        print(2)
    elif finger == 'Средний':
        print(3)
    elif finger == 'Безымянный':
        print(4)
    elif finger == 'Мизинец':
        print(5)
    else:
        print('Ошибка')
elif hand == 'Левая':
    finger = input('Введите название пальца: ')
    if finger == 'Большой':
        print(5)
    elif finger == 'Указательный':
        print(4)
    elif finger == 'Средний':
        print(3)
    elif finger == 'Безымянный':
        print(2)
    elif finger == 'Мизинец':
        print(1)
    else:
        print('Ошибка')
else:
    print('Ошибка')