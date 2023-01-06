# chapter03-01
# 숫자형

# 파이썬 지원 자료형
"""
int : 정수
float : 실수
complex : 복소수
bool : 불린
str : 문자열(시퀸스)
list : 리스트(시퀸스)
tuple : 튜플(시퀸스)
set : 집합
dict 사전
"""

# 데이터 타입   
str1 = "python"
bool1 = True
str2 = 'Anaconda'
float1 = 10.0 # 10 == 10.0  
int1 = 7
list1 = [str1,str2]
dict = {
    "name" : "Machine Running",
    "version" : "9.0"
}
tuple1 = (7,8,9)
set1 = {1,2,3}

# 데이터 타입 출력

print(type(str1))
print(type(bool1))
print(type(str2))
print(type(float1))
print(type(int1))
print(type(list1))
print(type(dict))
print(type(tuple1))
print(type(set1))
print()

# 숫자형 연산자
"""

+
-
*
/
// : 몫
% : 나머지
abs(x) : 절대값
pow(x,y) : x ** y -> 2 ** 3

"""

# 정수 선언
i = 77
i2 = -14
big_int = 77777777777777777777777777777

# 정수 출력
print(i)
print(i2)
print(big_int)
print()

# 실수 선언
f1 = 0.9999999
f2 = 3.14151324
f3 = -3.9
f4 = 3 / 9

# 실수 출력
print(f1)
print(f2)
print(f3)
print(f4)
print()

# 연산 실습
i1 = 89
i2 = 939
big_int1 = 77777779990908098098908
bit_int2 = 2319083019283091280392
f1 = 1.234
f2 = 3.939

# +
print(">>>>+")
print('i1 + i2 :',i1 + i2)
print('f1 + f2 :',f1 + f2)
print()

# 형 변환 실습
a = 3.
b = 6
c = .7
d = 12.7
print(type(a))
print(type(b))
print(type(c))
print(type(d))

# 형 변환
print(float(b))
print(int(c))
print(int(d))
print(int(True)) # True : 1 False : 0
print(complex(3))
print(complex('3')) # 문자형 -> 숫자형
print(complex(False))

# 수치 연산 함수
print(abs(-7))
x,y = divmod(100,8)
print(x,y)
print(pow(5,3))

# 외부 모듈
import math

print(math.pi)
print(math.ceil(5.1))