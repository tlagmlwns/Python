def mydef01(): i,j=10,20; print(i+j)
def mydef02(i,j):print(i+j)
def mydef03(i,j,p):
    if p == '+':print(i+j)
    elif p == '-':print(i-j)
    elif p == '*':print(i*j)
    elif p == '/':
        if i > j: print(i,"/",j,"=",i/j)
        else : print(j,"/",i,"=",j/i)
mydef01()
mydef02(10, 20)

n=int(input("첫 번째 숫자 입력 : "))
m=int(input("두 번째 숫자 입력 : "))
p=(input("(+,-,*,/ )기호 입력 : "))
mydef03(n,m,p)