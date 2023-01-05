# chapter02-01
# print 사용법

# 기본 출력
print('python start') 
print("python start") 
print('''python start''') 
print("""python start""") 

#separator 옵션
print('P','Y','T','H','O','N', sep='-')

print()

#end 옵션
print('Welcome to',end=' ')
print('IT news',end=' ')
print('Web Site',end='')

print()

#file 옵션
import sys

print('Learn python',file=sys.stdout)



# format 사용(d : 3, s : 'python', f : 3.14)
print('%s %s' % ('one','two'))
print('{} {}'.format('one',2))
print('{1} {0}'.format('one',2))



# %s
print('%10s'%('nice'))
print('{:>10}'.format('nice'))

print('%-10s'%('nice'))
print('{:10}'.format('nice'))


print('{:_>10}'.format('nice'))
print('{:^10}'.format('nice'))

print('%.5s'%('python study'))
print('{:10.5}'.format('python study'))

# %d
print('%d %d' % (1,2))
print('{} {}'.format(1,2))

print('%4d' % (42))
print('{:4d}'.format(42))

print('%1.16f'%(3.1414141414141))
print('{:f}'.format(3.1414141414141))

print('%6.2f'%(3.1414141414141))
print('{:6.2f}'.format(3.1414141414141))