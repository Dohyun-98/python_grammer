# chapter06-02
# 파이썬 모듈
# Module : 함수, 변수, 클래스 등 파이썬 구성 요소를 모아놓은 파일

def add(x,y):
    return x + y

def sub(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

def power(x,y):
    return x ** y

# __name__ 사용
if __name__ == '__main__':
    print(add(5,5))
    print(sub(15,5))
    print(multiply(10,2))
    print(divide(5,5))
    print(power(5,2))
    print()
