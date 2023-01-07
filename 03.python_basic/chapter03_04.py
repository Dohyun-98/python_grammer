# chapter03-04
# 파이썬 튜플
# 리스트와 비교 중요
# 튜플 자료형 (순서o, 중복o 수정x 삭제x) 불변

# 선언

a = ()
b = (1,)
c = (11,12,13,14)
d = (1000,10000,'Ace','Captine')
e = (1000,10000,('Ace','Captine'))

print(type(a),type(b))

# 인덱싱
print('>>>>')
print('d - ',d[1])
print('d - ',d[0]+d[1]+d[1])
print('d - ',e[-1])
print('d - ',list(e[-1][1]))

# 수정x
# d[0] = 1500

# 슬라이싱
print('>>>>')
print('d -',d[0:3])
print('d -',d[2:])
print('d -',d[2][1:3])

# 연산
print('>>>>')
print('c + d',c + d)
print('c * 3',c * 3)

# 튜플 함수
a = (5,2,3,1,4)
print('a -',a)
print('a -',a.index(3))
print('a -',a.count(2))

# 패킹 & 언패킹

# 패킹
t = ('too','bar','baz','qux')
# 하나로 묶다
# 선언

# 언패킹1
(x1,x2,x3,x4) = t
print(type(x1),type(x2),type(x3),type(x4))
print(x1,x2,x3,x4)

# 구조분해할당..

# 패킹 언패킹
t2 = 1,2,3
t3 = 4,
x1,x2,x3 = t2
x4,x5,x6 = 4,5,6

print(t2)
print(t3)
print(x1,x2,x3)