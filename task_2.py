a = int(input('Введите первый член прогрессии:'))
b = int(input('Введите знаменатель прогрессии: '))
c = int(input('Введите количество членов прогрессии:' ))

i = range(a, b **(c-1) * a + 3,4)
f = int(i[0])
print(f)

for i in range (1):
    x = a * b
    print(x)
    a = x