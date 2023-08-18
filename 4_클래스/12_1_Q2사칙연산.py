class Cal:
    def __init__(self,list):
        self.list = list
    def sum(self):
        hap = 0
        for i in self.list:
            hap +=i
        return hap
    def avg(self):
        hap2,c = 0,0
        for i in self.list:
            hap2 +=i
            c +=1
        ave = hap2 / c
        return ave
    
cal1 = Cal([1, 2, 3, 4, 5])
print(cal1.sum()) # 15
print(cal1.avg()) # 3.0

cal2 = Cal([6, 7, 8, 9, 10, 11])
print(cal2.sum()) # 51
print(cal2.avg()) # 8.5
