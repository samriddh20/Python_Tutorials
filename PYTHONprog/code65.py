#static method

"""
    Interview ques: is it correct that you can't make any method in a class wihtout 'self' ?
            Ans: No, we can make a method without 'self' by static method 
"""

class Math:
    def __init__(self, num):
        self.num = num
    
    def addtoNum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(num, n):
        return num * n
    
a = Math(4)
print(a.num)
a.addtoNum(6)
print(a.num)

print(a.add(4,3))
print(Math.add(4,3))



