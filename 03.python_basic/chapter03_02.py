# chapter03-02
# 문자형

# 문자열 생성
str1 = 'I am Python'
str2 = 'Python'
str3 = """How are you?"""
str4 = '''Thank you!'''

print(type(str1),type(str2),type(str3),type(str4))
print(len(str1),len(str2),len(str3),len(str4))
print()

# 빈 문자열
str1_t1 = ''
str2_t2 = str()

print(type(str1_t1),len(str1_t1))
print(type(str2_t2),len(str2_t2))
print()

# 이스케이프 문자 사용
# I'm Boy

print("I'm Boy")
print('I\'m Boy')

print('a \t b')
print('a \"\" b')


escape_str1 = "Do you have a \"retro game\"?"
print(escape_str1)
print()

# 탭, 줄바꿈
t_s1 = "Click \t Start!"
t_s2 = "New Line \n Check"

print(t_s1)
print(t_s2)

# Row String
raw_s1 = r'D:\python\test'
print(raw_s1)

# 멀티 라인 입력
multi_str = \
"""
String
MultiLine
Test
"""

print(multi_str)
print()

# 문자열 연산
str_o1 = "Python"
str_o2 = "Apple"
str_o3 = "How are you doing"
str_o4 = "Seoul Deajeon Busan Jinju"

print(str_o1 * 3)
print(str_o1 + str_o2)
print('y' in str_o1)
print('n' in str_o1)
print('P' not in str_o2)
print()

# 문자열 형 변환
print(str(66),type(str(66)))
print(str(10.1),type(str(10.1)))
print(str(True),type(str(True)))

# 문자열 함수(upper, isalnum, startswith, count, endswith, isaL)
print("Capitalize: ", str_o1.capitalize()) # 첫번째 문자를 대문자로 변환
print('endWith? :',str_o2.endswith('s') ) # 마지막 문자가 무엇인지 체크
print("replace :",str_o1.replace('thon','Good')) # 문자열 변경
print("sorted: ",sorted(str_o1)) # 정렬해서 리스트형태로 반환
print("split",str_o4.split(' '))

# 반복(시퀀스)
im_str = "Good Boy"
print(dir(im_str)) #_iter_ 시퀀스이다. 반복문을 사용가능하다.

# 출력
for i in im_str:
    print(i)

#슬라이싱
str_s1 = "Nice Python"

print(len(str_s1))
# 슬라이싱 연습
print(str_s1[0:3])
print(str_s1[5:11])
print(str_s1[5:])
print(str_s1[:len(str_s1)])
print(str_s1[1:4:2]) #  3번째 숫자는 스킵
print(str_s1[-5:])
print(str_s1[1:-2])
print(str_s1[::2])  
print(str_s1[::-1])

# 아스키 코드
a = 'z'
print(ord(a)) # 아스키 코드 변환
print(chr(122)) # 아스키 코드 문자 변환


