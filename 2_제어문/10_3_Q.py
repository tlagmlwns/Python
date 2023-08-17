user_input = "65,45,2,3,45,8"
a = user_input.split(",")
hap = 0
for i in a:
    hap+=int(i)
print(hap)