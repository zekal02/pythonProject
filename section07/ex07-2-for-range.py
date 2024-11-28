'''

for 문과 range() 함수

range()
    연속된 숫자를 만들어주는 함수

    ex) range(1,10) => 1,2,3,4,5,6,7,8,9

'''

dan = 2

# range(stop)
for n in range(10):  # range(10) : 0 ~ 9
    print(f'{dan}X{n}={dan * n}', end=" ")

#  range(start , stop)

dan = 3
for n in range(1,10):  # range(10) : 0 ~ 9
    print(f'{dan}X{n}={dan * n}', end= " ")
print()


dan = 4
#  range(start, stop , step)
for n in range(1,10,2): # 1부터 2씩 증가 <10
    print(f'{dan}X{n}={dan * n}', end=" ")
print()