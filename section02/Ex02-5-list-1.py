'''
EX02-5-LIST-1.PY

리스트(list)
    -순서가 있는 데이터 집합
    -중복 허용, 수정 가능
    -다양한 자료형 포함 가능
'''
from xmlrpc.client import boolean

# 1.리스트 생성과 접근
pokemon_list = ['피카츄','라이츄','파이리']
print('리스트 전체:',pokemon_list)
print('첫번째 포켓몬:',pokemon_list[0])
print('리스트 길이:',len(pokemon_list))
print('첫번째 포켓몬 문자열 길이:',len(pokemon_list[0]))
print('첫번째 포켓몬 문자열 길이:',len(pokemon_list[0].replace('피카츄','뮤')))

p2 = ['피카츄','라이츄']
print(p2[1])


# 2. 리스트 슬라이싱
fruit_list = ['블루베리', '사과', '자몽', '체리', '망고']
print(fruit_list[2:4])
print(fruit_list[1:]) #뒤도 생략가능
print(fruit_list[-3:])
print(fruit_list[::-1]) # 역순 문자열도 똑같음
print(fruit_list[5:2:-1]) #역순 두이 -1 이 붙으면 역순임
print(fruit_list[:3]) #앞도 생략가능

# print(fruit_list[X:Y:Z])

# 3. 다양한 데이터 타입
string_list = ['A', 'B', 'C']
number_list = [1, 2, 3, 4, 5] #숫자
boolean_list = [True,False,True] # bool 타입
mixed_list = ['문자열', 100, True, 3.14] # 여러 타입을 넣을 수 있음

# 4. 리스트 수정
pokemon_list  = ['피카츄','라이츄','파이리']
pokemon_list[1] = '잠만보' # 단일 항목 수정
print('수정된 리스트: ', pokemon_list)

# 5. 범위 수정
evolution_list = ['피카츄','파이리', '파이리', '리자드', '리자몽']
evolution_list[1:3] = ['라이츄Z', '메가 파이리']
print('진화 업데이트 :', evolution_list)


# 문자열 len()
print('문자열 길이:', len('Hello'))