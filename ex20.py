#입력을 받습니다
number=input("정수 입력> ")
last_character=number[-1]

#짝수 조건
if last_character in "02486":
    print("짝수입니다")

#홀수 조건
if last_character in "13759":
    print("홀수입니다")