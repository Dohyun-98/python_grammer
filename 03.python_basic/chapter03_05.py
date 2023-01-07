# chapter03-05
# 파이썬 딕셔너리
# 범용적으로 가장 많이 사용
# 딕셔너리 자료형(순서x, 키 중복x, 수정o, 삭제o)

# 선언
a = {'name' : 'Kim', 'phone':'01044449999','birth':'870514'}
b = {0:'Hello Python'}
c = {'arr':[1,2,3,4]}
d = {
    'Name':'niceman',
    'City':'Seoul',
    'Age': 33,
    'Grade' : 'A',
    'Status':True
}

e = dict([
      ('Name','niceman'),
      ('City','Seoul'),
    ('Age', 33,)
])


f = dict(
    Name = 'Niceman',
    City = 'Seoul',
    Age = 33,
    Grade = 'A',
    Status = True
)

print('a -',type(a),a)
print('a -',type(b),b)
print('a -',type(c),c)
print('a -',type(d),d)
print('a -',type(e),e)
print('a -',type(f),f)
print()

# 출력
print('a -',a['name']) # 존재X -> 에러발생
print('a -',a.get('name')) # 존재X -> None
print('b -',b[0])
print('b -',b.get(0))
print('f -',f.get('City'))
print('f -',f.get('Age'))

# 딕셔러니 추가
a['address'] = 'Seoul'
print(a)
a['rank'] = [1,2,3]
print('a -',a)

print('a -',len(a))
print('b -',len(b))
print('c -',len(c))
print('d -',len(d))

#dict_keys, dict_value, dict_items :  반복문에서 사용 가능

print('a -',a.keys())
print('b -',b.keys())
print('c -',list(c.keys()))
print('d -',list(d.keys()))

print()

print('a -',a.values())
print('b -',b.values())
print('c -',list(c.values()))
print('d -',list(d.values()))

print()

print('a -',a.items())
print('b -',b.items())
print('c -',c.items())

print('c -',c.pop('arr'))
print('c -',c)

print('f -',f.popitem())
print('f -',f.popitem())
print('f -',f.popitem())
print('f -',f.popitem())
print('f -',f.popitem())
# print('f -',f.popitem())

print()

print('a -','birth' in a)
print('a -','City' in d)


# 수정
a['test'] = 'test_dict'
print('a -',a)
a['address'] = 'dj'
print('a -',a)

a.update(birth='910994')
print('a -',a)

temp = {'address' : 'busan'}
a.update(temp)
print('a -',a)