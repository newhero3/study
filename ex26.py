numbers=[273,103,5,32,65,9,72,800,99]
for i in numbers:
    if  i % 2 == 1:
        print(i,"홀수입니다")
    else:
        print(i,"짝수입니다")
    
print()

for _ in numbers:
    print(f"{_}는 {len(str(_))}자릿수입니다.")
    