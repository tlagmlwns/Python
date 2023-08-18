f = open("sample.txt","r")
lines1 = f.readlines()
f.close()

print(lines1)
hap, average, count = 0,0,0
for i in lines1:
    hap += int(i)
    count += 1

average1 = hap / count #넣을때마다 count++ 한만큼
average2 = hap / len(lines1) #lines1의 길이만큼

f = open("result.txt", "+a")
f.write("count_average : "+str(average1)+"\n")
f.write("len()_average : "+str(average2)+"\n")
f.close