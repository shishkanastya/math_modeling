print('Hello')

print(3+4)

print(4-3)

print(7*3)

print(25/5)

print(5**3)

print(5//2)

print(11%3)

s = 3 + 4
memory_id = id(s)
print(s, memory_id)

print(type(4))

print(type(3.8))

print(type('Молодец'))

a = 'Molodec'
print(type(a))

a = ['Molodec', 1, 'Круто', 6,8]
print(type(True))

print(type(False))

print(type(None))

a = input('Введите число a:')
print(a)
print(type(a))

a = int(input('Введите число a:'))
print(type(a))

a = 'Good'
b = 'Bad'

print(a + b)
# print(a - b)
print(a * 4)

c = 40
d = 10
print(f'Вставим числа{c} и {d}')

a = [1,3,6]
print(a[0])

b = [8,10,11]

c = a + b
print(c)

# c = a - b

print(c * 3)

c.append('Good')
print(c)

c.append(b)
print(a)

print(len(a)) 