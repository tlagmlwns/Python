my_list = [0,1,2,3,4,5]
print(id(my_list)) #id는 주소값 출력하는 함수

my_list[1:3] = ["A", "B", "C"] 
#두번째 요소부터 세번째 요소까지 에 대입
print(id(my_list))

print(my_list)