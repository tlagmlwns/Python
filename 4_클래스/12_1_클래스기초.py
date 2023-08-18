class AutoMobile:
    def __init__(self, str):
        self.name = str
    def velocityPlus(self):
        self.velocity = self.velocity + 10
    def velocityDown(self):
        self.velocity = self.velocity - 10

        if self.velocity < 0 : 
            self.velocity = 0
    
ac = AutoMobile("율무차")
ac.velocity = 37
for i in range(1, 6):
    if i%2==1:
        ac.velocityPlus()
        print(ac.name + "의 속도은 %d 입니다."% ac.velocity)
    else :
        ac.velocityDown()
        print(ac.name + "의 속도은 %d 입니다."% ac.velocity)