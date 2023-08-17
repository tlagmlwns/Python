#list 사용하지 않고 숫자형 변수 4개 선언하여 출력한 예
a,b,c,d,hap=0,0,0,0,0
a=int(input("1번째 숫자 : "))
b=int(input("2번째 숫자 : "))
c=int(input("3번째 숫자 : "))
d=int(input("4번째 숫자 : "))
hap=a+b+c+d
print("합계1 -> %d" % hap)

#list 변수를 선언하여 앞 예제 수정
aa, hap=[0,0,0,0],0
for i in range(4):
    aa[i] = int(input("번째 숫자 입력 : "))
    hap += aa[i]
print("합계2 -> %d" % hap)