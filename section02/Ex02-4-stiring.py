'''
Ex02-4-stiring.py

문자열(string,str)

    - 문자들의 순서가 있는 나열
    - 작은 따옴표(') 또는 큰 따옴표(")로 표현
    - 문자열은 변경 불가능(immutable)
'''
#  1. 문자열 생성 방법
str1 = 'Hello Python' # 작은 따옴표
str2 = "Hello python" #큰 따옴표
#  여러줄 문지열 작은 따옴표

str3 = '''hello 
python
'''

# 여러줄 문자열 큰 따옴표
str4="""hello
python
"""

print(str1)
print(str2)
print(str3)
print(str4)

# 2. 문자열 인덱싱
'''
      |H | o | l | l | o |
index  0   1   2   3   4
역순번호-5  -4  -3  -2  -1
'''

str = 'Hello'
print('1번째 문자:',str[0])
print('마지막 문자:',str[4])
print('마지막 문자:',str[-1])

# 3. 문자열 슬라이싱
str = 'python progrmaming'
print('처음부터 4글자:', str[0:4])
print('처음부터 4글자:', str[:4])
print('7번째 문자부터 :', str[7:])
print('마지막 5글자 :', str[-5:])

# 4. 주요 문자열 메소드(함수)
str = '   p y t h o n   '
print('공백제거',str.strip())
print('모두 대문자',str.upper())
print('모두 소문자', str.lower())
print('문자 교체', str.replace('p','j'))
print('문자 사이까지 공백제거', str.replace(' ',''))

print('    가나다라    '.strip())
print('    가나다라    '.str.replace(' ',''))

