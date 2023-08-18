def strcheck(x):
    num = str(x)
    d = list(num)
    #print(d)
    for i in d:
        if '3'in d or '6'in d or '9' in d:
            return  True
        else:
            return False

def sam(y,):
    for i in range(1,y):
        if (strcheck(i) == True):
            print('x',end=" ")
        else :
            print(i,end=" ")

sam(100)