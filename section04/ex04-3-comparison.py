'''

관계 연산자(비교 연산자)
    두 값을 비교하여 bool 값 반환
    >,>=,<,<=, ==,!=

is 연산자
    두 객체가 동일한 메모리 주소를 가리키는지 비교
    즉 같은 객체 확인
'''

# 1. 포켓몬 레벨 비교

pikachu_lv = 25
charmander_lv = 20

print(f'피카츄 레벨 > 파이리 레벨 :{pikachu_lv > charmander_lv}')


#  타입 비교
tpye1 = "불꽃"
tpye2 = "물"

print(f'같은 타입? : {tpye1 == tpye2}')



# 3. is 연산자
x = [1,2,3]
y = [1,2,3]

print(x==y)
print(x is y)
