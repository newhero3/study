import datetime
now=datetime.datetime.now()

a=input("대화를 입력해주세요>")
if "안녕" in a:
    print("안녕하세요.")
elif "몇 시" in a:
    print("지금은 {}시 입니다.".format(now.hour))
else:
    print(a)