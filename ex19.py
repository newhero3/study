#날짜/시간과 관련된 기능을 가져옵니다.
import datetime

#현재 날짜/시간을 구합니다.
now=datetime.datetime.now()

#오전 구분
if now.hour<12:
    print("현재 시각은 {}시로 오전입니다!".format(now.hour))

#오후 구분
if now.hour>=12:
    print("현재 시각은 {}시로 오후입니다!".format(now.hour))
    

#계절 구분
#봄
if 3<=now.month<=5:
    print("이번달은 {}월로 봄입니다!".format(now.month))
#여름구분
if 6<=now.month<=8:
    print("이번달은 {}월로 여름입니다!".format(now.month))    
#가을구분
if 9<=now.month<=11:
    print("이번달은 {}월로 가을입니다!".format(now.month))
#겨울구분
if now.month==12 or 1<=now.month<= 2:
    print("이번달은 {}월로 겨울입니다!".format(now.month))