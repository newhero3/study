character={"name":"기사", "level":12, "items":{"sword":"불꽃의 검","armor":"풀플레이트"},
           "skill":["베기","세게 베기","아주 세게 베기"]}
for key in character:
    if type(character[key]) is dict:
        for i in character[key]:
                print(f"{i} : {character[key][i]}")
    elif type(character[key]) is list:
        for skill in character[key]:
            print(f"{key} : {skill} ")
    else:
        print(key, ":", character[key])