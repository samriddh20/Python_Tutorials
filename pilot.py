# print('hello world')

# def sum(a,b):
#     return(a+b)

# a = 8
# b = 6
# result = sum(a,b)
# print(f"This is the sum of {a} and {b} = {result}")

class Bike:
    def __init__(self, Model, Body, Color, Year ):
        self.Model = Model
        self.Body = Body
        self.Color = Color
        self.Year = Year
            
    def display_info(self):
        print(f"This is a {self.Year} {self.Model} {self.Body} in {self.Color} color.")

    def change_model(self, next):
        self.next = self.Year
        
        

mybike_1 = Bike("Bullet", "Classic 350", "Black", 2021)
mybike_2 = Bike("Bajaj", "Pulsar 150", "Blue", 2005)

mybike_1.display_info()

mybike_1.change_model(2005)

mybike_1.display_info()


        

        
    
    

    




