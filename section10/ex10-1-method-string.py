'''

메소드(method)
    특정 객체가 가지고 있는 함수를 의미 한다.
    객체.메소드() 사용이 가능함

'''

# String 객체 format 메소드
print('10자리 폭 왼 쪽 정렬"{:<10d}"'.format(123))
print('10자리 폭 오른쪽 정렬"{:>10d}"'.format(123))
print('10자리 폭 가운데 정렬"{:^10d}"'.format(123))

print('10자리 폭 왼 쪽 정렬 채움문자"{:*<10d}"'.format(123))
print('10자리 폭 오른쪽 정렬 채움문자"{:*>10d}"'.format(123))
print('10자리 폭 가운데 정렬 채움문자"{:*^10d}"'.format(123))

# join 메소드 추가 예제

s = '-'.join('python') # p-y-t-h-o-n
print(s)

s = '+'.join(['a','b','c','d','e']) #a+b+c+d+e
print(s)


# split() 메소드
s = '010-1234-1234'
result = s.split('-')
print(result)
print(result[2])

# strip() lstrip(), rstrip() 공백제거 메소드

s = '    apple    '
result = s.strip()
print(result)

result = s.lstrip()
print(result)


result = s.rstrip()
print(result)

s = '    a p p l e    '
result = s.strip()
print(result)


# replace 메소드
s = '    a p p l e    '
result = s.replace(' ','')
print(result)

s = 'Life is to short'
result = s.replace('short','long')
print(result)
