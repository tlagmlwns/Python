#def isOdd(arg):
#    return arg%2==1
#
#myDict = {x:x*x for x in range(11) if isOdd(x)}
#print(myDict)

def isSosu(qwer):
    for i in range(2, qwer):
        if ((qwer % 1 == 0)&(qwer % (i+1) == 0))==True:
            if (qwer != 1)&(qwer != 0) :
                return qwer

myDict2 = {x:x for x in range(10) if isSosu(x)}
print(myDict2)