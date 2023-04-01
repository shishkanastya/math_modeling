a = int(input('Введите год:'))
if a % 4 == 0:
    print(a, 'високосный', sep=' - ')
else:
    print(a, 'не високосный', sep=' - ')