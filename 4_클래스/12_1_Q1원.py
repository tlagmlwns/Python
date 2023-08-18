
class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
    def is_inside(self, i, j):
        if pow((i-self.x),2)+pow((j-self.y),2)<pow((self.r),2):
            return True
        else:
            return False


my_circle = Circle(1.0, 1.5, 0.8)
print(my_circle.is_inside(1.5, 0.9)) # True
print(my_circle.is_inside(0.4, 0.5)) # Fasle