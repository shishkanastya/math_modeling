print(bool(2 > 3))

print(bool(2))

print(bool('Good'))

print(bool[1, 4, 5])

print(bool(0))

print(bool(''))

print(bool([]))

print(bool([[]]))

a = 3 
if a > 1: 
    print(f'hello{a}')

b = 5
if b==5:
    print(f'hello{b}')

a = 3
if a > 4:
    print('hello 4')
else:
    print(f'hello {a}')

a = 3
if a > 5:
    print('hello 5')
elif: a < 2:
    print('hello 2')
else:
    print('Tupo hello')

a = 3
b = 4
c = 5

if a > 4 and b == 2:
    print('Good')
elif b > 3 or c == 5:
    print('Best')
else:
    print('Bad')

for i in 1, 3, 4:
    print(i ** 2, end=' ')

for i in 1, 3, 4:
    print(i ** 2, end='\n')

for i in 1,3, 4:
    print(i, i ** 2, sep=' - ')

a = [1, 5, 7, 10]
for i in a:
    print(f'{i}**3 = {i ** 3}')

a = range(0, 10,2)
print(a)
print(type(a))
print(a[3])

a = 'Good'
for i in range (0, 10, 0):
    if i < len(a):
        print(a{i} + ' - Bad')
    else:
        print(f'{i}' + ' - Good')

i = 5
while i < 15:
    print('i: ', i)
    i += 2

for i in 'hello world':
    if i =='o':
        break
    print(i)

for i in 'hello world':
    if i =='o':
        continue
    print(i)
    