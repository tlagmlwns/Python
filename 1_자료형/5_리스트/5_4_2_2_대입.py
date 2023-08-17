my_l = [0,1,2,3,4,5,6]
print(id(my_l))

my_l[1:5] = ["A", "B"]
#두번째 요소 부터 다섯번째 요소까지 
print(id(my_l))

print(my_l)
