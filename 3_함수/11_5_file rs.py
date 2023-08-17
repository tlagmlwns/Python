it = []
it.append("Clould")
it.append("Data Science")
it.append("AI")
it.append("Block Chain")
it.append("Smart contract")
it.append("Smart contract")

#입력
try:
    f = open("it.txt","w")
    for name in it:
        f.write(name)
        f.write("\n")
    f.close()
except:
    print("예외처리")

#읽기
f = open("it.txt","r")
it = f.readlines()
f.close()
print(it)

#\n 제거하기
r_it=[]
for item in it:
    r_it.append(f.strip())
    #r_it.append(f.replace("\n", "")) #다른 방법

print(r_it)
it = list(map(lambda s: s.strip(), it))
print(it)