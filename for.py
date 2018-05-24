# 반복문
a = ['cat', 'cow', 'tiger']

for animal in a:
    print(animal, end=' ')
else:
    print('')

# 복합 자료형을 사용하는 for문
l = [('루피', 10), ('상디', 20), ('조로', 30)]
for data in l:
    print('이름: %s, 나이: %d' % data)

for name, age in l:
    print('이름: {0}, 나이: {1}'.format(name, age))

l = [{'name': '루피', 'age': 30}, {'name': '루', 'age': 31}, {'name': '피', 'age': 32}]
for data in l:
    print('이름: %(name)s, 나이: %(age)d' % data)

# 1 ~ 10 합 구하기
s = 0
for i in range(1, 11):
    s += i
else:
    print(s)

# break
for i in range(10):
    if i > 5:
        break

    print(i, end=' ')
else:
    print('')

print('')
print('----------------')

# continue
for i in range(10):
    if i < 5:
        continue

    print(i, end=' ')
else:
    print()

# 구구단
for x in range(1, 10):
    for y in range(1, 10):
        print(str(y) + ' * ' + str(x) + ' = ' + str(x*y).rjust(2), end='\t')
    else:
        print('')
