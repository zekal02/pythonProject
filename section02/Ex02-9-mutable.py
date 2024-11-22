'''
Ex02-9-mutable.py

데이터 타입의 가변성
    mutable: 객체 생성 후 내용 변경 가능
        - 값 변경 시 메모리 주소 유지
        ex) list , set , dict
    immutable: 객체 생성 후 내용 변경 불가
        - 값 변경 시 새 메모리 주소 할당
        ex) nt, str , tuple 등


'''

# 1. mutable 예제
pokemon = ['피카츄','파이리','꼬부기']
print(pokemon)
print('메모리 주소:',id(pokemon))

pokemon[1] = '잠만보'
print('변경 후:', pokemon)
print('메모리 주소:',id(pokemon))

# 2. immutable 예제
level = 25
print('level:', level)
print('level 주소:',id(level))

level = level + 1
print('level+1 :', level)
print('level+1주소:',id(level))

age = 25
print('age:',age)
print('메모리 주소', id(age))

print(id(25))

age = age + 1
print(age)
print(id(age))

'''
리터럴(Literal) - 소스코드에 고정된 값

immutable id(주소값) 값은 해당 값에 대한 주소이다 ex) 25에 대한 주소는 프로그램을 끄지 않는 이상 변경되지 않는다
age = 25 주소랑  level = 25 주소랑 같음


25 # 정수 리터럴
3.14 # 실수 리터럴
"홍길동" # 문자열 리터럴
True # 부울 리터럴

'''

tuple1 = ('파이썬', '자바', 'c++')
print('tuple1:', tuple1)
print('메모리 주소:', id(tuple1))

tuple1 = ('러스트', 'go','React')

print('tuple1:', tuple1)
print('메모리 주소:', id(tuple1))