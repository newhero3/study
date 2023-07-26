a="Hello Python Programming...!"
#대,소문자
print(a.upper())
print(a.lower())
#공백 비우기
input_a="""
         안녕하세요
문자열의 함수를 알아봅시다
"""

print(input_a.strip())

#숫자, 영어 확인
print("TrainA10".isalnum())

#스플릿=자르기
a="hello.welcome@.etverse.co.kr".split("@")

print(a)