'''

논리 연산자
    참 / 거짓을 판단하는 연산자
    and : 둘다 True 일 때 만 True
    or: 하나라도 True 이면 True
    not: True ↔ False 반전
'''

# 1.

a = 10
b = 0
print(f'{a}>0 and {b}>0 : {a >0 and b>0}')
print(f'{a}>=0 and {b}>=0 : {a >=0 and b>=0}')
print(f'{a}>0 or {b}>0 : {a >0 or b>0}')
print(f'not {a}: {not a}')
print(f'not {b}: {not b}')


