'''
Ex02-2-variable-2.py

변수명 규착:
    -영문, 한글 , 숫자, _로 구성
    -특수문자 사용 불가
    -첫 글자는 숫자 불가
    -키워드(명령어) 사용 불가

    주석 단축키 ctrl + /
    줄 복사 단축키 ctrl + d
    줄 삭제 단축기 ctrl + y

    단어이동 단축기 ctrl+ 화살표

'''
from idlelib.debugobj import myrepr

# 1. 여러 변수에 다른 값 할당
x,y,z = "피카츄","라이츄", "파이리"
print('포켓몬 1:',x)
print('포켓몬 1:',y)
print('포켓몬 1:',z)

# 2. 여러 변수에 같은 값 할당
x=y=z= '꼬부기'
print('변경된 포켓몬:',x)
print('변경된 포켓몬:',y)
print('변경된 포켓몬:',z)

#3.잘못된 변수명 예시
'''
2myvar = 'python1'  # 숫자로 시작
my-var = 'python2'  # 특수문자 포함
my var = 'python3'  # 공백 포함
'''

'''
my_var = 'python4'   _ 가능
'''
