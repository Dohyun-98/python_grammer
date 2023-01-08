# chapter04-02
# 파이썬 반목문
# For 실습

# 코딩의 핵심
# for in <collection>
#   <loop body>

for v1 in range(10):
    print('v1 is :',v1)

print()

for v2 in range(1,11):
    print('v2 is :',v2)

print()

for v3 in range(1,11,2):
    print('v3 is :',v3)

print()

# 1 ~ 1000의 합
sum1 = 0
for v in range(1,1001):
    sum1 += v
print('1 ~ 1000 Sum :',sum1)
print('1 ~ 1000 Sum :',sum(range(1,1001)))
print('1 ~ 1000 4의 배수의 합 :',sum(range(4,1001,4)))

# Iterables 자료형 반복
# 문자열, 리스트, 튜플, 집합, 사전(딕셔너리)
# iterable 리턴 함수 : range, reversed, enumerate, filter, map, zip

# 예제1
names = ['Kim','Park','Cho','Lee','Choi','Yoo']

for name in names:
    print('Your are :',name)

# 예제2
lotto_numbers = [11,19,21,28,36,37]

for n in lotto_numbers:
    print('Current Number :',n)

# 예제3
word = 'Beautiful'
for s in word:
    print('word :',s)

# 예제4
my_info = dict(
    Name = 'Lee',
    Age = 33,
    City = 'Seoul'
)

for key in my_info:
    print('key:',my_info.get(key))

for v in my_info.values():
    print('value :',v)


# 예제 5
name = "FineAppLE"

for n in name:
    if n.isupper():
        print(n)
    else:
        print(n.upper())

# break

number = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for i in number:
    if i == 34:
        print('number :',i)
        break

# continue

lt = ["1",2,5,True,4.3,complex(4)]
for v in lt:
    if type(v) is bool:
        continue
    else :
        print('Current Type :',type(v))


numbers = [14,3,4,7,10,24,17,2,33,15,34,36,38]

for num in numbers:
    if num == 3:
        print('Found : 3')
        break
else:
    print('Not found :3')

# 구구단
for i in range(2,10):
    for j in range(1,10):
        print('{:4d}'.format(i * j),end='')
    print()
