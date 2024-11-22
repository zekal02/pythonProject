'''
Ex03-1-eacape.py

이스케이프 문자(Escape Character)
    -특수 기능을 가진 제어 문자
    -백 슬래시(\)로 시작


    \t : 탭
    \b : 백스페이스
    \' : 작은 따옴표
    \" : 큰 따옴표
    \n : 개행(줄 바꿈)
    \\ : 백 슬레시
'''


# 1. 이스케이프 문자 활용
pokemon_info = 'ID : \'피카츄\'\n 타입:\'전기\'\t level: 25'
print(pokemon_info)

# 2. 경로 표시
file_path = 'C:\\Program Files\\Google'
print()