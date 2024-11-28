'''

이름 국어 영어 수학
john 90 85 95
EMily 92 88 96
Micheal 98 90 92
jessica 88 82 78
'''

#  alt + shift + insert 세로 편집 모드
students = [
    {'이름':'John','국어':90,'영어':85,'수학':95},
    {'이름':'Emily','국어':92,'영어':88,'수학':96},
    {'이름':'Micheal','국어':98,'영어':90,'수학':92},
    {'이름':'Micheal','국어':88,'영어':82,'수학':78},
]

for student in students:
    print(f'{student['이름']}', end=' ')
    print(f'{student['국어']}', end=' ')
    print(f'{student['영어']}', end=' ')
    print(f'{student['수학']}', end=' ')
    print()



mike = students[2]
for k, v in mike.items():
    print(f'{k}: {v}')