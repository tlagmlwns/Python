import time
filename = time.strftime("%Y%m%d_%H%M%S")
print(filename)

f = open(filename + ".txt", "w")
for item in id:
    f.write(item)
    f.write("\n")
f.close()