# chapter04-01
# 파이썬 제어문
# IF 실습

# 기본 형식
print(type(True)) # 0이 아닌수, "abc", [1,2,3], (1,2,3) ...
print(type(False)) # 0, "", [], (), {}...

# 예1)
if  True :
    print('Good')

if False:
    print('bad')

# 예2)

if False:
    print('Bad')
else:
    print('Good')


# 관계 연산자
# >, >=, <, <=, ==, !=
x = 15
y = 10
# 양변이 같을 경우 참
print(x == y)
# 양변이 다를 경우 참
print(x != y)
# 왼쪽이 클 때 참
print(x>y)
# 왼쪽이 크거나 같을 때 참
print(x>=y)
# 오른쪽이 클 때 참
print(x<y)
# 오른쪽이 크거나 같을 때 참
print(x<=y)


# 예3)
city = ""
if city :
    print('You are in:',city)
else:
    print("plz enter your city")

# 예4)
city2 = ""
if city2 :
    print('You are in:',city2)
else:
    print("plz enter your city")

# 논리 연산자(중요)
# and, or, not

a = 75
b = 40
c = 10

print('and:',a > b and b > c)
print('or', a > b | b > c)
print('not',not a > b )

# 산술 , 관계, 논리 우선순위
print('el :',3 + 12 > 7 + 3)
print('e2 :',5 + 10 * 3 > 7 + 3 * 20)
print('e2 :',5 + 10 > 3 and 7 + 3 == 10)

# 예4)
score1 = 90
score2 = 'A'
if score1 >= 90 and score2 == 'A':
    print('pass')
else:
    print('fail')

# 예5)
id1 =  'vip'
id2 = 'admin'
grade = 'platinum'

if id1 == 'vip' or id2 == 'admin':
    print('관리자 입장')

if id2 =='admin' and grade == 'platinum':
    print('최상위 관리자')


# 예6)
num = 90
if num >= 90:
    print('Grade : A')
elif num >= 80:
    print('Grade : B')
elif num >= 70:
    print('Grade : C')
else:
    print('과락')

# 예7)
# 중첩 조건문
grade = 'A'
total = 95

if grade == 'A':
    if total >= 90:
        print('장학금 100%')
    elif total > 80:
        print('장학금 80%')
    else:
        print('장학금 50%')
else:
    print('장학금 없음')

q = [10,20,30]
w = {70,80,90,100}
e = dict(
    name = 'Lee',
    city = 'Seoul',
    grade = 'A',
)
r = (10,12,14)

print(15 in q)
print(90 in w)
print(12 not in r)
print('name' in e)
print('Seoul' in e.values())