'''
EX03-3-format.py

문자열 포매팅
    - % 포매팅: 파이썬 초기부터 있던 변수
    - format(): 파이선 2.6 부터 도입
    - f-string: 파이썬 3.6부터 도입(현재 권장)


'''
# 1. % 포매팅(레거시)
'''
print() 형식 문자
    %d :정수 데이터
    %f : 실수 데이터
    %o : 8진수 데이터
    %x : 16진수 데이터
    %s : 문자열 데이터
    %c : 문자 하나 데이터 
'''

pokemon = '피카츄'
level = 25
hp = 35.5
print('포켓몬:%s' % pokemon)
print('level:%d' %level)
print('hp:%.1f' % hp)
print('%s의 level은 %d입니다.' %(pokemon, level))


print('format()함수')
print('포켓몬: {}'.format(pokemon))
print('레벨: {}'.format(level))
print('체력: {:.1f}'.format(hp))

int1 = 3
int2 = 1.5

print('%d * %.1f = %.1f' %(int1 , int2 , int1*int2))



print('3. f-string')
print(f'포켓몬: {pokemon}')
print(f'레벨: {level}')
print(f'체력: {hp:.2f}')


print('%o' %16)

# 8진수
oct = 0o10
print('%d' %oct)

# 16진수

hex = 0x10
print('%d' %hex)



