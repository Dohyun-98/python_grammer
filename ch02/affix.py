num = int(input())
result = str(num)

if num>=1000000:
	result = str(num//1000000) + 'M'
elif num >= 1000:
	result = str(num//1000) + 'K'
else :
	pass

print(result)
