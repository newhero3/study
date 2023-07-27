example_list=["요소A", "요소B", "요소C"]
for i, value in enumerate(example_list):
    print("{}번째 요소는{}입니다.".format(i,value))
    
sample_dictionary={"키A":"값A", "키B":"값B", "키C":"값C"}

for key,element in sample_dictionary.items():
    print("dictionary[{}]={}".format(key, element))