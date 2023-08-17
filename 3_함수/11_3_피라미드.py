def draw_pyramid(nl):
    for j in range(1, nl+1):
        for i in range(nl - j):
            print(" ", end="0")
            
        for i in range(j * 2 - 1):
            print("*",end="")

        print()

a=int(input("숫자입력 : "))
draw_pyramid(a)