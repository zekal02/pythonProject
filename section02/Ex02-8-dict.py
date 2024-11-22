'''
Ex02-8-dict.py

딕셔너리(dict)
    -key:value 쌍으로 이루어진 자료구조
    -key는 중복 불가
    -실제 데이터를 구조화 하는데 유용


'''

# 1. 딕셔너리 생성
pokemon = {
    "name": '피카츄',
    "type":"전기",
    "level":25,
    "skill":["백만볼트","전광석화"]

}
print('포켓몬 정보:',pokemon)

# 접근
print('name:',pokemon["name"]) # 대괄호 접근
print('type:',pokemon["type"])
print('level:',pokemon.get("level")) # get() 메소드 접근
print('skill:',pokemon["skill"][1])

# 2. 딕셔너리 수정
pokemon["level"] = 30   # 값 수정

print('수정 후 :', pokemon)

pokemon["speed"] = 10
print('항목 추가 후:', pokemon)

pokemon.update({"HP": 200})

# 3. 딕셔너리 삭제 메소드
remove_value = pokemon.pop("speed")
print("삭제된 정보:", remove_value)
print("삭제 후:", pokemon)

last_item = pokemon.popitem() # 마지막 항목 삭제
print("마지막 삭제 항목:", last_item)

# 딕셔너리 메소드
print("모든 키:", type(pokemon.keys()))
print("모든 키:", pokemon.keys())
print("모든 값:", pokemon.values())


print("키 요소1:", list(pokemon.keys())[0])
print("값 요소1:", list(pokemon.values())[0])

print("모든 쌍:", pokemon.items())


# 숙제 ! 이해하기
print("요소1:", list(pokemon.items())[0][1])