output=[i for i in range(1,100+1) if "{:b}".format(i).count("0")==1] 

print("합계:", sum(output))