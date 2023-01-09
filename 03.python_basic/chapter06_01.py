# chapter06-01
# 파이썬 클래스
# OOP (객체지향), Self, 인스턴스 메소드, 인스턴스 변수

# 클래스 & 인스턴스 차이 중요

# 예제1
class Dog: #Object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age

#  인스턴스가 객체에 포함된다
print(Dog)

# 인스턴스화
a = Dog('mikky', 2)
b = Dog('baby', 3)

# 비교
print(a == b)
# 클래스 변수와 인스턴스 변수는 동일한 이름일 경우 인스턴스 변수가 우선
print('dog1',a.__dict__)
print('dog2',b.__dict__)

# 인스턴스 속성 확인
print('{} is  {} and {} is {}.'.format(a.name, a.age, b.name, b.age))

if a.species == 'firstdog':
    print   ('{} is a {}    '.format(a.name, a.species))

print(Dog.species)
print(a.species)
print(b.species)

# 예제2
# self의 이해
class SelfTest:
    def function1():
        print('function1 called!')
    def function2(self):
        print(id(self))
        print('function2 called!')

f = SelfTest()
# print(dir(f))
print(id(f))
# f.function1() # 에러
f.function2() 

SelfTest.function1()
# SelfTest.function2() # 에러
SelfTest.function2(f)

class WareHouse:
    # 클래스 변수
    stock_num = 0
    def __init__(self, name):
        self.name = name
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1

user1 = WareHouse('Lee')
user2 = WareHouse('Cho')

print(WareHouse.stock_num)
print(user1.name)
print(user2.name)
print(user1.__dict__)
print(user2.__dict__)
print('before',WareHouse.__dict__)
print('>>>', user1.stock_num)

del user1
print('after',WareHouse.__dict__)

class Dog: #Object 상속
    # 클래스 속성
    species = 'firstdog'

    # 초기화/인스턴스 속성
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        return '{} is {} years old.'.format(self.name, self.age)

    def speak(self, sound):
        return '{} says {}!'.format(self.name, sound)

# 인스턴스 생성
c = Dog('july', 4)
d = Dog('Marry', 10)
# 메소드 호출
print(c.info())
print(d.info())
print(c.speak('멍멍'))
print(d.speak('왈왈'))

