user_input = int(input("2~9 입력 : "))
if (user_input > 1 & user_input < 10):
    for i in range(10):
        print(user_input*(i+1),end=" ")
else:
    print("잘못입력하셨음")
