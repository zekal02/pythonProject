'''


'''

eng_dict = {
    'sun':'태양',
    'moon':'달',
    'star':'별',
    'space':'우주'
}

for word in eng_dict:
    print(f'{word}의 뜻: {eng_dict[word]}')

    eng_dict_key = eng_dict.keys()
    for k in eng_dict_key:
        print(f'eng_dict의 key: {k}')

eng_dict_valuse = eng_dict.values()
print(eng_dict_valuse)
for v in eng_dict_valuse:
    print(f'eng_dict의 value: {v}')