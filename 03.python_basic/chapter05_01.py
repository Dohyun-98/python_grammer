# chapter05-01
# 파이썬 함수 및 중요성
# 파이썬 함수식 및 람다(Lambda)

def first_func(w):
    print('Hello ',w)

word = 'Goodboy'

first_func(word)
print()

def return_func(w1):
    value = "Hello, " + str(w1)
    return value

x = return_func('GoodBoy')
print(x)

# 예제 반환
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return y1,y2,y3

x,y,z = func_mul(10)
print(x,y,z)


# 튜플 리턴
def func_mul(x):
    y1 = x * 10
    y2 = x * 20
    y3 = x * 30
    return (y1,y2,y3)

q = func_mul(10)
print(type(q),q)
print()
# 리스트, 딕셔너리로 리턴 가능

# 중요
# *args, **Rwargs
# *args(언패킹) 가변 인자 
def args_func(*args): # 매개변수명 자유
    for i,v in enumerate(args):
        print('Result : {}'.format(i),v)

args_func('LEE')
print()

# **kwargs(언패킹)
def kwargs_func(**kwargs):
    for v in kwargs.keys():
        print('{}'.format(v), kwargs[v])
    print('---')

kwargs_func(name1='Lee',name2 = 'Park',name3='Cho')

# 전체 혼합
def example(args_1,args_2, *args, **kwargs):
    print(args_1, args_2, args, kwargs)

example(10,20, 'Lee','Park','Cho',age1=20,age2=30,age3=40)
print()

# 중첩함수 (클로저)
def nest_func(num):
    def func_in_func(num):
        print('>>>',num)
    print('in func')
    func_in_func(num + 100)

nest_func(100)

# 람다식 예제
# 메모리 절약, 가독성 향상, 코드 간결
# 함수는 객체를 생성 -> 리소스(메모리) 향상
# 람다는 즉시 실행 함수(Heap 초기화) -> 메모리 초기화
# 남발시, 가독성 오히려 감소

# def mul_func(x,y):
#     return x * y

# lambda_mul_func = lambda x,y : x * y

def mul_func(x,y):
    return x * y
q = mul_func(10,50)
print(q)

lambda_mul_func = lambda x,y : x * y
print(lambda_mul_func(10,50))

def func_final(x,y,func):
    print(x * y * func(100,100))

func_final(10,10,lambda x,y : x * y)

# Hint
# 함수의 매개변수에 강제로 타입을 지정할 수 있다.
def args_func(name, age:int, *args, **kwargs):
    print(name)
    print(age)
    print(args)
    print(kwargs)

args_func('Lee', 20, 'Park', 'Kim', 'Cho', age1=20, age2=30, age3=40)